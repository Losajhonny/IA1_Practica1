from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin

app = Flask(__name__)
#cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
CORS(app)

@app.route('/')
def ini():
    return 'Bienvenido'

@app.route('/load', methods=['GET'])
@cross_origin()
def load():
    #data = request.json
    #print(data['id'])
    #return jsonify(data)
    return 'nada'

if __name__ == '__main__':
    app.run(debug=True, port=4000)