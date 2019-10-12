# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""

import requests
import json

oreneta=requests.get("http://api.gbif.org/v1/occurrence/1986554608")
print(oreneta.json())
orepy=oreneta.json()
coords=[orepy["decimalLongitude"],orepy["decimalLatitude"]]
