# Callbacks in ADK

This example demonstrates how to use callbacks in the Agent Development Kit (ADK) to intercept and modify agent behavior at different stages of execution. Callbacks provide powerful hooks into the agent's lifecycle, allowing you to add custom logic for monitoring, logging, content filtering, and result transformation.

## What are Callbacks in ADK?

Callbacks are functions that execute at specific points in an agent's execution flow. They allow you to:

    1. Monitor and Log: Track agent activity and performance metrics
    2. Filter Content: Block inappropriate requests or responses
    3. Transform Data: Modify inputs and outputs in the agent workflow
    4. Implement Security Policies: Enforce compliance and safety measures
    6. Add Custom Logic: Insert business-specific processing into the agent flow

ADK provides several types of callbacks that can be attached to different components of your agent system.

## Callback Parameters and Context

Each type of callback provides access to specific context objects that contain valuable information about the current execution state. Understanding these parameters is key to building effective callbacks.

### Callback Context

The `CallbackContext` object is provided to all callback types and contains:

    * ```agent_name```: The name of the agent being executed
    *```invocation_id```: A unique identifier for the current agent invocation
    *```state```: Access to the session state, allowing you to read/write persistent data
    *```app_name```: The name of the application
    *```user_id```: The ID of the current user
    *```session_id```: The ID of the current session

### ToolContext (for Tool Callbacks)

The `ToolContext` object is provided to tool callbacks and contains:

    *```agent_name```: The name of the agent that initiated the tool call
    *```state```: Access to the session state, allowing tools to read/modify shared data
    *```properties```: Additional properties specific to the tool execution

### LlmRequest (for Model Callbacks)

The `LlmRequest` object is provided to the before_model_callback and contains:

    *```contents```: List of Content objects representing the conversation history
    *```generation_config```: Configuration for the model generation
    *```safety_settings```: Safety settings for the model
    *```tools```: Tools provided to the model

### LlmResponse (for Model Callbacks)

The `LlmResponse` object is returned from the model and provided to the after_model_callback:

    *```content```: Content object containing the model's response
    *```tool_calls```: Any tool calls the model wants to make
    *```usage_metadata```: Metadata about the model usage (tokens, etc.)

## Types of Callbacks Demonstrated

This project includes three examples of callback patterns:

1. Agent Callbacks (`before_after_agent/`)

   - Before Agent Callback: Runs at the start of agent processing
   - After Agent Callback: Runs after the agent completes processing

2. Model Callbacks (`before_after_model/`)

   - Before Model Callback: Intercepts requests before they reach the LLM
   - After Model Callback: Modifies responses after they come from the LLM

3. Tool Callbacks (`before_after_tool`)
   - Before Tool Callback: Modifies tool arguments or skips tool execution
   - After Tool Callback: Enhances tool responses with additional information

## Example 1: Agent Callbacks

The agent callbacks example demonstrates: 1. Request Logging: Recording when requests start and finish 2. Performance Monitoring: Measuring request duration 3. State Management: Using session state to track request counts

Testing Agent Callbacks

Any interaction will demonstrate the agent callbacks, which log requests and measure duration

## Example 2: Model Callbacks

The model callbacks example demonstrates:

    1. Content Filtering: Blocking inappropriate content before it reaches the model
    2. Response Transformation: Replacing negative words with more positive alternatives

#### Testing Model Callbacks

To test content filtering in the before_model_callback:

    * "This website sucks, can you help me fix it?"
    * "Everything about this project sucks."

To test word replacement in the after_model_callback:

    * "What's the biggest problem with machine learning today?"
    * "Why is debugging so difficult in complex systems?"
    * "I have a problem with my code that's very difficult to solve."

## Example 3: Tool Callbacks

The tool callbacks example demonstrates:

    1. Argument Modification: Transforming input arguments before tool execution
    2. Request Blocking: Preventing certain tool calls completely
    3. Response Enhancement: Adding additional context to tool responses
    4. Error Handling: Improving error messages for better user experience

#### Testing Tool Callbacks

To test argument modification:

    * "What is the capital of USA?"" (converts to "United States")
    * "What is the capital of Merica?" (converts to "United States")

To test request blocking:

    * "What is the capital of restricted?" (blocks the request)

To test response enhancement:

    * "What is the capital of the United States?" (adds a patriotic note)

To see normal operation:

    * "What is the capital of France?" (no modifications)

## Running the Examples

```bash
    cd 9-callbacks
    adk web
```

Then select the agent you want to test from the dropdown menu in the web UI:

    * "before_after_agent" to test agent callbacks
    * "before_after_model" to test model callbacks
    * "before_after_tool" to test tool callbacks
