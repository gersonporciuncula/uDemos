from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField, IntegerField, DecimalField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo, Length
from app.models import User

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Lembrar de mim')
    submit = SubmitField('Entrar')

class RegistrationForm(FlaskForm):
    nome = StringField('Nome', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')
        
class EditProfileForm(FlaskForm):
    nome = StringField('Nome', validators=[DataRequired()])
    data_nasc = StringField('Data Nascimento', validators=[DataRequired()])
    nacionalidade = StringField('Nacionalidade', validators=[DataRequired()])
    about_me = TextAreaField('About me', validators=[Length(min=0, max=140)])
    submit = SubmitField('Submit')

    def __init__(self, original_username, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        self.original_username = original_username
    
    def validate_username(self, username):
        if username.data != self.original_username:
            user = User.query.filter_by(username=self.email.data).first()
            if user is not None:
                raise ValidationError('Please use a different username.')
            
class MetasForm(FlaskForm):
   meta1 = StringField('Quantas vezes você lavou as mãos?', validators=[DataRequired()])
   meta2 = StringField('Tomou quantas dozes de vacina?', validators=[DataRequired()])
   meta3 = StringField('Quantas vezes você usou mascara hoje?', validators=[DataRequired()])
   submit = SubmitField('Submit')