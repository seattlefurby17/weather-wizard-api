import requests
import os
from flask import Flask, request, render_template
from flask_cors import CORS, cross_origin
from dotenv import load_dotenv
load_dotenv()
api_key = os.getenv('API_KEY')
base_url = 'https://api.openweathermap.org/data/2.5/'