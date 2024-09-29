import textwrap
from openai_wrapper.base_client import BaseClient
from openai_wrapper.error_handler import handle_openai_exceptions


class TextClient(BaseClient):
    """
    A client class for generating text using the OpenAI API.

    This class inherits from BaseClient and provides methods to send prompts
    to the OpenAI ChatGPT model and format the responses.

    Methods:
        wrap_text(text, width=150): Wraps the given text to the specified width while preserving pre-existing line breaks.
        generate_text(user_input): Sends a prompt to the ChatGPT model and returns the formatted response.
    """

    def wrap_text(self, text, width=150):
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
        wrapped_lines = []
        for line in text.splitlines():
            wrapped_lines.extend(wrapper.wrap(line))
        return "\n".join(wrapped_lines)

    def generate_text(self, user_input):
        """
        Sends a prompt to the ChatGPT model and returns the formatted response.

        This function makes a chat completion request to the OpenAI API using the provided user prompt.
        The response from the API is then wrapped to a specified width and returned.
        Any exceptions encountered during the process are handled using a custom exception handler.

        Args:
            user_input (str): The user's input to send to the ChatGPT model.

        Returns:
            str: The wrapped content from the ChatGPT response, or None if an error occurred.

        Raises:
            Exception: Handles any exceptions that occur during the API request and response processing.
        """
        try:
            completion = self.client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": user_input}
                ]
            )
            response_content = completion.choices[0].message.content.strip()
            wrapped_content = self.wrap_text(response_content)
            return wrapped_content
        except Exception as e:
            handle_openai_exceptions(e, self.logger)
            return None
