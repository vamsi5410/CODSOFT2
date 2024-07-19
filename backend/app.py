from flask import Flask, request, jsonify
from task_manager import TaskManager
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
task_manager = TaskManager()

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(task_manager.list_tasks())

@app.route('/tasks', methods=['POST'])
def add_task():
    data = request.get_json()
    task = task_manager.add_task(data['name'], data.get('reminder_time'))
    return jsonify(task), 201

@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    data = request.get_json()
    task = task_manager.update_task(task_id, data['name'], data.get('reminder_time'))
    if task:
        return jsonify(task)
    return 'Task not found', 404

@app.route('/tasks/<int:task_id>/complete', methods=['PUT'])
def complete_task(task_id):
    task = task_manager.mark_completed(task_id)
    if task:
        return jsonify(task)
    return 'Task not found', 404

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = task_manager.delete_task(task_id)
    if task:
        return jsonify(task)
    return 'Task not found', 404

if __name__ == '__main__':
    app.run(debug=True)
