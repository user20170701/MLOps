import argparse
import os

import yaml
from dotenv import load_dotenv

from settings import Settings


def export_envs(environment: str = "dev") -> None:
    env_file_path = f"config/.env.{environment}"
    if not os.path.exists(env_file_path):
        raise FileNotFoundError(f"Config file not found: {env_file_path}")
    load_dotenv(env_file_path)


def export_secrets(secrets_path: str = "secrets.yaml") -> None:
    with open(secrets_path) as secrets_file:
        secrets = yaml.safe_load(secrets_file)
    if "sops" in secrets:
        raise RuntimeError(f"{secrets_path} is encrypted, decrypt it with sops first")
    for key, value in secrets.items():
        os.environ[key] = str(value)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Load environment variables from specified .env file."
    )
    parser.add_argument(
        "--environment",
        type=str,
        default="dev",
        help="The environment to load (dev, test, prod)",
    )
    args = parser.parse_args()

    export_envs(args.environment)
    export_secrets()

    settings = Settings()

    print("APP_NAME: ", settings.APP_NAME)
    print("ENVIRONMENT: ", settings.ENVIRONMENT)
    print("API_KEY: ", settings.API_KEY)
