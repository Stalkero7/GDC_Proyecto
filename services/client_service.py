from database.db_manager import DBManager
from services.api_integration import validate_identity, send_welcome_email
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class ClientService:
    """
    Coordina las operaciones de lógica de negocio para los clientes.
    """
    def __init__(self, db_manager: DBManager):
        """
        Inicializa una nueva instancia de la clase ClientService.

        Args:
            db_manager (DBManager): Una instancia del gestor de la base de datos.
        """
        self.db_manager = db_manager

    def create_client(self, client):
        """
        Orquesta la creación de un nuevo cliente.

        El proceso incluye:
        1. Validar la identidad del cliente.
        2. Añadir el cliente a la base de datos.
        3. Enviar un correo de bienvenida.

        Args:
            client (Cliente): El objeto cliente a crear.

        Returns:
            bool: True si el cliente se creó con éxito, False en caso contrario.
        """
        logging.info(f"Iniciando proceso de creación para el cliente: {client.nombre}")

        # 1. Validar identidad
        if not validate_identity(client.id):
            logging.error(f"La validación de identidad falló para el cliente ID: {client.id}. Proceso abortado.")
            return False

        # 2. Añadir a la base de datos
        try:
            with self.db_manager as db:
                db.add_client(client)
        except Exception as e:
            logging.error(f"No se pudo guardar el cliente en la base de datos: {e}. Proceso abortado.")
            return False

        # 3. Enviar correo de bienvenida
        if not send_welcome_email(client.email, client.nombre):
            logging.warning(f"El cliente '{client.nombre}' fue creado, pero el correo de bienvenida no pudo ser enviado.")
            # Se podría implementar una lógica de reintento aquí.
            # Por ahora, la creación se considera exitosa si se guarda en la BD.
        
        logging.info(f"Cliente '{client.nombre}' creado y procesado exitosamente.")
        return True
