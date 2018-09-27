import 
user_name = string
server_name = string
folders = list()

def user_exists:
   """
   Checks if user's file exists.
   """
def new_user:
    """
    Adds a new user if it did not exist before.
    """

if user_exists:
    with open('/server/%s/%s.json'.format(server_name,user_name)) as f:
        user_data = json.load(f)
else:
    new_file
if discord_server not in folders:
    #create new folder
