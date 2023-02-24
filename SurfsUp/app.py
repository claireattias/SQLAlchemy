# import libraries
from flask import Flask, jsonify
import datetime as dt
import numpy as np
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

########## DATABASE SETUP

# create engine
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(engine, reflect=True)

# View all of the classes that automap found
Base.classes.keys()

# Save references to each table
measurement = Base.classes.measurement
station = Base.classes.station

########## FLASK SETUP

# create an app 
app = Flask(__name__)

# define homepage and list all available routes 
@app.route("/")
def welcome():
    """List all available api routes"""
    return (
        f"Welcome to my home page"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation"
        f"/api/v1.0/stations"
        f"/api/v1.0/tobs"
        f"/api/v1.0/<start>"
        f"/api/v1.0/<start>/<end>"
    )

# Convert the query results from precipitation analysis to a dictionary using date as the key and prcp as the value
@app.route("/api/v1.0/precipitation")
def precipitation():
    session = Session(engine)
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    prcp_query = session.query(measurement.date, measurement.prcp).order_by(measurement.date).filter(measurement.date >= prev_year).all()
    prcp_date = []
    for x in prcp_query:
        prcp_date_dict = {}
        prcp_date_dict["date"] = x.date
        prcp_date_dict["prcp"] = x.prcp
        prcp_date.append(x)

    # Return the JSON representation of your dictionary
    return jsonify(prcp_date)

# Return a JSON list of stations from the dataset
@app.route("/api/v1.0/stations")
def stations():
    session = Session(engine)
    station_query = session.query(station.station).all()
    station_list = list(np.ravel(station_query))
    return jsonify(station_list)
    
# Query the dates and temperature observations of the most-active station for the previous year of data
# Return a JSON list of temperature observations for the previous year
@app.route("/api/v1.0/tobs")
def tobs():
    session = Session(engine)
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    tobs_query = session.query(measurement.tobs).filter(measurement.station == 'USC00519281').filter(measurement.date >= prev_year).all()
    temps = list(np.ravel(tobs_query))
    return jsonify(temps)

# Return a JSON list of the minimum temperature, the average temperature, and the maximum temperature 
# for a specified start or start-end range.
# For a specified start, calculate TMIN, TAVG, and TMAX for all the dates greater than or equal to the start date.
# For a specified start date and end date, calculate TMIN, TAVG, and TMAX for the dates from the start date to the end date, inclusive.

@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")
def start(start=None, end=None):
    sel = [func.min(measurement.tobs), func.avg(measurement.tobs), func.max(measurement.tobs)]
    if not end:
        results = session.query(*sel).filter(measurement.date >= start).filter(measurement.date <= end).all()
        temps = list(np.ravel(results))
        return jsonify(temps)
    results = session.query(*sel).filter(measurement.date >= start).filter(measurement.date <= end).all()
    temps = list(np.ravel(results))
    return jsonify(temps)

# if __name__ == "__main__":
    # app.run(debug=True)


