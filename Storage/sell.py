from sqlalchemy import Column, Integer, String, DateTime, Float
from base import Base
import datetime

class Sell(Base):
    __tablename__ = "sell"

    id = Column(Integer, primary_key=True)
    sell_id = Column(String(250), nullable=False)
    item_name = Column(String(250), nullable = False)
    item_price = Column(Integer, nullable=False)
    sell_qty = Column(Integer, nullable=False)
    date_created = Column(DateTime, nullable=False)
    

    def __init__(self, sell_id, item_name, item_price, sell_qty):
        
        self.sell_id = sell_id
        self.item_name = item_name
        self.item_price = item_price
        self.sell_qty = sell_qty
        self.date_created = datetime.datetime.now()

    def to_dict(self):
        dict = {}
        dict['sell_id'] = self.sell_id
        dict['item_name'] = self.item_name
        dict['item_price'] = self.item_price
        dict['sell_qty'] = self.sell_qty
        dict['date_created'] = self.date_created

        return dict
