from flask import Blueprint, request, jsonify

main = Blueprint("main", __name__)

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
    if not data or "title" not in data or "descricao" not in data or "data_hora" not in data:
        return jsonify ({"error":"Dados incompletos"}), 400

    refeicao = {
        "id": refeicao_id_counter,
        "title": data.get("title"),
        "descricao": data.get("descricao"),
        "data_hora": data.get("data_hora")
        }

    refeicoes.append(refeicao)
    refeicao_id_counter += 1
    return jsonify({"message": "Refeição criada", "data":refeicao}), 201

@main.route("/refeicoes/<int:id>", methods=["PUT"])
def update_refeicao(id):
    data = request.get_json()
    if not data or "title" not in data or "descricao" not in data or "data_hora" not in data:
        return jsonify ({"error":"Dados incompletos"}), 400
    for refeicao in refeicoes:
         if refeicao["id"]==id:
            refeicao["title"] = data.get("title", refeicao["title"])
            refeicao["descricao"] = data.get("descricao", refeicao["descricao"])
            refeicao["data_hora"] = data.get("data_hora", refeicao["data_hora"])
            return jsonify({"message": "Refeição atualizada com sucesso", "data":refeicao}), 200
    return jsonify({"error": "Refeição não encontrada"}), 404

@main.route("/refeicoes/<int:id>", methods=["DELETE"])
def delete_refeicao(id):
    for refeicao in refeicoes:
        if refeicao["id"] == id:
            refeicoes.remove(refeicao)
            return jsonify({"message": "refeicao Deletada!"}), 200
    return jsonify({"error": "Refeição não encontrada"}), 404











