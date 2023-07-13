# Implement Authentication System

import json


def init():
    """Use functions given below to generate or load Config.json"""
    try:
        # load config.json if it exists
        cfg_object = load_config()
    except Exception:
        # start config.json initialization if file doesnt exist.
        cfg_object = auth_gen_interactive()

    return cfg_object


def auth_gen(username, useragent, keylist, default_type):
    """Function to Generate config.json based on given inputs."""

    # Initialize config dict
    config = {}

    # Set values for config
    config["useragent"] = useragent
    config["username"] = username
    config["default_type"] = default_type
    config["keylist"] = keylist

    with open("config.json", "w+") as f:
        json.dump(config, f, indent=4)

    return config


# Interactive function to Generate config.json
def auth_gen_interactive():
    print("Config not found.\nCreating new config file. Please enter your credentials.")

    # initializing var
    user_agent = input("Enter User Agent: ")
    user_name = input("Enter default username: ")
    default_type = input("Enter default type (JSON or CSV): ").lower()
    print()
    keyls = []

    # Fetch n
    notNum = True
    while notNum is True:
        n = input("Enter Number of Keys: ")
        try:
            n = int(n)
        except Exception:
            pass
        if type(n) == int:
            notNum = False
            n = int(n)

    # Fetch n keys
    for i in range(n):
        new_key = input("Enter Key {} (leave blank if unavailable): ".format(i + 1))
        keyls.append(new_key)

    # Remove Redundant keys
    for i in range(len(keyls)):
        k = keyls[i]
        if k == "":
            keyls.pop(i)

    config = auth_gen(
        username=user_name,
        useragent=user_agent,
        keylist=keyls,
        default_type=default_type,
    )
    print("Your configuration has been saved to config.json!\n")
    config = load_config()

    return config


# return an auth object
def load_config():
    with open("config.json", "r") as f:
        config = json.load(f)

    # New class Conf that takes in newly loaded config
    class Config:
        useragent = ""
        username = ""
        type = ""
        keylist = []
        num = 0

        def __init__(self, cfg):
            self.useragent = cfg["useragent"]
            self.username = cfg["username"]
            self.keylist = cfg["keylist"]
            self.type = cfg["default_type"]
            self.file_name = cfg["username"] + "." + cfg["default_type"]
            self.num = -1

        def getKey(self):
            # Return keys one by one from the key list

            length = len(self.keylist)

            if self.num == length - 1:
                self.num = -1

            self.num += 1

            return self.keylist[self.num]

    print("Config Loaded Successfully.")
    return Config(config)
