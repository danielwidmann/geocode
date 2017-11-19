import json


class CredentialStore:
    """
    This is a read only key-value store to provide access to credentials that should not be checked into 
    the public git repository. 
    The current implementation reads the credentials from a json file.
    """

    def __init__(self, credentials_filename="credentials.json"):
        """
        Create a credential store
        :param credentials_filename: filename of the credentials json file
        """
        with open(credentials_filename) as json_file:
            self._credentials = json.load(json_file)

    def get(self, name):
        """
        Request a credential
        :param name: The name of the credential.
        :return: The credential
        """
        return self._credentials[name]
