from flask import Flask, render_template, request, redirect, session, flash, url_for

app = Flask(__name__)
app.secret_key = 'victor$gasparotti'

class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console
    
jogo1 = Jogo('GTA VI', 'Ação e aventura', 'Playstation - Xbox')
jogo2 = Jogo('Homem Aranha', 'Ação e aventura', 'Playstation - Xbox - PC')
jogo3 = Jogo('EA SPORTS FC 27', 'Esportes', 'Playstation - Xbox - PC - Switch')
lista = [jogo1, jogo2, jogo3]

class Usuario:
    def __init__(self, nome, nickname, senha):
        self.nome = nome
        self.nickname = nickname
        self.senha = senha

usuario1 = Usuario('Victor', 'vg', 'victor123')
usuario2 = Usuario('Johnny', 'johnjohn', '0987654321')
usuraio3 = Usuario('Marina', 'mamarina', 'mariloka01')

usuarios = {usuario1.nickname : usuario1, usuario2.nickname : usuario2, usuraio3.nickname : usuraio3}

@app.route('/')
def index():
    return render_template('lista.html', titulo='Jogos', jogos=lista)

@app.route('/cadastrar')
def cadastrar():
    if 'usuario_logado' not in session or session ['usuario_logado'] == None:
        return redirect(url_for('login', proxima=url_for('cadastrar')))
    return render_template('cadastrar.html', titulo='Cadastrar novo jogo')

@app.route('/criar', methods=['POST'])
def criar():
    nome=request.form['nome']
    categoria=request.form['categoria']
    console=request.form['console']

    jogo = Jogo(nome, categoria, console)
    lista.append(jogo)
    return redirect(url_for('index'))

@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    return render_template('login.html', proxima=proxima)

@app.route('/autenticar', methods=['POST'])
def autenticar():
    if request.form['usuario'] in usuarios:
        usuario = usuarios[request.form['usuario']]
        if request.form['senha'] == usuario.senha:
            session['usuario_logado'] = usuario.nickname
            flash(usuario.nickname + ' logado com sucesso!')
            proxima_pagina = request.form['proxima']
            return redirect(proxima_pagina)
    else:
        flash('usuario não logado')
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Logout efetuado com sucesso!')
    return redirect(url_for('index'))



if __name__ == '__main__':
    app.run(debug=True)