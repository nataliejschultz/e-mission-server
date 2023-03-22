from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from future import standard_library
standard_library.install_aliases()
from builtins import *
import logging
# It is not clear if we need to copy here, given that we are almost
# immdediately going to save to the database. Let us assume that we don't.
# We can add it if it turns out that there are issues with mutability.
import copy
import attrdict as ad
import pytz
import datetime as pydt
import geojson
# This change should be removed in the next server update, by which time hopefully the new geojson version will incorporate the long-term fix for their default precision
# See - jazzband/geojson#177
# See = https://github.com/e-mission/e-mission-server/pull/900/commits/d2ada640f260aad8cbcfecb81345f4087c810baa
geojson.geometry.Geometry.__init__.__defaults__ = (None, False, 15)
import arrow

import emission.net.usercache.formatters.common as fc
import emission.storage.decorations.local_date_queries as ecsdlq

def format(entry):
    # assert(entry.metadata.key == "background/location")
    return format_location_simple(entry)

def format_location_simple(entry):
    formatted_entry = ad.AttrDict()
    formatted_entry["_id"] = entry["_id"]
    formatted_entry.user_id = entry.user_id

    metadata = entry.metadata
    fc.expand_metadata_times(metadata)
    formatted_entry.metadata = metadata

    data = entry.data
    fc.expand_data_times(data, metadata)
    data.loc = geojson.Point((data.longitude, data.latitude))
    data.heading = entry.data.bearing
    del data.bearing
    formatted_entry.data = data

    return formatted_entry
