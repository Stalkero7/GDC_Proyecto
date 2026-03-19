from flask import Flask, render_template, request, redirect, url_for, flash
from database.db_manager import DBManager
from models.subclasses import RegularClient, PremiumClient, CorporateClient
from services.client_service import ClientService
import logging
import io

app = Flask(__name__)
app.secret_key = 'supersecretkey'

# Configuración de logging para mostrar en la app
log_capture_string = io.StringIO()
ch = logging.StreamHandler(log_capture_string)
ch.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logging.getLogger().addHandler(ch)


db_manager = DBManager()
client_service = ClientService(db_manager)

@app.route('/')
def index():
    """
    Muestra la lista de todos los clientes y el feed de actividad reciente.
    """
    try:
        with db_manager as db:
            clients = db.get_all_clients()
        
        log_contents = log_capture_string.getvalue()
        return render_template('index.html', clients=clients, logs=log_contents)
    except Exception as e:
        flash(f"Error al cargar la página: {e}", "danger")
        return render_template('index.html', clients=[], logs="")

@app.route('/add', methods=['GET', 'POST'])
def add_client():
    """
    Gestiona la adición de un nuevo cliente.
    """
    if request.method == 'POST':
        try:
            client_id = int(request.form['id'])
            nombre = request.form['nombre']
            email = request.form['email']
            telefono = request.form['telefono']
            direccion = request.form['direccion']
            tipo_cliente = request.form['tipo_cliente']

            if tipo_cliente == 'PremiumClient':
                nivel = request.form['nivel_membresia']
                client = PremiumClient(client_id, nombre, email, telefono, direccion, nivel)
            elif tipo_cliente == 'CorporateClient':
                empresa = request.form['nombre_empresa']
                client = CorporateClient(client_id, nombre, email, telefono, direccion, empresa)
            else:
                client = RegularClient(client_id, nombre, email, telefono, direccion)

            if client_service.create_client(client):
                flash('Cliente añadido y procesado con éxito!', 'success')
            else:
                flash('Error al procesar el cliente.', 'danger')

            return redirect(url_for('index'))
        except Exception as e:
            flash(f"Error al añadir cliente: {e}", "danger")
            return redirect(url_for('add_client'))
            
    return render_template('add_client.html')

if __name__ == '__main__':
    with DBManager() as db:
        db.setup_database()
    app.run(debug=True)
