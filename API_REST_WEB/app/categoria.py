from flask import Flask,request,jsonify
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__) #Instacia la aplicacion
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost:3386/bdpythonapi' #String de conenxion
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False #Deshabilita la gestión de notificaciones de sqlalchemy

db = SQLAlchemy(app) #rear un objeto que representa nuestra base de datos
ma = Marshmallow(app)

class Categoria(db.model):
    cat_id = db.Column(db.Integer, primary_key=True)
    cat_nom = db.Column(db.String(100))
    cat_desp = db.Column(db.String(100))

    def __init_(self,cat_nom,cat_desp):
        self.cat_nom = cat_nom
        self.cat_desp = cat_desp

db.create_all()

#Mensaje de Bienvenida
@app.route('/',methods=['GET'])
def index ():
    return jsonify({'Mensaje':'Bienvenido al tutorial API REST Python'})
    

if __name__ == "__main__":
    app.run(debug=True) #ejecuta la app y va compilando con el parametro debug