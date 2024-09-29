from openai_wrapper.base_client import BaseClient
from openai_wrapper.error_handler import handle_openai_exceptions


class ImageClient(BaseClient):
    """
    A client class for generating images using the OpenAI API.

    This class inherits from BaseClient and provides a method to generate images based on a text prompt.

    Methods:
        generate_image(prompt, n=1, size="1024x1024"): Generates images based on the provided text prompt.
    """
    def generate_image(self, prompt, n=1, size="1024x1024"):
        """
        Generates images based on the provided text prompt.

        This function makes a request to the OpenAI API to generate images from the given prompt.
        The response URLs of the generated images are returned. Any exceptions encountered during
        the process are handled using a custom exception handler.

        Args:
            prompt (str): The text prompt to generate images from.
            n (int): The number of images to generate. Default is 1.
            size (str): The size of the generated images. Default is "1024x1024".

        Returns:
            list: A list of URLs of the generated images, or None if an error occurred.

        Raises:
            Exception: Handles any exceptions that occur during the API request and response processing.
        """
        try:
            response = self.client.images.generate(
                prompt=prompt,
                n=n,
                size=size
            )
            urls = [image.url for image in response.data]
            return urls
        except Exception as e:
            handle_openai_exceptions(e, self.logger)
            return None
