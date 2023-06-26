In this activity, a climate analysis is conducted to help with future trip planning

Part 1: Analyze and Explore the Climate Data
-

This section uses Python (Pandas and Matplotlib) and SQLAlchemy ORM queries to do a basic climate analysis and data exploration

**Precipitation Analysis**

- The previous 12 months of precipitation data ("date" and "prcp" values) was collected

- Query results were loaded into Pandas DataFrame then plotted

**Station Analysis**

- The total number of stations in the dataset was calculated
  
- The most-active station was determined then the min, max, and average temperatures were calculated for this station

- A query was designed to get the previous 12 months of temperature observation (TOBS) data
  
- Query results were saved to a Pandas DataFrame then plotted into a histogram 

Part 2: Design Your Climate App
-

In this section, a Flask API was designed based on the developed queries 

**API Static Routes**

Precipitation route:
- Returns json with the date as the key and the value as the precipitation

A stations route:
- Returns jsonified data of all of the stations in the database

A tobs route:
- Returns jsonified data for the most active station 

**API Dynamic Route**

Start route:
- Accepts the start date as a parameter from the URL
- Returns the min, max, and average temperatures calculated from the given start date to the end of the dataset

Start/end route:
- Accepts the start and end dates as parameters from the URL
- Returns the min, max, and average temperatures calculated from the given start date to the given end date


