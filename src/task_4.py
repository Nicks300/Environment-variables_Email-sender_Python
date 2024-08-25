from typing import Dict
from src.config_4 import Configuration
import json


def main() -> Dict:
    DOCTORS_DIR = "doctors"

    configuration = Configuration()
    with open(f"{configuration.base_folder}/{DOCTORS_DIR}/{configuration.login}.json", 'r') as f:
        dictionary = json.load(f)
    return dictionary


if __name__ == "__main__":
    (main())
