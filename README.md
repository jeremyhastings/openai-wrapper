# openai-wrapper

## Introduction

`openai-wrapper` is a simple Python package designed to facilitate interactions with the OpenAI API. It includes modules for setting up logging, handling OpenAI clients, and processing and handling OpenAI exceptions.

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
   cd openai-wrapper
   ```

3. **Install the required packages**:  
   ```sh
   pip install -r requirements.txt
   ```

### Usage

Below is an example of how to use the main components of `openai-wrapper` in your `main.py`:

```python
import logger_setup
from client_setup import OpenAIClient
from error_handler import handle_openai_exceptions

# Call the function to configure logging
logger_setup.setup_logging()

# Example of using the logger instance
logger = logger_setup.logger

client_instance = OpenAIClient()
client = client_instance.get_client()

try:
    # Example usage: Make a chat completion request
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Write a haiku about recursion in programming."}
        ]
    )

    # Print the response
    print(completion.choices[0].message["content"].strip())

except Exception as e:
    handle_openai_exceptions(e, logger)
```

This script demonstrates how to set up logging, initiate the OpenAI client, and handle potential exceptions when making a completion request to the OpenAI API.

### Logging

The logging is configured using a dedicated setup function in `logger_setup.py`. Ensure that logging is set up before making any API requests to capture any logs or errors.

### Exception Handling

The `handle_openai_exceptions` function in `error_handler.py` processes and logs various OpenAI API exceptions. This ensures that your application gracefully handles errors and provides meaningful log messages for debugging.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.