from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.usuario import Usuario
from flask_app.models.visita import Visita
from flask import Blueprint


usuarios_bp = Blueprint('usuarios',__name__)

@usuarios_bp.route("/register", methods=["POST"])
def register():
    data={
        "nombre":request.form["nombre"],
        "apellido": request.form["apellido"],
        "email": request.form["email_1"],
        "password": request.form["contra_1"]
    }

    if Usuario.ValidarEmail(data["email"]) is None:
        Usuario.save(data)
        usuario=Usuario.ValidarEmail(data["email"])
        session["id"]=usuario["id"]
        session["nombre"]=usuario["nombre"]
        session["apellido"]=usuario["apellido"]
        session["password"]=usuario["password"]
        return redirect('/dashboard')
    else: 
        flash("El email ya esta registrado")
        return redirect(request.referrer)

@usuarios_bp.route("/login", methods=["POST"])
def login():
    datos={
        "email": request.form["email_2"],
        "password": request.form["contra_2"]
    }
    usuario=Usuario.login(datos)
    if usuario is None:
        flash("Email o contraseña incorrectos")
        return redirect(request.referrer)
    else:
        session["nombre"]=usuario["nombre"]
        session["apellido"]=usuario["apellido"]
        session["password"]=datos["password"]
        session["id"]=usuario["id"]
        return redirect("/dashboard")

@usuarios_bp.route("/logout")
def logout():
    session.clear()
    return redirect("/")



