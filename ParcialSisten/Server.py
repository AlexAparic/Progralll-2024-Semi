from flask import Flask, request, jsonify, render_template
import ProFabd  
app = Flask(__name__)


@app.route('/')
def inicio():
    return render_template('usuarios.html')

@app.route('/api/usuarios', methods=['GET'])
def listar_usuarios():
    usuarios = ProFabd.listar_usuarios()  
    return jsonify(usuarios)


@app.route('/api/usuario', methods=['POST'])
def agregar_usuario():
    datos = request.json
    if not all(key in datos for key in ['nombre', 'direccion', 'telefono']):
        return jsonify({"mensaje": "Datos incompletos"}), 400
    ProFabd.agregar_usuario(datos['nombre'], datos['direccion'], datos['telefono'])  # Asumimos que esta función está en ProFabd
    return jsonify({"mensaje": "Usuario agregado con éxito"}), 201


@app.route('/api/usuario/<int:id>', methods=['PUT'])
def editar_usuario(id):
    datos = request.json
    if not all(key in datos for key in ['nombre', 'direccion', 'telefono']):
        return jsonify({"mensaje": "Datos incompletos"}), 400
    ProFabd.actualizar_usuario(id, datos['nombre'], datos['direccion'], datos['telefono'])  # Asegúrate de que esta función esté implementada
    return jsonify({"mensaje": "Usuario actualizado con éxito"}), 200


@app.route('/api/usuario/<int:id>', methods=['DELETE'])
def eliminar_usuario(id):
    
    ProFabd.eliminar_usuario(id)  
    return jsonify({"mensaje": "Usuario eliminado con éxito"}), 200


@app.route('/api/buscarUsuarios', methods=['GET'])
def buscar_usuarios():
    busqueda = request.args.get('q')
    usuarios = ProFabd.buscar_usuarios(busqueda)  
    return jsonify(usuarios)


if __name__ == '__main__':
    app.run(debug=True)
