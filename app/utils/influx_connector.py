from datetime import datetime
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

import logging

class InfluxConnector:
    __instance = None

    def __new__(cls, url, token, org):
        if cls.__instance is None:
            cls.__instance = super(InfluxConnector, cls).__new__(cls)
        return cls.__instance

    def __init__(self, url, token, org):
        if hasattr(self, '__initialized'):
            return
        self.__initialized = True

        self.__url =    url
        self.__token =  token
        self.__org =    org
    
    def connect(self):
        self.__connection = InfluxDBClient(
            url = self.__url,
            token = self.__token,
            org = self.__org
        )

        try:
            self.__connection.ping()
            logging.info('[InfluxConnector] Connection to database succeeded!')
        except Exception:
            self.__connection = None
            logging.error('[InfluxConnector] Connection to database failed!')
    
    def write(self, bucket, measurement, tag_key, tag_value, field_key, field_value):

        point = Point(measurement).tag(tag_key, tag_value).field(field_key, field_value).time(datetime.utcnow(), WritePrecision.S)
        write_api = self.__connection.write_api(write_options=SYNCHRONOUS)
        write_api.write(bucket=bucket, record=point)


    def query(self, query):
        query_api = self.__connection.query_api()
        result = query_api.query(query=query)

        data = []
        for table in result:
            for record in table.records:
                data.append(record.values)
        
        return data
    
    def close(self):
        self.__connection.close()
        logging.info('[InfluxConnector] Connection to database closed!')