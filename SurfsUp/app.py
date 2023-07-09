# Import the dependencies.
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify
import numpy as np
import datetime as dt

#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(autoload_with=engine)

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Flask Routes
#################################################
@app.route("/")

def welcome():
    """List all the available routes.."""
    return (
        f"Climate APP API:<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/temp/start_date -- enter a start date in YYYY-MM-DD format from 2010-01-01 to 2017-08-23,<br/>"
        f"results are Min Temp, Avg Temp and Max Temp for all dates greater than or equal to the start date,<br/>"
        f"/api/v1.0/temp/start_date/end_date -- enter a start date and end date in YYYY-MM-DD format from 2010-01-01 to 2017-08-23 ,<br/>"
        f"results are Min Temp, Avg Temp and Max Temp the dates from the start date to the end date, inclusive"
    )

# Precipitation
@app.route("/api/v1.0/precipitation")
def precipitation():
    # Create our session (link) from Python to the DB
    session = Session(engine)
    
    # From the most recent date get the previous year (from the .ipynb file)
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)

    # Get the date and precipitation for prev_year
    precipitation = session.query(Measurement.date, Measurement.prcp) .\
        filter(Measurement.date >= prev_year).all()
     
    precip = {date: prcp for date, prcp in precipitation}
    session.close()
    return jsonify(precip)

# Stations
@app.route("/api/v1.0/stations")
def stations():
    # Create our session (link) from Python to the DB
    session = Session(engine)
    results = session.query(Station.station).all()

    # Convert list of tuples into normal list
    stations = list(np.ravel(results))
    session.close()
    return jsonify(stations=stations)

# Tobs
@app.route("/api/v1.0/tobs")
def monthly_temp():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    # Temperature observations (tobs in the DB) for the previous year.
    # From the most recent date get the previous year
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)

    # For all tobs (temperatures observed) of the most-active station for the prev. year of data.
    # USC00519281 from the ipynb file
    results = session.query(Measurement.tobs).\
        filter(Measurement.station == 'USC00519281').\
        filter(Measurement.date >= prev_year).all()

    # Convert list of tuples into normal list
    temp = list(np.ravel(results))
    session.close()
    # Return a JSON list of temperature observations for the previous year
    return jsonify(temp)

# Start-End Day Route
@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")
def date_range(start=None, end=None):
    # Create our session (link) from Python to the DB
    session = Session(engine)

    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs),func.max(Measurement.tobs)]

    if end == None: 
        # Query data from start date to recent date
        start_data = session.query(*sel).\
                        filter(Measurement.date >= start).all()
        # Convert list of tuples into normal list
        start_list = list(np.ravel(start_data))

        # Return a JSON list
        return jsonify(start_list)
    else:
        # Query the data from start date to the end date
        start_end_data = session.query(*sel).\
                        filter(Measurement.date >= start).\
                        filter(Measurement.date <= end).all()
        # Convert list of tuples into normal list
        start_end_list = list(np.ravel(start_end_data))

        # Return a JSON list
        return jsonify(start_end_list)

        # use in this format to enter the route api/v1.0/temp/2016-10-01/2016-10-30          
session.close()

if __name__ == '__main__':
    app.run(debug=True)