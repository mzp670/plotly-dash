"""This contains the main app set-up for the dashboard where main dashboard layout is defined, the updated
functions are set and the callbacks that displays the information required to the dashboard. """

from dash import Dash, html
import geopandas as gpd
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import plotly.express as px
import plotly.graph_objects as go
import textwrap
import NZIV_DF, header, year_slider, plots, map, metrics

#-----------------------------  COMPONENTS  -----------------------------

external_stylesheets=['/assets/styles.css', dbc.themes.MORPH,dbc.icons.BOOTSTRAP]
app = Dash(__name__, external_stylesheets=external_stylesheets)
header_components = header.create_header()
year_slider_components = year_slider.create_year_slider()
plots_components = plots.create_plot()
map_components = map.create_map()
metrics_components = metrics.create_metrics()

#-----------------------------  LAYOUT  -----------------------------
app.layout = html.Div(
    [       
        header_components,
        html.Br(),
        year_slider_components,
        dbc.Row(
            dbc.Col(metrics_components, width={"size": 11, "offset":1 }),
        ),
        html.Br(),
        dbc.Row(
            [
                dbc.Col(plots_components, width={"size": 5, "offset":1}),                 
                dbc.Col(map_components, width={"size": 5, "offset": 0}),  
            ],    className="my-1" 
        ),
    ],
)

#-----------------------------  SUPPORT FUNCTIONS  -----------------------------

def customwrap(s,width=30):
    """function to wrap long texts in multiple rows"""
    return "<br>".join(textwrap.wrap(s,width=width))

#-----------------------------  METRICS  -----------------------------

@app.callback(
    Output('international-value', 'children'),
    Output('domestic-value', 'children'),
    Output('pax-value', 'children'),
    Output('spend-value', 'children'),
    Output('night-value', 'children'),    
    Input('year-slider', 'value')
)
def update_expenditure_table(selected_year):
    """this function returns data related to metrics based on selected year"""

    # 1st database source
    revenue = NZIV_DF.generate_metrics('revenue_breakdown')
    filtered_data = revenue.query('Year == @selected_year')
    international_value = filtered_data.loc[:, 'International tourism expenditure'].item()
    domestic_value = filtered_data.loc[:, 'Domestic tourism expenditure'].item()

    # 2nd database source
    expense = NZIV_DF.generate_metrics('mean_spending')
    filtered_data1 = expense.query('Year == @selected_year')
    pax_value = filtered_data1.loc[:, 'Total Visitors'].item()
    mean_value = filtered_data1.loc[:, 'Mean Visitor Spend'].item()
    night_value = filtered_data1.loc[:, 'Average Spend per Night'].item()

    # Format the values
    international_value = "${:,.0f} M".format(international_value)
    domestic_value = "${:,.0f} M".format(domestic_value)
    pax_value = "{:,.0f}".format(pax_value)
    mean_value = "${:,.0f}".format(mean_value)
    night_value = "${:,.0f}".format(night_value)
    return str(international_value), str(domestic_value), str(pax_value), str(mean_value), str(night_value)

