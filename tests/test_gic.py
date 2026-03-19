import pytest
from models.subclasses import PremiumClient, RegularClient
from database.db_manager import DBManager
import os

@pytest.fixture
def db():
    """
    Fixture para configurar y limpiar la base de datos de prueba.
    """
    db_path = "test_gdc.db"
    db_manager = DBManager(db_path)
    with db_manager as db:
        db.setup_database()
    yield db_manager
    os.remove(db_path)

def test_premium_client_discount():
    """
    Verifica que los descuentos del PremiumClient se calculen correctamente.
    """
    oro_client = PremiumClient(1, "Test Oro", "oro@test.com", "123456789", "Dir", "oro")
    plata_client = PremiumClient(2, "Test Plata", "plata@test.com", "123456789", "Dir", "plata")
    otro_client = PremiumClient(3, "Test Otro", "otro@test.com", "123456789", "Dir", "bronce")

    assert oro_client.calcular_descuento() == 0.20
    assert plata_client.calcular_descuento() == 0.10
    assert otro_client.calcular_descuento() == 0.05

def test_database_save_and_retrieve(db):
    """
    Verifica que un cliente se pueda guardar y recuperar de la base de datos.
    """
    client = RegularClient(10, "DB Test", "db@test.com", "987654321", "Calle Falsa 123")
    
    with db:
        db.add_client(client)
        retrieved_client = db.get_client(10)
    
    assert retrieved_client is not None
    assert retrieved_client.id == client.id
    assert retrieved_client.nombre == client.nombre
    assert retrieved_client.email == client.email
