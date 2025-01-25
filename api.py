# api.py
import json
from flask import Flask, request
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

@app.route('/api/<names>', methods=['GET'])
def get_marks():
    # Load student data
    student_data = load_student_data()


    # Get list of 'name' parameters from the query
    names = request.args.getlist('names')
     # Split the comma-separated names in the path (e.g., 'X,Y' -> ['X', 'Y'])
    names_list = names.split(',')

    # Fetch the marks for each name, return 'Not found' if not in the database
    marks = [student_data.get(name, "Not found") for name in names_list]

    # Return the marks in JSON format
    return json.dumps({"marks": marks})


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0")
