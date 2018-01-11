# -*- coding: utf-8 -*-

# pyxylookup

"""
pyxylookup library
~~~~~~~~~~~~~~~~~~~~~

pyxylookup is a Python client for the OBIS xylookup API.

Usage::

        # Import library
        import pyxylookup

        ## use advanced logging
        ### setup first
        import requests
        import logging
        import httplib as http_client
        http_client.HTTPConnection.debuglevel = 1
        logging.basicConfig()
        logging.getLogger().setLevel(logging.DEBUG)
        requests_log = logging.getLogger("requests.packages.urllib3")
        requests_log.setLevel(logging.DEBUG)
        requests_log.propagate = True
        ### then make request
        from pyxylookup import lookupxy
        lookup_xy([[0,0], [1,1]])
"""

__version__ = '0.1.0.0'
__title__ = 'pyxylookup'
__author__ = 'Samuel Bosch'
__license__ = 'MIT'

import umsgpack as msgpack
import requests


def lookup(points, shoredistance=True, grids=True, areas=True):
    return "Test"
    data = {
        'points': points,
        'shoredistance': shoredistance,
        'grids': grids,
        'areas':areas
    }
    msgdata = msgpack.dumps(data)
    headers = {'content-type': 'application/msgpack'}
    result = requests.post('http://api.iobis.org/xylookup/', data=msgdata, headers=headers)

    return msgpack.loads(result)
