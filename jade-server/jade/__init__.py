from flask import Flask
from flask_cors import CORS

import configparser, os

from .database import JadeDB

# Initiate flask app
app = Flask(__name__, static_folder='./assets')
CORS(app)

settings = {}

# Load configuration file
config = configparser.ConfigParser()
configfile = os.path.dirname(os.path.realpath(__file__)) + '/jade.ini'
config.read(configfile)

# Set configuration
app.config['DB_HOST'] = config.get('database', 'host', fallback='localhost')
app.config['DB_PORT'] = config.get('database', 'port', fallback='5432')
app.config['DB_USER'] = config.get('database', 'username', fallback='postgres')
app.config['DB_PASS'] = config.get('database', 'password', fallback='postgres')
app.config['DB_NAME'] = config.get('database', 'dbname', fallback='jade')
app.config['DB_SSL']  = config.get('database', 'ssl', fallback='prefer')

# Initialize DB controller
jadedb = JadeDB(app)

from .routes import objects
from .routes import pages
