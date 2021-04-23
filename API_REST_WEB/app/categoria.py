from flask import Flask, jsonify

app = Flask(__name__) #Instacia la aplicacion


@app.route('/',methods=['GET'])

def index ():
    return jsonify({'Mensaje':'Bienvenido al tutorial API REST Python'})

if __name__ == "__main__":
    app.run(debug=True) #ejecuta la app y va compilando con el parametro debug