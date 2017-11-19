class GeocodeResult:
    """
    Result of a geocode operation.
    """

    def __init__(self, lat, lng):
        """
        Create a geocode result with latitude and longitude.
        :param lat: latitude
        :param lng: longitude
        """
        self._lat = lat
        self._lng = lng

    @property
    def lat(self):
        """
        Get the latitude.
        """
        return self._lat

    @property
    def lng(self):
        """
        Get the longitude
        """
        return self._lng
