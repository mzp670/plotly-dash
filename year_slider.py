"""This function file is for the year slider layout"""

import dash_bootstrap_components as dbc
from dash import html, dcc

def create_year_slider():
    """ function to generate a layout for the year slider"""
    # Pre-defined year range
    years = list(range(2000, 2021))    
    
    # Create a year slider for the table and plots
    marks = {str(year): str(year) for year in years[::2]}  
    year_slider_components = dbc.Row(
        [
            dbc.Col(
                [
                    html.Strong(
                        "Select Year:",
                        style={"font-size": "13px"},
                    ),
                ],
                width=1,
                align="center",
            ),
            dbc.Col(
                [
                    dcc.Slider(
                        id="year-slider",
                        min=min(years),
                        max=max(years),
                        value=2010,
                        marks=marks,
                        step=1,
                        className="slider-custom", 
                    ),
                ],
                width=8,
                align="center",
                style={"font-size": "10px", "transform": "scale(1)"},
            ),
        ],
        justify="center",
        align="center",
        className="year-slider-row",  
    )

    return year_slider_components
