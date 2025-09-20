from flask import Flask, render_template, request, redirect, url_for, session, flash, request, jsonify
from flask_mysqldb import MySQL
import MySQLdb.cursors
import mysql.connector
import bcrypt
from controllers.usuario_controller import login_controller, registro_controller


app = Flask(__name__)
app.secret_key = ''
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '22Torres12'
app.config['MYSQL_DB'] = 'cafe_db'
mysql = MySQL(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/header')
def header():
    return render_template('header.html')

@app.route('/footer')
def footer():
    return render_template('footer.html')   

@app.route('/Menu')
def Menu():
    return render_template('Menu.html')

@app.route('/Tienda')
def Tienda():
    return render_template('Tienda.html')

@app.route('/Contacto')
def Contacto(): 
    return render_template('Contacto.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    return login_controller(mysql, request)

@app.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        return registro_controller(mysql, request)
    return render_template('registro.html')

"htmls qwue faltan agregar y confirar en el proyecto"
@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

@app.route('/metodos_pago')
def metodos_pago():
    return render_template('metodos_pago.html')

@app.route('/historial')
def historial():
    return render_template('historial.html')

@app.route('/info_personal')
def info_personal():
    return render_template('info_personal.html')


if __name__ == '__main__':
    app.run(debug=True)
