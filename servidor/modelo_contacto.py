from google.appengine.ext import ndb

class Contacto(ndb.Model):
    nombre = ndb.StringProperty()
    telefono = ndb.StringProperty()
    email = ndb.StringProperty()


