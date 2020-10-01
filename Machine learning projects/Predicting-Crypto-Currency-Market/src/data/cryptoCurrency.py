import requests
import datetime
from sqlalchemy import create_engine, Column, Table, ForeignKey, MetaData
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (
    Integer, String, Date, DateTime, Float, Boolean, Text)


Base = declarative_base()


class Crypto(Base):
    __tablename__ = "Crypto"

    date = Column(Date, primary_key=True)
    symbol = Column(String, primary_key=True)
    name = Column(String)
    current_price = Column(Float)
    market_cap = Column(Float)
    market_cap_rank = Column(Integer)
    fully_diluted_valuation = Column(Float)
    total_volume = Column(Float)
    high_24h = Column(Float)
    low_24h = Column(Float)
    price_change_24h = Column(Float)
    price_change_percentage_24h = Column(Float)
    market_cap_change_24h = Column(Float)
    market_cap_change_percentage_24h = Column(Float)
    circulating_supply = Column(Float)
    total_supply = Column(Float)
    max_supply = Column(Float)
    ath = Column(Float)
    ath_date = Column(String)
    atl = Column(Float)
    atl_date = Column(String)

# CODE MUST BE RUN IN THE ROOT DIR OF PROJECT
engine = create_engine('sqlite:///data/gathered/Crypto_index.db', echo=True)
Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)

# fetch the data
response = requests.get(
    "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=100&page=1"
    "&sparkline=false")
print(response.status_code)
date = datetime.datetime.now().date()
data = response.json()

for elem in data:
    """Save quotes in the database
    This method is called for every item pipeline component
    """
    session = Session()
    crypto = Crypto()

    crypto.date = date
    crypto.symbol = elem["symbol"]
    crypto.name = elem["name"]
    crypto.current_price = elem["current_price"]
    crypto.market_cap = elem["market_cap"]
    crypto.market_cap_rank = elem["market_cap_rank"]
    crypto.fully_diluted_valuation = elem["fully_diluted_valuation"]
    crypto.total_volume = elem["total_volume"]
    crypto.high_24h = elem["high_24h"]
    crypto.low_24h = elem["low_24h"]
    crypto.price_change_24h = elem["price_change_24h"]
    crypto.price_change_percentage_24h = elem["price_change_percentage_24h"]
    crypto.market_cap_change_24h = elem["market_cap_change_24h"]
    crypto.market_cap_change_percentage_24h = elem["market_cap_change_percentage_24h"]
    crypto.circulating_supply = elem["circulating_supply"]
    crypto.total_supply = elem["total_supply"]
    crypto.max_supply = elem["max_supply"]
    crypto.ath = elem["ath"]
    crypto.ath_date = elem["ath_date"]
    crypto.atl = elem["atl"]
    crypto.atl_date = elem["atl_date"]

    try:
        session.add(crypto)
        session.commit()

    except:
        session.rollback()
        raise

    finally:
        session.close()
