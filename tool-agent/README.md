# Tool Agent Example

## What is a Tool Agent?

A Tool Agent extends the basic ADK agent by incorporating tools that allow the agent to perform actions beyond just generating text responses. Tools enable agents to interact with external systems, retrieve information, and perform specific functions to accomplish tasks more effectively.

In this example, we demonstrate how to build an agent that can use built-in tools (like Google Search) and custom function tools to enhance its capabilities.

## Key components

### 1. Built-in Tools

ADK provides several built-in tools that you can use with your agents:

- **Google Search**: Allows your agent to search the web for information
- **Code Execution**: Enables your agent to run code snippets
- **Vertex AI Search**: Lets your agent search through your own data

**Important Note**: Currently, for each root agent or single agent, only one built-in
