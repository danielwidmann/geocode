from flask import request
from flask_restful import Resource

from geocode_exceptions import GeocodeNotFoundException


class GeocodeResource(Resource):
    """
    A resource that resolves a query into a latitude/longitude. Different geocoding providers can be use to resolve the 
    query.
    
    See https://github.com/danielwidmann/geocode for API specification.
    """

    def __init__(self, **kwargs):
        """
        Create the resource.
        :param geocode_provider: The geocode provider that should be used to resolve the requests.
        """
        self._geocode_provider = kwargs["geocode_provider"]

    def get(self):
        # get the query string from the GET request parameters
        query = request.args["query"]

        try:
            # resolve the query using the provider given in the constructor
            result = self._geocode_provider.resolve(query)
        except GeocodeNotFoundException:
            # no result was found, send an empty response
            return {}

        # format the result according to the API specification
        return {"lat": result.lat, "lng": result.lng}
