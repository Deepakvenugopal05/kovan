from model.database import db
class Student(db.Model):
    student_id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String,nullable = False)
    age = db.Column(db.Integer,nullable = False)
    students = db.relationship('StudentLogin',backref='student',lazy=True)

    def to_dict(self):
        return {
            'student_id': self.student_id,
            'name' : self.name,
            'age': self.age
        }

    def __repr__(self):
        return f"'student_id':{self.student_id},'name':{self.name},'age':{self.age}"
    