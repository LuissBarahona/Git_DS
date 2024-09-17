from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    #return "Hola Luis David"
    return render_template('index.html') #llama al archivo html


@app.route('/productos')
def index_products(): #
    return render_template('productos/index.html') #llama al archivo html


@app.route('/clientes')
def index_clientes(): #
    return render_template('clientes/index.html') #llama al archivo html



if __name__ == '__main__':
    app.run(debug=True, port=3000)
