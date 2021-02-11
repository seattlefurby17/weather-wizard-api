import requests
import os
from flask import Flask, request, render_template
from flask_cors import CORS, cross_origin
from dotenv import load_dotenv
load_dotenv()
str_api_key = os.getenv('API_KEY')
str_base_url = 'https://api.openweathermap.org/data/2.5/'

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/temperature', methods=['GET'])
@cross_origin()
def temperature():
  str_current_city = requests.args.get('Current city')
  r = requests.get(str_base_url + 'weather?q='+str_current_city+'&units=imperial&appid='+str_api_key+'')
  return r.json()

@app.route('/forecast', methods=['GET'])
@cross_origin()
def forecast():
  str_current_city = requests.args.get('Current city')
  r = requests.get(str_base_url + 'forecast?q='+str_current_city+'&units=imperial&appid='+str_api_key+'')
  return r.json()

if __name__ == '__main__':
  app.run(debug=True)