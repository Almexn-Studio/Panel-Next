import toml

config = toml.load("config.toml")

def get(group=None,key=None):
    if group is None:
        return config[key]
    if key is None:
        return config[group]
    return config[group][key]