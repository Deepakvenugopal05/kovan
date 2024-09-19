from model.database import db
class StudentLogin(db.Model):
    __tablename__ = 'student_login'
    login_id = db.Column(db.Integer,primary_key=True,nullable=False)
    user_name = db.Column(db.String(20),unique=True,nullable=False)
    password = db.Column(db.String(20),nullable=False)
    student_id = db.Column(db.Integer, db.ForeignKey('student.student_id'))

    def to_dict(self):
        return {
            "login_id":self.login_id,
            "user_name": self.user_name,
            "password" : self.password,
            "student_id" : self.student_id
        }