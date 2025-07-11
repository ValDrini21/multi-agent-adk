"""
Disk Information Tool

This module provides a tool for gathering disk information.
"""

import time
from typing import Any, Dict
import os
import psutil
import platform

def get_disk_info() -> Dict[str, Any]:
    """
    Gather disk information including partitions and usage.
    Windows-compatible version with better error handling.

    Returns:
        Dict[str, Any]: Dictionary with disk information structured for ADK
    """
    try:
        # Get disk information
        disk_info = {"partitions": []}
        partitions_over_threshold = []
        total_space = 0
        used_space = 0

        # Windows-specific partition detection
        if platform.system() == "Windows":
            partitions = []
            # Try the standard method first
            try:
                partitions = psutil.disk_partitions()
            except Exception:
                # If that fails, manually check drive letters
                import string
                for letter in string.ascii_uppercase:
                    drive = f"{letter}:\\"
                    try:
                        if os.path.exists(drive):
                            usage = psutil.disk_usage(drive)
                            # Create a mock partition object
                            partition = type('Partition', (), {
                                'device': drive,
                                'mountpoint': drive,
                                'fstype': 'NTFS'
                            })()
                            partitions.append(partition)
                    except (PermissionError, FileNotFoundError, OSError):
                        continue
        else:
            # Non-Windows systems
            try:
                partitions = psutil.disk_partitions()
            except Exception as e:
                return {
                    "result": {"error": f"Failed to enumerate partitions: {str(e)}"},
                    "stats": {"success": False},
                    "additional_info": {"error_type": str(type(e).__name__)},
                }

        # Process each partition
        for partition in partitions:
            try:
                # Safely get partition usage
                partition_usage = psutil.disk_usage(partition.mountpoint)

                # Track high usage partitions
                if partition_usage.percent > 85:
                    partitions_over_threshold.append(
                        f"{partition.mountpoint} - {partition_usage.percent:.1f}%"
                    )

                # Add to totals
                total_space += partition_usage.total
                used_space += partition_usage.used

                # Format sizes safely
                total_gb = partition_usage.total / (1024 ** 3)
                used_gb = partition_usage.used / (1024 ** 3)
                free_gb = partition_usage.free / (1024 ** 3)

                disk_info["partitions"].append(
                    {
                        "device": str(partition.device),
                        "mountpoint": str(partition.mountpoint),
                        "filesystem_type": str(partition.fstype),
                        "total_size": f"{total_gb:.2f} GB",
                        "used": f"{used_gb:.2f} GB",
                        "free": f"{free_gb:.2f} GB",
                        "percentage_used": f"{partition_usage.percent:.1f}%",
                    }
                )
            except (PermissionError, FileNotFoundError, OSError) as e:
                # Skip inaccessible partitions
                continue
            except Exception as e:
                # Log other errors but continue
                print(f"Error processing partition {partition.mountpoint}: {e}")
                continue

        # If no partitions were found, try a different approach for Windows
        if not disk_info["partitions"] and platform.system() == "Windows":
            # Try using wmic command as fallback
            try:
                import subprocess
                result = subprocess.run(['wmic', 'logicaldisk', 'get', 'size,freespace,caption'],
                                     capture_output=True, text=True, timeout=10)
                if result.returncode == 0:
                    lines = result.stdout.strip().split('\n')[1:]  # Skip header
                    for line in lines:
                        if line.strip():
                            parts = line.split()
                            if len(parts) >= 3:
                                drive = parts[0]
                                try:
                                    total_bytes = int(parts[1])
                                    free_bytes = int(parts[2])
                                    used_bytes = total_bytes - free_bytes

                                    total_gb = total_bytes / (1024 ** 3)
                                    used_gb = used_bytes / (1024 ** 3)
                                    free_gb = free_bytes / (1024 ** 3)
                                    usage_percent = (used_bytes / total_bytes) * 100 if total_bytes > 0 else 0

                                    if usage_percent > 85:
                                        partitions_over_threshold.append(
                                            f"{drive} - {usage_percent:.1f}%"
                                        )

                                    total_space += total_bytes
                                    used_space += used_bytes

                                    disk_info["partitions"].append({
                                        "device": drive,
                                        "mountpoint": drive,
                                        "filesystem_type": "NTFS",
                                        "total_size": f"{total_gb:.2f} GB",
                                        "used": f"{used_gb:.2f} GB",
                                        "free": f"{free_gb:.2f} GB",
                                        "percentage_used": f"{usage_percent:.1f}%",
                                    })
                                except (ValueError, IndexError):
                                    continue
            except Exception:
                pass

        # Calculate overall disk stats
        overall_usage_percent = (
            (used_space / total_space) * 100 if total_space > 0 else 0
        )

        # Format for ADK tool return structure
        return {
            "result": disk_info,
            "stats": {
                "partition_count": len(disk_info["partitions"]),
                "total_space_gb": total_space / (1024 ** 3),
                "used_space_gb": used_space / (1024 ** 3),
                "overall_usage_percent": overall_usage_percent,
                "partitions_with_high_usage": len(partitions_over_threshold),
            },
            "additional_info": {
                "data_format": "dictionary",
                "collection_timestamp": time.time(),
                "high_usage_partitions": (
                    partitions_over_threshold if partitions_over_threshold else None
                ),
            },
        }
    except Exception as e:
        return {
            "result": {"error": f"Failed to gather disk information: {str(e)}"},
            "stats": {"success": False},
            "additional_info": {"error_type": str(type(e).__name__)},
        }
