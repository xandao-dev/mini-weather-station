import json


def load(env_file_path):
    f = open(env_file_path, "r")
    env = json.loads(str(f.read()))
    f.close()
    return env
