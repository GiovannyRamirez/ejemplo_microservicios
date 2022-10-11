from flask import redirect

from config_app import create_app, db
from models import producto

app = create_app()

@app.route("/")
def listar():
    data = producto.query.all()
    diccionario_productos = {}
    for d in data:
        p = {
            "id": d.id,
            "nombre": d.producto_nombre,
            "cantidad": d.producto_cantidad,
            "valor": d.producto_valor
        }
        diccionario_productos[d.id] = p
    return diccionario_productos

@app.route("/agregar/<nombre>/<int:cantidad>/<int:valor>")
def agregar(nombre, cantidad, valor):
    datos = {
        "nombre": nombre,
        "cantidad": cantidad,
        "valor": valor
    }
    p = producto(datos)
    db.session.add(p)
    db.session.commit()
    return redirect("/productos/")

@app.route("/eliminar/<int:id>")
def eliminar(id):
    p = producto.query.filter_by(id=id).first()
    db.session.delete(p)
    db.session.commit()
    return redirect("/productos/")

@app.route("/editar/<int:id>/<nombre>/<int:cantidad>/<int:valor>")
def editar(id, nombre, cantidad, valor):
    p = producto.query.filter_by(id=id).first()
    p.producto_nombre = nombre
    p.producto_cantidad = cantidad
    p.producto_valor = valor
    db.session.commit()
    return redirect("/productos/")

@app.route("/buscar/<int:id>")
def buscar(id):
    p = producto.query.filter_by(id=id).first()
    datos = {
        "id": p.id,
        "nombre": p.producto_nombre,
        "cantidad": p.producto_cantidad,
        "valor": p.producto_valor
    }
    return datos


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")