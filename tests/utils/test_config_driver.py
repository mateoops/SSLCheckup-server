from app.utils.config_driver import ConfigDriver
import pathlib
import unittest

class TestConfigDriver(unittest.TestCase):
    def setUp(self):
        path= pathlib.Path(__file__).with_name('test_config.yaml')
        self.cd = ConfigDriver(path)

    def test_read_all_settings(self):

        result = self.cd.read_all_settings()

        self.assertIsInstance(result, dict)
        self.assertEqual(result['testKey'], 'testValue')
        self.assertIsInstance(result['list'], list)

    def test_write(self):

        self.cd.write({'testKey': 'testValue2'})
        result = self.cd.read_all_settings()

        self.assertEqual(result['testKey'], 'testValue2')
        self.assertNotEqual(result['testKey'], 'testValue')

        self.cd.write({'testKey': 'testValue'})
        result = self.cd.read_all_settings()

        self.assertEqual(result['testKey'], 'testValue')
        self.assertNotEqual(result['testKey'], 'testValue2')

        
if __name__ == '__main__':
    unittest.main()