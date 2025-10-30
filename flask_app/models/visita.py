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
        query = """
            SELECT v.*, u.nombre AS nombre_usuario, u.apellido AS apellido_usuario
            FROM visitas v
            LEFT JOIN usuarios u ON v.usuarios_id = u.id;
        """
        visitas_en_bd = Conexion('parque_db').query_db(query)
        return visitas_en_bd
    
    @classmethod
    def get_one(cls, id):
        query = "SELECT * FROM visitas WHERE id = %(id)s;"
        data={"id": id}
        return Conexion('parque_db').query_db(query, data)
    
    @classmethod 
    def update(cls, data):
        query = "UPDATE visitas SET parque=%(parque)s, fecha_visita=%(fecha_visita)s, rating=%(rating)s, detalles=%(detalles)s WHERE id = %(id)s;"
        return Conexion('parque_db').query_db(query,data)
    
    @classmethod
    def delete(cls, id):
        query = "DELETE FROM visitas WHERE id = %(id)s;"
        data={"id": id}
        return Conexion('parque_db').query_db(query, data)