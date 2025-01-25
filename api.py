# api.py
import json
from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # This enables CORS for all routes

# A mock database for marks associated with names
marks_db = [{
    "name": "HuhER",
    "marks": 92
  },
  {
    "name": "735ol4zsq",
    "marks": 53
  },
  {
    "name": "lXp26l1tY",
    "marks": 88
  },
  {
    "name": "ZMcdP",
    "marks": 1
  },
  {
    "name": "1ctsGHvIjV",
    "marks": 72
  },
  {
    "name": "XLklr",
    "marks": 56
  },
  {
    "name": "m",
    "marks": 7
  },
  {
    "name": "1LIYCHcd",
    "marks": 88
  },
  {
    "name": "L",
    "marks": 61
  },
  {
    "name": "sxdhoIFuH8",
    "marks": 98
  },
  {
    "name": "2",
    "marks": 27
  },
  {
    "name": "kT",
    "marks": 95
  },
  {
    "name": "LlRQtoD",
    "marks": 17
  },
  {
    "name": "fEkB",
    "marks": 40
  },
  {
    "name": "yoh",
    "marks": 10
  },
  {
    "name": "O9X",
    "marks": 61
  },
  {
    "name": "jD7vuBe",
    "marks": 25
  },
  {
    "name": "C",
    "marks": 9
  },
  {
    "name": "yg",
    "marks": 39
  },
  {
    "name": "ymWI",
    "marks": 74
  },
  {
    "name": "5woHfK",
    "marks": 60
  },
  {
    "name": "HtJvqlzHA",
    "marks": 24
  },
  {
    "name": "KnGBYv2kV",
    "marks": 92
  },
  {
    "name": "xS",
    "marks": 21
  },
  {
    "name": "E5EreM",
    "marks": 23
  },
  {
    "name": "dJ9F3AQi",
    "marks": 16
  },
  {
    "name": "BHMnL1C7d",
    "marks": 45
  },
  {
    "name": "MlHyJ2h6ZL",
    "marks": 74
  },
  {
    "name": "Rl1vsIvGe",
    "marks": 68
  },
  {
    "name": "M4kInc",
    "marks": 71
  },
  {
    "name": "f",
    "marks": 44
  },
  {
    "name": "rFFw22",
    "marks": 14
  },
  {
    "name": "TTwp8lbEO",
    "marks": 86
  },
  {
    "name": "e",
    "marks": 98
  },
  {
    "name": "Jz1",
    "marks": 64
  },
  {
    "name": "ggNDZdGC",
    "marks": 46
  },
  {
    "name": "SuMzG6oY1a",
    "marks": 55
  },
  {
    "name": "o5bf",
    "marks": 37
  },
  {
    "name": "SgWT",
    "marks": 48
  },
  {
    "name": "HGO",
    "marks": 68
  },
  {
    "name": "jMiINzZ",
    "marks": 50
  },
  {
    "name": "G",
    "marks": 70
  },
  {
    "name": "sC",
    "marks": 36
  },
  {
    "name": "nuuhLh",
    "marks": 26
  },
  {
    "name": "NGespllMa",
    "marks": 31
  },
  {
    "name": "8ugxc3q",
    "marks": 38
  },
  {
    "name": "dgR",
    "marks": 12
  },
  {
    "name": "pMZ",
    "marks": 70
  },
  {
    "name": "Gdc",
    "marks": 79
  },
  {
    "name": "HrWVWjY2B3",
    "marks": 94
  },
  {
    "name": "RN7tZ",
    "marks": 46
  },
  {
    "name": "BCXpUY41J",
    "marks": 27
  },
  {
    "name": "z58VF",
    "marks": 89
  },
  {
    "name": "b51GJtFWS",
    "marks": 79
  },
  {
    "name": "Rgx2Gz",
    "marks": 65
  },
  {
    "name": "loMCXu",
    "marks": 7
  },
  {
    "name": "Qt",
    "marks": 30
  },
  {
    "name": "yLjYuljVKS",
    "marks": 97
  },
  {
    "name": "hX",
    "marks": 64
  },
  {
    "name": "WfWIHdTAzc",
    "marks": 9
  },
  {
    "name": "Zn",
    "marks": 47
  },
  {
    "name": "sPMzBQ7",
    "marks": 26
  },
  {
    "name": "VEo0",
    "marks": 58
  },
  {
    "name": "GlOORZz",
    "marks": 56
  },
  {
    "name": "xlLPBHg",
    "marks": 22
  },
  {
    "name": "i1qQcltcJ",
    "marks": 6
  },
  {
    "name": "eAJQpQ38wm",
    "marks": 62
  },
  {
    "name": "7Xs",
    "marks": 19
  },
  {
    "name": "X",
    "marks": 2
  },
  {
    "name": "3ogqH",
    "marks": 48
  },
  {
    "name": "rB",
    "marks": 49
  },
  {
    "name": "TRgPRoiP",
    "marks": 16
  },
  {
    "name": "Ufyrh60lY",
    "marks": 97
  },
  {
    "name": "OZWf88",
    "marks": 71
  },
  {
    "name": "DXqDF",
    "marks": 21
  },
  {
    "name": "S7q8u7",
    "marks": 74
  },
  {
    "name": "yvAh5APV",
    "marks": 93
  },
  {
    "name": "rOQ1",
    "marks": 45
  },
  {
    "name": "zI0i5",
    "marks": 90
  },
  {
    "name": "SGuiXJ",
    "marks": 33
  },
  {
    "name": "4o7ZTcLNNw",
    "marks": 66
  },
  {
    "name": "iM9",
    "marks": 15
  },
  {
    "name": "ltst",
    "marks": 78
  },
  {
    "name": "X1DO",
    "marks": 29
  },
  {
    "name": "deMqBABJ",
    "marks": 0
  },
  {
    "name": "nosTpCu4",
    "marks": 32
  },
  {
    "name": "e0L",
    "marks": 68
  },
  {
    "name": "BvUXYmk",
    "marks": 23
  },
  {
    "name": "3J",
    "marks": 96
  },
  {
    "name": "gB",
    "marks": 33
  },
  {
    "name": "ku2",
    "marks": 45
  },
  {
    "name": "2",
    "marks": 93
  },
  {
    "name": "fQi5Y6MXR",
    "marks": 85
  },
  {
    "name": "ohwjqsKC3",
    "marks": 93
  },
  {
    "name": "WO4mGvFT",
    "marks": 64
  },
  {
    "name": "Wi",
    "marks": 40
  },
  {
    "name": "p3N",
    "marks": 66
  },
  {
    "name": "AE8DinF6",
    "marks": 79
  },
  {
    "name": "rctGZgNumX",
    "marks": 74
  },
  {
    "name": "qQm5LyFBsK",
    "marks": 41
  }]

@app.route('/api', methods=['GET'])
def get_marks():
    names = request.args.getlist('name')
    marks = [marks_db.get(name, "Not found") for name in names]
    return json.dumps({"marks": marks})

if __name__ == '__main__':
    app.run(debug=True)
