import unittest
from unittest import TestCase

from credential_store import CredentialStore
from geocode_provider_here import GeocodeProviderHere


class GeocodeUnittestHere(TestCase):
    def setUp(self):
        self._provider = GeocodeProviderHere(CredentialStore())

    def test_here_working(self):
        """
        Test a successful access to the here API
        """
        result = self._provider.resolve("858 Beatty street, Vancouver, BC")

        self.assertAlmostEqual(result.lat, 49.2767302)
        self.assertAlmostEqual(result.lng, -123.1150056)


if __name__ == '__main__':
    unittest.main()
