from app import app
from flask import render_template

nome = 'Julio Cesar'

@app.route('/')
@app.route('/index')
def index():
    dados = {'idade': 57, 'instrumento': 'Baixo elétrico'} 
    return render_template('index.html', nome=nome, dados=dados)

@app.route('/contato')
def contato():
    email = 'jslanzon@gmail.com'
    fone = '(11) 9 9996-0494'
    return render_template('contato.html', email=email, fone=fone, nome=nome)