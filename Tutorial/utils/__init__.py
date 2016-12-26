from utils import database

try:
    database.init_db()
except Exception as err:
    print("Não pude iniciar o db: {}".format(err))
