
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship, backref
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey


from settings import DATABASES

DB_URI = "{0}://{1}:{2}@{3}:{4}/{5}".format(
    DATABASES['default']['ENGINE'],
    DATABASES['default']['USER'],
    DATABASES['default']['PASSWORD'],
    DATABASES['default']['HOST'],
    DATABASES['default']['PORT'],
    DATABASES['default']['NAME']
)

# an Engine, which the Session will use for connection
engine = create_engine(DB_URI)
# create a configured "Session" class
Session = sessionmaker(bind=engine)
# create a Session
session = Session()

def get_connection():
    return engine.connect()


def query_test():
    connection = get_connection()
    result = connection.execute("select name from test")
    for row in result:
        print("name:", row['name'])
    connection.close()


def transaction_test():
    connection = get_connection()
    trans = connection.begin()
    try:
        connection.execute()
        trans.commit()
    except:
        trans.rollback()
