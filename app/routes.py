from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash


main = Blueprint("main", __name__)

@main.route("/")
def home():
    return "API rodando 🚀"

users = []
user_id_counter = 1

@main.route("/users", methods=['GET'])
def get_users():
    return jsonify(users)

@main.route("/users/<int:id_user>", methods=['GET'])
def get_user(id_user):
    for user in users:
        if user["id"]==id_user:
            return jsonify(user)
    return {"error": "Usuário não encontrado"}, 404

@main.route("/users", methods=['POST'])
def create_user():
    global user_id_counter
    data = request.json
    if not data or "username" not in data or "password" not in data or "email" not in data:
        return jsonify({"message": "Dados incompletos"}), 400

    user = {
        "id": user_id_counter,
        "username": data.get("username"),
        "password": generate_password_hash(data.get("password")),
        "email": data.get("email")
        }

    users.append(user)
    user_id_counter += 1
    return jsonify({"message": "Usuário criado com sucesso", "data":user}), 201

@main.route("/users/<int:id_user>", methods=['PUT'])
def update_user(id_user):
    data = request.json
    if not data:
        return jsonify({"message": "Dados incompletos"}), 400

    for user in users:
        if user["id"] == id_user:
            # Atualiza apenas se o campo existir no JSON
            if "username" in data:
                user["username"] = data["username"]
            if "password" in data:
                user["password"] = generate_password_hash(data["password"])
            if "email" in data:
                user["email"] = data["email"]

            return jsonify({"message": "Usuário atualizado com sucesso", "data": user}), 200

    return jsonify({"error": "Usuário não encontrado"}), 404

@main.route("/users/<int:id_user>", methods=['DELETE'])
def delete_user(id_user):
    for user in users:
        if user["id"]==id_user:
            users.remove(user)
            return jsonify({"message":"Usuário deletado com sucesso"}), 200
    return jsonify({"error":"Usuário não encontrado"}), 404



refeicoes = []
refeicao_id_counter = 1

@main.route("/refeicoes",  methods=["GET"])
def get_refeicoes():
    return jsonify(refeicoes)

@main.route("/refeicoes/<int:id>", methods=["GET"])
def get_refeicao(id):
    for refeicao in refeicoes:
        if refeicao["id"]==id:
            return jsonify(refeicao)
    return {"error": "Refeição não encontrada."}, 404

@main.route("/refeicoes", methods=["POST"])
def create_refeicao():
    global refeicao_id_counter
    data = request.json
    if not data or "title" not in data or "descricao" not in data or "data_hora" not in data or "in_dieta" not in data:
        return jsonify ({"error":"Dados incompletos"}), 400

    refeicao = {
        "id": refeicao_id_counter,
        "title": data.get("title"),
        "descricao": data.get("descricao"),
        "data_hora": data.get("data_hora"),
        "in_dieta": data.get("in_dieta")
        }

    refeicoes.append(refeicao)
    refeicao_id_counter += 1
    return jsonify({"message": "Refeição criada", "data":refeicao}), 201

@main.route("/refeicoes/<int:id>", methods=["PUT"])
def update_refeicao(id):
    data = request.get_json()
    if not data:
        return jsonify({"error": "Dados incompletos"}), 400
    for refeicao in refeicoes:
         if refeicao["id"]==id:
            refeicao["title"] = data.get("title", refeicao["title"])
            refeicao["descricao"] = data.get("descricao", refeicao["descricao"])
            refeicao["data_hora"] = data.get("data_hora", refeicao["data_hora"])
            refeicao["in_dieta"] = data.get("in_dieta", refeicao["in_dieta"])
            return jsonify({"message": "Refeição atualizada com sucesso", "data":refeicao}), 200
    return jsonify({"error": "Refeição não encontrada"}), 404

@main.route("/refeicoes/<int:id>", methods=["DELETE"])
def delete_refeicao(id):
    for refeicao in refeicoes:
        if refeicao["id"] == id:
            refeicoes.remove(refeicao)
            return jsonify({"message": "refeicao Deletada!"}), 200
    return jsonify({"error": "Refeição não encontrada"}), 404











