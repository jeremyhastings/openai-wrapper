import json
import openai
from openai import OpenAI


class OpenAIClient:
    """
    A client for interacting with the OpenAI API.

    This class is responsible for loading API configuration,
    initializing the OpenAI client, and providing access to
    the client for making API requests.

    Attributes:
        config_file_path (str): Path to the configuration file.
        api_key (str): OpenAI API key.
        client (OpenAI): Initialized OpenAI client.
    """

    def __init__(self, config_file_path='config.json'):
        """
        Initializes the OpenAIClient with the given configuration file path.

        Args:
            config_file_path (str): Path to the JSON configuration file. Default is 'config.json'.
        """
        self.config_file_path = config_file_path
        self.api_key = None
        self.client = None
        self._load_config()
        self._initialize_client()

    def _load_config(self):
        """
        Loads the API configuration from the JSON file.

        Reads the configuration file to retrieve the OpenAI API key,
        validates it, and sets the OpenAI API key.

        Raises:
            ValueError: If the API key is not found in the configuration file.
        """
        # Load the JSON configuration file
        with open(self.config_file_path, 'r') as config_file:
            config = json.load(config_file)

        # Access the API key
        self.api_key = config.get('openai_api_key')

        # Validate the API key
        if not self.api_key:
            raise ValueError("API key not found in config.json")

        # Set the OpenAI API key
        openai.api_key = self.api_key

    def _initialize_client(self):
        """
        Initializes the OpenAI client using the loaded API key.

        Sets the client attribute to an instance of the OpenAI client.
        """
        self.client = OpenAI(api_key=self.api_key)

    def get_client(self):
        """
        Returns the initialized OpenAI client.

        Returns:
            OpenAI: The initialized OpenAI client instance.
        """
        return self.client
