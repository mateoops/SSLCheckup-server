from db import db_influx
import datetime

class SSLConfiguration():
    @staticmethod
    def save(host, address, port, description):

        #write(self, bucket, measurement, tag: dict, field: dict)
        db_influx.write('ssl_configuration', 'ssl_configuration_meas', 'tag_key', 'tag_value', 'host', host)
        db_influx.write('ssl_configuration', 'ssl_configuration_meas', 'tag_key', 'tag_value', 'address', address)
        db_influx.write('ssl_configuration', 'ssl_configuration_meas', 'tag_key', 'tag_value', 'port', port)
        db_influx.write('ssl_configuration', 'ssl_configuration_meas', 'tag_key', 'tag_value', 'description', description)

    @staticmethod
    def get_all():
        query = 'from(bucket:"{}") |> range(start: -1h)'.format('ssl_configuration')
        result = db_influx.query(query)

        return result