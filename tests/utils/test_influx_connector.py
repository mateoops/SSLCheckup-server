from server.utils.influx_connector import InfluxConnector
import unittest
import logging
from influxdb import InfluxDBClient
from unittest.mock import patch, MagicMock

class TestInfluxConnector(unittest.TestCase):
    @patch('server.utils.influx_connector.InfluxDBClient')
    def test_connection(self, mock_client):
        # Mock the InfluxDBClient instance
        mock_instance = MagicMock()
        mock_client.return_value = mock_instance
        mock_instance.ping.return_value = True

        # Create an instance of the InfuxConnector
        connector = InfluxConnector('test_hostname', 8086, 'test_db', 'test_username', 'test_password')

        # Call the connect method
        connector.connect()

        # Assert that the InfluxDBClient was called with the correct parameters
        mock_client.assert_called_with(
            host='test_hostname',
            port=8086,
            database='test_db',
            username='test_username',
            password='test_password'
        )

        # Assert that the __connection attribute was set correctly
        self.assertEqual(connector._InfluxConnector__connection, mock_instance)

        # Assert that the ping method was called once
        mock_instance.ping.assert_called_once()

    @patch('server.utils.influx_connector.InfluxDBClient')
    def test_connection_failed(self, mock_client):
        # Mock the InfluxDBClient instance and the ping method
        mock_instance = MagicMock()
        mock_client.return_value = mock_instance
        mock_instance.ping.side_effect = Exception('Connection error')

        # Create an instance of the InfuxDBConnector
        connector = InfluxConnector('test_hostname', 8086, 'test_db', 'test_username', 'test_password')

        # Call the connect method
        connector.connect()

        # Assert that the InfluxDBClient was called with the correct parameters
        mock_client.assert_called_with(
            host='test_hostname',
            port=8086,
            database='test_db',
            username='test_username',
            password='test_password'
        )

        # Assert that the __connection attribute is None
        self.assertIsNone(connector._InfluxConnector__connection)

        # Assert that the ping method was called once
        mock_instance.ping.assert_called_once()

    @patch('server.utils.influx_connector.InfluxDBClient')
    def test_write(self, mock_client):
        # Mock the InfluxDBClient instance
        mock_instance = MagicMock()
        mock_client.return_value = mock_instance
        mock_instance.ping.return_value = True

        # Create an instance of the InfuxConnector
        connector = InfluxConnector('test_hostname', 8086, 'test_db', 'test_username', 'test_password')

        # Call the connect method
        connector.connect()

        # Call the write method
        connector.write('test_measurement', {'test_tag': 'test_value'}, {'test_field': 'test_value'})

        # Assert that the write_points method was called with the correct parameters
        mock_instance.write_points.assert_called_with([
            {
                'measurement': 'test_measurement',
                'tags': {'test_tag': 'test_value'},
                'fields': {'test_field': 'test_value'}
            }
        ])

    @patch('server.utils.influx_connector.InfluxDBClient')
    def test_query(self, mock_client):
        # Mock the InfluxDBClient instance
        mock_instance = MagicMock()
        mock_client.return_value = mock_instance
        mock_instance.ping.return_value = True

        # Create an instance of the InfuxConnector
        connector = InfluxConnector('test_hostname', 8086, 'test_db', 'test_username', 'test_password')

        # Call the connect method
        connector.connect()

        # Mock the query result
        mock_result = MagicMock()
        mock_result.raw = 'test_result'
        mock_instance.query.return_value = mock_result

        # Call the query method
        result = connector.query('test_query')

        # Assert that the query method was called with the correct parameters
        mock_instance.query.assert_called_with('test_query')

        # Assert that the result is correct
        self.assertEqual(result, 'test_result')

    @patch('server.utils.influx_connector.InfluxDBClient')
    def test_close(self, mock_client):
        # Mock the InfluxDBClient instance
        mock_instance = MagicMock()
        mock_client.return_value = mock_instance
        mock_instance.ping.return_value = True

        # Create an instance of the InfuxConnector
        connector = InfluxConnector('test_hostname', 8086, 'test_db', 'test_username', 'test_password')

        # Call the connect method
        connector.connect()

        # Call the close method
        connector.close()

        # Assert that the close method was called
        mock_instance.close.assert_called_once()