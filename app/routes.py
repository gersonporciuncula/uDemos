from flask import render_template, flash, redirect, url_for, request
from app import app, db
from app.forms import LoginForm, EditProfileForm, RegistrationForm, MetasForm
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User, hora, Mot_int, Mot_ext_int, Mot_ext_ide, Mot_ext_intr, Mot_ext_ext, Falta_motivacao 
from werkzeug.urls import url_parse
from .utils import get_latest_news
import random
from app.calc_metas import calc_metas

@app.route('/')
@app.route('/index')
@login_required
def index():
    return render_template('index.html', title='Home Page')

'''''''''
@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit(): 
        user = User.query.filter_by(email=form.email.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
            return redirect(next_page)
        if user.questionario :
            return redirect(url_for('index'))
        else:
            return redirect(url_for('formulario'))

        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)
'''''''''

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit(): 
        user = User.query.filter_by(email=form.email.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        user.last_seen = hora()
        user.count_login = user.count_login + 1
        db.session.commit()
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
            user.last_seen = hora()
            db.session.commit()
            return redirect(next_page)

        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)


@app.route('/logout')
def logout():
    current_user.last_logoff = hora()
    db.session.commit()
    logout_user()
    
    
    return redirect(url_for('index'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email=form.email.data, name=form.nome.data)
        user.set_password(form.password.data)
        user.count_login = 0
        user.meta_1 = 0
        user.meta_2 = 0
        user.meta_3 = 0
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route('/user/<id>')
@login_required
def user(id):
    user = User.query.filter_by(id=id).first_or_404()
    posts = [
        {'author': user, 'body': 'Test post #1'},
        {'author': user, 'body': 'Test post #2'}
    ]
    return render_template('user.html', user=user, posts=posts)



#@app.before_request
#def before_request():
#    if current_user.is_authenticated:
#        current_user.last_seen = hora()
#        db.session.commit()

    



@app.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    user = User.query.filter_by(email=current_user.email).first()
    if request.method == 'POST':
        name = request.form.get('name')
        about_me = request.form.get('about_me')
        nationality = request.form.get('nationality')
        dob = request.form.get('dob')
        user.name = name
        user.about_me = about_me
        user.nationality = nationality
        user.dob = dob
       
        db.session.commit()

        return redirect(url_for('edit_profile'))

    return render_template('edit_profile.html', user=user)



@app.route('/metas', methods=['GET', 'POST'])
@login_required
def metas():
    user = User.query.filter_by(email=current_user.email).first()
    if request.method == 'POST':
        meta_1 = request.form.get('meta1')
        meta_2 = request.form.get('meta2')
        meta_3 = request.form.get('meta3')
        user.meta_1 = meta_1
        user.meta_2 = meta_2
        user.meta_3 = meta_3


        db.session.commit()
        print('----')
        print(user.id)
        print('----')
        metas = calc_metas(user.id)
       # print(metas)
        if metas:
            return render_template('meta1.html', metas=metas)
        elif metas == 0:
            return render_template('meta1.html', metas=metas)


     #   if metas == 0:
        #    return render_template('meta1.html')
      #  elif metas == 1:
       #     return render_template('meta2.html')
       # else:
        #    return render_template('meta3.html')

    return render_template('metas.html', user=user)
        

@app.route('/formulario', methods=['GET', 'POST'])
@login_required
def formulario():
    user = User.query.filter_by(email=current_user.email).first()
    if request.method == 'POST':
        sims1 = request.form.get('sims1')
        sims2 = request.form.get('sims2')
        sims3 = request.form.get('sims3')
        sims4 = request.form.get('sims4')
        sims5 = request.form.get('sims5')
        sims6 = request.form.get('sims6')
        sims7 = request.form.get('sims7')
        sims8 = request.form.get('sims8')
        sims9 = request.form.get('sims9')
        sims10 = request.form.get('sims10')
        sims11 = request.form.get('sims11')
        sims12 = request.form.get('sims12')
        sims13 = request.form.get('sims13')
        sims14 = request.form.get('sims14')
        sims15 = request.form.get('sims15')
        sims16 = request.form.get('sims16')
        user.sims1 = sims1
        user.sims2 = sims2
        user.sims3 = sims3
        user.sims4 = sims4
        user.sims5 = sims5
        user.sims6 = sims6
        user.sims7 = sims7
        user.sims8 = sims8
        user.sims9 = sims9
        user.sims10 = sims10
        user.sims11 = sims11
        user.sims12 = sims12
        user.sims13 = sims13
        user.sims14 = sims14
        user.sims15 = sims15
        user.sims16 = sims16
        user.questionario = 1

        db.session.commit()

        return redirect(url_for('formulario'))
    return render_template('formulario.html', user=user)


@app.route('/bpnss', methods=['GET', 'POST'])
@login_required
def bpnss():
    user = User.query.filter_by(email=current_user.email).first()
    if request.method == 'POST':
        bpnss1 = request.form.get('bpnss1')
        bpnss2 = request.form.get('bpnss2')
        bpnss3 = request.form.get('bpnss3')
        bpnss4 = request.form.get('bpnss4')
        bpnss5 = request.form.get('bpnss5')
        bpnss6 = request.form.get('bpnss6')
        bpnss7 = request.form.get('bpnss7')
        bpnss8 = request.form.get('bpnss8')
        bpnss9 = request.form.get('bpnss9')
        bpnss10 = request.form.get('bpnss10')
        bpnss11 = request.form.get('bpnss11')
        bpnss12 = request.form.get('bpnss12')
        bpnss13 = request.form.get('bpnss13')
        bpnss14 = request.form.get('bpnss14')
        bpnss15 = request.form.get('bpnss15')
        bpnss16 = request.form.get('bpnss16')
        bpnss17 = request.form.get('bpnss17')
        bpnss18 = request.form.get('bpnss18')
        bpnss19 = request.form.get('bpnss19')
        bpnss20 = request.form.get('bpnss20')
        bpnss21 = request.form.get('bpnss21')
        user.bpnss1 = bpnss1
        user.bpnss2 = bpnss2
        user.bpnss3 = bpnss3
        user.bpnss4 = bpnss4
        user.bpnss5 = bpnss5
        user.bpnss6 = bpnss6
        user.bpnss7 = bpnss7
        user.bpnss8 = bpnss8
        user.bpnss9 = bpnss9
        user.bpnss10 = bpnss10
        user.bpnss11 = bpnss11
        user.bpnss12 = bpnss12
        user.bpnss13 = bpnss13
        user.bpnss14 = bpnss14
        user.bpnss15 = bpnss15
        user.bpnss16 = bpnss16
        user.bpnss17 = bpnss17
        user.bpnss18 = bpnss18
        user.bpnss19 = bpnss19
        user.bpnss20 = bpnss20
        user.bpnss21 = bpnss21
        user.bpnss = 1

        db.session.commit()

        return redirect(url_for('bpnss'))
    return render_template('bpnss.html', user=user)

#@app.route('/notificacoes', methods=['GET', 'POST'])
#@login_required
#def notificacoes():
 #   user = User.query.filter_by(email=current_user.email).first()
 #   if request.method == 'POST':
 #       resposta1 = request.form.get('resposta1')
 #       resposta2 = request.form.get('resposta2')
 #       resposta3 = request.form.get('resposta3')
 #       resposta4 = request.form.get('resposta4')
 #       user.resposta1 = resposta1
 #       user.resposta2 = resposta2
 #       user.resposta3 = resposta3
 #       user.resposta4 = resposta4
     #   nova_resposta = Resposta(resposta=resposta)
      #  db.session.add(nova_resposta)
  #      db.session.commit()
  #  return render_template('notificacoes.html', user=user)

@app.route('/news')
@login_required
def news_headlines():
    news_articles = get_latest_news()
    user = User.query.filter_by(email=current_user.email).first()
    user.readnews = 1
    db.session.commit()
    return render_template("noticias.html", news_articles=news_articles)


@app.route('/notificacoes')
@login_required
def notificacoes():
    user = User.query.filter_by(email=current_user.email).first()
    motiv = ['[1,0,0,0,0,0]', '[0,1,0,0,0,0]', '[0,0,1,0,0,0]', '[0,0,0,1,0,0]', '[0,0,0,0,1,0]', '[0,0,0,0,0,1]']
    user.motivacao = random.choice(motiv)
   
    db.session.commit()
    #Mot_int, Mot_ext_int, Mot_ext_ide, Mot_ext_intr, Mot_ext_ext, Falta_motivacao 
    escolha = User.query.filter_by(email=current_user.email).first()
    if escolha.motivacao == "[1,0,0,0,0,0]":
        #mensagem = random.choice(mot_int)
        selecao = Mot_int.query.order_by(Mot_int.nota.desc()).first()
        mensagem = selecao.msg
        id = selecao.id
        table = "Mot_int"

    elif escolha.motivacao == "[0,1,0,0,0,0]":
        selecao = Mot_ext_int.query.order_by(Mot_ext_int.nota.desc()).first()
        mensagem = selecao.msg
        id = selecao.id
        table = "Mot_ext_int"
       
    elif escolha.motivacao == "[0,0,1,0,0,0]":
        selecao = Mot_ext_ide.query.order_by(Mot_ext_ide.nota.desc()).first()
        mensagem = selecao.msg
        id = selecao.id
        table = "Mot_ext_ide"

    elif escolha.motivacao == "[0,0,0,1,0,0]":
        selecao = Mot_ext_intr.query.order_by(Mot_ext_intr.nota.desc()).first()
        mensagem = selecao.msg
        id = selecao.id
        table = "Mot_ext_intr"

    elif escolha.motivacao == "[0,0,0,0,1,0]":
        selecao = Mot_ext_ext.query.order_by(Mot_ext_ext.nota.desc()).first()
        mensagem = selecao.msg
        id = selecao.id
        table = "Mot_ext_ext"
        
    elif escolha.motivacao == "[0,0,0,0,0,1]":
        selecao = Falta_motivacao.query.order_by(Falta_motivacao.nota.desc()).first()
        mensagem = selecao.msg
        id = selecao.id
        table = "Falta_motivacao"

    else:
        selecao = 'Erro'

    return render_template('notificacoes.html', mensagem=mensagem, id=id, table=table)
#    return render_template('roleta.html', mensagem=mensagem)

@app.route('/submit', methods=['POST'])
def submit():
    # Aqui você pode processar os dados do formulário enviados pelo método POST.
    # Por exemplo, se você tem um formulário com campos "name" e "email",
    # pode acessar os dados assim:
    nota = request.form['nota']
    id = request.form['id']
    table = request.form['table']
    idInt = int(id)
    notas = int(nota)
   # print(type(table), type(id), type(idInt))
   # print(table, id,idInt)

   # Mot_int, Mot_ext_int, Mot_ext_ide, Mot_ext_intr, Mot_ext_ext, Falta_motivacao
    if table == "Mot_int":
        query = Mot_int.query.filter_by(id=idInt).first()
        #print(query.msg)
        query.nota = notas
      #  query.nota = notas
    
    elif table == "Mot_ext_int":
        query = Mot_ext_int.query.filter_by(id=idInt).first()
        print(query)
        query.nota = notas

    elif table == "Mot_ext_ext":
        query = Mot_ext_ext.query.filter_by(id=idInt).first()
        print(query)
        query.nota = notas

    elif table == "Mot_ext_intr":
        query = Mot_ext_intr.query.filter_by(id=idInt).first()
        print(query)
        query.nota = notas
    
    elif table == "Mot_ext_ext":
        query = Mot_ext_ext.query.filter_by(id=idInt).first()
        print(query.nota)
        query.nota = notas

    else:
        query = Falta_motivacao.query.filter_by(id=idInt).first()
        print(query)
        query.nota = notas
    
    
    db.session.commit()

  #  print(table)

    # Depois de processar os dados, você pode redirecionar para outra página
    # usando a função redirect do Flask:
    return redirect('/index')