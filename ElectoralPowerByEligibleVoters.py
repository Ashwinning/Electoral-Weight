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
    'Voting Eligible Population In 2016 : '+df['Voting-Eligible-Population']+ '<br>'+\
    '2016 Eligible Voters Per Elector : '+df['Eligible-Voters-Per-Elector']+ '<br>'+\
    'Weight by Turnout : '+df['Weight']+ '%<br>'+\
    'Weight By Eligibility : '+df['Weight-By-Eligibility']+ '%<br>' +\
    'Power Utilization : '+df['Power Utilization']+ '%<br>'

data = [ dict(
        type='choropleth',
        colorscale = scl,
        autocolorscale = False,
        locations = df['Postal-Code'],
        z = df['Power Utilization'].astype(float),
        locationmode = 'USA-states',
        name = df['Power Utilization'],
        text = df['text'],
        marker = dict(
            line = dict (
                color = 'rgb(241,241,241)',
                width = 2
            ) ),
        colorbar = dict(
            title = "Power Utilization % Compared to U.S. Average")
        ) ]

layout = dict(
        title = '2016 Electoral Power Utilization %.',
        geo = dict(
            scope='usa',
            projection=dict( type='albers usa' ),
            showlakes = True,
            lakecolor = 'rgb(255, 255, 255)'),
             )

fig = dict( data=data, layout=layout )
plot( fig, filename='Interactive/Electoral-Power-Utilization.html' )
