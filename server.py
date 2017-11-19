import argparse
from flask import Flask
from flask_restful import Api

from credential_store import CredentialStore
from geocode_provider_google import GeocodeProviderGoogle
from geocode_provider_here import GeocodeProviderHere
from geocode_provider_reliable import GeocodeProviderReliable
from geocode_resource import GeocodeResource


def run_server(host, port, debug):
    app = Flask(__name__)
    api = Api(app)

    # setup the provider we are going to use for resolving requests
    geocode_provider = GeocodeProviderReliable(
        GeocodeProviderHere(CredentialStore()),
        GeocodeProviderGoogle(CredentialStore()))

    # create and register the resource
    api.add_resource(GeocodeResource, '/geocode', resource_class_kwargs={'geocode_provider': geocode_provider})

    # start the server
    app.run(host=host, port=port, debug=debug)


if __name__ == '__main__':
    # add a simple command line interface to the server application
    parser = argparse.ArgumentParser(description='Reliable Geocoding Proxy Server.')
    parser.add_argument('--host', type=str, default="127.0.0.1",
                        help='the host ip address to listen on')
    parser.add_argument('--port', type=int, default=5000,
                        help='the port to listen on')
    parser.add_argument('--debug', type=bool, default=False,
                        help='debug mode')

    args = parser.parse_args()

    run_server(args.host, args.port, args.debug)
