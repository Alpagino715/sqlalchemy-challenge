#################################################
# Dependencies Setup
#################################################

import datetime as dt

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

#################################################
# Database Setup
#################################################

# --- create engine using the `hawaii.sqlite` database file ---
engine = create_engine('sqlite:///Resources/hawaii.sqlite')

# --- reflect an existing database into a new model ---
Base = automap_base()

# --- reflect the tables ---
Base.prepare(engine, reflect=True)

# --- save references to the tables ---
measurement = Base.classes.measurement
station = Base.classes.station

#################################################
# Flask Setup
#################################################

# --- create an instance of the Flask class ---
app = Flask(__name__)

#################################################
# --- Flask Routes ---
#################################################

@app.route("/")
def home():
    print("Server requested climate app home page...")
    return (

        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/start<br/>"
        f"/api/v1.0/start/end<br/>"
    )
@app.route("/api/v1.0/precipitation")
def precipitation():
    session = Session(engine)

    prcp_data = session.query(measurement.date, measurement.prcp).all()

    session.close()

    prcp_dict = {}
    for date, prcp in prcp_data:
        prcp_dict[date] = prcp

    return jsonify(prcp_dict)

if __name__ == "__main__":
    app.run(debug=True)
