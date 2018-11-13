# importing dependencies

import datetime as dt
import numpy as np
import pandas as pd
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy import create_engine, func
from flask import Flask, jsonify


#database setup

engine = create_engine("sqlite:///hawaii.sqlite")
Base = automap_base()
Base.prepare(engine, reflect = True)

#saving reference to the table

Base.classes.keys()

Measurement = Base.classes.Measurement