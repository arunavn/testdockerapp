import os

def set_all_variable(env_dict):
  for k, v in env_dict:
    os.environ[k] = str(v)
