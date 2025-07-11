# Parallel Agents in ADK

This example demonstrates how to implement a Parallel Agent in the Agent Development kit (ADK). The main agent in this example, `system_monitor_agent`, uses a Parallel Agent to gather system information concurrently and then synthesizes it into a comprehensive system health report.

## What are Parallel Agents?

Parallel Agents are workflow agents in ADK that:

    1. ***Execute Concurrently***: Sub-agents run simultaneously rather than sequentially
    2. ***Operate Independently***: Each sub-agent works independently without sharing state during execution
    3. ***Improve Performance***: Dramatically speed up workflows where tasks can be performed in parallel

Use Parallel Agents when you need to execute multiple independent tasks efficiently and time is a critical factor.

## System Monitoring Example

In this example, we've created a system monitoring application that uses a Parallel Agent to gather system information. The workflow consists of:

    1. ***Parallel System Information Gathering***: Using a ```ParallelAgent``` to concurrently collect data about:

        - CPU usage and statistics
        - Memory utilization
        - Disk space and usage

    2. Sequential Report Synthesis: After parallel data collection, a synthesizer agent combines all information into a comprehensive report

    ### Sub-Agents

        1. CPU Info Agent: Collects and analyzes CPU information

            - Retrieves core counts, usage statistics, and performance metrics
            - Identifies potential performance issues (high CPU usage)

        2. Memory Info Agent: Gathers memory usage information

            - Collects total, used, and available
            - Analyzes memory pressure and swap usage

        3. Disk Info Agent: Analyzes disk space and usage

            - Reports on total, used, and free disk space
            - Identifies disks that are running low on space

        4. System Report Synthesizer: Combines all gathered information into a comprehensive system health report

            - Creates an executive summary of system health
            - Organizes component-specific information into sections
            - Provides recommendations based on system metrics

    ### How It Works

    The architecture combines both parallel and sequential workflow patterns:

        1. First, the ```system_info_gather``` Parallel Agent runs all three information agents concurrently
        2. Then, the ```system_report_synthesizer``` uses the collected data to generate a final report

    This hybrid approach demonstrates how to combine workflow agent types for optimal performance and logical flow.

    ### Running the Example

    ```bash
        cd 11-parallel-agent
        adk web
    ```
    Then select "system_monitor_agent" from the dropdown menu in the web UI.

## Example Interactions

Try these example prompts:

```bash
    Check my system health
```

```bash
    Provide a comprehensive system report with recommendations
```

```bash
    Is my system running out of memory or disk space?
```

## Key Concepts: Independent Execution

One key aspect of Parallel Agents is that sub-agents run independently without sharing state during execution. In this example:

    1. Each information gathering agent operates in isolation
    2. The results from each agent are collected after parallel execution completes
    3. The synthesizer agent then uses these collected results to create the final report

This approach is ideal for scenarios where tasks are completely independent and don't require interaction during execution.

## How Parallel Agents Compare to Other Workflow Agents

ADK offers different types of workflow agents for different needs:

    - Sequential Agents: For strict, ordered execution where each step depends on previous outputs
    - Loop Agents: For repeated execution of sub-agents based on conditions
    - Parallel Agents: For concurrent execution of independent sub-agents (like this example)
