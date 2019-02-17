from flask import Flask, request
from flaskext.mysql import MySQL


app = Flask(__name__)

mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'quality'
app.config['MYSQL_DATABASE_PASSWORD'] = 'fruit'
app.config['MYSQL_DATABASE_DB'] = 'qualitydata'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

conn = mysql.connect()
cursor = conn.cursor()

@app.route('/')
def entry_point():
    return 'Hello World!'

@app.route('/input',methods = ['GET','POST'])
def input():
      unitID = request.args.get('id');
	  temperature = request.args.get('t')
      pressure = request.args.get('p')
      humidity = request.args.get('h')
      gas = request.args.get('gas')
      lat = request.args.get('lat')
	  lon = request.args.get('lon')
	  vibration = request.args.get('vib')
	  if(lat < 1 and lat > -1 ):
		lat = 45.382476
		lon = -75.696632
      
	  query = 'INSERT INTO records ( unitid, temperature,pressure, humidity, gas, latitude, longitude, vibration ) VALUES ({},{},{},{},{},{},{},{});'.format(unitID,temperature,pressure,humidity,gas, lat, lon, vibration)
      cursor.execute(query) 
      conn.commit() 
      return query
	  
	
if __name__ == '__main__':
	app.run(host='0.0.0.0', port=1900)