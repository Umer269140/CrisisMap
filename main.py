from flask import Flask, request, jsonify, render_template
import re
from openai import OpenAI
from flask_cors import CORS
import os
from geopy.geocoders import Nominatim

reports = []


os.environ["OPENAI_API_KEY"] = "sk-xx"
client = OpenAI()
app = Flask(__name__, template_folder='.', static_folder='.', static_url_path='')
import json
CORS(app, origins="*")



   
    


#api score, it collects the data, reports it to report route
@app.route('/api/score', methods=['POST'])
def score():
    data = request.get_json()
    user_message = data.get('message')
    location = data.get('location')
    user_name = data.get('name')

   #prompt for AI, model is nano, OpenAI
    prompt=f"""
         You are an emergency management assistant. Analyze the following form entry and generate a clean JSON output.
            
            Form Entries:
            - Reporter Name: {user_name}
            - Inputted Location: {location if location else 'Not specified'}
            - Emergency Situation: {user_message}

            Return ONLY a raw JSON object with these exact keys:
            {{
                "score": (number 1-5 evaluting severity),
                "location_english": "The inputted location or location details parsed from message in English",
                "location_urdu": "Translate the location name/details into clean Urdu script",
                "incident_english": "A brief summary of the incident in English",
                "incident_urdu": "Translate nthe brief incident summary of the incident into clean Urdu script ",
                "reason": "Categorize the hazard (e.g., Fire Outbreak, Medical Emegency, Road Accident)",
                "name": "The Reporter Name provided above"
                "coordinates": "Longitude and Latitude of Location"
                


            }}
            After obtaining location, convert that location into coordinates and present it.

            No markdown formatting, no backticks, no trailing text-just the raw JSON string.

        
        """


    response = client.responses.create(
        model="gpt-4.1-nano",
        input=prompt
        )   
  

    parsed = json.loads(response.output_text)
#So I have updated the fields in the report. I have added Longitude and Latitude because map.html needs it to drop the pin.
    reports.append({
        'message': user_message,
        'score': parsed['score'],
        'location_english': parsed['location_english'],
        'location_urdu': parsed['location_urdu'],
        'incident_english': parsed['incident_english'],
        'incident_urdu': parsed['incident_urdu'],
        'reason': parsed['reason'],
        'name': parsed['name'],
        'latitude': parsed.get('latitude', 24.8607),
        'longitude': parsed.get('longitude', 67.0011),
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

#This was suggested by AI for automatic reloading when detected change in terminal.
if __name__ == '__main__':
    app.run(debug=True)




    
         

