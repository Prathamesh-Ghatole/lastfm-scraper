# Implement Authentication System

import json

# Setting up the config for usage.
def authenticate():
    try:
        with open('config.json', 'r') as f:
            config = json.load(f)
        user_agent = config['user_agent']
        key1 = config['key1']
        key2 = config['key2']
        key3 = config['key3']
        username = config['username']
        print("Config Loaded Successfully.")
        key_list = [key1, key2, key3]
        
    except:
        print('config.json wasn\'t found.\nCreating new config file. Please enter your credentials.')
        user_agent = input('Enter User Agent: ')
        username = input('Enter your username: ')
        key1 = input('Enter Secret Key: ')
        key2 = input('Enter Secret Key 2:\nLeave blank if you don\'t have mirror keys. ')
        if key2 == '':
            key2 = key1
        key3 = input('Enter Secret Key 3:\nLeave blank if you don\'t have mirror keys. ')
        if key3 == '':
            key3 = key1
        
    #     with open('config.json.sample','r') as f:
    #         config = json.load(f)
        config = {'user_agent':None,'key1':None, 'key2':None, 'key3':None, 'username':None}
        config['user_agent'] = user_agent
        config['key1'] = key1
        config['key2'] = key2
        config['key3'] = key3
        config['username'] = username
        
        with open('config.json','w+') as f:
            json.dump(config, f)
        
        key_list = [key1, key2, key3]

        print()
        print("Your configuration has been saved to config.json!")
        
    # Fetches variables: user_agent, username, key1, key2, key3, key_list