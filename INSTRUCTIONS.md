
Project Name: GDC_Proyecto (Intelligent Client Manager).


Client: Solution Tech (Tech Startup).
Goal: Develop a modular Python system using OOP to manage different client types, ensuring data persistence and external API integration.
Core Architecture: Modular design with strict separation of concerns (Models, Database, Services, Utils).

RECUERDA: LAS EXPLICACIONES DENTRO DEL CODIGO DEBEN SER EN ESPAÑOL
REMEMBER: THE EXPLANATIONS INSIDE THE CODE MUST BE IN SPANISH

RECUERDA: LA INTERFAZ DE USUARIO DEBE ESTAR EN ESPAÑOL
REMEMBER: THE USER INTERFACE MUST BE IN SPANISH



Archives Structure:

A. Models (models/)
base_client.py: Contains the Cliente base class with private attributes (Encapsulation).
subclasses.py: Implements RegularClient, PremiumClient, and CorporateClient using Inheritance and Polymorphism.

B. Data Layer (database/)
db_manager.py: Handles all SQLite operations (Create, Read, Update, Delete).
file_manager.py: Handles exporting and importing data via JSON and CSV.

C. External Services (services/)
api_integration.py: Contains logic for Identity Validation and Email Notifications using the requests library.

D. Utilities (utils/)
validators.py: Advanced regex for email, phone, and address validation.
logger.py: Implements a logging system to record every system operation.

ROAD MAP: DO NOT MOVE FORWARD UNLESS EACH PHASE IS FINISHED IN ORDER.

Phase 1: Foundation (Models)
Implement the Cliente class with attributes: id, name, email, phone, and address.
Apply the __str__ and __eq__ special methods.
Create the subclasses with specialized discount or service logic.

Phase 2: Persistence (Database & Files)
Set up the SQLite schema for clients.
Ensure the system can save a client object directly to the database and export the list to JSON.

Phase 3: Integration (APIs & Logic)
Create a "Service" that simulates checking a client's ID against an external API.
Implement a "Welcome Email" trigger when a new client is successfully added.

Phase 4: Interface & Quality (GUI & Tests)
Build a basic Flask interface to manage these clients.

Write Unit Tests in the tests/ folder to verify that PremiumClient logic and Database saves are working correctly.

4. The "Master Rules" for the Agent
Add these constraints to the prompt to keep the AI aligned with your needs:
Code Quality: Every function must have a docstring explaining what it does in spanish.
Error Handling: Use try-except blocks for all database and API calls.
Encapsulation: No class attribute should be accessed directly; use getters and setters (properties).
Step-by-Step: Ask for confirmation after finishing each file before proceeding to the next.