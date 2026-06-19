"""ops agent definition."""

from google.adk import Agent

agent = Agent(
    name="ops_agent",
    model="gemini-2.5-flash",
    instruction="You are the ops team lead for Forsch.",
)
