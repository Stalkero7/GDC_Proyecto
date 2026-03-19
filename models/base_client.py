import re

class Cliente:
    """
    Clase base que representa un cliente con sus datos básicos.

    Attributes:
        _id (int): Identificador único del cliente.
        _nombre (str): Nombre del cliente.
        _email (str): Correo electrónico del cliente.
        _telefono (str): Teléfono del cliente.
        _direccion (str): Dirección del cliente.
    """
    def __init__(self, id, nombre, email, telefono, direccion):
        """
        Inicializa una nueva instancia de la clase Cliente.

        Args:
            id (int): Identificador único del cliente.
            nombre (str): Nombre del cliente.
            email (str): Correo electrónico del cliente.
            telefono (str): Teléfono del cliente.
            direccion (str): Dirección del cliente.
        """
        self._id = id
        self._nombre = nombre
        self.email = email  # Usa el setter para la validación
        self.telefono = telefono  # Usa el setter para la validación
        self._direccion = direccion

    @property
    def id(self):
        """Obtiene el ID del cliente."""
        return self._id

    @property
    def nombre(self):
        """Obtiene el nombre del cliente."""
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        """Establece el nombre del cliente."""
        self._nombre = nombre

    @property
    def email(self):
        """Obtiene el email del cliente."""
        return self._email

    @email.setter
    def email(self, email):
        """
        Establece el email del cliente, validando su formato.

        Raises:
            ValueError: Si el formato del email no es válido.
        """
        if not re.match(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", email):
            raise ValueError("Formato de correo electrónico no válido.")
        self._email = email

    @property
    def telefono(self):
        """Obtiene el teléfono del cliente."""
        return self._telefono

    @telefono.setter
    def telefono(self, telefono):
        """
        Establece el teléfono del cliente, validando su formato.

        Raises:
            ValueError: Si el formato del teléfono no es válido.
        """
        if not re.match(r"^\+?1?\d{9,15}$", telefono):
            raise ValueError("Formato de teléfono no válido.")
        self._telefono = telefono

    @property
    def direccion(self):
        """Obtiene la dirección del cliente."""
        return self._direccion

    @direccion.setter
    def direccion(self, direccion):
        """Establece la dirección del cliente."""
        self._direccion = direccion

    def __str__(self):
        """Devuelve una representación en cadena del cliente."""
        return f"Cliente(ID: {self.id}, Nombre: {self.nombre}, Email: {self.email})"

    def __eq__(self, other):
        """Compara si dos clientes son iguales basándose в el ID."""
        if isinstance(other, Cliente):
            return self.id == other.id
        return False
