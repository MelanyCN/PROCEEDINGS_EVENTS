from mongoengine import connect

#def init_db():
#    connect(db='nombre_del_db', host='localhost', port=27017)

class Config:
    DEBUG = True
    SECRET_KEY = 'supersecretkey'