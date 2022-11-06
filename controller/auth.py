from requests_oauthlib import OAuth2Session
import config
import json
settings = config.get_settings()

from common.Response import Response

CLIENT_ID = settings.get('google','CLIENT_ID')
CLIENT_SECRET = settings.get('google','CLIENT_SECRET')
authorization_base_url = settings.get('google','authorization_base_url')
token_url = settings.get('google','token_url')


class AuthManager:
    def __init__(self):
        pass

    def is_authorized(self, args):
        pass

    def get_credentials(self, args):
        #credentials = client.credentials_from_code( CLIENT_ID, CLIENT_SECRET, scope='', code=args['auth_code'])
        #print(credentials)
        pass

    def login(self, args={}):
        google = OAuth2Session(CLIENT_ID,  redirect_uri="postmessage")
        fetch_info = google.fetch_token(token_url,code=args['code'], client_secret=CLIENT_SECRET)
        profile = google.get('https://www.googleapis.com/oauth2/v1/userinfo')
        #auth = oauth2.WebApplicationClient(CLIENT_ID, code=args['code'])
        #print(resp)
        #'4/0AfgeXvsqscHI7LYcaPDSOoHpQGbhyc0t_g1IToe2MczgyMBoW1No_lFg_o1Jz6iDAxamKg'
        #credentials = client.credentials_from_code( CLIENT_ID, CLIENT_SECRET, scope='', code=args['auth_code'])

        info = json.loads(profile.text)
        info["access_token"] = fetch_info.get('access_token')
        return Response().from_raw_data(info)
    