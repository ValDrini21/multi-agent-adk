from google.adk.agents import Agent
from google.adk.tools import google_search
from datetime import datetime

def get_current_time() -> dict:
    """
    Get the current time in the format DD.MM.YYYY HH:MM:SS
    """
    return {
        "current_time": datetime.now().strftime("%d.%m.%Y %H:%M:%S"),
    }

root_agent = Agent(
    name="tool_agent",
    model="gemini-2.0-flash",
    description="Tool agent",
    instruction="""
    You are a helpful assistant that can use the following tools:
    - get_current_time
    """,
    # tools=[google_search],
    tools=[get_current_time],
    # tools=[google_search, get_current_time], # <-- Doesn't work
)