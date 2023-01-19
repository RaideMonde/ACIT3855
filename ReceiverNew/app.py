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
    # TODO remove timestamp
    trace_id = str(uuid.uuid4())
    event['trace_id'] = trace_id
    headers = {"content-type": "application/json"}

    # TODO remove logic for writing to file and insterting into list

    # TODO add call to requests.post using Storage url and endpoint parameter
    # TODO save the response from requests.post in a variable named 'res'
    res = requests.post(f'http://localhost:8090/{endpoint}', headers=headers, data=json.dumps(event))
    # TODO remove return NoContent, 201
    # TODO return res.text, res.status_code
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