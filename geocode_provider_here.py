import requests

from geocode_result import GeocodeResult


class GeocodeProviderHere:
    def __init__(self, credential_store):
        self._credential_store = credential_store

    def resolve(self, query):
        # build the url parameters for the API request
        parameters = {
            "app_id": self._credential_store.get("here_app_id"),
            "app_code": self._credential_store.get("here_app_code"),
            "searchtext": query
        }

        # do the actual request
        response = requests.get("https://geocoder.cit.api.here.com/6.2/geocode.json", params=parameters)

        # parse the relevant data from the response
        response_json = response.json()
        position = response_json["Response"]["View"][0]["Result"][0]["Location"]["DisplayPosition"]
        result = GeocodeResult(position["Latitude"], position["Longitude"])

        return result
