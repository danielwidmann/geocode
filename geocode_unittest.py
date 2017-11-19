import unittest
from unittest import TestCase

from credential_store import CredentialStore
from geocode_exceptions import GeocodeException
from geocode_provider_here import GeocodeProviderHere


class GeocodeUnittestHere(TestCase):
    def setUp(self):
        self._provider = GeocodeProviderHere(CredentialStore())

    def test_here_working(self):
        result = self._provider.resolve("858 Beatty street, Vancouver, BC")

        self.assertAlmostEqual(result.lat, 49.2767302)
        self.assertAlmostEqual(result.lng, -123.1150056)

    def test_here_failed(self):
        self._provider = GeocodeProviderHere(CredentialStore(), api_url="https://geocoder.cit.api.here.com/xyz")

        with self.assertRaises(GeocodeException):
            result = self._provider.resolve("a")

    def test_here_timeout(self):
        self._provider = GeocodeProviderHere(CredentialStore(), api_url="https://1.2.3.4")

        with self.assertRaises(GeocodeException):
            result = self._provider.resolve("a")

if __name__ == '__main__':
    unittest.main()
