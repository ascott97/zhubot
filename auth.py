import yaml

def get_auth():
    try:
        auth_file = open('auth.yaml', 'r')
        content = yaml.load(auth_file)
        return content
    except:
        print("Unable to open auth.yaml!")
        print("Does it exist?")




