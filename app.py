from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = 'ef4e1f1ed84aef584053dec093ceffb2'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///produtos.db'
db = SQLAlchemy(app)

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)

class Produto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(150), nullable=False)
    preco = db.Column(db.String(50), nullable=False)

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = Usuario.query.filter_by(username=username, password=password).first()
        if user:
            session['user_id'] = user.id # Armazena o ID do usuário na sessão
            return redirect(url_for('index'))  # Redireciona para a página de produtos
        else:
            return "Login falhou"
    return render_template('login.html')

@app.route('/index')
def index():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    produtos = Produto.query.all()
    return render_template('index.html', produtos=produtos)

@app.route('/produto/novo', methods=['GET', 'POST'])
def cadastrar_produto():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    if request.method == 'POST':
        nome = request.form['nome']
        preco = request.form['preco']
        novo_produto = Produto(nome=nome, preco=preco)
        db.session.add(novo_produto)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('cadastro_produto.html')

@app.route('/produto/editar/<int:id>', methods=['GET', 'POST'])
def editar_produto(id):
    if 'user_id' not in session:
        return redirect(url_for('login'))
    produto = Produto.query.get_or_404(id)
    if request.method == 'POST':
        produto.nome = request.form['nome']
        produto.preco = request.form['preco']
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('editar_produto.html', produto=produto)

@app.route('/produto/excluir/<int:id>')
def excluir_produto(id):
    if 'user_id' not in session:
        return redirect(url_for('login'))
    produto = Produto.query.get_or_404(id)
    db.session.delete(produto)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/logout')
def logout():
    session.pop('user_id', None)  # Remove o ID do usuário da sessão
    flash('Você saiu da sessão.', 'success')
    return redirect(url_for('login'))

if __name__ == '__main__':
    #db.create_all()
    app.run(debug=True)
