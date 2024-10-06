from flask import Flask, request, g
import sqlite3

app = Flask(__name__)
DATABASE = 'mi_base_de_datos.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route('/')
def home():
    return 'Servidor funcionando'

@app.route('/submit', methods=['POST'])
def submit_form():
    nombre = request.json.get('nombre')
    email = request.json.get('email')
    mensaje = request.json.get('mensaje')

    db = get_db()
    db.execute('INSERT INTO mensajes (nombre, email, mensaje) VALUES (?, ?, ?)', (nombre, email, mensaje))
    db.commit()
    return 'Formulario enviado'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
