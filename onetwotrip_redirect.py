import unittest
import requests

HOSTNAME = "https://www.onetwotrip.com"

class MainTestSuite(unittest.TestCase):
    def test_redirect(self):
        # setup
        headers = {'Connection': 'close'}
        # execute
        response = requests.request(
            "GET", HOSTNAME, headers=headers, verify=False, allow_redirects=False)
        response.raise_for_status()
        # assert
        resp = dict(response.headers)
        self.assertEqual(resp['location'], '{0}{1}'.format(HOSTNAME, '/ru/'))

if __name__ == '__main__':
    unittest.main()