from init import db

class Student(db.model):
  __tablename__ = "students"

  id = db.column(db.Integer, primary_key=True)

  name = db.column(db.String(100), nullable=False)
  email = db.column(db.String(100), nullable=True, unique=True)
  address = db.column(db.String(100))


class StudentSchema(ma.Schema):
  class Meta:
    fields = ("id", "name", "email", "address")
  
student_schema = StudentSchema(many=True)