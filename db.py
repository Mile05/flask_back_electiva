from flask_mysqldb import MySQL

def inicializar_db(app):
    app.config['MYSQL_HOST'] = '127.0.0.1'
    app.config['MYSQL_USER'] = 'root'
    app.config['MYSQL_PASSWORD'] = 'my-secret-pw'
    app.config['MYSQL_DB'] = 'flask_db'

    mysql = MySQL(app)
    
    return mysql
