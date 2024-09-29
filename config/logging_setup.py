import logging
import logging.config
import json
import os

def setup_logging(default_path='config/logging_config.json', default_level=logging.INFO, env_key='LOG_CFG'):
    """
    Sets up the logging configuration.

    This function configures the root logger based on a configuration file in JSON format.
    If the configuration file is not found, it defaults to basic logging configuration.

    Args:
        default_path (str): Path to the logging configuration file. Default is 'config/logging_config.json'.
        default_level (int): Default logging level if the configuration file is not found. Default is logging.INFO.
        env_key (str): Environment variable that can override the default path to the configuration file. Default is 'LOG_CFG'.

    Logging Configuration:
        The logging configuration should be specified in a JSON file with the following structure:
        {
            "version": 1,
            "disable_existing_loggers": false,
            "formatters": {
                "standard": {
                    "format": "%(asctime)s - %(levelname)s - %(message)s"
                }
            },
            "handlers": {
                "file_handler": {
                    "class": "logging.FileHandler",
                    "formatter": "standard",
                    "filename": "../app.log",
                    "mode": "a"
                },
                "console": {
                    "class": "logging.StreamHandler",
                    "formatter": "standard"
                }
            },
            "root": {
                "handlers": ["file_handler", "console"],
                "level": "INFO"
            },
            "loggers": {
                "openai_wrapper_logger": {
                    "handlers": ["file_handler"],
                    "level": "INFO",
                    "propagate": false
                }
            }
        }

    Example Usage:
        Call this function at the beginning of your application to configure logging:

            import logging_setup
            logging_setup.setup_logging()

        Optionally, set the environment variable to use a different logging configuration:

            export LOG_CFG=/path/to/your/logging_config.json

    If the configuration file is not found, a default logging configuration will be used.
    """
    path = default_path
    value = os.getenv(env_key, None)
    if value:
        path = value
    if os.path.exists(path):
        with open(path, 'rt') as f:
            config = json.load(f)
        logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=default_level)

# Optional: Example of setting up a specific named logger if you need to use named loggers
logger = logging.getLogger('openai_wrapper_logger')