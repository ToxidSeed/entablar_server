from oauth2client import client
CLIENT_ID = '435471540706-icu11lq037akvpb6p2eep3s49f6v5icc.apps.googleusercontent.com'
CLIENT_SECRET = 'lzIL-ekDrqJoMg5YertucG_5'

class SessionManager:
    def __init__(self):
        pass

    def is_authorized(self, args):
        pass

    def get_credentials(self, args):
        credentials = client.credentials_from_code(CLIENT_ID, CLIENT_SECRET, scope='', code=args['auth_code'])
        print(credentials)

    
    