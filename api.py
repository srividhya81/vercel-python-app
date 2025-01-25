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

        # Prepare the response dictionary
    result = {}

    # For each name, check if it exists in the database (case-insensitive)
    for name in names_list:
        name_lower = name.lower()  # Convert the input name to lowercase
        mark = student_data.get(name_lower, "Not found")  # Get the mark or 'Not found'
        result[name] = mark  # Return name as it was entered with the corresponding mark

    # Return the result as a JSON object
    return json.dumps(result)

if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0")
