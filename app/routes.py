from flask import Blueprint, request, jsonify

main = Blueprint("main", __name__)

tasks = []
task_id_counter = 1

@main.route("/tasks",  methods=["GET"])
def get_tasks():
    return jsonify(tasks)

@main.route("/tasks/<int:id>", methods=["GET"])
def get_task(id):
    for task in tasks:
        if task["id"]==id:
            return jsonify(task)
    return {"error": "Task não encontrada."}, 404

@main.route("/tasks", methods=["POST"])
def create_task():
    global task_id_counter
    data = request.json

    task = {
        "id": task_id_counter,
        "title": data.get("title"),
        "done" : False
        }

    tasks.append(tasks)
    task_id_counter += 1
    return jsonify({"message": "Task criada", "data":data}), 201

@main.route("/tasks/<int:id>", methods=["PUT"])
def update_task(id):
    data = request.get_json()
    for task in tasks:
         if task["id"]==id:
            task["title"] = data.get("title", task["title"])
            task["done"] = data.get("done", task["done"])
            return jsonify(task)
    return ("error": "Task não encontrada"), 404








