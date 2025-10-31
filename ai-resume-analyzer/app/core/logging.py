import logging
import sys

def setup_logging(log_level=logging.INFO):
    """
    Set up logging configuration for the application.

    Args:
        log_level (int): The logging level to set. Defaults to logging.INFO.
    """
    logging.basicConfig(
        level=log_level,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.StreamHandler(sys.stdout),
            logging.FileHandler('app.log')
        ]
    )

# Initialize logging
setup_logging()