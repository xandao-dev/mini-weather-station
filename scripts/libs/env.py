from json import loads as json_loads


def load(env_file_path):
    f = open(env_file_path, "r")
    env = json_loads(str(f.read()))
    f.close()
    return env
