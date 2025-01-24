import json,jsonify
from http.server import BaseHTTPRequestHandler

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','application/json')
        self.end_headers()
        self.wfile.write(json.dumps({"message": "Hello!"}).encode('utf-8'))
        return
    
from fastapi.middleware.cors import CORSMiddleware

from flask import Flask,request

app = Flask(__name__)
app.add_middleware(CORSMiddleware, allow_origins=["*"]) # Allow GET requests from all origins
# Or, provide more granular control:
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://example.com"],  # Allow a specific domain
    allow_credentials=True,  # Allow cookies
    allow_methods=["GET", "POST", "PUT", "DELETE"],  # Allow specific methods
    allow_headers=["*"],  # Allow all headers
)

with open('data.json', 'r') as file:
    data = json.load(file)
@app.route('/')
def home():
    return 'Hello welcome home'

@app.route('/get-marks', methods=['GET'])
def get_marks():
    # Get the student's name from the query parameter
    student_name = request.args.get('name')
    
    if not student_name:
        return jsonify({"error": "Please provide a student name."}), 400

    # Look up the student's marks
    marks = data.get(student_name)

    if marks is None:
        return jsonify({"error": f"Student '{student_name}' not found."}), 404

    return jsonify({"name": student_name, "marks": marks})

if __name__ == '__main__':
    app.run(debug=True)