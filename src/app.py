"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

# create the jackson family object
jackson_family = FamilyStructure("Jackson")



# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/members', methods=['GET'])
def handle_hello():
    
    # this is how you can use the Family datastructure by calling its methods
    members = jackson_family.get_all_members()
    response_body = {
        "hello": "world",
        "family": members
    }

    return jsonify(response_body), 200  


@app.route("/member", methods=['POST'])
def add_members():
    body = request.json
    success = jackson_family.add_member(body)
    if success == True:
        return jsonify({"msg":"creado con exito"}), 201
    return jsonify(success), 400



@app.route("/member/<int:member_id>", methods=['DELETE'])
def delete_members(member_id):
    success = jackson_family.delete_member(member_id)
    if success == True:
        return jsonify({"msg":"eliminado con exito"}), 200
    return jsonify({"msg":f"no se encontro el miembro con el id {member_id}"}), 400



@app.route("/member/<int:member_id>", methods=['GET'])
def get_member(member_id):
    success = jackson_family.get_member(member_id)
    if success:
        return jsonify(success), 200
    return jsonify({"msg":f"no se encontro el miembro con el id {member_id}"}), 400

@app.route("/member/<int:member_id>", methods=['PUT'])
def edit_members(id):
    body = request.json
    if "last_name" in body:
        success = jackson_family.edit_member(id, body["last_name"])
        if success == True:
            return jsonify({"msg":"editado con exito"}), 200
        return jsonify({"msg":f"no se encontro el miembro con el id {id}"}), 400
    return jsonify({"msg":"last_name no esta en el body"}), 400








# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)
