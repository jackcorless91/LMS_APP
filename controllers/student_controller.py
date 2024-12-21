from flask import Blueprint, request
from sqlalchemy.exc import IntegrityError
from psycopg2 import errorcodes

from init import db, ma
from models.student import Student, students_schema, Student_schema


students_bp = Blueprint("students", __name__, url_prefix="/students")


#  read all - /students - GET
@students_bp.route("/")
def get_students():
  stmt = db.select(Student)
  students_list = db.session.scalars(stmt)
  data = students_schema.dump(students_list)
  # plural
  return data


# Read one - /students/id - GET
@students_bp.route("/<int:student_id>")
def get_student(student_id):
  # student id pararmeter dynamic routing
  stmt = db.select(Student).filter_by(id=student_id)
  student = db.session.scalar(stmt)
  if student:
    data = Student_schema.dump(student)
    return data
  else:
    return {"message": f"Student with id {student_id} does not exist"}, 404
 #  scalar not scalars, single student_id



#  Create - /students - POST
@students_bp.route("/", methods=["POST"])
def create_student():
  try:
    # get information from request body
    body_data = request.get_json()
    # create student instance 
    new_student = Student(
      name=body_data.get("name"),
      email=body_data.get("email"),
      address=body_data.get("address")
    )
    # add to the session 
    db.session.add(new_student)
    # commit
    db.session.commit()
    # return a response
    return Student_schema.dump(new_student), 201
  except IntegrityError as err:
    print(err.orig.pgcode)
    if err.orig.pgcode == errorcodes.NOT_NULL_VIOLATION:
      # not null violation
      return {"message": f"The field {err.orig.diag.column_name} is required"}, 409
    if err.orig.pgcode == errorcodes.UNIQUE_VIOLATION:
      # unique constraint violation
      return {"message": "Email address already in use"}, 409
    

# DELETE - /students/id - DELETE
@students_bp.route("/<int:student_id>", methods=["DELETE"])
def delete_student(student_id):
  # find the student to be deleted using id 
  stmt = db.select(Student).filter_by(id=student_id)
  student = db.session.scalar(stmt)
  # if student exists
  if student:
    # delete
    db.session.delete(student)
    db.session.commit()
    # return a response
    return {"message": f"Student {student_id} deleted successfully"}
  else:
    return {"message": f"Student with id {student_id} does not exist"}, 404
