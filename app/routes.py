from app import app
from flask import render_template
from flask import request



@app.route('/')
@app.route('/index', defaults={'nome': 'Usuário'})
@app.route('/index/<nome>')
def index(nome):
    dados = {'idade': 57, 'carro': 'Gol 2022-Plus'} 
    return render_template('index.html', nome=nome, dados=dados)

@app.route('/contato', defaults={'nome':'User'})
@app.route('/contato/<nome>')
def contato(nome):
    email = 'jslanzon@gmail.com'
    fone = '(11) 9 9996-0494'
    return render_template('contato.html', email=email, fone=fone, nome=nome)

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/autenticar', methods=['GET'])
def autenticar():
    user = request.args.get('user')
    senha = request.args.get('senha')
    return'user: {} | senha: {}'.format(user, senha)