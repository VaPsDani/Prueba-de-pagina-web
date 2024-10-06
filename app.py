from flask import Flask, request, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mi_base_de_datos.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Mensaje(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    mensaje = db.Column(db.Text, nullable=False)

@app.route('/')
def home():
    return render_template('principal.html')

@app.route('/submit', methods=['POST'])
def submit_form():
    nombre = request.form['nombre']
    email = request.form['email']
    mensaje = request.form['mensaje']

    nuevo_mensaje = Mensaje(nombre=nombre, email=email, mensaje=mensaje)
    db.session.add(nuevo_mensaje)
    db.session.commit()
    return redirect(url_for('home'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, host='0.0.0.0', port=5000)

