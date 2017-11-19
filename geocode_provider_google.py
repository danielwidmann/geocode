import requests

from geocode_exceptions import GeocodeException
from geocode_result import GeocodeResult


class GeocodeProviderGoogle:
    """
    This provider uses the Google API to do geocoding.
    """
    def __init__(self, credential_store, api_url="https://maps.googleapis.com/maps/api/geocode/json"):
        """
        Create a Google geocode provider
        :param credential_store: credential store used to app key
        :param api_url: The url of the here api
        """
        self._credential_store = credential_store
        self._api_url = api_url

    def resolve(self, query):
        """
        Resolves a query into a latitude/longitude
        :param query: The query string
        :return: The query result
        """
        # build the url parameters for the API request
        parameters = {
            "key": self._credential_store.get("google_api_key"),
            "address": query
        }

        try:
            # do the actual request
            response = requests.get(self._api_url, params = parameters, timeout=2)

            # parse the relevant data from the response
            response_json = response.json()
            location = response_json["results"][0]["geometry"]["location"]
            result = GeocodeResult(location["lat"], location["lng"])
        except Exception as e:
            # something went wrong during the request. Let the caller know
            raise GeocodeException("Error resolving with Google API", e)

        return result
