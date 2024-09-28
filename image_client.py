from client_setup import OpenAIClient
from error_handler import handle_openai_exceptions

# Create an instance of OpenAIClient
client_instance = OpenAIClient()

# Get the OpenAI client object
client = client_instance.get_client()


def generate_image(prompt, logger, n=1, size="1024x1024"):
    """
    Generates images based on a given prompt using the OpenAI API and returns their URLs.

    This function interacts with the OpenAI API to generate images based on the provided prompt.
    It logs any exceptions that occur during the process.

    Args:
        prompt (str): The text prompt to generate images from.
        logger (logging.Logger): The logger instance for logging errors.
        n (int): The number of images to generate. Default is 1.
        size (str): The size of the images to generate. Default is "1024x1024".

    Returns:
        list: A list of URLs pointing to the generated images, or None if an error occurred.

    Raises:
        Exception: Handles any exceptions that occur during the API request and response processing.
    """
    try:
        # Example usage: Make an image generation request to the OpenAI API
        response = client.images.generate(
            prompt=prompt,
            n=n,
            size=size
        )

        urls = [image.url for image in response.data]
        for url in urls:
            print(url)
        return urls

    except Exception as e:
        # Handle any exceptions using a custom exception handler
        handle_openai_exceptions(e, logger)
        return None