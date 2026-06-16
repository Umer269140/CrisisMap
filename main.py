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

   CRISIS_ANALYSIS_INSTRUCTIONS = """
            You are a disaster response classification engine.

            Analyze emergency reports and return structured data.

            Required fields:
            - severity_level
            - emergency_category
            - recommended_action
            - confidence_score


            Return ONLY a valid JSON object.
            Do not include markdown.
            Do not include explanations.
            Do not add extra keys.
            """


    response = client.responses.create(
        model="gpt-4.1-nano",
        input=CRISIS_ANALYSIS_INSTRUCTIONS
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




    
         

