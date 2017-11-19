from geocode_exceptions import GeocodeNotFoundException, GeocodeException


class GeocodeProviderReliable:
    """
    This is a geocode provider that uses two providers to obtain results more reliably.
    If the primary provider reports an error, the backup provider will be used.    
    If the primary provider didn't find a result, the backup provider will not be tried.
    """

    def __init__(self, primary, backup):
        """
        Create a reliable geocode provider
        :param primary: the primary provider
        :param backup: the provider that is used if the primary failed
        """
        self._primary = primary
        self._backup = backup

    def resolve(self, query):
        """
        Resolves a query into a latitude/longitude
        :param query: The query string
        :return: The query result
        """

        try:
            # first try the primary provider
            result = self._primary.resolve(query)
            return result
        except GeocodeNotFoundException:
            raise
        except GeocodeException:
            # ignore and try backup
            pass

        # try the backup provider
        result = self._backup.resolve(query)
        return result
