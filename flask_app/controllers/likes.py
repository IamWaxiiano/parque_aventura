from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.usuario import Usuario
from flask_app.models.visita import Visita
from flask_app.models.like import Like
from flask import Blueprint

likes_bp = Blueprint("likes", __name__)

@likes_bp.route("/like")
def like():
    datos = {
        "visitas_id": request.form["visitas_id"],
        "usuarios_id": request.form["usuarios_id"]
    }
    Like.save(datos)
    return redirect("/dashboard")