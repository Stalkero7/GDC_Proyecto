
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
1. Create models/base_client.py. Implement a base class Cliente with private attributes for id, name, email, phone, and address to ensure encapsulation.
2. Include advanced validations for the email and phone within the class.
3. Implement special methods __str__ and __eq__.
4. Create models/subclasses.py. Implement RegularClient, PremiumClient, and CorporateClient using inheritance.
5. Use super() in the subclasses and ensure they follow the project's requirement for polymorphism (e.g., a method to calculate a discount that varies by type)

Phase 2: Persistence (Database & Files)
1.  SQLite Setup: Create database/db_manager.py. Initialize a SQLite database named gdc_database.db and create a table for Clients with columns matching the attributes from Phase 1.
2.  CRUD Operations: Write functions inside db_manager.py to Create, Read, Update, and Delete clients from the database.
3.  File Management: Create database/file_manager.py. Implement functions to export the entire list of clients from the database into a .json file and a .csv file.
4.  Error Handling: Implement robust try-except blocks to handle potential issues, such as a "Database Connection Failed" or "File Not Found" error.
5.  Activity Log: Ensure that every time a record is saved or exported, a message is sent to your logging system.

Standard: Keep the code modular. The database logic should not be mixed with the client model logic.

Phase 3: Integration (APIs & Logic)
Identity Validation: Create services/api_integration.py. Implement a function validate_identity(client_id) that simulates or calls an external API to verify a client's ID.
2. Automated Notifications: Implement a function send_welcome_email(client_email) that simulates sending a "Welcome" email to new clients using the requests library.
3. Business Logic: Create a "Service Coordinator" in services/client_service.py that orchestrates the flow: when a client is created, it first validates their identity, then saves them to the database, and finally sends the email.
4. Handling Failures: Ensure that if an API call fails, the system logs the error instead of crashing.

Phase 4: Interface & Quality (GUI & Tests)
. Web Interface (Flask): Since we installed Flask, create a basic web dashboard in main.py (or a ui/ folder).
* Create a form to add new clients (Regular, Premium, or Corporate).
* Create a table view to see all clients currently stored in the SQLite database.
2. Unit Testing: Create tests/test_gic.py.
* Write tests to verify that PremiumClient correctly applies its unique discounts.
* Write a test to ensure a client can be saved and then retrieved from the database.
3. Activity Logs: Ensure the GUI displays a "Recent Activity" feed pulled from the logs created in the utils/ folder

The "Master Rules" for the Agent
Add these constraints to the prompt to keep the AI aligned with your needs:
Code Quality: Every function must have a docstring explaining what it does in spanish.
Error Handling: Use try-except blocks for all database and API calls.
Encapsulation: No class attribute should be accessed directly; use getters and setters (properties).
Step-by-Step: Ask for confirmation after finishing each file before proceeding to the next.