from flask import Blueprint, request, jsonify

products_api = Blueprint('products_api', __name__)

@products_api.route('/productos', methods=['GET'])
def obtener_usuarios():
    from main import mysql
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM products")
    productos = cur.fetchall()
    cur.close()
    
    productos_list = []
    for producto in productos:
        producto_dict = {
            'id': producto[0],
            'name': producto[1],
            'price': producto[2],
            'stock': producto[3]
        }
        productos_list.append(producto_dict)
        
    return jsonify(productos_list)

@products_api.route('/crear_producto', methods=['POST'])
def crear_usuario():
    if request.method == 'POST':
        from main import mysql
        data = request.json
        name = data.get('name')
        price = data.get('price')
        stock = data.get('stock')
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO products (name, price, stock) VALUES (%s, %s, %s)", (name, price, stock))
        mysql.connection.commit()
        cur.close()
        return 'Producto creado exitosamente'

@products_api.route('/actualizar_producto/<int:id>', methods=['PUT'])
def actualizar_usuario(id):
    if request.method == 'PUT':
        from main import mysql
        data = request.json
        name = data.get('name')
        price = data.get('price')
        stock = data.get('stock')
        
        if name is None or price is None or stock is None:
            return jsonify({'error': 'Se requieren los campos "name", "price" y "stock"'}), 400
        
        cur = mysql.connection.cursor()
        cur.execute("UPDATE products SET name=%s, price=%s, stock=%s WHERE id=%s", (name, price, stock, id))
        mysql.connection.commit()
        cur.close()
        return 'Usuario actualizado exitosamente'

@products_api.route('/eliminar_producto/<int:id>', methods=['DELETE'])
def eliminar_usuario(id):
    if request.method == 'DELETE':
        from main import mysql
        cur = mysql.connection.cursor()
        cur.execute("DELETE FROM products WHERE id=%s", (id,))
        mysql.connection.commit()
        cur.close()
        return 'Producto eliminado exitosamente'
