#slqalchemy traduzir os comandos em python em sql
#sqlite

from sqlalchemy import create_engine, Column, String, Integer, Boolean, Float, ForeignKey #permite criar o banco de dados / ForeingnnKey permite conectar tabelas diferentes
from sqlalchemy.orm import declarative_base #criando a base do banco de dados
from sqlalchemy_utils.types import ChoiceType

db = create_engine('sqlite:///banco.db') #copiar e colar no arquivo alembic.ini

#criar a base do banco de dados
Base = declarative_base() #permite criar tabela

#criar as classes/tabelas do banco
#Usuario
class Usuario(Base): #subclasse da classe Base
    __tablename__ = 'usuarios'
    #definir campos
    id = Column('id',Integer,primary_key=True,autoincrement=True) #todo id tem que ter uma chave primaria, que é único para cada item da tabela
    nome = Column('nome',String)
    email = Column('email', String, nullable=False)#nullable nao permite que essa coluna seja vazia
    senha = Column('senha', String)
    ativo = Column('ativos',Boolean)
    admin = Column('admin', Boolean, default=False) #o padrao é falso, ou seja, nesse caso só vai ser admin quando for indicado que é admin 
    #ele vai ser sempre preenchido como verdadeiro ou podemos editar para falso quando for criado, nao é obrigado a passar esse campo conforme parametros

    def __init__(self,nome,email, senha, ativo=True, admin=False): #init diz que quando dentro do codigo, quando criar um usuario, ela espera o comando que quiser quando iniciar um novo usuario
        self.nome = nome
        self.email = email
        self.senha = senha
        self.ativo = ativo
        self.admin = admin

#Pedido
class Pedido(Base):
    __tablename__ = 'pedidos'

    #choicetype precisa de uma lista de tupla ou tupla de tuplas (chave, valor) chave é o que vai ser armazenado do banco e valor o que enxergar quando print
    # STATUS_PEDIDOS = (
    #     ('PENDENTE','PENDENTE'),
    #     ('CANCELADO', 'CANCELADO'),
    #     ('FINALIZADO', 'FINALIZADO') 
    #     )

    id = Column('id',Integer,primary_key=True,autoincrement=True)
    status = Column('status',String) #pendente, cancelado, finalizado
    usario = Column('usuario', ForeignKey('usuarios.id'))
    preco = Column('preco',Float,nullable=False) #obrigado a ter o preço
    # itens = 

    def __init__(self, usuario, status='PENDENTE',preco=0):
        self.usario = usuario
        self.preco = preco
        self.status = status

#ItensPedido
class ItemPedido(Base):
    __tablename__ = 'itens_pedido'

    id = Column('Id',Integer,primary_key=True,autoincrement=True)
    quantidade = Column('quantidade', Integer)
    sabor = Column('sabor', String)
    tamanho = Column('tamanho',String) #poderia definir como Choicetypes
    preco_unitario = Column('preco_unitario',Float) #poderia definir como Choicetypes
    pedido = Column('pedido', ForeignKey('pedidos.id'))


    def __init__(self, quantidade, sabor,tamanho, preco_unitario, pedido):
        self.quantidade = quantidade
        self.sabor = sabor
        self.tamanho = tamanho
        self.preco_unitario = preco_unitario
        self.pedido - pedido


#executa a criação dos metadados do seu banco (cria efetivamente o banco de dados)
