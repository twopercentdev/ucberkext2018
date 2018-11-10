import numpy as np
import pandas as pd

from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from flask import Flask, jsonify
from datetime import datetime as dt

import datetime

engine = create_engine("sqlite:///hawaii.sqlite", connect_args={'check_same_thread': False})
Base = automap_base()
Base.prepare(engine, reflect=True)
Measurement = Base.classes.measurement
Station = Base.classes.station
session = Session(engine)
app = Flask(__name__)

oneYearAgo = dt.now() - datetime.timedelta(days=2 * 365)


@app.route('/')
def landing():
    return (
        'Climate App API ver 1.0<br/>'
        'Available Routes:<br/>'
        '/api/v1.0/precipitation<br/>'
        '/api/v1.0/stations<br/>'
        '/api/v1.0/tobs<br/>'
        '/api/v1.0/&lt;start&gt;<br/>'
        '/api/v1.0/&lt;start&gt;/&lt;end&gt;'
    )


@app.route('/api/v1.0/precipitation')
def precipitation_df():
    results = pd.DataFrame(session.query(Measurement.date, Measurement.prcp)
                           .filter(Measurement.date >= oneYearAgo)
                           .all()).set_index('date')

    return jsonify(results.to_dict())


@app.route('/api/v1.0/stations')
def station_list():
    results = session.query(Station.name)

    all_names = list(np.ravel(results))

    return jsonify(all_names)


@app.route('/api/v1.0/tobs')
def tobs_df():
    results = pd.DataFrame(session.query(Measurement.date, Measurement.tobs)
                           .filter(Measurement.date >= oneYearAgo)
                           .all()).set_index('date')

    return jsonify(results.to_dict())


@app.route('/api/v1.0/<start>')
def start_calcs(start):
    results = pd.DataFrame(session.query(Measurement.date, Measurement.tobs)
                           .filter(Measurement.date >= start)
                           .all()).set_index('date')

    return jsonify(
        {'min temp': results['tobs'].min(), 'ave temp': results['tobs'].mean(), 'max temp': results['tobs'].max()})


@app.route('/api/v1.0/<start>/<end>')
def startend_calcs(start, end):
    results = pd.DataFrame(session.query(Measurement.date, Measurement.tobs)
                           .filter(Measurement.date >= start)
                           .filter(Measurement.date <= end)
                           .all()).set_index('date')

    return jsonify(
        {'TMIN': results['tobs'].min(), 'TAVG': results['tobs'].mean(), 'TMAX': results['tobs'].max()})


if __name__ == '__main__':
    app.run()
