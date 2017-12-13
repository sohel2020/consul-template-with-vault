import os , sys
from flask import Flask
from flask import render_template
import psycopg2

d = {}

PORT=8080

with open('env') as file:
    for line in file:
        if line.strip():
            conf = line.split('=', 1)
            d[conf[0].strip()] = conf[1].strip()

def create_connection():
    try:
        connect_str = "host={} dbname={} user={} password={}".format(d["DB_HOST"], d["DB_DATABASE"], d["DB_USERNAME"], d["DB_PASSWORD"])
        return psycopg2.connect(connect_str)
    except:
        raise
        sys.exit("DB connection Error")

app = Flask(__name__)
app.debug = True

@app.route('/')
def index():
    connection = create_connection()
    if connection:
        # user = {'username': 'Miguel'}
        return '''
            <html>
                <head>
                    <title>VAULT Home Page</title>
                </head>
                <body>
                    <h2><center>VAULT Demo Appliation</center></h2>
                    <hr>
                    <p><b>Database EndPoint:</b> ''' + d['DB_HOST'] + '''</p>
                    <p><b>Database Port:</b> ''' + d['DB_PORT'] + '''</p>
                    <p><b>Database Name:</b> ''' + d['DB_DATABASE'] + '''</p>
                    <p><b>Database Username:</b> ''' + d['DB_USERNAME'] + '''</p>
                    <p><b>Database Password:</b> ''' + d['DB_PASSWORD'] + '''</p>
                </body>
            </html>'''
    connection.close()

app.run(host="0.0.0.0", port=PORT)    
