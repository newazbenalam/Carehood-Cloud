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

### Deploying on AWS EC2

To deploy the Carehood Application on an AWS EC2 instance, follow these steps:

1. **Launch an EC2 Instance:**
    - Choose an appropriate instance type (e.g., Ubuntu).
    - Set up security groups to allow inbound traffic on necessary ports (e.g., 80, 443).

2. **Connect to Your EC2 Instance:**
    - Use SSH to connect to your EC2 instance:
      ```bash
      ssh -i your-key.pem ubuntu@your-ec2-public-ip
      ```

3. **Clone the Repository:**
    - Clone this repository into the home directory:
      ```bash
      git clone https://github.com/your-username/Carehood-Cloud.git
      ```

4. **Install Dependencies and Setup:**
    - Install Python and required packages:
      ```bash
      sudo apt update
      sudo apt install python3 python3-pip -y
      sudo pip3 install -r requirements.txt
      ```

5. **Run the Application:**
    - Navigate to the project directory and start the Flask application:
      ```bash
      cd Carehood-Cloud
      python3 app.py
      ```

6. **Access the Application:**
    - Access the application via your web browser using your EC2 instance's public IP address.


### User Script

User custom script for EC2. Which automatacially download and setup the envirnoment. Makes efficient for elastic load balanceing.

```
#!/bin/bash
sudo apt-get update -y
sudo apt install -y python3-pip apache2 apache2-utils ssl-cert libapache2-mod-wsgi-py3
# Clone the repository
git clone https://github.com/newazbenalam/Carehood-Cloud /home/ubuntu/Carehood-Cloud
pip3 install -r /home/ubuntu/Carehood-Cloud/requirements.txt

echo "# Flask secret key
SECRET_KEY='gjr39dkjn344_!67#'
# Database URI for SQLAlchemy
SQLALCHEMY_DATABASE_URI='mysql://mysql:12345@192.168.0.72:3306/carehood'
# HOST and PORT for Flask
HOST=0.0.0.0
PORT=80
DEBUG=false" > /home/ubuntu/Carehood-Cloud/.env

# Grant capabilities to bind to privileged ports
sudo setcap 'cap_net_bind_service=+ep' /usr/bin/python3.10
sudo setcap 'cap_net_bind_service=+ep' /usr/bin/python3

# Stop and disable Apache (if running)
sudo systemctl stop apache2
sudo systemctl disable apache2

# Run your Flask application
sudo cp /home/ubuntu/Carehood-Cloud/myflaskapp.service /etc/systemd/system/myflaskapp.service

sudo systemctl daemon-reload
sudo systemctl enable myflaskapp
sudo systemctl start myflaskapp
```


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

### Setting Up Elastic Load Balancer (ELB) with EC2 Instances

An Elastic Load Balancer (ELB) distributes incoming application traffic across multiple EC2 instances to ensure high availability and fault tolerance. Here's a step-by-step guide to set up an ELB with EC2 instances:

1. **Launch EC2 Instances**
    - Launch two or more EC2 instances in different availability zones. Ensure they run the application you want to load balance.
    - Configure the security groups for the instances to allow incoming traffic from the load balancer (usually on ports 80 and 443 for HTTP/HTTPS).

2. **Create an Application Load Balancer**
    - Go to the AWS Management Console and navigate to the EC2 service.
    - Select "Load Balancers" and click "Create Load Balancer".
    - Choose "Application Load Balancer".
    - Configure the load balancer settings, including its name, scheme (internet-facing/internal), listeners (HTTP or HTTPS), and availability zones.
    - Configure the security settings and select or create a new SSL certificate if using HTTPS.
    - Configure routing and specify the target group. Create a new target group and select the registered EC2 instances.

3. **Configure Target Groups**
    - Define a target group specifying the protocol, port, health checks, and the registered EC2 instances.
    - Set up health checks to monitor the health of instances. Adjust health check settings based on your application's behavior and requirements.

4. **Register EC2 Instances**
    - Register the previously launched EC2 instances to the target group associated with the load balancer.
    - Ensure that the instances pass the health checks before proceeding.

5. **Adjust Load Balancer Settings**
    - Configure additional settings like load balancer attributes, cross-zone load balancing, connection draining, etc., based on your application's needs.

6. **Test the Load Balancer**
    - Access the application using the load balancer's DNS name or IP address.
    - Verify that requests are distributed across the registered EC2 instances and that the application works as expected.

7. **Monitor and Scale**
    - Monitor the load balancer's performance and configure alarms to handle traffic spikes.
    - Configure auto-scaling policies to automatically scale EC2 instances based on the load balancer's metrics.

Conclusion:

Setting up an Elastic Load Balancer (ELB) with EC2 instances provides improved fault tolerance, scalability, and efficient distribution of incoming traffic. Ensure to regularly monitor and optimize configurations for optimal performance.


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
