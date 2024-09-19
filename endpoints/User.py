from flask import jsonify, request, Blueprint
from model.database import db
from model.User_db import Student

student_bp = Blueprint('student_bp', __name__)

@student_bp.route('/get', defaults={'age': None}, methods=['GET'])
@student_bp.route('/get/<int:age>', methods=['GET'])
def get_details(age):
    try:
        data = Student.query.all()
        if age is not None:
            return jsonify([user.to_dict() for user in data if user.age <= age]), 200
        return jsonify([i.to_dict() for i in data]), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@student_bp.route('/get_specific/<int:std_id>', methods=['GET'])
def get_specific_details(std_id):
    try:
        data = Student.query.get(std_id)
        if data:
            return jsonify(data.to_dict()), 200
        return jsonify({'error': f'No details for ID {std_id}'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@student_bp.route('/add', methods=['POST'])
def add_details():
    try:
        request_json = request.get_json()
        if 'name' not in request_json:
            return jsonify({'error': 'No Name is given'}), 400
        if 'student_id' not in request_json:
            return jsonify({'error': 'No ID is given'}), 400
        if 'age' not in request_json:
            return jsonify({'error': 'No Age is given'}), 400
        add_data = Student(**request_json)
        db.session.add(add_data)
        db.session.commit()
        return jsonify({'message': f"{request_json} is added!"}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@student_bp.route('/update_details/<int:std_id>', methods=['PATCH'])
def update_details(std_id):
    try:
        data = Student.query.get(std_id)
        if data:
            request_json = request.get_json()
            if 'name' in request_json:
                data.name = request_json['name']
            if 'age' in request_json:
                data.age = request_json['age']
            db.session.commit()
            return jsonify({'message': f'{request_json} is updated!'}), 200
        return jsonify({'error': f'No ID {std_id} found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@student_bp.route('/delete/<int:std_id>', methods=['DELETE'])
def delete_specific(std_id):
    try:
        data = Student.query.get(std_id)
        if data:
            db.session.delete(data)
            db.session.commit()
            return jsonify({'message': 'Deleted successfully'}), 200
        return jsonify({'error': 'Invalid student ID given'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    

"""
# Using Query string filter data of AGE
# INPUT: http://127.0.0.1:5000/get?min_age=10&max_age=25&sort=desc
@app.route('/get',methods=['GET'])
def get_details():
    try:
        data = Student.query.all()
        min_age = request.args.get('min_age',type=int)
        max_age = request.args.get('max_age',type=int)
        sort = request.args.get('sort')
        if min_age :
            query = Student.query
            if min_age:
                query = Student.query.filter(Student.age >= min_age)
            if max_age:
                query = Student.query.filter(Student.age <= max_age)
            if sort == 'desc':
                query = query.order_by(Student.age.desc())
            users = query.all()
            return jsonify([i.to_dict() for i in users])
        
        return jsonify([i.to_dict() for i in data]),200
    except Exception as e:
        return str(e),500
"""
