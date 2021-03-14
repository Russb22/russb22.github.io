import unittest
import requests
from urllib.parse import quote

HOSTNAME = "https://www.onetwotrip.com"

class MainTestSuite(unittest.TestCase):
    def test_departure_api_positive(self):
        # setup
        query_city = quote("Москва")
        url_query = ''.join([HOSTNAME, '/_bus/geo/suggest?query=', query_city, '&limit=10'])
        headers = {'Connection': 'close'}
        # execute
        response = requests.request(
            "GET", url_query, headers=headers, verify=False)
        response.raise_for_status()
        # assert
        responseTmp = response.json()
        self.assertEqual(responseTmp['data'][0]['name'], 'Москва')

    def test_departure_api_negative(self):
        # setup
        query_city = '00000'
        url_query = ''.join([HOSTNAME, '/_bus/geo/suggest?query=', query_city])
        headers = {'Connection': 'close'}
        # execute
        response = requests.request(
            "GET", url_query, headers=headers, verify=False)
        response.raise_for_status()
        # assert
        responseTmp = response.json()
        print(responseTmp)
        with self.assertRaises(IndexError):
            responseTmp['data'][0]['name']

if __name__ == '__main__':
    unittest.main()