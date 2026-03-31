from . import db
from werkzeug.security import generate_password_hash

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(150), nullable=False, unique=True)
    role = db.Column(db.String(100), nullable=False, default="user")

    def set_password(self, password):
        self.password = generate_password_hash(password)

class Refeicao(db.Model):
    __tablename__ = "refeicoes"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    descricao = db.Column(db.String(150), nullable=False)
    data_hora = db.Column(db.String(150), nullable=False)
    in_dieta = db.Column(db.Boolean, nullable=False)

