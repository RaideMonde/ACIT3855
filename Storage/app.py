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
    
    session = DB_SESSION()

    buy = Buy(
        body['buy_id'],
        body['item_name'],
        body['item_price'],
        body['item_qty']
    )
    
    session.add(buy)
    session.commit()
    session.close()
    
    return NoContent, 201

def get_buys():
    # placeholder for future labs
    pass

def sell(body):
    session = DB_SESSION()
    sell = Buy(
        body['sell_id'],
        body['item_name'],
        body['item_price'],
        body['item_qty']
    )
    session.add(sell)
    session.commit()
    session.close()
    
    return NoContent, 201
# end

def get_sells():
    # placeholder for future labs
    pass

app = connexion.FlaskApp(__name__, specification_dir='')
app.add_api('openapi.yaml', strict_validation=True, validate_responses=True)

if __name__ == "__main__":
    app.run(port=8090)