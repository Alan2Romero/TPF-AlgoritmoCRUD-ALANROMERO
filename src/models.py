from database import get_db_connection

class ProductoModel:
    @staticmethod
    def get_all():
        conn = get_db_connection()
        query = '''
            SELECT productos.id, productos.nombre, productos.precio, categorias.nombre as categoria 
            FROM productos 
            LEFT JOIN categorias ON productos.categoria_id = categorias.id
        '''
        productos = conn.execute(query).fetchall()
        conn.close()
        return [dict(row) for row in productos]

    @staticmethod
    def create(nombre, precio, categoria_id):
        conn = get_db_connection()
        conn.execute('INSERT INTO productos (nombre, precio, categoria_id) VALUES (?, ?, ?)', 
                     (nombre, precio, categoria_id))
        conn.commit()
        conn.close()

    @staticmethod
    def delete(producto_id):
        conn = get_db_connection()
        conn.execute('DELETE FROM productos WHERE id = ?', (producto_id,))
        conn.commit()
        conn.close()