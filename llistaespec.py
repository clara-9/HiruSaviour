# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 07:38:57 2019

@author: Clara Rull
"""

import csv
import pandas

result = pandas.read_csv('specieslist.csv',sep='\t')
sespec=result.loc[: , "scientificName"]
#sespec[0] retorna el nom de la especie com a string
print(sespec[4])