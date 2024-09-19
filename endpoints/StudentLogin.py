from flask import request, Blueprint, jsonify
from model.database import db
from model.Login_db import StudentLogin

student_login_bp = Blueprint('student_login_bp', __name__)

@student_login_bp.route('/add/login', methods=['POST'])
def post_details():
    try:
        request_json = request.get_json()
        if 'username' not in request_json or 'password' not in request_json:
            return jsonify({'error': 'Missing username or password'}), 400
        
        new_data = StudentLogin(**request_json)
        db.session.add(new_data)
        db.session.commit()
        return jsonify({'message': 'Login details added successfully!'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500
