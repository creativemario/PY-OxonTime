import requests
import json
import time

import oxontime_stop

#KEEP THE TRAILING FORWARD SLASH
api_url = 'https://oxontime.com/pwi/departureBoard/'

def get_stop(stop_code):
    resp = requests.get(url=api_url+stop_code)
    data = resp.json() # Check the JSON Response Content documentation below
    stop = oxontime_stop.stop(data[stop_code])
    return stop



