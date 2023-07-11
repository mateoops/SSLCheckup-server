from app.utils.influx_connector import InfluxConnector
import unittest
import logging
from influxdb_client import InfluxDBClient
from unittest.mock import patch, MagicMock
from influxdb_client.client.write_api import SYNCHRONOUS

class TestInfluxConnector(unittest.TestCase):
    @patch('app.utils.influx_connector.InfluxDBClient')
    def test_connection(self, mock_client):
        # Mock the InfluxDBClient instance
        mock_instance = MagicMock()
        mock_client.return_value = mock_instance
        mock_instance.ping.return_value = True

        # Create an instance of the InfuxConnector
        connector = InfluxConnector('test_url', 'test_token', 'test_org')

        # Call the connect method
        connector.connect()

        # Assert that the InfluxDBClient was called with the correct parameters
        mock_client.assert_called_with(
            url='test_url',
            token='test_token',
            org='test_org'
        )

        # Assert that the __connection attribute was set correctly
        self.assertEqual(connector._InfluxConnector__connection, mock_instance)

        # Assert that the ping method was called once
        mock_instance.ping.assert_called_once()

    @patch('app.utils.influx_connector.InfluxDBClient')
    def test_connection_failed(self, mock_client):
        # Mock the InfluxDBClient instance and the ping method
        mock_instance = MagicMock()
        mock_client.return_value = mock_instance
        mock_instance.ping.side_effect = Exception('Connection error')

        # Create an instance of the InfuxDBConnector
        connector = InfluxConnector('test_url', 'test_token', 'test_org')

        # Call the connect method
        connector.connect()

        # Assert that the InfluxDBClient was called with the correct parameters
        mock_client.assert_called_with(
            url='test_url',
            token='test_token',
            org='test_org'
        )

        # Assert that the __connection attribute is None
        self.assertIsNone(connector._InfluxConnector__connection)

        # Assert that the ping method was called once
        mock_instance.ping.assert_called_once()

    @patch('app.utils.influx_connector.InfluxDBClient')
    def test_write(self, mock_client):
        # Mock the InfluxDBClient instance
        mock_instance = MagicMock()
        mock_client.return_value = mock_instance
        mock_instance.ping.return_value = True

        # Create an instance of the InfuxConnector
        connector = InfluxConnector('test_url', 'test_token', 'test_org')

        # Call the connect method
        connector.connect()

        # Call the write method
        connector.write('test_bucket', 'test_measurement', 'test_tag', 'test_value', 'test_field', 'test_value')

        # Assert that the write method was called with the correct parameters
        mock_instance.write_api.assert_called_with(write_options=SYNCHRONOUS)

        #Assert that the write method was called with the correct parameters
        mock_instance.write_api.return_value.write.assert_called()
        

    @patch('app.utils.influx_connector.InfluxDBClient')
    def test_query(self, mock_client):
        # Mock the InfluxDBClient instance
        mock_instance = MagicMock()
        mock_client.return_value = mock_instance
        mock_instance.ping.return_value = True

        # Create an instance of the InfuxConnector
        connector = InfluxConnector('test_url', 'test_token', 'test_org')

        # Call the connect method
        connector.connect()

        # Mock the query result
        mock_result = MagicMock()
        mock_result.get_query_result.return_value = 'test_result'
        mock_instance.query_api.return_value.query.return_value = mock_result

        # Call the query method
        result = connector.query('test_query')

        # Assert that the query method was called with the correct parameters
        mock_instance.query_api.return_value.query.assert_called_with(query='test_query')

    @patch('app.utils.influx_connector.InfluxDBClient')
    def test_close(self, mock_client):
        # Mock the InfluxDBClient instance
        mock_instance = MagicMock()
        mock_client.return_value = mock_instance
        mock_instance.ping.return_value = True

        # Create an instance of the InfuxConnector
        connector = InfluxConnector('test_url', 'test_token', 'test_org')

        # Call the connect method
        connector.connect()

        # Call the close method
        connector.close()

        # Assert that the close method was called
        mock_instance.close.assert_called_once()