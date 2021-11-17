"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure

app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

# create the jackson family object
jackson_family = FamilyStructure("Jackson")

jackson_family.add_member({"first_name": "John","age": 33,"lucky_numbers": [7, 13, 22]})
jackson_family.add_member({"first_name": "Jane","age": 35,"lucky_numbers": [10, 14, 3]})
jackson_family.add_member({"first_name": "Jimmy","age": 5,"lucky_numbers": [1]})

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/members', methods=['GET'])
def get_members():
    if request.method != 'GET':
        return "Bad method", 400
    
    members = jackson_family.get_all_members()
    return jsonify(members), 200

@app.route('/member', methods=['POST'])
def add_new_member():
    body = request.json
    jackson_family.add_member(body)

    return jsonify("todo ok"), 200

@app.route('/member/<int:member_id>', methods=['GET'])
def get_member(member_id):
    member = jackson_family.get_member(member_id)
    return jsonify(member)

@app.route('/member/<int:member_id>', methods=['DELETE'])
def remove_member(member_id):
    msg = jackson_family.delete_member(member_id)
    output = {
        'done': True,
        'msg': msg
    }
    return jsonify(output)


# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)
