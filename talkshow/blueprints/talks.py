from flask import Blueprint, jsonify
from flask import current_app as app    


blueprint = Blueprint('talks', __name__)

@blueprint.route('/talks/')
def get_all_talks():
    events_db = app.db['events'].find()
    events = []
    
    for event in events_db:
        events.append({'name':event['name'], 'date':event['date']})
    
    return jsonify(events)

def configure(app):
    app.register_blueprint(blueprint)