# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from sqlalchemy.orm import sessionmaker
from scrapy.exceptions import DropItem
from .models import Index, db_connect, create_table
import logging


class StockindicesPipeline(object):

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
        index = Index()
        index.index = item["index"][0]
        index.country = item["country"][0]
        index.last = item["last"][0]
        index.high = item["high"][0]
        index.low = item["low"][0]
        index.changeTotal = item["changeTotal"][0]

        try:
            session.add(index)
            session.commit()

        except:
            session.rollback()
            raise

        finally:
            session.close()

        return item
