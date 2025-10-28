from flask_app.config.conexion import Conexion

class Visita:
    def __init__(self,data):
        self.id = data['id']
        self.parque = data['parque']
        self.fecha_visita = data["fecha_visita"]
        self.rating = data["rating"]
        self.detalles = data["detalles"]
        self.usuarios_id = data["usuarios_id"]

    @classmethod
    def save(cls,data):
        query = "INSERT INTO visitas (parque, fecha_visita, rating, detalles, usuarios_id) VALUES (%(parque)s, %(fecha_visita)s,%(rating)s, %(detalles)s, %(usuarios_id)s);"
        return Conexion('parque_db').query_db(query, data)
    
    @classmethod
    def get_all(cls):
        query= "SELECT * from visitas"
        visitas_en_bd=Conexion('parque_db').query_db(query)
        visitas=[]
        for visita in visitas_en_bd:
            visitas.append(cls(visita))
        return visitas
    
    @classmethod
    def get_one(cls, id):
        query = "SELECT * FROM visitas WHERE id = %(id)s;"
        data={"id": id}
        return Conexion('parque_db').query_db(query, data)