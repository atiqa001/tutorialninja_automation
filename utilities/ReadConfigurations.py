import os
from configparser import ConfigParser


def read_configuration(category, key):
    config = ConfigParser()

    # Dynamically get the absolute path to the config file
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # project root
    config_path = os.path.join(base_dir, "configurations", "config.ini")

    files_read = config.read(config_path)

    if not files_read:
        raise FileNotFoundError(f"Could not load config file at {config_path}")

    return config.get(category, key)
