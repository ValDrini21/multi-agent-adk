# LiteLLM Agent Example

LiteLLM is a Python library that provides a unified interface for interacting with multiple
Large Language Model (LLM) providers through a single, consistent API. It servers as an
adapter that allows you to:

- Use the same code to access 100+ different LLMs from providers like OpenAI, Anthropic,
  Google, AWS Bedrock, and more
- Standardize inputs and outputs across different LLM providers
- Track costs, manage API keys, and handle errors consistently
- Implement fallbacks and load balancing across different models

In essence, LiteLLM acts as a unified wrapper that makes it easy to switch between different LLM
providers without changing your application code.

## Why Use LiteLLM with ADK?

The Agent Development Kid (ADK) is designed to be model-agnostic, meaning it can work with
various LLM providers. LiteLLM enhances this capability by:
