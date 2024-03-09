from flask import Flask
from usuarios import usuarios_api
from products import products_api
from sell import sell_api
from db import inicializar_db

app = Flask(__name__)
mysql = inicializar_db(app)

app.register_blueprint(usuarios_api, mysql=mysql)
app.register_blueprint(products_api, mysql=mysql)
app.register_blueprint(sell_api, mysql=mysql)

if __name__ == '__main__':
    app.run(debug=True)
