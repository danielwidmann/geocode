import subprocess
import unittest
import requests
import json


class ServerUnitest(unittest.TestCase):
    def setUp(self):
        # startup an instance the server
        self._process = subprocess.Popen(["python", "server.py"])

    def tearDown(self):
        # make sure we don't leave the server running after the test
        self._process.terminate()

    def test_request_success(self):
        response = requests.get("http://localhost:5000/geocode", params={"query": "858 Beatty street, Vancouver, BC"})

        # make sure the reply is json formatted and has the correct content
        result = response.json()
        self.assertAlmostEqual(result["lat"], 49.2767302)
        self.assertAlmostEqual(result["lng"], -123.1150056)


if __name__ == "__main__":
    unittest.main()
