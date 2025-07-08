# Stateful Multi-Agent Systems in ADK

This example demonstrates how to create a stateful multi-agent system in ADK, combining the power of persistent state management with specialized agent delegation. This approach creates intelligent agent systems that remember user information across interactions while leveraging specialized domain expertise.

## What is a Stateful Multi-Agent System?

A Stateful Multi-Agent System combines two powerful patterns:

    1. **State Management**: Persisting information about users and conversations across interactions
    2. **Multi-Agent Architecture**: Distributing tasks among specialized agents based on their expertise

The result is a sophisticated agent ecosystem that can:

    - Remember user information and interaction history
    - Route queries to the most appropriate specialized agent
    - Provide personalized responses based on past interactions
    - Maintain context across multiple agent delegates

This example implements a customer service system for an online course platform, where specialized agents handle different aspects of customer support while sharing a common state.

## Key Components

### 1. Session Management

The example uses `InMemorySessionService` to store session state:

### 2. State Sharing Across Agents

All agents in the system can access the same session state, enabling:

    - Root agent to track interaction history
    - Sales agent to update purchased courses
    - Course support agent to check if user has purchased specific courses
    - All agents to personalize responses based on user information

### 3. Multi-Agent Delegation

The customer service agent routes queries to specialized sub-agents:

## How It Works

1. **Initial Session Creation**:

   - A new session is created with user information and empty interaction history
   - Session state is initialized with default values

2. **Conversation Tracking**:

   - Each user message is added to interaction_history in the state
   - Agents can review past interactions to maintain context

3. **Query Routing**:

   - The root agent analyzes the user query and decides which specialist should handle it
   - Specialized agents receive the full state context when delegated to

4. **State Updates**:

   - When a user purchases a course, the sales agent updates `purchased_courses`
   - These updates are available to all agents for future interactions

5. **Personalized Responses**:
   - Agents tailor responses based on purchase history and previous interactions
   - Different paths are taken based on what the user has already purchased

### Running the Example

```bash
    python main.py
```

## Production Considerations

For a production implementation, consider:

    1. ***Persistent Storage***: Replace ```InMemorySessionService``` with ```DatabaseSessionService``` to persist state across application restarts
    2. ***User Authentication***: Implement proper user authentication to securely identify users
    3. ***Error Handling***: Add robust error handling for agent failures and state corruption
    4. ***Monitoring***: Implement logging and monitoring to track system performance
