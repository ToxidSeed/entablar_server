from itsdangerous import URLSafeSerializer
from datetime import date
from oauth2client import client
from model.Usuario import Usuario
from app import app, db
from flask_mail import Mail, Message
from flask import url_for

class SessionManager:    
    def __init__(self):
        pass

    def login(self, args):
        if(args["provider"] == "google" ):
            google_manager = GoogleManager()
            google_manager.login(args)  

    def confirm(self, token):
        serializer = URLSafeSerializer(app.config['SECRET_KEY'])
        email = serializer.loads(token,salt=app.config['SECURITY_PASSWORD_SALT'])
        not_confirmed_user = Usuario.query.filter_by(email=email).first()
        not_confirmed_user.confirmado = True
        not_confirmed_user.fch_confirmacion = date.today()
        db.session.commit()

class GoogleManager:    
    def __init__(self):
        pass

    def login(self, args):        

        credentials = client.credentials_from_code(app.config["GOOGLE_CLIENT_ID"], app.config["GOOGLE_CLIENT_SECRET"], scope="", code=args["code"])

        email = credentials.id_token['email']

        usuario_info = Usuario.query.filter_by(email=email).first()

        if(usuario_info is None):
            self.register(credentials.id_token)


    def register(self, login_data):
        
        user_data = Usuario()
        user_data.nombre = login_data["name"]
        user_data.provider = "google"
        user_data.email = login_data["email"]
        user_data.fch_creacion = date.today()
        user_data.confirmado = False
        #user_data.fch_confirmacion = current_date_time
        db.session.add(user_data)
        db.session.commit()

        self.sent_conformation_mail(user_data.email)

    def sent_conformation_mail(self, email):
        Confirmation(email).send_mail()
        


class Confirmation:
    def __init__(self, email):
        self.email = email

    def gen_confirmation_token(self):
        

        serializer = URLSafeSerializer(app.config['SECRET_KEY'])
        return serializer.dumps(self.email, salt=app.config['SECURITY_PASSWORD_SALT'])

    def send_mail(self):        

        token = self.gen_confirmation_token()

        confirm_url = url_for('confirm',token=token,_external=True)

        mail = Mail(app)
        msg = Message("Hello", sender=app.config["MAIL_USERNAME"], recipients=[self.email])
        msg.html = '<a href="{}">confirmar</a>'.format(confirm_url)                        
        mail.send(msg)
        




    






    


    