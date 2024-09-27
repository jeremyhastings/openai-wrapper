import logger_setup
from client_setup import OpenAIClient
from error_handler import handle_openai_exceptions

# Call the function to configure logging
logger_setup.setup_logging()

# Example of using the logger instance
logger = logger_setup.logger

# Create an instance of OpenAIClient
client_instance = OpenAIClient()

# Get the OpenAI client object
client = client_instance.get_client()

try:
    # Example usage: Make a chat completion request to the OpenAI API
    completion = client.chat.completions.create(
        model="gpt-4o-mini",  # Specify the model to use
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            # System message setting the assistant's behavior
            {"role": "user", "content": "Write a haiku about recursion in programming."}  # User's prompt
        ]
    )

    # Print the response's content. The response contains the completion generated by the model.
    print(completion.choices[0].message.content.strip())

except Exception as e:
    # Handle any exceptions using a custom exception handler
    handle_openai_exceptions(e, logger)
