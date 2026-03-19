import json
import csv
import logging
from database.db_manager import DBManager

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class FileManager:
    """
    Gestiona la exportación de datos de clientes a/desde archivos JSON y CSV.
    """

    @staticmethod
    def export_to_json(db_manager, file_path):
        """
        Exporta una lista de clientes de la base de datos a un archivo JSON.

        Args:
            db_manager (DBManager): Instancia del gestor de la base de datos.
            file_path (str): La ruta al archivo JSON de salida.
        """
        try:
            clients = db_manager.get_all_clients()
            data_to_export = []
            for client in clients:
                client_data = {
                    "id": client.id,
                    "nombre": client.nombre,
                    "email": client.email,
                    "telefono": client.telefono,
                    "direccion": client.direccion,
                    "tipo": type(client).__name__
                }
                if hasattr(client, 'nivel_membresia'):
                    client_data["nivel_membresia"] = client.nivel_membresia
                if hasattr(client, 'nombre_empresa'):
                    client_data["nombre_empresa"] = client.nombre_empresa
                data_to_export.append(client_data)

            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(data_to_export, f, indent=4, ensure_ascii=False)
            logging.info(f"Datos exportados correctamente a {file_path}")
        except IOError as e:
            logging.error(f"Error al exportar a JSON: {e}")
        except Exception as e:
            logging.error(f"Un error inesperado ocurrió al exportar a JSON: {e}")

    @staticmethod
    def export_to_csv(db_manager, file_path):
        """
        Exporta una lista de clientes de la base de datos a un archivo CSV.

        Args:
            db_manager (DBManager): Instancia del gestor de la base de datos.
            file_path (str): La ruta al archivo CSV de salida.
        """
        try:
            clients = db_manager.get_all_clients()
            with open(file_path, 'w', newline='', encoding='utf-8') as f:
                fieldnames = ['id', 'nombre', 'email', 'telefono', 'direccion', 'tipo', 'nivel_membresia', 'nombre_empresa']
                writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction='ignore')

                writer.writeheader()
                for client in clients:
                    client_data = {
                        "id": client.id, "nombre": client.nombre, "email": client.email,
                        "telefono": client.telefono, "direccion": client.direccion,
                        "tipo": type(client).__name__
                    }
                    if hasattr(client, 'nivel_membresia'):
                        client_data["nivel_membresia"] = client.nivel_membresia
                    if hasattr(client, 'nombre_empresa'):
                        client_data["nombre_empresa"] = client.nombre_empresa
                    writer.writerow(client_data)
            logging.info(f"Datos exportados correctamente a {file_path}")
        except IOError as e:
            logging.error(f"Error al exportar a CSV: {e}")
        except Exception as e:
            logging.error(f"Un error inesperado ocurrió al exportar a CSV: {e}")
