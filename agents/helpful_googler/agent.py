"""launch a Gemini agent"""
import os
from google.adk.agents import Agent
from google.adk.tools import google_search
from google.adk.runners import InMemoryRunner
from google.adk.tools import google_search
from google.genai import types

print("ADK components imported successfully")

root_agent = Agent(
    name="helpful_assistant",
    model="gemini-2.5-flash",
    description="A helpful assistant that can answer questions and perform tasks.",
    instruction="You are a helpful assistant. Use google search to find current information or answer questions if you are unsure.",
    tools=[google_search]
)

print("Root agent created successfully")