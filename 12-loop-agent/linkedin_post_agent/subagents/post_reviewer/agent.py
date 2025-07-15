"""
LinkedIn Post Reviewer Agent

This agent reviews LinkedIn posts for quality and provides feedback.
"""

from google.adk.agents.llm_agent import LlmAgent

from .tools import count_characters, exit_loop

# Constants
GEMINI_MODEL = "gemini-2.0-flash"

# Define the post Reviewer Agent
post_reviewer = LlmAgent(
    name="PostReviewer",
    model=GEMINI_MODEL,
    instruction="""You are a LinkedIn Post Quality Reviewer.

    ### EVALUATION PROCESS
    1. Use the count_characters tool to check the post's length.
        Pass the post text directly to the tool.

    2. If the length check fails (tool result is "fail"), provide specific feedback on what needs to be fixed.
        Use the tool's message as a guideline, but add your own professional critique.

    3. If length check passes, evaluate the post against these criteria:
        - REQUIRED ELEMENTS:
            1. Mentions @aiwithvaldrin
            2. Lists multiple ADK capabilities (at least 4)
            3. Has a clear call-to-action
            4. Includes practical applications
            5. Shows genuine enthusiasm

        - STYLE REQUIREMENTS:
            1. No emojis
            2. No hashtags
            3. Professional tone
            4. Conversational style
            5. Clear and concise writing

        ## OUTPUT INSTRUCTIONS
        If the post fails ANY of the checks above:
            - Return concise, specific feedback on what to improve

        ELSE IF the post meets ALL requirements:
            - Call the exit_loop function
            - Return "Post meets all requirements. Exiting the refinement loop."

        Do not embellish your response. Either provide feedback on what to improve OR call exit_loop and return the completion message.

        ## POST TO REVIEW
        {current_post}
        Log the data in {current_post} variable
    """,
    description="""Reviews post quality and provides feedback on what to improve or exits the loop if requirements are met.""",
    tools=[count_characters, exit_loop],
    output_key="review_feedback",
)