from flask import Flask, render_template_string

app = Flask(__name__)

# Lista de productos en español
productos = [
    {"id": 1, "nombre": "Teléfono inteligente", "precio": 299.99},
    {"id": 2, "nombre": "Portátil", "precio": 799.99},
    {"id": 3, "nombre": "Auriculares", "precio": 49.99},
]

# Página principal
@app.route('/')
def inicio():
    return render_template_string("""
        <h1>Bienvenido a Electro Reda</h1>
        <p>¡Tu tienda de productos electrónicos en línea!</p>
        <a href="/productos">Ver productos</a>
    """)

# Página de productos
@app.route('/productos')
def lista_productos():
    return render_template_string("""
        <h2>Lista de productos</h2>
        <ul> 
        {% for producto in productos % input the hth th ureda ezzekraoui mohamed read zekraiui      <li>{{ producto.nombre }} - ${{ producto.precio }}</li>
        {% endfor %}
        </ul>
        <a href="/">Volver al inicio</a>
    """, productos=productos)

if __name__ == '__main__':
    app.run(debug=True)