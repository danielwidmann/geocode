

class GeocodeException(Exception):
    """
    Exception raised if something went wrong while trying to resolve a geocode query.             
    """
    def __init__(self, message, cause):
        """
        Create a GeocodeException Exception
        :param message: Message what happened
        :param cause: An optional exception that caused this exception
        """
        super(GeocodeException, self).__init__(message + ", caused by " + repr(cause))
        self.cause = cause

