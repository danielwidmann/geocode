import requests

from geocode_exceptions import GeocodeException, GeocodeNotFoundException
from geocode_result import GeocodeResult


class GeocodeProviderHere:
    """
    This provider uses the Here API to do geocoding.
    """
    def __init__(self, credential_store, api_url="https://geocoder.cit.api.here.com/6.2/geocode.json"):
        """
        Create a Here geocode provider
        :param credential_store: credential store used to get the api id and code
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
            "app_id": self._credential_store.get("here_app_id"),
            "app_code": self._credential_store.get("here_app_code"),
            "searchtext": query
        }

        try:
            # do the actual request
            response = requests.get(self._api_url, params = parameters, timeout=2)

            # parse the relevant data from the response
            response_json = response.json()

            if len(response_json["Response"]["View"]) == 0:
                # no result found
                raise GeocodeNotFoundException()

            position = response_json["Response"]["View"][0]["Result"][0]["Location"]["DisplayPosition"]
            result = GeocodeResult(position["Latitude"], position["Longitude"])
        except GeocodeNotFoundException as e:
            raise
        except Exception as e:
            # something went wrong during the request. Let the caller know
            raise GeocodeException("Error resolving with Here API", e)

        return result
