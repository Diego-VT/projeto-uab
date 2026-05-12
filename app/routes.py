from app.models.equipment import Equipment
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
            return redirect(url_for('main.dashboard'))

        return "Login inválido"

    return render_template('login.html')

@main.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))

@main.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')

@main.route('/equipamentos/cadastro', methods=['GET', 'POST'])
@login_required
def cadastro_equipamento():
    if request.method == 'POST':
        nome = request.form['nome']
        patrimonio = request.form['patrimonio']
        descricao = request.form['descricao']

        equipamento = Equipment(
            nome=nome,
            patrimonio=patrimonio,
            descricao=descricao
        )

        db.session.add(equipamento)
        db.session.commit()

        return redirect(url_for('main.dashboard'))

    return render_template('equipamento_cadastro.html')

@main.route('/equipamentos')
@login_required
def listar_equipamentos():
    equipamentos = Equipment.query.order_by(Equipment.id.desc()).all()
    return render_template(
        'equipamentos.html',
        equipamentos=equipamentos
    )
@main.route('/equipamentos/excluir/<int:id>', methods=['POST'])
@login_required
def excluir_equipamento(id):
    equipamento = Equipment.query.get_or_404(id)

    db.session.delete(equipamento)
    db.session.commit()

    return redirect(url_for('main.listar_equipamentos'))


@main.route('/equipamentos/editar/<int:id>', methods=['GET', 'POST'])
@login_required
def editar_equipamento(id):
    equipamento = Equipment.query.get_or_404(id)

    if request.method == 'POST':
        equipamento.nome = request.form['nome']
        equipamento.patrimonio = request.form['patrimonio']
        equipamento.descricao = request.form['descricao']

        db.session.commit()

        return redirect(url_for('main.listar_equipamentos'))

    return render_template(
        'equipamento_editar.html',
        equipamento=equipamento
    )
