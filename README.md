Passo a Passo para Executar o Script Flask com SQLite

1. Instalar o Python
Verifique se o Python 3.x está instalado na sua máquina:

Se não estiver, faça o download e instale o Python pelo site oficial: https://www.python.org/downloads/

2. Criar um Ambiente Virtual (opcional, mas recomendado)
No diretório onde o script será executado, crie um ambiente virtual para isolar as dependências do projeto:

python -m venv venv
Ative o ambiente virtual:

No Windows:
venv\Scripts\activate
No Linux/Mac:
source venv/bin/activate

3. Instalar as Dependências
Com o ambiente ativado, instale as bibliotecas necessárias:
pip install flask flask_sqlalchemy

5. Configurar os Arquivos HTML
Certifique-se de que você tem os arquivos HTML nas pastas corretas dentro do diretório do projeto:

templates/login.html
templates/index.html
templates/cadastro_produto.html
templates/editar_produto.html
O Flask espera que todos os templates HTML estejam na pasta templates.

5. Criar o Banco de Dados
Antes de rodar a aplicação, você precisa criar o banco de dados SQLite. No final do seu script Python, a linha #db.create_all() está comentada. Você precisará descomentar essa linha temporariamente para criar o banco.

Descomente a linha e execute o script:

python
Copiar código
if __name__ == '__main__':
    db.create_all()  # Esta linha deve estar descomentada
    app.run(debug=True)
Rode o script:

python nome_do_seu_script.py
Isso criará o arquivo produtos.db.

Depois de criar o banco, comente novamente a linha db.create_all() para evitar recriar o banco toda vez que rodar o script:
#db.create_all()

6. Rodar o Servidor Flask
Agora você pode rodar a aplicação:

python nome_do_seu_script.py
Você verá uma saída semelhante a:

* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
Abra o navegador e vá para http://127.0.0.1:5000/ para acessar a aplicação.

7. Interagir com a Aplicação
Login: Você pode criar diretamente um usuário no banco de dados ou fazer uma página de registro.
Cadastrar produtos: Use a página de cadastro para adicionar produtos ao sistema.
Editar/Excluir produtos: Navegue pelo sistema para editar ou excluir produtos.
