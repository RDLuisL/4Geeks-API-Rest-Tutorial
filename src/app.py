from flask import Flask, jsonify, request, abort

app = Flask(__name__)

todos=[
    {"label": "My first task", "done": True},
    {"label": "My second task", "done": True},
    {"label": "My third task", "done": True}
]

@app.route('/todos', methods=['GET'])
def hello_world():
    json_text = jsonify(todos)
    return json_text

@app.route('/todos', methods=['POST'])
def add_new_todo():
    #Lineas de condicionales para verificar objetos
    request_body = request.json
    if not request_body:
        abort(400, description="Request body must be JSON and contain 'label' and 'done' keys.")
    if 'label' not in request_body or 'done' not in request_body:
        abort(400, description="Request body must contain 'label' and 'done' keys.")
    # Comando para agregar un objeto en la lista
    todos.append(request_body)
    return jsonify(todos), 200

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    #Lineas de condicionales para verificar la ruta <int:position>
    if position < 0 or position >= len(todos):
        abort(404, description="Todo with the given position not found.")
    
    print("This is the position to delete:", position)
    #borra de la lista de objetos segun la posicion: todos.pop(position)
    deleted_todo = todos.pop(position)
    return jsonify(todos), 200

if __name__=='__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)
