import datetime
import logging
# sql conn
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, Column, Table, ForeignKey, MetaData
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (
    Integer, String, Date, DateTime, Float, Boolean, Text)

# scrapy api
import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy import signals
from scrapy.utils import log
from twisted.internet import reactor
from scrapy.settings import Settings

# from scrapy.loader import ItemLoader

# CONNECTION TO DATABASE
Base = declarative_base()


def db_connect():
    """
    Performs database connection using database settings from settings.py.
    Returns sqlalchemy engine instance
    """
    return create_engine('sqlite:///concerts.db')


def create_table(engine):
    Base.metadata.create_all(engine)


class Concert(Base):
    __tablename__ = "Concerts"

    date = Column(Date, primary_key=True)
    name = Column(String, primary_key=True)
    price = Column(String)
    concert_date = Column(String)


# ITEMS
class ConcertItem(scrapy.Item):
    name = scrapy.Field()
    price = scrapy.Field()
    con_date = scrapy.Field()


# PIPELINES
class ConcertsPipeline(object):
    date = datetime.datetime.now().date()

    def __init__(self):
        """
        Initializes database connection and sessionmaker
        Creates tables
        """
        engine = db_connect()
        create_table(engine)
        self.Session = sessionmaker(bind=engine)
        logging.info("****SaveQuotePipeline: database connected****")

    def process_item(self, item, spider):
        """Save quotes in the database
        This method is called for every item pipeline component
        """
        session = self.Session()
        concert = ConcertItem()
        concert.date = self.date
        concert.name = item["index"]
        concert.price = item["country"]
        concert.con_date = item["con_date"]

        try:
            session.add(concert)
            session.commit()

        except:
            session.rollback()
            raise

        finally:
            session.close()

        return item


# SPIDER


class ConcertSpider(scrapy.Spider):
    name = "Concert"
    start_urls = [
        "https://www.eventim.de/events/konzerte-1"
    ]
    allowed_domains = ["eventim.de"]

    def parse(self, response):
        concerts = response.xpath('//*[@id="main"]/section[@data-c="clusterresult"]/article')
        logging.info("======================================")
        for concert in concerts:
            logging.info(concert)
            # loader = ItemLoader(item=ConcertItem(), response=concert)
            # loader.add_xpath("name", '/div/div[2]/div[1]/text()')
            # loader.add_xpath("price", '/div/div[2]/div[4]/text()')
            # loader.add_xpath("con_date", '/div/div[2]/div[3]/span[1]/span[1]/test()')
            # concert_item = loader.load_item()

            concert_item = ConcertItem()
            concert_item["name"] = concert.xpath("/div/div[2]/div[1]/text()")
            concert_item["price"] = concert.xpath("/div/div[2]/div[4]/text()")
            concert_item["con_date"] = concert.xpath("/div/div[2]/div[3]/span[1]/span[1]/text()")

            yield concert_item


class Scraper:
    def __init__(self):
        self.process = CrawlerProcess({
            "USER_AGENT": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_1) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/60.0.3112.101 Safari/537.36",
            "ROBOTSTXT_OBEY": False,
            "ITEM_PIPELINES": {"Scrapy-without-framework.ConcertsPipeline": 300}
        })

        self.spider = ConcertSpider

    def run_spider(self):
        self.process.crawl(self.spider)
        self.process.start()


MyScraper = Scraper()
MyScraper.run_spider()