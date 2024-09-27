import openai
import re
import ast
import json


def process_error_message(error_message_str, logger):
    """
    Process and log error messages by extracting JSON portions if available.

    This function attempts to extract a JSON portion from a string containing an error message,
    process the JSON to obtain a more user-friendly message, and log the error details using a logger.

    Args:
        error_message_str (str): The error message string containing potential JSON text.
        logger (logging.Logger): The logger instance used for logging error details.

    Raises:
        n/a: Any exceptions related to JSON decoding and evaluation are logged and handled within the function.
    """
    # Extract JSON portion using regex
    json_str_match = re.search(r"({.*})", error_message_str)
    if json_str_match:
        json_str = json_str_match.group(1)
        try:
            # Safely evaluate the string as a Python literal
            error_dict = ast.literal_eval(json_str)
            # Convert the Python dictionary to JSON string and then back to dictionary
            error_dict_json = json.dumps(error_dict)
            error_dict_final = json.loads(error_dict_json)

            # Access the message
            user_message = error_dict_final['error']['message']
            print(user_message)
            logger.error(f"Error: {error_dict_final}")
        except (json.JSONDecodeError, ValueError) as decode_error:
            logger.error(f"Error decoding JSON: {decode_error}")
            print("An internal error occurred while processing the error message.")
    else:
        print("No JSON part found in the error message.")
        logger.error(f"Error message: {error_message_str}")


def handle_openai_exceptions(e, logger):
    """
    Handle different OpenAI exceptions and log them accordingly.

    This function identifies the type of OpenAI exception raised, processes the error message,
    and logs it using a specified logger. It handles common OpenAI exceptions (APIConnectionError,
    RateLimitError, APIStatusError, APIError) and prints/logs user-friendly messages for unknown exceptions.

    Args:
        e (Exception): The exception object raised by OpenAI API methods.
        logger (logging.Logger): The logger instance used for logging error details.

    Raises:
        n/a: Any exceptions related to JSON decoding and evaluation are logged and handled within the function.
    """
    if isinstance(e, openai.APIConnectionError):
        error_message_str = e.message or "The server could not be reached."
    elif isinstance(e, openai.RateLimitError):
        error_message_str = e.message or "A 429 status code was received; we should back off a bit."
    elif isinstance(e, openai.APIStatusError):
        error_message_str = e.message or "A non-success status code was received."
    elif isinstance(e, openai.APIError):
        error_message_str = e.message or "An API error occurred. Please try again later."
    else:
        # General exception handling
        user_message = "An unexpected error occurred. Please try again later."
        print(user_message)
        logger.error(f"Unexpected error: {e}")
        return

    process_error_message(error_message_str, logger)
