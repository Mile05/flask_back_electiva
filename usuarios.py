from flask import Blueprint, request, jsonify

usuarios_api = Blueprint('usuarios_api', __name__)

@usuarios_api.route('/usuarios', methods=['GET'])
def obtener_usuarios():
    from main import mysql
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM users")
    usuarios = cur.fetchall()
    cur.close()
    
    usuarios_list = []
    for usuario in usuarios:
        usuario_dict = {
            'id': usuario[0],
            'username': usuario[1],
            'password': usuario[2],
            'full_name': usuario[3]
        }
        usuarios_list.append(usuario_dict)
        
    return jsonify(usuarios_list)

@usuarios_api.route('/crear_usuario', methods=['POST'])
def crear_usuario():
    if request.method == 'POST':
        from main import mysql
        data = request.json
        username = data.get('username')
        password = data.get('password')
        full_name = data.get('full_name')
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO users (username, password, full_name) VALUES (%s, %s, %s)", (username, password, full_name))
        mysql.connection.commit()
        cur.close()
        return 'Usuario creado exitosamente'

@usuarios_api.route('/actualizar_usuario/<int:id>', methods=['PUT'])
def actualizar_usuario(id):
    if request.method == 'PUT':
        from main import mysql
        data = request.json
        username = data.get('username')
        password = data.get('password')
        full_name = data.get('full_name')
        
        if username is None or password is None or full_name is None:
            return jsonify({'error': 'Se requieren los campos "username", "password" y "full_name"'}), 400
        
        cur = mysql.connection.cursor()
        cur.execute("UPDATE users SET username=%s, password=%s, full_name=%s WHERE id=%s", (username, password, full_name, id))
        mysql.connection.commit()
        cur.close()
        return 'Usuario actualizado exitosamente'

@usuarios_api.route('/eliminar_usuario/<int:id>', methods=['DELETE'])
def eliminar_usuario(id):
    if request.method == 'DELETE':
        from main import mysql
        cur = mysql.connection.cursor()
        cur.execute("DELETE FROM users WHERE id=%s", (id,))
        mysql.connection.commit()
        cur.close()
        return 'Usuario eliminado exitosamente'
