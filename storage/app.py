import datetime
import json

import connexion
from connexion import NoContent
import swagger_ui_bundle

import mysql.connector 
import pymysql
import yaml
import logging
import logging.config

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from base import Base
from buy import Buy
from sell import Sell

with open('./Storage/app_conf.yml', 'r') as f:
    app_config = yaml.safe_load(f.read())

# TODO: create connection string, replacing placeholders below with variables defined in log_conf.yml
user     = app_config['user']
password = app_config['password']
hostname = app_config['hostname']
port     = app_config['port']
db       = app_config['db']
DB_ENGINE = create_engine(f"mysql+pymysql://{user}:{password}@{hostname}:{port}/{db}")
Base.metadata.bind = DB_ENGINE
DB_SESSION = sessionmaker(bind=DB_ENGINE)

# Endpoints
def buy(body):
    # TODO create a session
    session = DB_SESSION()

    # TODO additionally pass trace_id (along with properties from Lab 2) into Buy constructor
    b = Buy(
        body ['buy_id'],
        body['trace_id'],
        body['item_price'],
        body['buy_qty'],
        body['trace_id']
    )
    # TODO add, commit, and close the session
    session.add(b)
    session.commit()
    session.close()

    # TODO: call logger.debug and pass in message "Stored buy event with trace id <trace_id>"
    logger.debug(f"Stored buy event with {body['trace_id']}")
    # TODO return NoContent, 201
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
    for row in rows:
        data.append(row.to_dict())

    # TODO close the session
    session.close()

    # TODO log the request to get_buys including the timestamp and number of results returned
    logger.debug(f'Returning {len(data)} buy events at {timestamp}')
    return data, 200

def sell(body):
    session = DB_SESSION()

    s = Sell(
        body['sell_id'],
        body['trace_id'],
        body['item_price'],
        body['sell_qty'],
        body['trace_id']
    )
    
    session.add(s)
    session.commit()
    session.close()

    logger.debug(f"Stored sell event with {s['trace_id']}")
    
    return NoContent, 201

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

logger = logging.getLogger('basic')

if __name__ == "__main__":
    app.run(port=8090)