import csv
import pandas

gener = pandas.read_csv('bo.csv',sep=',',error_bad_lines=False,low_memory=False).query("year>1995")

import plotly.express as px
fig = px.scatter_geo(gener, lat="decimalLatitude", lon="decimalLongitude",
                     animation_frame="month", color="year", projection = "natural earth")
      
fig.show()






