#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 07:33:01 2024

@author: brigitanderson
"""

from ebird.api import *
import requests
import os

api_key = "i430r0mdn2as"
output_path = r'/Users/brigitanderson/Documents/Thesis/jsons'

#create list of all country codes
countries = get_regions(api_key, 'country', 'world')
country_codes = []
for country in countries:
    country_codes.append((country['code']))




#request data for each country and write to json
for code in country_codes:
    records = requests.get_observations(api_key, code, detail='full')
    path = os.path.join(output_path, "{0}.json".format(code))
    with open(path, 'w') as outf:
        outf.write(records.content)
        
        
    