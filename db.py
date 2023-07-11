import os
from app.utils.influx_connector import InfluxConnector

db_influx = InfluxConnector(os.environ['INFLUXDB_URL'],
                            os.environ['INFLUXDB_TOKEN'],
                            os.environ['INFLUXDB_ORG'])
db_influx.connect()