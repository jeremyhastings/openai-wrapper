import logging

def setup_logging():
    """
    Sets up the logging configuration.

    This function configures the root logger to log messages to a file named 'app.log'.
    The log messages will be appended to the file (if it exists) and will include the timestamp,
    log level, and message. The logging level is set to INFO, which means it will capture
    INFO, WARNING, ERROR, and CRITICAL messages.

    Log format:
        %(asctime)s - %(levelname)s - %(message)s
        Example: 2023-10-05 10:20:30,123 - INFO - This is an info message

    File handler:
        - Filename: 'app.log'
        - File mode: 'a' (append mode)
        - Log level: INFO

    Usage:
        Call this function at the beginning of your application to configure logging.
    """
    logging.basicConfig(
        filename='app.log',
        filemode='a',  # Append mode
        format='%(asctime)s - %(levelname)s - %(message)s',
        level=logging.INFO
    )

# Optional: Example of setting up a specific named logger if you need to use named loggers
logger = logging.getLogger('openai_wrapper_logger')