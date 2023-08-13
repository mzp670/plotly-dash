"""This function file is for the layout of the map and its components"""

import NZIV_DF
import dash_bootstrap_components as dbc
from dash import html, dcc

def create_map():
    """ function to generate the layout of the map with dropdown option"""  
      
    products = NZIV_DF.generate_products()
    initial_product = "Total visitors"
    map_components = dbc.Container(
        [
        dbc.Row(
            html.Strong(
                "Demand per Region",
                style={"margin-left": "1%", "font-size": "15px"}
            )
        ),          
        dbc.Row(
            [
                dbc.Col(
                    [   
                        html.Strong(
                            "Select a product/service: ",
                            style={"margin-left": "5%", "font-size": "12px"},
                        ),
                    ],
                    md=0,
                ),
                dbc.Col(
                    [
                        dcc.Dropdown(
                            id='product-dropdown',
                            options=[{'label': product, 'value': product} for product in products['Products'].unique()],
                            value=initial_product,
                            style={'width': '100%', 'font-size': '90%',"margin-left": "1px"},
                        ),
                    ],
                    md=0,
                ),
            ],
            className='mt-0',

        ),
        dbc.Row(
            [
                dbc.Col(
                    dcc.Graph(id='map') #, style={'width': '120%', 'height': '300px'}
                )
            ]
        ),
    ],
    fluid=True,
    )

    return map_components
