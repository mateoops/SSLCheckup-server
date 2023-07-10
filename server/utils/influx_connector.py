from influxdb import InfluxDBClient
import logging

class InfluxConnector:
    def __init__(self, hostname, port, database_name, username, password) -> None:
        self.__hostname =   hostname
        self.__port =       port
        self.__database =   database_name
        self.__username =   username
        self.__password =    password
    
    def connect(self):
        self.__connection = InfluxDBClient(
            host = self.__hostname,
            port = self.__port,
            database = self.__database,
            username = self.__username,
            password = self.__password
        )

        try:
            self.__connection.ping()
            logging.info('[InfluxConnector] Connection to database succeeded!')
        except Exception:
            self.__connection = None
            logging.error('[InfluxConnector] Connection to database failed!')
    
    def write(self, measurement, tags, fields):
        body = [
            {
                "measurement": measurement,
                "tags": tags,
                "fields": fields
            }
        ]
        self.__connection.write_points(body)

    def query(self, query):
        result = self.__connection.query(query)
        return result.raw
    
    def close(self):
        self.__connection.close()
        logging.info('[InfluxConnector] Connection to database closed!')