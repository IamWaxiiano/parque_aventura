from flask_app import app
from flask import render_template
from flask_app.controllers.usuarios import usuarios_bp
from flask_app.controllers.visitas import visitas_bp
from flask_app.controllers.likes import likes_bp

app.register_blueprint(usuarios_bp)
app.register_blueprint(visitas_bp)
app.register_blueprint(likes_bp)

@app.route('/')
def index():
    return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)