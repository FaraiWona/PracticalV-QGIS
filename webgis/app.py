from flask import Flask, jsonify, render_template, request
import psycopg2
import math

app = Flask(__name__)

conn_params = dict(
    dbname="Hospita_GIS",
    user="postgres",
    password="Pedri123",
    host="localhost",
    port="5432"
)

ef connect_db():
    return psycopg2.connect(**conn_params)

def distance_km(lat1, lon1, lat2, lon2):

     R = 6371
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = (math.sin(dlat/2)**2 +
         math.cos(math.radians(lat1)) *
         math.cos(math.radians(lat2)) *
         math.sin(dlon/2)**2)
    return round(R * (2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))), 2)