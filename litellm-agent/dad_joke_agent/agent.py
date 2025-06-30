import os
import random

from google.adk.agents import Agent
# from google.adk.models.lite_llm import LiteLLM
from litellm import LiteLLM

# https://docs.litellm.ai/docs/providers/openrouter
# model = LiteLLM(
#     # model="openrouter/google/gemini-2.0-flash-001",
#     # api_key=os.getenv("OPENROUTER_API_KEY"),
#     model="google/gemini-2.0-flash-001",
#     api_key=os.getenv("GOOGLE_API_KEY"),
# )

def get_dad_joke():
    jokes = [
        "Why did the chicken cross the road? To get to the other side!",
        "What do you call a belt made of watches? A waist of time.",
        "What do you call fake spaghetti? An impasta!",
        "Why did the scarecrow win an award? Because he was outstanding in his field!"
    ]
    return random.choice(jokes)

root_agent = Agent(
    name="dad_joke_agent",
    # model=model,
    model="gemini-2.0-flash",    description="Dad Joke Agent",
    instruction="""
    You are a helpful assistant that can tell dad jokes.
    Only use the tool 'get_dad_joke'
    """,
    tools=[get_dad_joke],
)