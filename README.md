# Carehood Application

The Carehood Application is a Python Flask-based solution tailored as a comprehensive nursing assistance application for the elderly. It offers various essential features:
- **Medication Reminders:** Provides scheduling and reminders for medication intake.
- **Emergency Support:** Offers quick access to emergency services and support.
- **Hospital Locator:** Locates nearby hospitals or healthcare facilities.
- **Live Chat:** Facilitates instant communication for swift assistance.

## Usage

Please follow these steps to run the Carehood Application locally:

1. Clone this repository.
2. Install the necessary dependencies using `pip install -r requirements.txt`.
3. Create a `.env` file in the root directory based on the provided `.env_example` file.
4. Configure the environment variables in the `.env` file.
5. Run the Flask application using `python app.py`.
6. Access the application via your web browser at `http://localhost:5000`.

### Environment Variables (.env file)

Configure your `.env` file with the following parameters:


#### Example .env file
```
# Flask secret key
SECRET_KEY=your_secret_key

# Database URI for SQLAlchemy
SQLALCHEMY_DATABASE_URI=your_database_uri
```

This updated section now includes specific instructions for creating the `.env` file, configuring it with the required parameters, and running the Flask application locally. Adjust the instructions according to your project's specific requirements.

## Application Structure
```
Carehood_Application/
└── app/
    ├── __init__.py                   # Initialization file for the app module
    ├── main/
    │   ├── events.py                 # Contains event handling functions
    │   ├── forms.py                  # Manages forms and form submissions
    │   ├── model.py                  # Includes database models and interactions
    │   ├── routes.py                 # Defines URL routes and their corresponding views
    │   └── __init__.py               # Initialization file for the main module
    ├── static/
    │   ├── aos.css                   # CSS file for AOS library
    │   ├── aos.js.download           # JavaScript file for AOS library
    │   ├── bootstrap.bundle.min.js.download  # Minified JavaScript for Bootstrap
    │   ├── detector.js.download      # JavaScript for detector
    │   ├── logo-dark.png             # Image file for the app logo
    │   ├── plugins.min.js.download   # Minified JavaScript for plugins
    │   ├── preview.css               # CSS file for preview
    │   ├── scripts.min.js.download   # Minified JavaScript for scripts
    │   ├── smiles.php                # PHP file for smiles
    │   ├── styles.min.css            # Minified CSS for styles
    │   └── team-1.jpg                # Image file for a team
    ├── templates/
    │   ├── base.html                 # Base HTML template for other pages to extend
    │   ├── chat.html                 # HTML template for chat functionality
    │   ├── dashboard.html            # HTML template for the dashboard
    │   ├── index.html                # HTML template for the home or landing page
    │   ├── login.html                # HTML template for user login
    │   ├── reminder.html             # HTML template for medicine reminder
    │   ├── signup.html               # HTML template for user sign-up
    │   └── static.html               # Static HTML template
    └── .env                          # Environment variables file for configuration

```

## Dependencies

This project relies on the following major dependencies:

- **Flask**: Flask is a micro web framework for building web applications in Python.
- **Socket.io**: Socket.IO enables real-time bidirectional event-based communication.
- **Flask-Alchemy**: Flask-SQLAlchemy is an extension for Flask that adds support for SQLAlchemy, a powerful relational database toolkit.

These dependencies are crucial for the functionality and architecture of the Carehood Application.

## Contributing

Contributions to the Carehood Application are welcome! To contribute:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-branch-name`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature/your-branch-name`).
5. Create a new Pull Request.

## License

This project is licensed under the [license name]. For more information, please see the [LICENSE](link-to-license) file.
