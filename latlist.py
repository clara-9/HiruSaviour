# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 02:55:29 2019

@author: Clara Rull
"""
def mitjana (df3):
    latlist=[]
    for y in range(1980,2018):
        for x in range(1,12):
              latvar=0
              count=1
              for line in range(1,6669442):
                  if df3[line][3]==x and df3[line][4]==y:
                    latvar=latvar+df3[line][1]
                    count+=1
              latlist.append(latvar/count)
    return latlist

