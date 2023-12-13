from flask import Flask, jsonify, request


app = Flask(__name__)


@app.route('/', methods=['GET'])
def hello_world():
    return 'Hello, World!'

@app.route('/todos', methods=['GET'])
def hello():
    response_body = jsonify(todos)
    return response_body

@app.route('/todos', methods=['POST'])
def add_new_todo():
    data = request.json
    print("Incoming request with the following body", data)
    todos.append(data)
    response_body = todos
    return response_body

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    print("This is the position to delete: ", position)
    del todos[position]
    response_body = todos
    return f'Task {position} deleted succesfully'

@app.route('/todos/<int:position>', methods=['PUT', 'GET'])
def manage_task(position):
    if request.method == 'PUT':
        data = request.json
        print("Incoming update request for task ", position, "with", data)
        todos[position] = data
        return (f'Task {position} updated succesfully')
    if request.method == 'GET':
        print("Incoming GET request for task ", position)
        return todos[position]




some_data = {"name": "Bobby", "lastname": "Rixer"}

todos = [
    {"label": "My first task", "done": False},
    {"label": "My second task", "done": False}
]


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)