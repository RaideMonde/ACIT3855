import datetime
import json

import connexion
from connexion import NoContent
import swagger_ui_bundle

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from base import Base
from buy import Buy
from sell import Sell

DB_ENGINE = create_engine("sqlite:///events.sqlite")
Base.metadata.bind = DB_ENGINE
DB_SESSION = sessionmaker(bind=DB_ENGINE)

# Endpoints
def buy(body):
    # TODO create a session

    # TODO create a Buy object and populate it with values from the body

    # TODO add, commit, and close the session

    return NoContent, 201
# end

def get_buys(timestamp):
    # TODO create a DB SESSION
    session = DB_SESSION()

    # TODO query the session and filter by Buy.date_created >= timestamp
    # e.g. rows = session.query(Buy).filter etc...
    rows = session.query(Buy).filter(Buy.date_created >= timestamp)

    # TODO create a list to hold dictionary representations of the rows
    data = []
    # TODO loop through the rows, appending each row (use .to_dict() on each row) to 'data'
    

    # TODO close the session

    # TODO log the request to get_buys including the timestamp and number of results returned

    return data, 200

def sell(body):
    # TODO create a session

    # TODO create a Buy object and populate it with values from the body

    # TODO add, commit, and close the session

    return NoContent, 201
# end

def get_sells(timestamp):
    # TODO create a DB SESSION


    # TODO query the session and filter by Sell.date_created >= timestamp
    # e.g. rows = session.query(Sell).filter etc...

    # TODO create a list to hold dictionary representations of the rows
    data = []
    # TODO loop through the rows, appending each row (use .to_dict() on each row) to 'data'

    # TODO close the session

    # TODO log the request to get_sells including the timestamp and number of results returned

    return data, 200

app = connexion.FlaskApp(__name__, specification_dir='')
app.add_api('openapi.yaml', strict_validation=True, validate_responses=True)

if __name__ == "__main__":
    app.run(port=8090)