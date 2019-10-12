import csv
import pandas

orenetes = pandas.read_csv('orenetes.csv',sep='\t',error_bad_lines=False,)

import plotly.graph_objects as go
fig = go.Figure(go.Densitymapbox(lat=orenetes.decimalLatitude, lon=orenetes.decimalLongitude, z=orenetes.individualCount, radius=30))
fig.update_layout(mapbox_style="stamen-terrain", mapbox_center_lon=180)
fig.update_layout(margin={"r":0, "t":o, "l":0, "b":0})
fig.show()


