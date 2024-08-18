from app import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from hashlib import md5
from datetime import datetime
from pytz import timezone



def hora():
    data_e_hora_atuais = datetime.now()
    fuso_horario = timezone('America/Sao_Paulo')
    data_e_hora_sao_paulo = data_e_hora_atuais.astimezone(fuso_horario)
    data_e_hora_sao_paulo_em_texto = data_e_hora_sao_paulo.strftime("%d/%m/%Y %H:%M")
    return(data_e_hora_sao_paulo_em_texto)


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(60), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    name = db.Column(db.String(62))
    dob = db.Column(db.String, nullable=True)
    nationality = db.Column(db.String(50),nullable=True)
    about_me = db.Column(db.String(140),nullable=True)
    last_seen = db.Column(db.String, default=hora)
    last_logoff = db.Column(db.String, default=hora)
    readnews = db.Column(db.Integer, nullable=True)
    count_login = db.Column(db.Integer, nullable=True)
    meta_1 = db.Column(db.Integer, nullable=True)
    meta_2 = db.Column(db.Integer, nullable=True)
    meta_3 = db.Column(db.Integer, nullable=True)
    sims1 = db.Column(db.Integer, nullable=True)
    sims2 = db.Column(db.Integer, nullable=True)
    sims3 = db.Column(db.Integer, nullable=True)
    sims4 = db.Column(db.Integer, nullable=True)
    sims5 = db.Column(db.Integer, nullable=True)
    sims6 = db.Column(db.Integer, nullable=True)
    sims7 = db.Column(db.Integer, nullable=True)
    sims8 = db.Column(db.Integer, nullable=True)
    sims9 = db.Column(db.Integer, nullable=True)
    sims10 = db.Column(db.Integer, nullable=True)
    sims11 = db.Column(db.Integer, nullable=True)
    sims12 = db.Column(db.Integer, nullable=True)
    sims13 = db.Column(db.Integer, nullable=True)
    sims14 = db.Column(db.Integer, nullable=True)
    sims15 = db.Column(db.Integer, nullable=True)
    sims16 = db.Column(db.Integer, nullable=True)
    bpnss1 = db.Column(db.Integer, nullable=True)
    bpnss2 = db.Column(db.Integer, nullable=True)
    bpnss3 = db.Column(db.Integer, nullable=True)
    bpnss4 = db.Column(db.Integer, nullable=True)
    bpnss5 = db.Column(db.Integer, nullable=True)
    bpnss6 = db.Column(db.Integer, nullable=True)
    bpnss7 = db.Column(db.Integer, nullable=True)
    bpnss8 = db.Column(db.Integer, nullable=True)
    bpnss9 = db.Column(db.Integer, nullable=True)
    bpnss10 = db.Column(db.Integer, nullable=True)
    bpnss11 = db.Column(db.Integer, nullable=True)
    bpnss12 = db.Column(db.Integer, nullable=True)
    bpnss13 = db.Column(db.Integer, nullable=True)
    bpnss14 = db.Column(db.Integer, nullable=True)
    bpnss15 = db.Column(db.Integer, nullable=True)
    bpnss16 = db.Column(db.Integer, nullable=True)
    bpnss17 = db.Column(db.Integer, nullable=True)
    bpnss18 = db.Column(db.Integer, nullable=True)
    bpnss19 = db.Column(db.Integer, nullable=True)
    bpnss20 = db.Column(db.Integer, nullable=True)
    bpnss21 = db.Column(db.Integer, nullable=True)
    
    motivacao = db.Column(db.String(10), nullable=True)
    questionario = db.Column(db.String(2), nullable=True)
    bpnss = db.Column(db.String(2), nullable=True)
    #resposta2 = db.Column(db.String(2), nullable=True)
    #resposta3 = db.Column(db.String(2), nullable=True)
    #resposta4 = db.Column(db.String(2), nullable=True)


    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def avatar(self, size):
        digest = md5(self.email.lower().encode('utf-8')).hexdigest()
        return 'https://www.gravatar.com/avatar/{}?d=identicon&s={}'.format(
            digest, size)

class Motiv_usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    motivacao = db.Column(db.String(260), index=True)
    id_user = db.Column(db.Integer, nullable=True)

#Intrinsica
class Mot_int(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    msg = db.Column(db.String(260), index=True, unique=True)
    nota = db.Column(db.Integer, nullable=True)


#Integrada
class Mot_ext_int(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    msg = db.Column(db.String(260), index=True, unique=True)
    nota = db.Column(db.Integer, nullable=True)

#Identificada
class Mot_ext_ide(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    msg = db.Column(db.String(260), index=True, unique=True)
    nota = db.Column(db.Integer, nullable=True)

#Introjetada
class Mot_ext_intr(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    msg = db.Column(db.String(260), index=True, unique=True)
    nota = db.Column(db.Integer, nullable=True)
    
#Externa
class Mot_ext_ext(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    msg = db.Column(db.String(260), index=True, unique=True)
    nota = db.Column(db.Integer, nullable=True)

class Falta_motivacao(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    msg = db.Column(db.String(260), index=True, unique=True)
    nota = db.Column(db.Integer, nullable=True)


@login.user_loader
def load_user(id):
    return User.query.get(int(id))