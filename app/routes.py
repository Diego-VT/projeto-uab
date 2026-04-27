from flask_login import logout_user, login_required
from flask_login import login_user
from werkzeug.security import generate_password_hash, check_password_hash
from flask import Blueprint, render_template, request, redirect, url_for
from app import db
from app.models.user import User

main = Blueprint('main', __name__)


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        senha = generate_password_hash(request.form['senha'])

        usuario_existente = User.query.filter_by(email=email).first()

        if usuario_existente:
            return "E-mail já cadastrado. Use outro e-mail."

        novo_usuario = User(
            nome=nome,
            email=email,
            senha=senha,
            tipo='solicitante'
        )

        db.session.add(novo_usuario)
        db.session.commit()

        return redirect(url_for('main.index'))

    return render_template('cadastro.html')


@main.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']

        usuario = User.query.filter_by(email=email).first()

        if usuario and check_password_hash(usuario.senha, senha):
            login_user(usuario)
            return redirect(url_for('main.index'))

        return "Login inválido"

    return render_template('login.html')

@main.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))
