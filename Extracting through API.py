#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 29 10:56:16 2018

@author: karan.ganesh.dumbre
"""

import requests


# url 
url = 'https://api.data.gov/ed/collegescorecard/v1/schools?school.name=boston%20college&api_key=EqAhxT1RjSfZmd8MHsgOskrXcw3yAlc4StPEWMSq'

# using get command , returns response object
result = requests.get(url)

# exploring response object : status_code
result.status_code

# exploring response object : headers
result.headers

# exploring response object : text
result.text

# in json object
result.json()

