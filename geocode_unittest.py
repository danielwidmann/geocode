import unittest
from unittest import TestCase

from credential_store import CredentialStore
from geocode_exceptions import GeocodeException
from geocode_provider_google import GeocodeProviderGoogle
from geocode_provider_here import GeocodeProviderHere


class GeocodeUnittestHere(TestCase):
    def setUp(self):
        self._provider = GeocodeProviderHere(CredentialStore())

    def test_working(self):
        result = self._provider.resolve("858 Beatty street, Vancouver, BC")

        self.assertAlmostEqual(result.lat, 49.2767302)
        self.assertAlmostEqual(result.lng, -123.1150056)

    def test_failed(self):
        self._provider = GeocodeProviderHere(CredentialStore(), api_url="https://geocoder.cit.api.here.com/xyz")

        with self.assertRaises(GeocodeException):
            result = self._provider.resolve("a")

    def test_timeout(self):
        self._provider = GeocodeProviderHere(CredentialStore(), api_url="https://1.2.3.4")

        with self.assertRaises(GeocodeException):
            result = self._provider.resolve("a")


class GeocodeUnittestGoogle(TestCase):
    def setUp(self):
        self._provider = GeocodeProviderGoogle(CredentialStore())

    def test_working(self):
        result = self._provider.resolve("858 Beatty street, Vancouver, BC")

        self.assertAlmostEqual(result.lat, 49.276851)
        self.assertAlmostEqual(result.lng, -123.1147964)

    def test_failed(self):
        self._provider = GeocodeProviderHere(CredentialStore(), api_url="https://maps.googleapis.com/maps/api/geocodes")

        with self.assertRaises(GeocodeException):
            result = self._provider.resolve("a")

    def test_timeout(self):
        self._provider = GeocodeProviderHere(CredentialStore(), api_url="https://1.2.3.4")

        with self.assertRaises(GeocodeException):
            result = self._provider.resolve("a")


if __name__ == '__main__':
    unittest.main()
