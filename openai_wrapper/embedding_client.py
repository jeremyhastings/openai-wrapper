from openai_wrapper.client_setup import OpenAIClient
from openai_wrapper.error_handler import handle_openai_exceptions

# Create an instance of OpenAIClient
client_instance = OpenAIClient()

# Get the OpenAI client object
client = client_instance.get_client()


def create_vector_embeddings(text, logger):
    """
    Creates vector embeddings for the given text using the OpenAI API.

    This function sends a request to the OpenAI API to generate embeddings
    for the provided text and returns the response.

    Args:
        text (str): The text for which to create embeddings.
        logger (logging.Logger): The logger instance for logging errors.

    Returns:
        dict: The response from the OpenAI API containing the embeddings.
    """
    try:
        response = client.embeddings.create(
            model="text-embedding-3-large",
            input=text
        )
        return response

    except Exception as e:
        # Handle any exceptions using a custom exception handler
        handle_openai_exceptions(e, logger)
        return None
