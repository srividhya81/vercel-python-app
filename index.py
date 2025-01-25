from flask import Flask, request, jsonify
from flask_cors import CORS
import json
from http.server import BaseHTTPRequestHandler
from asgiref.wsgi import WsgiToAsgi  # ASGI wrapper for Flask
class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','application/json')
        self.end_headers()
        self.wfile.write(json.dumps({"message": "Hello!"}).encode('utf-8'))
        return
app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

def load_data():
    with open('data.json', 'r') as file:  # Replace 'data.json' with your JSON file path
        return json.load(file)

@app.route('/api', methods=['GET'])
def get_marks():
    # Retrieve 'name' query parameters from the request
    names = request.args.getlist('name')

    if not names:
        return jsonify({"error": "At least one 'name' parameter is required."}), 400

    try:
        # Load data from JSON file
        data = load_data()

        # Fetch marks for the given names
        marks = [item['marks'] for item in data if item['name'] in names]

        return jsonify({"name": names},{"marks": marks})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

asgi_app = WsgiToAsgi(app)
#if __name__ == '__main__':
 #   app.run(debug=True,port=8000)