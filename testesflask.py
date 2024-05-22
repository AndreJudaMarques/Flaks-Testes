from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
      return '<h1>Bem-vindo ao meu aplicativo Flask!</h1><a href="/api"><button>Próxima Página</button></a>'
    

@app.route('/api')
def mensagem():
      return 'Primeira Pagina'

if __name__ == '__main__':
      app.run()