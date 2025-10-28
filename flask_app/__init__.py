from flask import Flask

app = Flask(__name__) #Crea instancia de Flask

app.secret_key = "clave secreta, shhhh!"