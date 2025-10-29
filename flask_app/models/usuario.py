from flask_app.config.conexion import Conexion
import bcrypt

class Usuario:
    def __init__(self, data):     
        self.id = data['id']
        self.nombre = data['nombre']
        self.apellido = data['apellido']
        self.email = data['email']
        self.password = data['password']

    @classmethod
    def save(cls, data):
        hashed_password=bcrypt.hashpw(data['password'].encode('utf-8'),bcrypt.gensalt())
        data["password"]=hashed_password
        usuario= cls.ValidarEmail(data["email"])
        if usuario is None:
            query = "INSERT INTO usuarios (nombre, apellido, email, password) VALUES (%(nombre)s, %(apellido)s, %(email)s, %(password)s);"
            return Conexion('parque_db').query_db(query, data)
        else: return None
        
    @classmethod
    def ValidarEmail(cls, email):
        query= "SELECT * from usuarios where email=%(email)s"
        data = {"email": email}
        usuario=Conexion('parque_db').query_db(query, data)
        return usuario[0] if usuario else None
    
    @classmethod
    def get_all(cls):
        query= "SELECT * from usuarios"
        usuarios_en_bd= Conexion('parque_db').query_db(query)
        usuarios=[]
        for usuario in usuarios_en_bd:
            usuarios.append(cls(usuario))
        return usuarios
    
    @classmethod
    def login(cls,datos):
        query= "SELECT * from usuarios where email=%(email)s"
        data = {"email": datos["email"]}
        usuario= Conexion('parque_db').query_db(query, data)
        hashed_password=usuario[0]["password"].encode('utf-8')
        if bcrypt.checkpw(datos["password"].encode('utf-8'),hashed_password):
            return usuario[0] if usuario else None
        
    @classmethod
    def get_name(cls,datos):
        query="SELECT * from usuarios where id=%(id)s"
        data={"id": datos["usuarios_id"]}
        usuario= Conexion('parque_db').query_db(query, data)
        return usuario[0]["nombre"] if usuario else None