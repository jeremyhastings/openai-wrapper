# openai-wrapper

## Introduction

`openai-wrapper` is a simple Python package designed to facilitate interactions with the OpenAI API. It includes modules for setting up logging, interacting with ChatGPT, generating images, and handling exceptions.

## Setup

### Configuration

Before you can use `openai-wrapper`, you need to create a configuration file named `config.json` in the root directory of your project. This file should contain your OpenAI API key in the following format:

```json
{
    "openai_api_key": "your-key-here"
}
```

Make sure to replace `"your-key-here"` with your actual OpenAI API key.

### Installation

To get started with `openai-wrapper`, follow these steps:

1. **Clone the repository**:  
   ```sh
   git clone https://github.com/your-repo/openai-wrapper.git
   ```

2. **Navigate to the project directory**:  
   ```sh
   cd openai_wrapper
   ```

3. **Install the required packages**:  
   ```sh
   pip install -r requirements.txt
   ```

## Usage

Below is an example of how to use the main components of `openai-wrapper`:

### Example `main.py`

```python

from config import logging_setup
from chatgpt_client import generate_text
from image_client import generate_image

# Call the function to configure logging
logger_setup.setup_logging()

# Example of using the logger instance
logger = logger_setup.logger


def display_menu():
   """
   Displays the menu options to the user.

   This function prints the options available for the user to interact
   with the OpenAI API. Currently, the options include sending a
   question to ChatGPT and generating an image.
   The user can also type 'EXIT' to quit the program.
   """
   print("Menu:")
   print("1. Generate Text")
   print("2. Generate an image")
   print("Type 'EXIT' to quit")
   print()


# Prompt the user for input in a loop
if __name__ == '__main__':
   """
   Main loop for user interaction with the OpenAI API.

   This loop continuously displays the menu to the user, accepts user 
   input for various options, and processes the input accordingly. 
   The user can choose to send a prompt to ChatGPT for a text response 
   or generate an image. The loop continues until the user types 'EXIT'.
   """
   while True:
      display_menu()
      user_choice = input("Choose an option: ")

      # Check if the user wants to exit
      if user_choice.upper() == 'EXIT':
         print("Exiting the program...")
         break

      if user_choice == '1':
         user_input = input("Enter your prompt for ChatGPT: ")
         # Send prompt to ChatGPT and display the response
         generate_text(user_input, logger)

      elif user_choice == '2':
         user_input = input("Enter your prompt for image generation: ")
         # Generate image based on the prompt and display the URLs
         generate_image(user_input, logger)

      else:
         print("Invalid choice. Please select a valid option.")
```

### Logging

The logging is configured using a dedicated setup function in `logger_setup.py`. Ensure that logging is set up before making any API requests to capture any logs or errors.

### Exception Handling

The `handle_openai_exceptions` function in `error_handler.py` processes and logs various OpenAI API exceptions. This ensures that your application gracefully handles errors and provides meaningful log messages for debugging.

### Individual Modules

#### `chatgpt_client.py`

This module includes a function `send_prompt_to_chatgpt` which sends a text prompt to the ChatGPT API and prints the response.

#### `image_client.py`

This module includes a function `generate_image` which sends an image generation request to the OpenAI API and prints the URLs of the generated images.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.