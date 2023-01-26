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

with open('app_conf.yml', 'r') as f:
    app_config = yaml.safe_load(f.read())

# TODO: create connection string, replacing placeholders below with variables defined in log_conf.yml
DB_ENGINE = create_engine(f"mysql+pymysql://user:password@hostname:port/db")
Base.metadata.bind = DB_ENGINE
DB_SESSION = sessionmaker(bind=DB_ENGINE)

# Endpoints
def buy(body):
    # TODO create a session

    # TODO additionally pass trace_id (along with properties from Lab 2) into Buy constructor

    # TODO add, commit, and close the session

    # TODO: call logger.debug and pass in message "Stored buy event with trace id <trace_id>"

    # TODO return NoContent, 201
    return NoContent, 201
# end

def get_buys():
    # placeholder for future labs
    pass

def sell(body):
    # TODO create a session

    # TODO additionally pass trace_id (along with properties from Lab 2) into Sell constructor

    # TODO add, commit, and close the session

    # TODO: call logger.debug and pass in message "Stored buy event with trace id <trace_id>"

    return NoContent, 201
# end

def get_sells():
    # placeholder for future labs
    pass

app = connexion.FlaskApp(__name__, specification_dir='')
app.add_api('openapi.yaml', strict_validation=True, validate_responses=True)

with open('log_conf.yml', 'r') as f:
    log_config = yaml.safe_load(f.read())
    logging.config.dictConfig(log_config)

logger = logging.getLogger('basic')

if __name__ == "__main__":
    app.run(port=8090)