#-----------------------------  GRAPHS  -----------------------------
class PlotUpdater:
    def __init__(self):
        self.layout_settings = {'height': 400,'width': 600,'font_family': "Arial, sans-serif",'font_color': "#485785",
            'font_size': 9,'margin': dict(l=70, r=50, t=50, b=50),'plot_bgcolor': 'white' }

        self.xaxis_settings = {'mirror': True,'ticks': 'outside','linecolor': 'lightgrey','gridcolor': 'lightgrey'}

    def generate_bar_graph(self, dataframe, y_column, title, xaxis_title, yaxis_title, marker_color, selected_year):
        """Generate a bar graph with custom settings."""
        filtered_df = dataframe.query("`Year Ending` == @selected_year")
        bar_fig = go.Figure(go.Bar(
            y=filtered_df[y_column].map(customwrap),x=filtered_df['Value'],orientation='h',
            text=[f'{value/1_000_000:.1f}M' for value in filtered_df['Value']],  # Divide value by 1,000,000 and format as million
            hovertemplate='<b>%{y}</b><br>Number of People: %{text}',
            textposition='none'
        ))
        bar_fig.update_layout(
            title=title,xaxis=dict(title=xaxis_title, **self.xaxis_settings), yaxis=dict(title=yaxis_title),
            **self.layout_settings
        )
        bar_fig.update_traces(marker_color=marker_color)
        return bar_fig

    def update_plot(self, selected_year, active_tab):
        if active_tab == 'activity-tab':
            act_df = NZIV_DF.generate_top_activities(selected_year)
            title = f'<b>Top 10 Activities for Year {selected_year}</b>'
            xaxis_title = '<b>Number of People</b>'
            yaxis_title = '<b>Activity Type</b>'
            marker_color = 'lightblue'
            return self.generate_bar_graph(act_df, 'Activities', title, xaxis_title, yaxis_title, marker_color, selected_year)

        elif active_tab == 'accommodation-tab':
            accom_df = NZIV_DF.generate_top_accommodations(selected_year)
            title = f'<b>Top 10 Accommodation for Year {selected_year}</b>'
            xaxis_title = '<b>Number of People</b>'
            yaxis_title = '<b>Accommodation Type</b>'
            marker_color = 'lightsalmon'
            return self.generate_bar_graph(accom_df, 'Main accommodation used', title, xaxis_title, yaxis_title, marker_color, selected_year)

        elif active_tab == 'transportation-tab':
            trn_df = NZIV_DF.generate_top_transport(selected_year)
            title = f'<b>Top 10 Transportation for Year {selected_year}</b>'
            xaxis_title = '<b>Number of People</b>'
            yaxis_title = '<b>Mode of Transport</b>'
            marker_color = 'lightgreen'
            return self.generate_bar_graph(trn_df, 'Transport method', title, xaxis_title, yaxis_title, marker_color, selected_year)

plot_updater = PlotUpdater()

@app.callback(
    Output('plot-content', 'figure'),
    [Input('year-slider', 'value'),
     Input('plot-tabs', 'active_tab')])

def update_plots(selected_year, active_tab):
    return plot_updater.update_plot(selected_year, active_tab)

#-----------------------------  MAP  -----------------------------

# Callback function to update the figure
@app.callback(
    Output('map', 'figure'),
    Input('year-slider', 'value'),
    Input('product-dropdown', 'value'))

def update_map(year, product):
    """this function returns New Zealand map with related regional revenue indicators based on selected year"""

    # Set up the file path and read the shapefile data
    gdf = gpd.read_file('RTO.shp', encoding='utf-8')
    gdf = gdf.to_crs(epsg=4326)
    gdf['geometry'] = gdf['geometry'].simplify(0.01, preserve_topology=True)
    
    # Read the CSV data and merge shapefile and dataframe
    products = NZIV_DF.generate_products()
    merged_df = gdf.merge(products, left_on='RTO2022__1', right_on='Region1')
    filtered_df = merged_df[(merged_df['Year ending'] == year) & (merged_df['Products'] == product)]
   
   # Create plot for the map
   
    fig = px.choropleth(filtered_df, geojson=filtered_df.geometry, 
                        locations=filtered_df.index, color="Value",
                        height=500,
                        color_continuous_scale="Blues_r",
                        hover_name='Region1',
   )    
    fig.update_geos(fitbounds="locations", visible=True)
    # Add a disclaimer annotation
    disclaimer_message = "Note: Value for Total visitors refers to the number of count while for other options it is spending amount."
    fig.add_annotation(
    text=disclaimer_message, xref="paper", yref="paper", x=0.5, y=0.95, showarrow=False, font=dict(family="Arial",color="#485785",size=10,)
    )
    fig.update_layout(
        title_text=f'<b>Regional Demand for {product} in {year}</b>', width=600, height=400, margin={"r": 0, "t": 50, "l": 10, "b": 10},
        coloraxis_colorbar={'title': 'Value', 'len': 0.7}, font=dict(family="Arial", color="#485785", size=9, )
    )
    return fig

#-----------------------------  Local Deploy  -----------------------------

if __name__ == "__main__":  
    app.run_server(debug=True)
