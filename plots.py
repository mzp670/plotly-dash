"""This function file is for the layout of the chosen graphs and the tabs section"""

from dash import dcc
import dash_bootstrap_components as dbc
from dash import html

def create_plot():
    """ function to generate a layout for the multi graph section"""
    
    plots = html.Div([
        dbc.Row(
            html.Strong(
                "Top 10 Choices for International Visitors ",
                style={"margin-left": "1%", "font-size": "15px"}
            )
        ),
        dbc.Row(
            dbc.Tabs(
                [
                    dbc.Tab(label="Activity", tab_id="activity-tab", style={'width': '100px'}),
                    dbc.Tab(label="Accommodation", tab_id="accommodation-tab", style={'width': '100px'}),
                    dbc.Tab(label="Transportation", tab_id="transportation-tab", style={'width': '100px'})
                ],
                id="plot-tabs",
                active_tab="activity-tab",
                className='mt-4,',
                    style={ 'font-size': '12px','height': '30px','width': '315px', 'margin-left': '295px'}
            )
        ),
        dbc.Row(
            [
                dbc.Col(
                    dcc.Graph(id='plot-content')
                )
            ],
            justify='start'
        )
    ])
    
    return plots