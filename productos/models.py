from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class producto(db.Model):
    id = db.Column("producto_id", db.Integer, primary_key=True)
    producto_nombre = db.Column(db.String(50))
    producto_cantidad = db.Column(db.Integer)
    producto_valor = db.Column(db.Integer)
    

    def __init__(self, datos):
        self.producto_nombre = datos["nombre"]
        self.producto_cantidad = datos["cantidad"]
        self.producto_valor = datos["valor"]
        