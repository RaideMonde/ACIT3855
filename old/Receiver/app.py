import connexion
from connexion import NoContent 
import datetime
import pykafka
from pykafka import KafkaClient
import requests
import uuid
import yaml
import requests
import json

# TODO remove list

# TODO add 'endpoint' parameter to process_event function
def process_events(event, endpoint):
    trace_id = str(uuid.uuid4())
    event['trace_id'] = trace_id
    headers = {"content-type": "application/json"}
    
    res = requests.post(f'http://localhost:8090/{endpoint}', headers=headers, data=json.dumps(event))
    return res.text, res.status_code
    

# Endpoints
def buy(body):
    return process_events(body, 'buy')

def sell(body):
    return process_events(body, 'sell')

app = connexion.FlaskApp(__name__, specification_dir='')
app.add_api("openapi.yml", strict_validation=True, validate_responses=True)

if __name__ == "__main__":
    app.run(port=8080)