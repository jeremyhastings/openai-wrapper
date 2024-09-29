import textwrap
from openai_wrapper.client_setup import OpenAIClient
from openai_wrapper.error_handler import handle_openai_exceptions

# Create an instance of OpenAIClient
client_instance = OpenAIClient()

# Get the OpenAI client object
client = client_instance.get_client()


# Function to wrap text while preserving pre-existing line breaks
def wrap_text(text, width=150):
    """
    Wraps the given text to the specified width while preserving pre-existing line breaks.

    This function splits the given text into lines and wraps each line individually,
    ensuring that the whitespace within the text is preserved.

    Args:
        text (str): The text to wrap.
        width (int): The width to wrap the text at. Default is 150 characters.

    Returns:
        str: The wrapped text, preserving the original line breaks.
    """
    wrapper = textwrap.TextWrapper(width=width, replace_whitespace=False, drop_whitespace=False)
    # Split text into lines, wrap each line individually
    wrapped_lines = []
    for line in text.splitlines():
        wrapped_lines.extend(wrapper.wrap(line))
    return "\n".join(wrapped_lines)


def generate_text(user_input, logger):
    """
    Sends a prompt to the ChatGPT model and prints the formatted response.

    This function makes a chat completion request to the OpenAI API using the provided user prompt.
    The response from the API is then wrapped to a specified width and printed to the console.
    Any exceptions encountered during the process are handled using a custom exception handler.

    Args:
        user_input (str): The user's input to send to the ChatGPT model.
        logger (logging.Logger): The logger instance for logging errors.

    Returns:
        str: The wrapped content from the ChatGPT response.

    Raises:
        Exception: Handles any exceptions that occur during the API request and response processing.
    """
    try:
        # Example usage: Make a chat completion request to the OpenAI API with user input
        completion = client.chat.completions.create(
            model="gpt-4o-mini",  # Specify the model to use
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_input}  # User's prompt
            ]
        )

        # Get the response content
        response_content = completion.choices[0].message.content.strip()  # Clean response

        # Wrap the text content
        wrapped_content = wrap_text(response_content)

        return wrapped_content

    except Exception as e:
        # Handle any exceptions using a custom exception handler
        handle_openai_exceptions(e, logger)
        return None
