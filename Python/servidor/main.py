from flask import Flask, render_template, request, redirect
from modelo_contacto import Contacto
app = Flask(__name__)
app.secret_key = 'password'
app.debug = True

app = Flask(__name__)

@app.route(r'/', methods=['GET'])
def agenda():
    #return "Hola Ingenieros de Softaware de Platzi"
    contactos = Contacto.query().fetch()
    return render_template('agenda.html',contactos=contactos)

@app.route(r'/adicionar', methods=['GET', 'POST'])
def adicionarContacto():

    if request.form:
        contacto = Contacto(nombre=request.form.get('nombre'),
                            telefono=request.form.get('telefono'),
                            email=request.form.get('email'))
        contacto.put()
        flash('¡ Se añadio el contato !')

        print(request.form.get('nombre'))
        print(request.form.get('telefono'))
        print(request.form.get('email'))

    return render_template('adicionar_contacto.html')

@app.route(r'/contactos/<uid>', methods=['GET'])
def detallesContacto(uid):
    contacto = Contacto.get_by_id(int(uid))

    if not contacto:
        return redirect('/', code=301)

    return render_template('contacto.html', contacto=contacto)

@app.route(r'/borrar',methods=['POST'])
def borrarContacto():
    contacto = Contacto.get_by_id(int(request.form.get('uid')))
    contacto.key.delete()
    return redirect('/contactos/{}'.format(contacto.key.id()))

if __name__ == "__main__":
    app.run()
