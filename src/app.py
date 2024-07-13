from flask import Flask, jsonify, request, abort
app = Flask(__name__)

todos = [
    {"label": "My first task", "done": True},
    {"label": "My second task", "done": True},
    {"label": "My third task", "done": True}
]

@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todos)

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    print("Incoming request with the following body", request_body)
    
    # Agregar el nuevo todo a la lista
    todos.append(request_body)
    
    # Devolver la lista actualizada de todos
    return jsonify(todos), 201  # 201 Created es el código de estado HTTP adecuado

@app.route("/todos/<int:position>", methods=['DELETE'])
def delete_todo(position):
    if position < 0 or position >= len(todos):
        # Si el índice está fuera del rango, devolver un error 404
        abort(404, description="Todo not found")
    
    # Eliminar el todo del índice especificado
    print("This is the position to delete:", position)
    del todos[position]
    
    # Devolver la lista actualizada de todos
    return jsonify(todos), 200  # 200 OK es el código de estado HTTP adecuado

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)
