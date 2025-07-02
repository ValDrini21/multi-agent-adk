# Structured Outputs in ADK

This example demonstrates how to implement structured outputs in the Agent Development Kit
(ADK) using Pydantic models. The main agent is this example, `email_generator`, uses the
`output_schema` parameter to ensure its responses conform to a specific structured format.

## What are Structured Outputs?

ADK allows you to define structured data formats for agent inputs and outputs using Pydantic models:

1. **Controlled Output Format**: Using `output_schema` ensures the LLM produces respones in a
   consistent JSON structure
2. **Data Validation**: Pydantic validates that all required fields are present and correctly
   formatted
3. **Improved Downstream Processing**: Structured outputs are easier to handle in downstream
   applications or by other agents

Use structured outputs when you need guaranteed format consistency for integration with other
systems or agents.

## Email Generator Example

In this example, we've created an email generator agent that produces structured output with:
