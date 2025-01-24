import json


from flask import Flask,request

app = Flask(__name__)

with open('data.json', 'r') as file:
    data = json.load(file)
@app.route('/')
def home():
    return 'Hello welcome home,enter your name get you marks'

@app.route('/<name>', methods=['GET'])
def get_marks():
    # Get the student's name from the query parameter
    student_name = request.args.get('name')
    
    if not student_name:
        return ({"error": "Please provide a student name."}), 400

    # Look up the student's marks
    marks = data.get(student_name)

    if marks is None:
        return ({"error": f"Student '{student_name}' not found."}), 404

    return ({"name": student_name, "marks": marks})


if __name__ == '__main__':
    app.run(debug=True)