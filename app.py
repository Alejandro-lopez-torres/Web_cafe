from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_mysqldb import MySQL
import MySQLdb.cursors
from controllers.usuario_controller import login_controller



app = Flask(__name__)
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

@app.route('/registro')
def registro():
    return render_template('registro.html')

if __name__ == '__main__':
    app.run(debug=True)
