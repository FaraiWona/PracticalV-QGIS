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