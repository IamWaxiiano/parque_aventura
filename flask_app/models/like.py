from flask_app.config.conexion import Conexion

class Like:
    def __init__(self,data):
        self.id = data['id']
        self.visitas_id = data["visitas_id"]
        self.usuarios_id = data["usuarios_id"]

    @classmethod
    def save(cls,data):
        query = "INSERT INTO likes (visitas_id, usuarios_id) VALUES (%(visitas_id)s, %(usuarios_id)s);"
        return Conexion('parque_db').query_db(query, data)
    
    @classmethod
    def get_all_visita(cls, id):
        query= "SELECT * from visitas WHERE id=%(visitas_id)s"
        data={"visitas_id": id}
        likes_en_bd=Conexion('parque_db').query_db(query, data)
        likes=[]
        for like in likes_en_bd:
            likes.append(like)
        return likes