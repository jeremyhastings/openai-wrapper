from openai_wrapper.base_client import BaseClient
from openai_wrapper.error_handler import handle_openai_exceptions


class EmbeddingClient(BaseClient):
    """
    A client class for creating vector embeddings using the OpenAI API.

    This class inherits from BaseClient and provides a method to create vector embeddings based on input text.

    Methods:
        create_vector_embeddings(text): Creates vector embeddings for the provided text input.
    """
    def create_vector_embeddings(self, text):
        """
        Creates vector embeddings for the provided text input.

        This function makes a request to the OpenAI API to generate vector embeddings from the given text input.
        The response containing the embeddings is returned. Any exceptions encountered during
        the process are handled using a custom exception handler.

        Args:
            text (str): The text input for which to create vector embeddings.

        Returns:
            dict: A dictionary containing the embeddings response, or None if an error occurred.

        Raises:
            Exception: Handles any exceptions that occur during the API request and response processing.
        """
        try:
            response = self.client.embeddings.create(
                model="text-embedding-3-large",
                input=text
            )
            return response
        except Exception as e:
            handle_openai_exceptions(e, self.logger)
            return None
