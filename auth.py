# Implement Authentication System

import json

# Use functions given below to generate or load Config.json
def initialize():
    try:
        #load config.json if it exists
        cfg_object = loadConfig()
    except:
        #start config.json initialization if file doesnt exist.
        cfg_object = authGenInteractive()

    return cfg_object

# Non-interactive function to Generate config.json
def authGen(username,useragent,keylist):
    
    #Initialize config dict
    config = {}
    
    #Set values for config
    config['useragent'] = useragent
    config['username'] = username
    config['keylist'] = keylist

    # for i in range(len(keylist)):
    #     dict_key = "key{}".format(i+1)
    #     config[dict_key] = keylist[i]

    with open('configurations/config.json','w+') as f:
        json.dump(config, f)

    return config

# Interactive function to Generate config.json
def authGenInteractive():
    print('Config not found.\nCreating new config file. Please enter your credentials.')
    
    #initializing var
    user_agent = input('Enter User Agent: ')
    user_name = input('Enter your username: ')
    keyls = []

    # Fetch n
    notNum = True
    while (notNum==True):
        n = (input("Enter Number of Keys: "))
        try:
            n = int(n)
        except:
            pass
        if type(n)==int:
            notNum = False
            n = int(n)

    # Fetch n keys
    for i in range(n):
        new_key = input("Enter Key {} (leave blank if unavailable): ".format(i+1))
        keyls.append(new_key)
    
    # Remove Redundant keys
    for i in range(len(keyls)):
        k = keyls[i]
        if k == '':
            keyls.pop(i)

    config = authGen(username=user_name, useragent=user_agent, keylist=keyls)
    print("Your configuration has been saved to config.json!\n")
    config = loadConfig()


    return config

#return an auth object
def loadConfig():

    with open('configurations/config.json', 'r') as f:
        config = json.load(f)
    
    #New class Conf that takes in newly loaded config
    class ConfigClass:
        useragent = ''
        username = ''
        keylist = []
        num = 0

        def __init__(self, cfg):
            self.useragent = cfg['useragent']
            self.username = cfg['username']
            self.keylist = cfg['keylist']
            self.num = -1

        def getKey(self):
            # Return keys one by one from the key list
            
            length = len(self.keylist)
            
            if self.num==length-1:
                self.num = -1

            self.num += 1

            return self.keylist[self.num]

    print("Config Loaded Successfully.")
    return ConfigClass(config)
