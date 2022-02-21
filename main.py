import auth

print("Initializing main.py!")
print("Initiating API authorization")
print()

#authenticating & Loading ConfigClass object in variable config
config = auth.initialize()


#printing authenticated credentials
print("useragent: {}".format(config.useragent))
print("username: {}".format(config.username))
print("keylist: {}".format(config.keylist))
print()
for i in range(7):
    print(config.getKey())