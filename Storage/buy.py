from sqlalchemy import Column, Integer, String, DateTime, Float
from base import Base
import datetime

class Buy(Base):
    # TODO declare table name

    id = Column(Integer, primary_key=True)
    
    # TODO create the necessary columns following the id example above

    def __init__(self, buy_id, item_name, item_price, buy_qty):
        # TODO assign the parameter values to the object's properties
        self.date_created = datetime.datetime.now()
        pass

    def to_dict(self):
        # TODO create a dict, and assign object properties to your dict

        # TODO return dict
        pass