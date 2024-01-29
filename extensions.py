from flask_sqlalchemy import SQLAlchemy
from flask_restx import Api
from ._init_ import app

api = Api(app, version='1.0', title='Sample API',
          description='A sample API', doc='/swagger') #Instantiate function: assigned to a variable
db = SQLAlchemy() #Instantiate function: assigned to a variable
