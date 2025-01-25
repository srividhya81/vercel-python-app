# api.py
import json
from flask import Flask, request,jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # This enables CORS for all routes


@app.route('/')
def welcome():
    return "Welcome All!"

@app.route('/api')
def hello():
    return "Hello Students, Enter your name and see your marks"

def load_student_data():
    with open('data.json') as f:
        return json.load(f)
@app.route('/api',methods = ['GET'])
def get_queries():
       # Load student data from JSON database
    student_data = load_student_data()

    # Get the 'name' parameter from the query string (case-insensitive)
    name = request.args.get('name', '').strip()

    # Normalize the name to lowercase to handle case insensitivity
    name_lower = name.lower()

    # Check if the name exists in the database (case-insensitive)
    mark = student_data.get(name_lower, "Not found")

    # Return the result as a JSON response
    if mark == "Not found":
        return jsonify({"error": f"Student '{name}' not found"}), 404
    else:
        return jsonify({name: mark})
@app.route('/api/<names>', methods=['GET'])
def get_marks():
    # Load student data
    student_data = load_student_data()


  
 # Get the 'name' parameter from the query string (case-insensitive)
    name = request.args.get('name', '').strip()

    # Normalize the input name to lowercase to handle case insensitivity
    name_lower = name.lower()

    # Search for the name case-insensitively, but retain the original case from the JSON data
    found_name = None
    for key in student_data.keys():
        if key.lower() == name_lower:  # Case-insensitive comparison
            found_name = key  # Store the name in the original case
            break

    # If a match is found, return the mark, otherwise, return a "Not found" message
    if found_name:
        mark = student_data[found_name]  # Get the mark for the found name
        return jsonify({found_name: mark})
    else:
        return jsonify({"error": f"Student '{name}' not found"}), 404

if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0")
