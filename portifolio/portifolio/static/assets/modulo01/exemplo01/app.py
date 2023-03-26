from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return """
        <html>
            <head>
                <title>Meu Restaurante</title>
            </head>
            <body>
                <h2>Meu Restaurante</h2>
                <h3>Acesse o menu:</h3>
                <ul>
                    <li><a href="/orders">Listar Pedidos</a></li>
                    <li><a href="#">Listar Clientes</a></li>
                    <li><a href="#">Listar Funcionários</a></li>
                </ul>
                <p>Lembre-se de verificar corretamente os pedidos!</p>
                <p>Caso algum produto esteja inconsistente. Solicitar a alteração!</p>
                <p>Não realizamos a troca dos pedidos após a confecção!</p>
            </body>
        </html>
    """ 
            
@app.route('/orders')
def orders():
    return """
            <html>
                <head>
                    <title>Meu Restaurante</title>
                </head>
                <body>
                    <h2>Meus Pedidos</h2>
                    <ul>
                        <li>Combo 1, comanda 2.</li>
                        <li>Combo 2, comanda 5.</li>
                        <li>Executivo 2, comanda 3</li>
                        <li>Refri laranja, comanda 134</li>
                        <li>Cerveja, comanda 12</li>
                        <li>Batata Frita, comanda 14</li>
                    </ul>
                    <p>Voltar para <a href="/">página inicial</a>!</p>
                </body>
            </html>
            """

if __name__ == "__main__":
    app.run()
