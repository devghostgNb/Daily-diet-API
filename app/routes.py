from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash
from app.models import User, Refeicao
from app import db


main = Blueprint("main", __name__)

@main.route("/")
def home():
    return "API rodando 🚀"

@main.route("/users", methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([
        {
            "id": r.id,
            "username": r.username,
            "email": r.email
        }
        for r in users
    ])

@main.route("/users/<int:id_user>", methods=['GET'])
def get_user(id_user):
    user = User.query.get(id_user)
    if user:
            return jsonify({
                "id": user.id,
                "username": user.username,
                "email": user.email
            })
    return {"error": "Usuário não encontrado"}, 404

@main.route("/users", methods=['POST'])
def create_user():
    data = request.json
    if not data or "username" not in data or "password" not in data or "email" not in data:
        return jsonify({"message": "Dados incompletos"}), 400

    user = User (
        username=data["username"],
        email=data["email"]
        )
    user.set_password(data["password"])
    db.session.add(user)
    db.session.commit()

    return jsonify({"message": "Usuário criado com sucesso", "data": {
        "id": user.id,
        "username": user.username,
        "email": user.email
    }}), 201

@main.route("/users/<int:id_user>", methods=['PUT'])
def update_user(id_user):
    user = User.query.get(id_user)
    if not user:
        return jsonify({"error": "Usuário não encontrado"}), 404

    data = request.json
    if not data:
        return jsonify({"message": "Dados incompletos"}), 400

    if "username" in data:
                user.username = data["username"]
    if "password" in data:
                user.password = generate_password_hash(data["password"])
    if "email" in data:
                user.email = data["email"]

    db.session.commit()
    return jsonify({"message": "Usuário atualizado com sucesso", "data": {
    "id": user.id,
    "username": user.username,
    "email": user.email
}}), 200


@main.route("/users/<int:id_user>", methods=['DELETE'])
def delete_user(id_user):
    user = User.query.get(id_user)
    if not user:
        return jsonify({"error": "Usuário não encontrado"}), 404

    db.session.delete(user)
    db.session.commit()
    return jsonify({"message": "Usuário deletado com sucesso"}), 200


@main.route("/refeicoes",  methods=["GET"])
def get_refeicoes():
    refeicoes = Refeicao.query.all()
    return jsonify([{
        "id": r.id,
        "title": r.title,
        "descricao": r.descricao,
        "data_hora": r.data_hora}
        for r in refeicoes
    ])


@main.route("/refeicoes/<int:id>", methods=["GET"])
def get_refeicao(id):
    refeicao = Refeicao.query.get(id)
    if not refeicao:
        return jsonify({"error": "Refeição não encontrada"}), 404

    return jsonify({
        "id": refeicao.id,
        "title": refeicao.title,
        "descricao": refeicao.descricao,
        "data_hora": refeicao.data_hora,
        "in_dieta": refeicao.in_dieta
    })

@main.route("/refeicoes", methods=["POST"])
def create_refeicao():
    data = request.json
    if not data or "title" not in data or "descricao" not in data or "data_hora" not in data or "in_dieta" not in data:
        return jsonify({"error":"Dados incompletos"}), 400


    in_dieta = True if data["in_dieta"] == "sim" else False

    refeicao = Refeicao(
        title=data["title"],
        descricao=data["descricao"],
        data_hora=data["data_hora"], 
        in_dieta=in_dieta
    )
    db.session.add(refeicao)
    db.session.commit()
    return jsonify({"message": "Refeição criada", "data": {
        "id": refeicao.id,
        "title": refeicao.title,
        "descricao": refeicao.descricao,
        "data_hora": refeicao.data_hora,
        "in_dieta": refeicao.in_dieta
    }}), 201

@main.route("/refeicoes/<int:id>", methods=["PUT"])
def update_refeicao(id):
    refeicao = Refeicao.query.get(id)
    if not refeicao:
        return jsonify({"error": "Refeição não encontrada"}), 404

    data = request.json
    if not data:
        return jsonify({"error": "Dados incompletos"}), 400

    refeicao.title = data.get("title", refeicao.title)
    refeicao.descricao = data.get("descricao", refeicao.descricao)
    refeicao.data_hora = data.get("data_hora", refeicao.data_hora)
    refeicao.in_dieta = data.get("in_dieta", refeicao.in_dieta)

    if "in_dieta" in data:
        refeicao.in_dieta = True if data["in_dieta"] == "sim" else False


    db.session.commit()
    return jsonify({"message": "Refeição atualizada com sucesso", "data": {
        "id": refeicao.id,
        "title": refeicao.title,
        "descricao": refeicao.descricao,
        "data_hora": refeicao.data_hora,
        "in_dieta": refeicao.in_dieta
    }}), 200

@main.route("/refeicoes/<int:id>", methods=["DELETE"])
def delete_refeicao(id):
    refeicao = Refeicao.query.get(id)
    if not refeicao:
        return jsonify({"error": "Refeição não encontrada"}), 404

    db.session.delete(refeicao)
    db.session.commit()
    return jsonify({"message": "Refeição deletada com sucesso"}), 200











