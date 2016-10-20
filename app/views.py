import json

from app import app


@app.route('/', methods=['GET', 'POST'])
def index():
    resp = {
        'result': {
            'description': 'Nothing happens yet',
        },
    }
    return json.dumps(resp)
