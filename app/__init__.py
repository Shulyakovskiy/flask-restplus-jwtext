from flask import Blueprint
from flask_restplus import Api

from .main.controller.auth_controller import api as auth_ns
from .main.controller.user_controller import api as user_ns

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='FLASK RESTPLUS API BOILERPLATE WITH JWT',
          version='1.0',
          description='a boilerplate for flask restplus web service',
          doc=False,
          )

api.add_namespace(user_ns, path='/user')
api.add_namespace(auth_ns, path='/auth')
