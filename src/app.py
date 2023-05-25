from flask import Flask, jsonify
from flask_mysqldb import MySQL
from config import config


app = Flask(__name__)
conexion = MySQL(app)

@app.route('/cursos')
def index():
    try:
        cursor = conexion.connection.cursor()
        sql = "SELECT codigo, nombre, credios FROM curso"
        cursor.execute(sql)
        datos = cursor.fetchall()
        cursos=[]
        for fila in datos:
            curso={'codigo':fila[0], 'nombre':fila[1],'creditos':fila[2]}
            cursos.append(curso)
        return jsonify({'cursos':cursos, 'mensaje':'cursos listados.'})
    except Exception as ex:
        return jsonify({'mensaje':"Erorr"})

def pagina_no_encontrada(error):
    return "<h1>Pagina no encontrada</h1>"

if __name__=='__main__':
    app.config.from_object(config['development'])
    app.register_error_handler(404,pagina_no_encontrada)
    app.run()