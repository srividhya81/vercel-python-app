import json
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all origins

# Load the student data from the JSON file
with open('students.json') as f:
    student_data = json.load(f)

# Create a dictionary for fast lookup by name
student_dict = {student['name']: student['marks'] for student in student_data['students']}

@app.route('/api', methods=['GET'])
def get_marks():
    names = request.args.getlist('name')
    marks = [student_dict.get(name, "Not Found") for name in names]
    return jsonify({"marks": marks})

if __name__ == '__main__':
    app.run(debug=True)
