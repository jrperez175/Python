from flask import Flask,request,jsonify
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__) #Instancia la aplicacion
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost:3306/bdpythonapi' #String de conexion
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False #Deshabilita la gestión de notificaciones de sqlalchemy

db = SQLAlchemy(app) #Crear un objeto que representa nuestra base de datos
ma = Marshmallow(app)

#Creacion Tabla Categoria
class Categoria(db.Model):
    cat_id = db.Column(db.Integer, primary_key=True)
    cat_nom = db.Column(db.String(100))
    cat_desp = db.Column(db.String(100))

    def __init__(self,cat_nom,cat_desp):
        self.cat_nom = cat_nom
        self.cat_desp = cat_desp

db.create_all()

#Esquema Categoria
class CategoriaSchema(ma.Schema):
    class Meta:
        fields = ('cat_id','cat_nom','cat_desp')

#Una sola respuesta
categoria_schema =  CategoriaSchema()

#Varias respuestas
categorias_schema = CategoriaSchema(many = True)

#GET
@app.route('/categoria',methods=['GET'])
def get_categoria():
    all_categorias = Categoria.query.all()
    result = categorias_schema.dump(all_categorias)
    return jsonify(result)

#GET por Id
@app.route('/categoria/<id>',methods=['GET'])
def get_categoria_id(id):
    una_categoria = Categoria.query.get(id)
    return categoria_schema.jsonify(una_categoria)

#POST
@app.route('/categoria',methods=['POST'])
def insert_categoria():
    data = request.get_json(force=True) #Forza el texto a que sea JSON
    
    cat_nom = data['cat_nom']
    cat_desp = data['cat_desp']

    nuevo_registro = Categoria(cat_nom, cat_desp)

    db.session.add(nuevo_registro)
    db.session.commit()

    return categoria_schema.jsonify(nuevo_registro)


#Mensaje de Bienvenida
@app.route('/',methods=['GET'])
def index ():
    return jsonify({'Mensaje':'Bienvenido al tutorial API REST Python'})
    

if __name__ == "__main__":
    app.run(debug=True) #ejecuta la app y va compilando con el parametro debug