"""launch a Gemini agent"""
import os
from google.adk.agents import Agent, SequentialAgent, ParallelAgent, LoopAgent
from google.adk.tools import google_search, AgentTool, FunctionTool
from google.adk.runners import InMemoryRunner
from google.genai import types

print("ADK components imported successfully")


research_agent = Agent(
    name="ResearchAgent",
    model="gemini-2.5-flash-lite",
    instruction="""You are a specialized research agent. Your only job is to use the
    google_search tool to find 2-3 pieces of relevant information on the given topic and present the findings with citations.
    """,
    tools=[google_search],
    output_key="final_summary"
)

print("research agent created successfully")

summarizer_agent = Agent(
    name="SummarizerAgent",
    model="gemini-2.5-flash-lite",
    instruction="""Read the provided research findings: {research_findings}.
    Create a concise summary as a bulletted list with 3-5 key points.
    """,
    tools=[google_search],
    output_key="research_findings"
)

print("summarizer agent created successfully")

root_agent = Agent(
    name="ResearchCoordinator",
    model="gemini-2.5-flash-lite",
    instruction="""YOu are a research coordinator. Your goal is to answer the user's query by orchestrating a workflow.
    1. First you MUST call the `ResearchAgent` too to find the relevant information ont the topic provided by the user.
    2. Next, after receiving the research findings, you MUST call the `SummarizerAgent` to create a concise summary.
    3. Finally, present the final summary clearly to the user as your response.
    """,
    tools=[
        AgentTool(research_agent),
        AgentTool(summarizer_agent)
    ],
)


print("Root agent created successfully")