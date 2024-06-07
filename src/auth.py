from flask import Blueprint, request, jsonify, json
# from src.database import mysql
from src.sqlQuery import MySqlQuery
from werkzeug.security import check_password_hash, generate_password_hash
from src.constants.http_status_codes import HTTP_400_BAD_REQUEST, HTTP_409_CONFLICT
import re
import datetime

auth = Blueprint("auth", __name__, url_prefix="/api/v2/auth")


@auth.post('/register')
def register():
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    email = request.json['email']
    password = request.json['password']
    name = request.json['name']

    if len(str(password)) < 4:
        return jsonify({'error': "Password can't be less than 4 character"}), HTTP_400_BAD_REQUEST

    if len(name) == 0:
        return jsonify({'error': "Name can't be blank"}), HTTP_400_BAD_REQUEST
    elif len(name) < 3:
        return jsonify({'error': "Name can't be so small"}), HTTP_400_BAD_REQUEST

    if not re.fullmatch(regex, email):
        return jsonify({'error': "Invalid Email"}), HTTP_400_BAD_REQUEST

    qdict = {'table': 'users', 'checkValue': email, 'type': 'email_check'}
    qResult = MySqlQuery()
    checkEmailExist = qResult.selQuery(qdict)
    if checkEmailExist == 1:
        return jsonify({'error': "User already registered."}), HTTP_409_CONFLICT
    else:
        pwd_hash = generate_password_hash(str(password))
        current_time = datetime.datetime.now()
        idict = {
            'insertVal': {'email': email, 'password': pwd_hash, 'name': name, 'status': 1, 'createon': current_time},
            'type': 'register'
        }
        insertID = qResult.selQuery(idict)
        if insertID > 0:
            return jsonify({'success': "User record successfully registered"})
        else:
            return jsonify({'error': "Server busy, try after some time."})


@auth.get("/me")
def user_me():
    return {'user': 'me'}
