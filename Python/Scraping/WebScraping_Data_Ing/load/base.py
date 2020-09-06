from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#Documentacion
#https://j2logo.com/python/sqlalchemy-tutorial-de-python-sqlalchemy-guia-de-inicio/

engine = create_engine('sqlite:///newspaper.db') #Crea una instancia de la BD deseada
Session = sessionmaker(bind = engine) 
Base = declarative_base()

