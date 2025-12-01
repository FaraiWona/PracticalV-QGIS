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

@app.route("/")
def index():
    return render_template("map.html")

app.route("/search")
def search():
    amenity = request.args.get("amenity", "").lower()
    user_lat = request.args.get("user_lat", type=float)
    user_lon = request.args.get("user_lon", type=float)

     if not amenity or user_lat is None or user_lon is None:
        return jsonify([])

    conn = connect_db()
    cur = conn.cursor()

    # Fetch facilities from your table
    cur.execute("""
        SELECT name, amenity,
               ST_Y(geom) AS lat,
               ST_X(geom) AS lon
        FROM hotosm_mwi_health_facilities_points_shp
        WHERE LOWER(amenity) = %s;
    """, (amenity,))

    
    rows = cur.fetchall()
    conn.close()