from langchain_community.utilities import SQLDatabase
import urllib.parse

def init_database(user, password, host, port, database):
    password_encoded = urllib.parse.quote_plus(password)
    db_uri = f"mysql+mysqlconnector://{user}:{password_encoded}@{host}:{port}/{database}"
    return SQLDatabase.from_uri(db_uri)
