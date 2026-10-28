from jogoteca import app
import os
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = 'victor$gasparotti'

SQLALCHEMY_DATABASE_URI = \
    '{SGBD}://{usuario}:{senha}@{servidor}/{database}'.format(
    SGBD='mysql+mysqlconnector',
    usuario = 'root',
    senha = os.getenv('PASSWORD_SQL'),
    servidor = 'localhost',
    database = 'jogoteca'
    )