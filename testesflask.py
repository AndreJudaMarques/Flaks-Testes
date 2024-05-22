from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return """
    <div style="text-align: center;">
        <h1>Bem-vindo ao meu aplicativo Flask!</h1>
        <a href="/api"><button style="display: inline-block;">Próxima Página</button></a>
    </div>
    """

    

@app.route('/api')
def mensagem():
      return """
      <h1>Primeira Pagina do flask<h1>"""

if __name__ == '__main__':
      app.run()