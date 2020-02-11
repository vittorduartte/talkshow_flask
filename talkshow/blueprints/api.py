from flask import Blueprint, jsonify
from flask import current_app as app
from flask_restplus import Api, Resource, fields

api_v1 = Blueprint('api', __name__, url_prefix='/api/v1/')

api = Api(api_v1,
          version = '1.0',
          title = 'Talkshow Plataform API',
          description = 'The Oficial API for Talkshow Team to developers community.')

event_model = api.model('event_model',{
                        'title':fields.String(required=True, description='Event Title'),
                        'date':fields.String(required=True, description='Event Date')
                        })

ns = api.namespace('events', description='Events Data')

@ns.route('/')
class Events(Resource):

    @api.marshal_list_with(event_model)
    def get(self):
        return {'events': list(app.db['events'].find())}

def configure(app):
    app.register_blueprint(api_v1)