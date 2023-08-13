"""This code refers to the datasets used in the dashboard. Data source is from NZ Stats website. """

import pandas as pd

def convert_year_format(df, column_name):
    """ Convert column period to year """

    df[column_name] = pd.to_datetime(df[column_name].str[-4:] + "-" + df[column_name].str[2:5] + "-01", format='%Y-%b-%d').dt.strftime('%Y')
    df[column_name] = df[column_name].astype(int)
    df = df.rename(columns={column_name: "Year Ending"})
    return df

#-------------------------- FIGURE 1  -------------------------- 
def generate_metrics(metric_type):
    """Generate data for different tourism industry metrics"""

    if metric_type == 'revenue_breakdown':
        df8 = pd.read_excel("NZ Tourism Expenditure by Type.xlsx", sheet_name="Sheet1", header=1, skiprows=0)
        df8 = df8.dropna()
        df8 = df8[(df8['Year'] >= 1999) & (df8['Year'] <= 2019)]
        return df8

    elif metric_type == 'mean_spending':
        df2 = pd.read_excel("NZ IVS Expenditure.xlsx", sheet_name="NZ.Stat export", header=7, skiprows=0)
        df2 = df2.dropna()
        df2 = convert_year_format(df2, 'Year ending').astype(int)
        df2 = df2[(df2['Year Ending'] >= 1999) & (df2['Year Ending'] <= 2019)]
        df2.sort_values('Year Ending', inplace=True)

        df2_yearly_total = df2.groupby('Year Ending')[['Total visitor spend', 'Total Visitors', 'Number of respondents']].sum()
        df2_yearly_mean = df2.groupby('Year Ending')[['Mean Visitor Spend', 'Average Spend per Night']].mean().round(1)
        df2_yearly = pd.concat([df2_yearly_mean, df2_yearly_total], axis=1)
        df2_yearly.reset_index(inplace=True)
        df2_yearly.rename(columns={'Year Ending': 'Year'}, inplace=True)
        return df2_yearly

    else:
        return None
#--------------------------  GRAPH  -------------------------- 
def generate_top_data(file_name, column_name, value_filter, selected_year):
    """Generate Top 10 Data Types per year based on the given file, column, and value filter."""
    
    # Read in the data
    df = pd.read_excel(file_name, sheet_name="Sheet1")
    
    # Convert year and add filters
    df = convert_year_format(df, 'Year ending')
    df = df[(df['Year Ending'] >= 1999) & (df['Year Ending'] <= 2019) & 
            (df['Measure'] == 'Total visitors') & (~df[column_name].isin(value_filter))] 
    
    # Group, select top 10, and sort
    grouping = df.groupby(['Year Ending', column_name])['Value'].sum().reset_index()
    top_data = grouping.groupby('Year Ending').apply(lambda x: x.nlargest(10, 'Value')).reset_index(drop=True)
    sorted_df = top_data.sort_values('Value', ascending=True)
    
    # Filter data for the selected year
    selected_year = int(selected_year)
    filtered_df = sorted_df[sorted_df['Year Ending'] == selected_year]
    
    return filtered_df

def generate_top_accommodations(selected_year):
    """Generate Top 10 Accommodation Types per year"""
    return generate_top_data("NZ IVS Accomodation.xlsx", "Main accommodation used", 
                             ["All", "NOT SURE", "Other", "Unknown"], selected_year)

def generate_top_activities(selected_year):
    """Generate Top 10 Activities Types per year"""
    return generate_top_data("NZ IVS Activities.xlsx", "Activities", ["All", "None of these"], selected_year)

def generate_top_transport(selected_year):
    """Generate Top 10 Transportation Types per year"""
    return generate_top_data("NZ IVS Transport.xlsx", "Transport method", ["All", "Not sure"], selected_year)


#--------------------------  MAP  -------------------------- 
# Regional Services per Year

def generate_products():
    """ Generate Regional Services per Year"""

    # Read in the data
    df6 = pd.read_excel("NZ IVS Regions Products.xlsx")
    # Filter specific columns
    df6= df6[(df6['Year ending'] >= 1999) & (df6['Year ending'] <= 2019) 
              & (~df6['Regional tourism organisation'].isin(['All','Unknown']))] 
    df6 = df6.drop(columns = ['Region','Regional tourism organisation'])
    # Consolidate values based on groupings
    grouped = df6.groupby(['Year ending','Region1','Products'])['Value'].sum().reset_index()    
    grouped['Value'] = grouped['Value'].round(1)
    return grouped

#products = generate_products()
