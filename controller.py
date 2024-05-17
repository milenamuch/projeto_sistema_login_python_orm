from model import Pessoa
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import hashlib

def retorna_session():
    CONN = "sqlite:///projeto_login.db"
    engine = create_engine(CONN, echo = True)
    Session = sessionmaker(bind = engine)
    return Session()

class ControllerCadastro():
    @classmethod
    def verifica_dados(cls, nome, email, senha):
        
        if len(nome) > 50 or len(nome) < 3:
            return 2
        if len(email) > 200:
            return 3
        if len(senha) > 100 or len(senha) < 6:
            return 4
        
        return 1

    @classmethod
    def cadastrar(cls, nome, email, senha):
        session = retorna_session() #conectar no banco de dados
        usuario = session.query(Pessoa).filter(Pessoa.email == email).all() #vai pegar todos os cadastros que tem o mesmo email que o usuário vai passar, teoricamente pode trazer zero ou 1 resultado
        
        if len(usuario) > 0: #se o retorno for maior do que zero, quer dizer que já existe um email cadastrado no sistema
            return 5
        
        dados_verificados = cls.verifica_dados(nome, email, senha) #vai verificar os dados conforme definido na função
        
        if dados_verificados != 1: #o 1 é sucesso no cadastro, mas se for diferente disto, irá retornar o valor do respectivo erro
            return dados_verificados
        
        try:
            senha = hashlib.sha256(senha.encode()).hexdigest() #criptografa a senha do usuário
            pessoa = Pessoa(nome = nome, email = email, senha = senha) #instancia a classe Pessoa
            session.add(pessoa) #cria uma sessão para inserir no banco
            session.commit() #cria uma sessão para enviar os dados para o banco
            return 1
            
        except:
            return 6
        

class ControllerLogin():
    @classmethod
    def login(cls, email, senha):
        session = retorna_session() #cria uma instância de session
        senha = hashlib.sha256(senha.encode()).hexdigest()
        usuario_logado = session.query(Pessoa).filter(Pessoa.email == email).filter(Pessoa.senha == senha).all()
        
        if len(usuario_logado) == 1:
            return {'logado': True, 'id':usuario_logado[0].id}
        else:
            return False
        
        
print(ControllerCadastro.cadastrar('Maria', 'maria@gmail.com', 'maria@123'))