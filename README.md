# SQLAlchemy Challenge

## Instructions
Do a climate analysis about Honolulu, Hawaii using Python and SQLAlchemy.

## Part 1: Analyze and Explore the Climate Data
Perform a basic climate analysis and data exploration of your climate database. Specifically, using SQLAlchemy ORM queries, Pandas, and Matplotlib.

1- Used the provided files (climate_starter.ipynb and hawaii.sqlite) to complete the climate analysis and data exploration.

2- Used the SQLAlchemy create_engine() function to connect to the SQLite database.

3- Used the SQLAlchemy automap_base() function to reflect the tables into classes, and then save references to the classes named station and measurement.

4- Linked Python to the database by creating a SQLAlchemy session.

5- Performed a precipitation analysis and then a station analysis by completing the steps in the following two subsections.

### Precipitation Analysis
1- Found the most recent date in the dataset.

2- Using that date, got the previous 12 months of precipitation data by querying the previous 12 months of data.

3- Selected only the "date" and "prcp" values.

4- Loaded the query results into a Pandas DataFrame. Explicitly set the column names.

5- Sorted the DataFrame values by "date".

6- Plotted the results (by using the DataFrame plot method), producing the following image:

![Precipitation_by_Date](https://github.com/javsgon/sqlalchemy-challenge/assets/125521896/5a87e24e-217d-4a75-a234-b6401742fbce)

7- Used Pandas to print the summary statistics for the precipitation data.

### Station Analysis
1- Designed a query to calculate the total number of stations in the dataset.

2- Designed a query to find the most-active stations (that is, the stations that have the most rows). To do so, complete the following steps:

* Listed the stations and observation counts in descending order.
* Answered the following question: which station id has the greatest number of observations?

3- Designed a query that calculates the lowest, highest, and average temperatures that filters on the most-active station id found in the previous query.

4- Designed a query to get the previous 12 months of temperature observation (TOBS) data. To do so, complete the following steps:

* Filtered by the station that has the greatest number of observations.

* Queried the previous 12 months of TOBS data for that station.

* Plotted the results as a histogram with bins=12, producing the following image:

![Temperature Observations](https://github.com/javsgon/sqlalchemy-challenge/assets/125521896/ae314bbf-4e73-4f23-bd14-d244f4ba965f)

5- Closed the session.

## Part 2: Design the Climate App
Design a Flask API based on the queries developed. To do so, used Flask to create the routes as follows:

1- /

* Start at the homepage.
* List all the available routes.

2- /api/v1.0/precipitation

* Converted the query results from the precipitation analysis (i.e. retrieve only the last 12 months of data) to a dictionary using date as the key and prcp as the value.

* Returned the JSON representation of your dictionary.

3- /api/v1.0/stations

* Returned a JSON list of stations from the dataset.

4- /api/v1.0/tobs

* Queried the dates and temperature observations of the most-active station for the previous year of data.

* Returned a JSON list of temperature observations for the previous year.

5- /api/v1.0/<start> and /api/v1.0/<start>/<end>

* Returned a JSON list of the minimum temperature, the average temperature, and the maximum temperature for a specified start or start-end range in YYYY-MM-DD format.

* For a specified start, calculated minimum temperature, average temperature, and maximum temperature for all the dates greater than or equal to the start date in YYYY-MM-DD format..

* For a specified start date and end date in YYYY-MM-DD format, calculated minimum temperature, average temoerature, and maximum temperature for the dates from the start date to the end date, inclusive.

