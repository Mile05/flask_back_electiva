from flask import Blueprint, request, jsonify

sell_api = Blueprint('sell_api', __name__)

@sell_api.route('/ventas', methods=['GET'])
def obtener_usuarios():
    from main import mysql
    cur = mysql.connection.cursor()
    cur.execute("SELECT venta.id, venta.quantity, venta.observation, products.name FROM venta inner join products on venta.id_product = products.id")
    productos = cur.fetchall()
    cur.close()
    
    productos_list = []
    for producto in productos:
        producto_dict = {
            'id': producto[0],
            'quantity': producto[1],
            'observation': producto[2],
            'name_product': producto[3]
        }
        productos_list.append(producto_dict)
        
    return jsonify(productos_list)

@sell_api.route('/crear_ventas', methods=['POST'])
def crear_usuario():
    if request.method == 'POST':
        from main import mysql
        data = request.json
        quantity = data.get('quantity')
        observation = data.get('observation')
        id_product = data.get('id_product')
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO venta (quantity, observation, id_product) VALUES (%s, %s, %s)", (quantity, observation, id_product))
        mysql.connection.commit()
        cur.close()
        return 'venta creada exitosamente'

@sell_api.route('/actualizar_ventas/<int:id>', methods=['PUT'])
def actualizar_usuario(id):
    if request.method == 'PUT':
        from main import mysql
        data = request.json
        quantity = data.get('quantity')
        observation = data.get('observation')
        id_product = data.get('id_product')
        
        if quantity is None or observation is None or id_product is None:
            return jsonify({'error': 'Se requieren los campos "quantity", "observation" y "id_product"'}), 400
        
        cur = mysql.connection.cursor()
        cur.execute("UPDATE venta SET quantity=%s, observation=%s, id_product=%s WHERE id=%s", (quantity, observation, id_product, id))
        mysql.connection.commit()
        cur.close()
        return 'venta actualizada exitosamente'

@sell_api.route('/eliminar_ventas/<int:id>', methods=['DELETE'])
def eliminar_usuario(id):
    if request.method == 'DELETE':
        from main import mysql
        cur = mysql.connection.cursor()
        cur.execute("DELETE FROM venta WHERE id=%s", (id,))
        mysql.connection.commit()
        cur.close()
        return 'venta eliminada exitosamente'
