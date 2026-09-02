from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="tienda_celulares"
    )

@app.route('/')
def inicio():
    db = conectar()
    cursor = db.cursor()
    cursor.execute("SELECT marca, modelo, precio, stock FROM productos")
    productos = cursor.fetchall()
    db.close()
    return render_template('index.html', productos=productos)

if __name__ == '__main__':
    app.run(debug=True)