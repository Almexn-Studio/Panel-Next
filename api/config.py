import toml

config = toml.load("config.toml")

def get_config(group=None,key=None):
    if group is None:
        return config[key]
    return config[group][key]