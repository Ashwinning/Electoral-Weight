from plotly.offline import download_plotlyjs, init_notebook_mode, plot
from plotly.graph_objs import *
import pandas as pd

df = pd.read_csv('2016VoteData.csv')

for col in df.columns:
    df[col] = df[col].astype(str)

scl = [[0.0, 'rgb(140,81,10)'],[0.105, 'rgb(255,255,255)'],[1.0, 'rgb(1,102,94)']]

df['text'] = df['State'] + '<br>' +\
    'Electoral Votes : '+df['Electoral-Votes']+ '<br>'+\
    'Estimated Ballots Cast In 2016 : '+df['Estimated-Ballots-Cast-In-2016']+ '<br>'+\
    '2016 Ballots Cast Per Elector : '+df['Voters-Per-Elector']+ '<br>'+\
    'Weight : '+df['Weight']+ '%<br>'

data = [ dict(
        type='choropleth',
        colorscale = scl,
        autocolorscale = False,
        locations = df['Postal-Code'],
        z = df['Weight'].astype(float),
        locationmode = 'USA-states',
        name = df['Weight'],
        text = df['text'],
        marker = dict(
            line = dict (
                color = 'rgb(241,241,241)',
                width = 2
            ) ),
        colorbar = dict(
            title = "Weight % compared to U.S. average")
        ) ]

layout = dict(
        title = '2016 Electoral Power per State Based on Voter Turnout',
        geo = dict(
            scope='usa',
            projection=dict( type='albers usa' ),
            showlakes = True,
            lakecolor = 'rgb(255, 255, 255)'),
             )

fig = dict( data=data, layout=layout )
plot( fig, filename='Interactive/Electoral-Power-By-Voter-Turnout.html' )
