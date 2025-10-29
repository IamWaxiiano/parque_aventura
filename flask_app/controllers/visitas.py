from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.usuario import Usuario
from flask_app.models.visita import Visita
from flask_app.models.like import Like
from flask import Blueprint

visitas_bp = Blueprint("visitas", __name__)

def ordenar(e):
    return e["rating"]

@visitas_bp.route("/dashboard")
def dashboard():
    if "id" not in session:
        flash("Debes iniciar sesión primero")
        return redirect("/")
    else:
        listado=Visita.get_all()
        listado.sort(key=ordenar, reverse=True)
        usuario_v=[]
        for visita in listado:
            if visita["usuarios_id"]==session["id"]:
                listado.remove(visita)
                usuario_v.append(visita)
        return render_template('visitas.html',visitas=listado, usuario_v=usuario_v)

@visitas_bp.route("/nueva")
def nueva():
    if "id" not in session:
        flash("Debes iniciar sesión primero")
        return redirect("/")
    else:
        return render_template("nueva.html")
    
@visitas_bp.route("/crear_visita", methods=["POST"])
def crear_peli():
    datos = {
        "parque":request.form["parque"],
        "rating": request.form["rating"],
        "fecha_visita": request.form["fecha_visita"],
        "detalles": request.form["detalles"],
        "usuarios_id": request.form["usuarios_id"]
    }
    Visita.save(datos)
    return redirect("/dashboard")


@visitas_bp.route("/ver/<int:id>")
def ver(id):
    if "id" not in session:
        flash("Debes iniciar sesión primero")
        return redirect("/")
    else:
        visita= Visita.get_one(id)
        visita[0]["nombre_usuario"]=Usuario.get_name(visita[0])
        likes=Like.get_all_visita(visita[0]["id"])
        
        return render_template("ver.html", visita=visita[0], cant_likes=len(likes))
    
@visitas_bp.route("/editar/<int:id>")
def editar(id):
    if "id" not in session:
        flash("Debes iniciar sesión primero")
        return redirect("/")
    else: 
        visita= Visita.get_one(id)
        return render_template("editar.html", visita=visita[0])
    
@visitas_bp.route("/editar_visita", methods=["POST"])
def actualizar():
    datos = {
        "id": request.form["id"],
        "parque":request.form["parque"],
        "rating": request.form["rating"],
        "fecha_visita": request.form["fecha_visita"],
        "detalles": request.form["detalles"],
    }
    Visita.update(datos)
    return redirect("/dashboard")

@visitas_bp.route("/borrar/<int:id>")
def borrar(id):
    if "id" not in session:
        flash("Debes iniciar sesión primero")
        return redirect("/")
    else: 
        Visita.delete(id)
        return redirect("/dashboard")