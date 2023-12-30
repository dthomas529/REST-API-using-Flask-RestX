from flask-restx import Resource, Namespace

from .api_models import course_models, student_models
from .models import Course

ns = Namespace("api")

@ns.route("/hello")
class Hello(Resource):
  def get(self):
    return {"hello": "rest-x"}
    
@ns.route("/courses")
class CourseAPI(Resource):
  @ns.marshal_list_with(course_models)
  def get(self):
    return Course.query.all()

@ns.route("/students")
class StudentAPI(Resource):
  @ns.marshal_list_with(_models)
  def get(self):
    return Student.query.all()