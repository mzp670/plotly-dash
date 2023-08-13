## Analyzing tourism trends in New Zealand with an interactive International Visitors Dashboard

**Introduction**

New Zealand, a stunning island nation nestled in the Pacific Ocean, boasts captivating landscapes, a rich blend of cultures, and a thriving economy. With a population of 5.15 million and a robust GDP of 2.4 as of December 2022, the country is a haven for travelers seeking natural beauty, warm hospitality, and culinary delights. Tourism plays a pivotal role in this growth story, contributing a significant $10 billion to the GDP and fostering cultural exchange and commercial opportunities. This project aims to create a dashboard showcasing foreign tourism's economic impact, revealing spending patterns across locations, preferred activities, and accommodation choices, offering valuable insights for informed decision-making.


**About the Data**

Using the international visitors survey public datasets from NZ Stats, the intent is to produce a dashboard that will feature historical statistics and trends within the timeframe of year 2000 to 2020. Five references were used on this project that are related to international visitors: expenditure, main accommodation used, activities, transportation and regional spend.


**Design, Features and Functionality**

The overall dashboard is designed with the user's perspective in mind, prioritizing clarity, ease of use, and an aesthetically pleasant data presentation.

![dash](/assets/dash.png)

Header:
An eye-catching header showcases New Zealand's natural beauty and centers the dashboard's title, instantly capturing users' attention and conveying its purpose.

Choice Filters:
User-friendly choice filters, including tabs, sliders, and dropdowns, offer data interaction flexibility, enabling users to customize their views based on their preferences. The slider allows users to select the desired year, while sub-filters in graphs and maps enhance exploration by organizing data by activity, accommodation, and transportation.

Overall Layout:
The dashboard maintains a clean and balanced layout, ensuring logical organization and user-friendly navigation. Consistent color theming throughout creates a cohesive visual experience across all elements, enhancing aesthetic appeal.

Data Visualization:
Various visualization styles are employed for effective data presentation. Metrics are presented in card-style format, featuring icons and values for the chosen year. Interactive graphs with tabbed categories showcase top 10 choices datasets, with descending bars for easy comprehension. A map illustrates regional data, with color changes reflecting chosen indicators from the dropdown menu. Hovering over elements reveals specific information, ensuring clear and engaging data interpretation.


Three tabs for the Top 10 Choices of International Visitors:

![dash1](/assets/dash1.png)


![dash2](/assets/dash2.png)


![dash3](/assets/dash3.png)


Drop-down filter options for regional demand:

![dash4](/assets/dash4.png)



**References:**

Data Source:  
https://nzdotstat.stats.govt.nz/wbos/Index.aspx? 

Code & Design Sources:  
https://github.com/Coding-with-Adam/Dash-by-Plotly
https://github.com/plotly/dash-sample-apps/tree/2c05a6090d138b286da3b8fa66f805e3d7cff69d/apps
https://towardsdatascience.com/plot-choropleth-maps-with-shapefiles-using-geopandas-a6bf6ade0a49
https://github.com/plotly/dash-sample-apps/tree/main/apps/dash-baseball-statistics
https://dash.gallery/usa-gov-analytics/
https://dashcheatsheet.pythonanywhere.com/
https://chart-studio.plotly.com/~empet/15238/tips-to-extract-data-from-a-geojson-di/#/
https://plotly.com/python-api-reference/generated/plotly.graph_objects.Choroplethmapbox.html

Help Support:  
https://chat.openai.com/
https://community.plotly.com/
https://stackoverflow.com/

