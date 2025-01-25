import json
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Function to load student data from the JSON file
def load_student_data():
    with open('data.json') as f:
        return json.load(f)

# Function to search for the student case-insensitively
def find_student_mark(name, student_data):
    # Normalize the name to lowercase to handle case insensitivity
    name_lower = name.lower()

    # Search for the name case-insensitively, but retain the original case from the JSON data
    for key in student_data.keys():
        if key.lower() == name_lower:  # Case-insensitive comparison
            return key, student_data[key]  # Return the original case and the mark
    
    return None, None  # If not found, return None

@app.route('/')
def welcome():
    return "Welcome All!"

# Single route that handles only query parameters to retrieve marks
@app.route('/api', methods=['GET'])
def get_marks():
    student_data = load_student_data()

    # Get the 'name' parameter from the query string
    name = request.args.get('name', '').strip()

    if not name:
        return jsonify({"error": "No student name provided"}), 400

    # Use the helper function to search for the student mark
    found_name, mark = find_student_mark(name, student_data)

    if found_name:
        return jsonify({found_name: mark})
    else:
        return jsonify({"error": f"Student '{name}' not found"}), 404

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
