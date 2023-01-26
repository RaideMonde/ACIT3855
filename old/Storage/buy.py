from sqlalchemy import Column, Integer, String, DateTime, Float
from base import Base
import datetime

class Buy(Base):
    __tablename__ = "buy"

    id = Column(Integer, primary_key=True)
    buy_id = Column(String(250), nullable=False)
    item_name = Column(String(250), nullable = False)
    item_price = Column(Integer, nullable=False)
    buy_qty = Column(Integer, nullable=False)
    date_created = Column(DateTime, nullable=False)
    
    

    def __init__(self, buy_id, item_name, item_price, buy_qty):

        self.buy_id = buy_id
        self.item_name = item_name
        self.item_price = item_price
        self.buy_qty = buy_qty
        self.date_created = datetime.datetime.now()
        

    def to_dict(self):
        dict = {}
        dict['buy_id'] = self.buy_id
        dict['item_name'] = self.item_name
        dict['item_price'] = self.item_price
        dict['buy_qty'] = self.buy_qty
        dict['date_created'] = self.date_created

        return dict