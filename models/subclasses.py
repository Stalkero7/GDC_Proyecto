from models.base_client import Cliente

class RegularClient(Cliente):
    """
    Clase que representa a un cliente regular.
    Hereda de la clase Cliente.
    """
    def __init__(self, id, nombre, email, telefono, direccion):
        """
        Inicializa una nueva instancia de la clase RegularClient.

        Args:
            id (int): Identificador único del cliente.
            nombre (str): Nombre del cliente.
            email (str): Correo electrónico del cliente.
            telefono (str): Teléfono del cliente.
            direccion (str): Dirección del cliente.
        """
        super().__init__(id, nombre, email, telefono, direccion)

    def calcular_descuento(self):
        """
        Calcula el descuento para un cliente regular.
        Los clientes regulares no tienen descuento.

        Returns:
            float: El porcentaje de descuento (0).
        """
        return 0.0

class PremiumClient(Cliente):
    """
    Clase que representa a un cliente premium.
    Hereda de la clase Cliente y añade un nivel de membresía.
    """
    def __init__(self, id, nombre, email, telefono, direccion, nivel_membresia):
        """
        Inicializa una nueva instancia de la clase PremiumClient.

        Args:
            id (int): Identificador único del cliente.
            nombre (str): Nombre del cliente.
            email (str): Correo electrónico del cliente.
            telefono (str): Teléfono del cliente.
            direccion (str): Dirección del cliente.
            nivel_membresia (str): Nivel de membresía del cliente premium.
        """
        super().__init__(id, nombre, email, telefono, direccion)
        self.nivel_membresia = nivel_membresia

    def calcular_descuento(self):
        """
        Calcula el descuento para un cliente premium basado en su nivel de membresía.

        Returns:
            float: El porcentaje de descuento.
        """
        if self.nivel_membresia == 'oro':
            return 0.20  # 20% de descuento
        elif self.nivel_membresia == 'plata':
            return 0.10  # 10% de descuento
        return 0.05  # 5% de descuento por defecto para premium

class CorporateClient(Cliente):
    """
    Clase que representa a un cliente corporativo.
    Hereda de la clase Cliente y añade el nombre de la empresa.
    """
    def __init__(self, id, nombre, email, telefono, direccion, nombre_empresa):
        """
        Inicializa una nueva instancia de la clase CorporateClient.

        Args:
            id (int): Identificador único del cliente.
            nombre (str): Nombre del cliente.
            email (str): Correo electrónico del cliente.
            telefono (str): Teléfono del cliente.
            direccion (str): Dirección del cliente.
            nombre_empresa (str): Nombre de la empresa del cliente corporativo.
        """
        super().__init__(id, nombre, email, telefono, direccion)
        self.nombre_empresa = nombre_empresa

    def calcular_descuento(self):
        """
        Calcula el descuento para un cliente corporativo.

        Returns:
            float: El porcentaje de descuento (15%).
        """
        return 0.15  # 15% de descuento para todos los clientes corporativos
