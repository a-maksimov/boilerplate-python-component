from pathlib import Path

import yaml

CONFIG_FILENAME = "config.yaml"
ABS_TOLERANCE = 1e-4
REL_TOLERANCE = 1e-4


def get_config_file_path(filename: str) -> Path:
    """Get the full path to the configuration file."""
    return Path(__file__).parent / filename


def load_config(file_path: Path) -> dict:
    """Load the YAML configuration file."""
    try:
        with open(file_path, "r") as file:
            return yaml.safe_load(file)
    except FileNotFoundError:
        raise FileNotFoundError(f"Configuration file '{file_path}' not found.")
    except yaml.YAMLError as e:
        raise RuntimeError(f"Error parsing YAML file: {e}")


# Load configuration
config_file_path = get_config_file_path(CONFIG_FILENAME)
config_yml = load_config(config_file_path)

test_config = {item["name"]: item for item in config_yml.get("test_data", [])}
