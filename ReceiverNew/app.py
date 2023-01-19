import connexion
from connexion import NoContent 
import datetime
import pykafka
from pykafka import KafkaClient
import requests
import uuid
import yaml

# TODO remove list

# TODO add 'endpoint' parameter to process_event function
def process_events(event):
    # TODO remove timestamp
    trace_id = str(uuid.uuid4())
    event['trace_id'] = trace_id

    # TODO remove logic for writing to file and insterting into list

    # TODO add call to requests.post using Storage url and endpoint parameter
    # TODO save the response from requests.post in a variable named 'res'

    # TODO remove return NoContent, 201
    # TODO return res.text, res.status_code
    pass

# Endpoints
def buy(body):
    # TODO add second argument to process_events(), the name of the endpoint, e.g. 'buy'
    process_events(body)

    # TODO remove return NoContent, 201
    # TODO return the result of process_events()
    return NoContent, 201

def sell(body):
    # TODO add second argument to process_events(), the name of the endpoint, e.g. 'buy'
    process_events(body)

    # TODO remove return NoContent, 201
    # TODO return the result of process_events()
    return NoContent, 201

app = connexion.FlaskApp(__name__, specification_dir='')
app.add_api("openapi.yml", strict_validation=True, validate_responses=True)

if __name__ == "__main__":
    app.run(port=8080)