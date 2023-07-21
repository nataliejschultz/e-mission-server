from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from future import standard_library
standard_library.install_aliases()
from builtins import *
from builtins import object
import urllib.request, urllib.parse, urllib.error, urllib.request, urllib.error, urllib.parse
import logging
import json
import emission.core.get_database as edb
import emission.core.common as cm
import unittest

from emission.core.wrapper.trip_old import Coordinate

import emission.net.ext_service.geocoder.nominatim as eco

class NominatimTest(unittest.TestCase):
    def testURL(self):
        NOMINATIM_QUERY_URL = "http://nominatim.openstreetmap.org/reverse?lat=39.4818456&lon=-106.0445699&format=json"
        reverse_geocoded_json = eco.Geocoder.get_json_reverse(39.4818456, -106.0445699)
        expected_result = {'place_id': 161212506, 'licence': 'Data © OpenStreetMap contributors, ODbL 1.0. https://osm.org/copyright', 'osm_type': 'way', 'osm_id': 225428302, 'lat': '39.481845750000005', 'lon': '-106.04461232050828', 'display_name': "Fatty's Pizzaria, South Ridge Street, Breckenridge, Summit County, Colorado, 80424, United States", 'address': {'amenity': "Fatty's Pizzaria", 'road': 'South Ridge Street', 'town': 'Breckenridge', 'county': 'Summit County', 'state': 'Colorado', 'ISO3166-2-lvl4': 'US-CO', 'postcode': '80424', 'country': 'United States', 'country_code': 'us'}, 'boundingbox': ['39.4817808', '39.481879', '-106.0447033', '-106.0445205']}
        actual_result = reverse_geocoded_json
        self.assertEqual(expected_result, actual_result)



if __name__ == '__main__':
    # logging.basicConfig(level=logging.DEBUG)
    unittest.main()