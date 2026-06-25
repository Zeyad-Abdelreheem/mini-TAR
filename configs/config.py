
# from kaggle_secrets import UserSecretsClient

# user_secrets = UserSecretsClient()
# CACHE_DIR = user_secrets.get_secret("HF_DATASETS_CACHE")
# HF_HOME = user_secrets.get_secret("HF_HOME")
# TOKEN = user_secrets.get_secret("HF_TOKEN")
# SAVE_MODELS_DIR = user_secrets.get_secret("SAVE_MODELS_DIR")
# USER = user_secrets.get_secret("USER")

import os

TOKEN = os.environ["HF_TOKEN"]
CACHE_DIR = os.environ["HF_DATASETS_CACHE"]

HF_HOME = os.environ["HF_HOME"]
SAVE_MODELS_DIR = os.environ["SAVE_MODELS_DIR"]
USER = os.environ["USER"]
