from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.usuario import Usuario
from flask_app.models.visita import Visita
from flask_app.models.like import Like
from flask import Blueprint

likes_bp = Blueprint("likes", __name__)

@likes_bp.route("/like-post/<int:id_visita>")
def like(id_visita):
    visita= Visita.get_one(id_visita)
    if not visita:
        flash("La visita no existe")
    else:
        datos={
            "usuarios_id": session["id"],
            "visitas_id": id_visita
        }
        like=Like.save(datos)
    return redirect(f"/ver/{id_visita}")