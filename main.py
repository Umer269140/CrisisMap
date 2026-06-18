from flask import Flask, request, jsonify, render_template
import re
from openai import OpenAI
from flask_cors import CORS
import os
from geopy.geocoders import Nominatim

reports = []


client = OpenAI()
geolocator = Nominatim(user_agent="crisismap")
app = Flask(__name__, template_folder='.', static_folder='.', static_url_path='')
import json
CORS(app, origins="*")



# if geocoding fails (no internet) we fall back!
def get_coordinates(place_name):
    try:
        location = geolocator.geocode(place_name, timeout=5, country_codes='pk')
        print(f"Geocoding '{place_name}' -> {location}")
        if location:
            return location.latitude, location.longitude
    except Exception as e:
        print("geocoding failed:", e)
    return 24.8607, 67.0011 
    


#api score, it collects the data, reports it to report route
@app.route('/api/score', methods=['POST'])
def score():
    data = request.get_json()
    user_message = data.get('message')
    location = data.get('location')
    user_name = data.get('name')
  

   
         

    CRISIS_ANALYSIS_INSTRUCTIONS = """
            You are a disaster response classification engine.

            Analyze emergency reports and return structured data.

            Required fields:
           - message (string)
           - score (integer from 1 to 5)
           - location_english (string)
           - incident_english (string)
           - reason (string)
           - name (string)
           - latitude (float)
           - longitude (float)
           


            Return ONLY a valid JSON object.
            Do not include markdown.
            Do not include explanations.
            Do not add extra keys.
            """


    response = client.responses.create(
        model="gpt-4.1-nano",
        instructions=CRISIS_ANALYSIS_INSTRUCTIONS,
        input=f"Report message: {user_message}\nReported location: {location}\nReporter name: {user_name}"
        )   
  

    try:
        crisis_analyses = json.loads(response.output_text)
    except json.JSONDecodeError:
         print("Model didn't return valid JSON:", response.output_text)
         return jsonify({'error': 'Could not process this report. Please try again.'}), 500
    lat, lon = get_coordinates(crisis_analyses.get('location_english'))
#So I have updated the fields in the report. I have added Longitude and Latitude because map.html needs it to drop the pin.
    reports.append({
        'message':  user_message,
        'score': crisis_analyses.get('score'),
        'location_english': crisis_analyses.get('location_english'),
        'incident_english': crisis_analyses.get('incident_english'),
        'reason': crisis_analyses.get('reason'),
        'name': crisis_analyses.get('name'),
        'latitude': lat,
        'longitude': lon,
       
    })
    
    print(response.output_text)
    return jsonify({'reply': response.output_text})








#this is the report route, so I rendered it on report.html
@app.route('/reports')
def report_page():
    return render_template('report.html')



#this is original route, i have created it long before rendering it to report.html.
@app.route('/api/reports', methods=['GET'])
def get_reports():
    return jsonify(reports)

@app.route('/')
def home():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")




    
         

