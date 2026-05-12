from app import db


class Equipment(db.Model):
    __tablename__ = "equipments"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    patrimonio = db.Column(db.String(50), unique=True, nullable=False)
    descricao = db.Column(db.Text, nullable=True)
    status = db.Column(db.String(20), nullable=False, default="disponivel")
