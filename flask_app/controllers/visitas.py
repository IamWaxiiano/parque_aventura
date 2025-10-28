from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.usuario import Usuario
from flask_app.models.visita import Visita
from flask import Blueprint

visitas_bp = Blueprint("visitas", __name__)

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
        print(visita)
        visita[0]["nombre_usuario"]=Usuario.get_name({"id": visita[0]["usuarios_id"]})
        return render_template("ver.html", visita=visita[0])