import os
from configparser import ConfigParser


def read_configuration(category, key):
    config = ConfigParser()

    # Dynamically get the absolute path to the config file
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    config_path = os.path.join(base_dir, "configurations", "config.ini")

    if not config.read(config_path):
        raise FileNotFoundError(f"Could not load config file at {config_path}")

    return config.get(category, key)
