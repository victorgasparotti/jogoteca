from flask import Flask, render_template, request, redirect

app = Flask(__name__)

class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console
    
jogo1 = Jogo('GTA VI', 'Ação e aventura', 'Playstation - Xbox')
jogo2 = Jogo('Homem Aranha', 'Ação e aventura', 'Playstation - Xbox - PC')
jogo3 = Jogo('EA SPORTS FC 27', 'Esportes', 'Playstation - Xbox - PC - Switch')
lista = [jogo1, jogo2, jogo3]

@app.route('/')
def index():
    return render_template('lista.html', titulo='Jogos', jogos=lista)

@app.route('/cadastrar')
def cadastrar():
    return render_template('cadastrar.html', titulo='Cadastrar novo jogo')

@app.route('/criar', methods=['POST'])
def criar():
    nome=request.form['nome']
    categoria=request.form['categoria']
    console=request.form['console']

    jogo = Jogo(nome, categoria, console)
    lista.append(jogo)
    return redirect('/')

@app.route('/login')
def login():
    return render_template('login.html')



app.run(debug=True)