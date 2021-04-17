import requests
import configparser
from flask import Flask

app = Flask(__name__)

@app.route('/')
def weather_deshboard():
  return "Hello World"

@app.route('/results')
def render_results():
  return "Results Page"

if __name__ == '__main__':
  app.run()



def get_api_key():
  config = configparser.ConfigParser()
  config.read('config.ini')
  return config['openweathermap']['api']


def get_weather_results(zip_code, api_key):
  api_url = "http://api.openweathermap.org/data/2.5/weather?zip={}&appid={}".format(zip_code, api_key)
  r = requests.get(api_url)
  return r.json()

print(get_weather_results("94040",get_api_key()))