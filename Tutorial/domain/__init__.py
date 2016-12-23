"""Foi necessário inicializar Base aqui porque as classes de domínio herdam dele.
Tentei colocar no utils.database.py, mas não foi possível porque database importa
os modelos causando um conflito.
O declarative_base retorna um declarative o qual permite que o mapeamento dos
 atributos sejam feitos dentro da classe da maneira que está. Assim o código
 muito mais fácil de entender. Da maneira clássica, com o mapper, não fica legal
 apesar de funcionar também."""
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
