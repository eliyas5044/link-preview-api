from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from pyunfurl import unfurl

app = Flask(__name__)
cors = CORS(app)
app.config["DEBUG"] = True
app.config['CORS_HEADERS'] = 'Content-Type'

@app.get('/')
@cross_origin()
def home():
  
  # check if url in arg
  if 'url' in request.args:
    url = str(request.args['url'])

    res = unfurl(url)
  else:
    return "Error: No url field provided. Please specify url."
  
  return jsonify(res)

app.run()
