from flask import Flask, render_template, request, redirect, url_for
import requests
import io
from google.cloud import vision
from google.oauth2 import service_account
from werkzeug.utils import secure_filename
import os
from datetime import datetime

app = Flask(__name__)

# Specify the path to your service account key
CREDENTIALS = service_account.Credentials.from_service_account_file('/home/sahith-siddarth/Desktop/evolumin/Farmers/evolumin-439901-5ad3692754d2.json')

# Initialize the Vision API client
vision_client = vision.ImageAnnotatorClient(credentials=CREDENTIALS)

# Set the folder to store uploaded images
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure the upload folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Allowed extensions for image files
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.template_filter('unix_to_date')
def unix_to_date(timestamp):
    return datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d')

# Sample data for market prices
prices = {
    'Rice': 2000,
    'Wheat': 1500,
    'Sugar': 2500,
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/weather', methods=['GET'])
def weather():
    city = request.args.get('city', 'London')
    current_weather_data = get_current_weather_data(city)
    forecast_data = get_weather_forecast(city)

    if current_weather_data and 'main' in current_weather_data:
        return render_template('weather.html', current_weather=current_weather_data, forecast=forecast_data)
    else:
        return render_template('weather.html', current_weather=None, forecast=None)

def get_current_weather_data(city):
    api_key = 'e4e4415452b1d3cdb9ef931825ccc876'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    response = requests.get(url)
    return response.json() if response.status_code == 200 else None

def get_weather_forecast(city):
    api_key = 'e4e4415452b1d3cdb9ef931825ccc876'
    url = f'http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=metric&cnt=3'
    response = requests.get(url)
    return response.json() if response.status_code == 200 else None

@app.route('/upload', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        return redirect(request.url)

    file = request.files['file']
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)

        labels = analyze_image(filepath)
        return render_template('index.html', labels=labels, uploaded_image=filepath)

    return redirect(url_for('home'))

def analyze_image(image_path):
    with io.open(image_path, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)
    response = vision_client.label_detection(image=image)
    
    if response.error.message:
        raise Exception(f'{response.error.message}')

    labels = response.label_annotations
    return [label.description for label in labels]



# Corrected route for the pest management page
@app.route('/pest')
def pest():
    return render_template('pest.html')
@app.route('/marketprice')
    
def marketprice():
    return render_template('marketprice.html')

if __name__ == '__main__':
    app.run(debug=True)

