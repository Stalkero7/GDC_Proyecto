import requests
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def validate_identity(client_id):
    """
    Simula la validación de la identidad de un cliente contra una API externa.

    Args:
        client_id (int): El ID del cliente a validar.

    Returns:
        bool: True si la validación es exitosa, False en caso contrario.
    """
    # Usaremos un servicio de prueba como JSONPlaceholder para simular la API
    api_url = f"https://jsonplaceholder.typicode.com/users/{client_id}"
    try:
        response = requests.get(api_url)
        response.raise_for_status()  # Lanza una excepción para códigos de error HTTP
        logging.info(f"Validación de identidad para el cliente ID {client_id} fue exitosa.")
        return True
    except requests.exceptions.HTTPError as http_err:
        if response.status_code == 404:
            logging.warning(f"No se encontró el cliente con ID {client_id} en el servicio externo.")
        else:
            logging.error(f"Error HTTP durante la validación de identidad: {http_err}")
        return False
    except requests.exceptions.RequestException as req_err:
        logging.error(f"Error de conexión durante la validación de identidad: {req_err}")
        return False

def send_welcome_email(client_email, client_name):
    """
    Simula el envío de un correo electrónico de bienvenida a un nuevo cliente.

    Args:
        client_email (str): La dirección de correo electrónico del cliente.
        client_name (str): El nombre del cliente.

    Returns:
        bool: True si el correo se envió (simulado) con éxito, False en caso contrario.
    """
    # Usaremos un servicio como Mailtrap o un simple POST a un endpoint de prueba
    # Para este ejemplo, simularemos un POST a httpbin.org
    email_api_url = "https://httpbin.org/post"
    email_data = {
        "to": client_email,
        "from": "noreply@solutiontech.com",
        "subject": "¡Bienvenido a Solution Tech!",
        "body": f"Hola {client_name},\n\nGracias por registrarte. Estamos felices de tenerte con nosotros."
    }
    try:
        response = requests.post(email_api_url, json=email_data)
        response.raise_for_status()
        logging.info(f"Correo de bienvenida enviado a {client_email}.")
        return True
    except requests.exceptions.RequestException as req_err:
        logging.error(f"Error al enviar el correo de bienvenida: {req_err}")
        return False
