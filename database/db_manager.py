import sqlite3
import logging
from models.subclasses import RegularClient, PremiumClient, CorporateClient

# Configuración básica de logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class DBManager:
    """
    Gestiona las operaciones de la base de datos SQLite para los clientes.
    """
    def __init__(self, db_path="gdc_database.db"):
        """
        Inicializa una nueva instancia de la clase DBManager.

        Args:
            db_path (str): La ruta al archivo de la base de datos SQLite.
        """
        self.db_path = db_path
        self.conn = None

    def __enter__(self):
        """Establece la conexión con la base de datos."""
        try:
            self.conn = sqlite3.connect(self.db_path)
            self.conn.row_factory = sqlite3.Row
            return self
        except sqlite3.Error as e:
            logging.error(f"Error al conectar a la base de datos: {e}")
            raise

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Cierra la conexión con la base de datos."""
        if self.conn:
            self.conn.close()

    def setup_database(self):
        """Crea la tabla de clientes si no existe."""
        try:
            cursor = self.conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS clientes (
                    id INTEGER PRIMARY KEY,
                    nombre TEXT NOT NULL,
                    email TEXT NOT NULL UNIQUE,
                    telefono TEXT,
                    direccion TEXT,
                    tipo_cliente TEXT NOT NULL,
                    nivel_membresia TEXT,
                    nombre_empresa TEXT
                )
            """)
            self.conn.commit()
            logging.info("La base de datos y la tabla 'clientes' han sido configuradas.")
        except sqlite3.Error as e:
            logging.error(f"Error al crear la tabla: {e}")

    def add_client(self, client):
        """Añade un nuevo cliente a la base de datos."""
        try:
            cursor = self.conn.cursor()
            data = {
                "id": client.id, "nombre": client.nombre, "email": client.email,
                "telefono": client.telefono, "direccion": client.direccion,
                "tipo_cliente": type(client).__name__
            }
            if isinstance(client, PremiumClient):
                data["nivel_membresia"] = client.nivel_membresia
                data["nombre_empresa"] = None
            elif isinstance(client, CorporateClient):
                data["nivel_membresia"] = None
                data["nombre_empresa"] = client.nombre_empresa
            else: # RegularClient
                data["nivel_membresia"] = None
                data["nombre_empresa"] = None

            cursor.execute("""
                INSERT INTO clientes (id, nombre, email, telefono, direccion, tipo_cliente, nivel_membresia, nombre_empresa)
                VALUES (:id, :nombre, :email, :telefono, :direccion, :tipo_cliente, :nivel_membresia, :nombre_empresa)
            """, data)
            self.conn.commit()
            logging.info(f"Cliente '{client.nombre}' añadido a la base de datos.")
        except sqlite3.IntegrityError:
            logging.warning(f"El cliente con email '{client.email}' ya existe.")
        except sqlite3.Error as e:
            logging.error(f"Error al añadir cliente: {e}")

    def get_client(self, client_id):
        """Obtiene un cliente por su ID."""
        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT * FROM clientes WHERE id = ?", (client_id,))
            row = cursor.fetchone()
            if row:
                client_type = row["tipo_cliente"]
                if client_type == "PremiumClient":
                    return PremiumClient(row["id"], row["nombre"], row["email"], row["telefono"], row["direccion"], row["nivel_membresia"])
                elif client_type == "CorporateClient":
                    return CorporateClient(row["id"], row["nombre"], row["email"], row["telefono"], row["direccion"], row["nombre_empresa"])
                else:
                    return RegularClient(row["id"], row["nombre"], row["email"], row["telefono"], row["direccion"])
            return None
        except sqlite3.Error as e:
            logging.error(f"Error al obtener cliente: {e}")
            return None

    def get_all_clients(self):
        """Obtiene todos los clientes de la base de datos."""
        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT * FROM clientes")
            rows = cursor.fetchall()
            clients = []
            for row in rows:
                client_type = row["tipo_cliente"]
                if client_type == "PremiumClient":
                    client = PremiumClient(row["id"], row["nombre"], row["email"], row["telefono"], row["direccion"], row["nivel_membresia"])
                elif client_type == "CorporateClient":
                    client = CorporateClient(row["id"], row["nombre"], row["email"], row["telefono"], row["direccion"], row["nombre_empresa"])
                else:
                    client = RegularClient(row["id"], row["nombre"], row["email"], row["telefono"], row["direccion"])
                clients.append(client)
            return clients
        except sqlite3.Error as e:
            logging.error(f"Error al obtener todos los clientes: {e}")
            return []

    def update_client(self, client):
        """Actualiza un cliente existente en la base de datos."""
        try:
            cursor = self.conn.cursor()
            data = {
                "id": client.id, "nombre": client.nombre, "email": client.email,
                "telefono": client.telefono, "direccion": client.direccion,
                "tipo_cliente": type(client).__name__
            }
            if isinstance(client, PremiumClient):
                data["nivel_membresia"] = client.nivel_membresia
                data["nombre_empresa"] = None
            elif isinstance(client, CorporateClient):
                data["nivel_membresia"] = None
                data["nombre_empresa"] = client.nombre_empresa
            else: # RegularClient
                data["nivel_membresia"] = None
                data["nombre_empresa"] = None

            cursor.execute("""
                UPDATE clientes
                SET nombre = :nombre, email = :email, telefono = :telefono, direccion = :direccion,
                    tipo_cliente = :tipo_cliente, nivel_membresia = :nivel_membresia, nombre_empresa = :nombre_empresa
                WHERE id = :id
            """, data)
            self.conn.commit()
            logging.info(f"Cliente con ID '{client.id}' actualizado.")
        except sqlite3.Error as e:
            logging.error(f"Error al actualizar cliente: {e}")

    def delete_client(self, client_id):
        """Elimina un cliente de la base de datos por su ID."""
        try:
            cursor = self.conn.cursor()
            cursor.execute("DELETE FROM clientes WHERE id = ?", (client_id,))
            self.conn.commit()
            logging.info(f"Cliente con ID '{client_id}' eliminado.")
        except sqlite3.Error as e:
            logging.error(f"Error al eliminar cliente: {e}")
