## Multi-Agent Systems in ADK

This example demonstrates how to create a multi-agent system in ADK, where specialized agents collaborate to handle complex tasks, each focusing on their area of expertise.

## What is a Multi-Agent System?

A Multi-Agent System is an advanced pattern in the Agent Development Kit (ADK) that allows multiple specialized agents to work together to handle complex tasks. Each agent can focus on a specific domain or functionality, and they can collaborate through delegation and communication to solve problems that would be difficult for a single agent.

## Essential Structure Components:

### 1. Root Agent Package

- Must have the standard agent structure (like in the basic agent example)
- The agent.py file must define a root_agent variable

### 2. Sub-agents Directory

- Typically organized as a directory called sub_agents inside the root agent folder
- Each sub-agent should be in its own directory following the same structure as regular agents

### 3. Importing Sub-agents

- Root agent must import sub-agents to use them:

```
from .sub_agents.funny_nerd.agent import funny_nerd
from .sub_agents.stock_analyst.agent import stock_analyst
```

### 4. Command Location

- Always run `adk web` from the parent directory (`7-multi-agent`), not from inside any agent directory

This structure ensures that ADK can discover and correctly load all agents in the hierarchy

## Running the Example

To run the multi-agent example:

```bash
adk web
```
