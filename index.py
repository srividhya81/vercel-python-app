import json
from http.server import BaseHTTPRequestHandler

from flask import Flask,request
class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','application/json')
        self.end_headers()
        self.wfile.write(json.dumps({"message": "Hello!"}).encode('utf-8'))
        return

app = Flask(__name__)

with open('data.json', 'r') as file:
    data = json.load(file)
@app.route('/')
def home():
    return ('Hello welcome home')

@app.route('/api<name>', methods=['GET'])
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