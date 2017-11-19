class GeocodeException(Exception):
    """
    Exception raised if something went wrong while trying to resolve a geocode query.             
    """

    def __init__(self, message, cause):
        """
        Create a Geocode Exception
        :param message: Message what happened
        :param cause: An optional exception that caused this exception
        """
        super(GeocodeException, self).__init__(message + ", caused by " + repr(cause))
        self.cause = cause


class GeocodeNotFoundException(Exception):
    """
    Exception raised if no result was found for a geocoding query.             
    """

    def __int__(self):
        """
        Create a Geocode Not Found Excpetion        
        """
        super(GeocodeNotFoundException, self).__init__("No result was found")
