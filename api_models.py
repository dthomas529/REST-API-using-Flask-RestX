from flask_restx import fields
from .extensions import api

students_model = api.model('Student', {
"id": fields.Integer,
"name": fields.String,
"course": fields.nested(course.model)
})

course_model = api.model('Course', {
"id": fields.Integer,
"name": fields.String,
  "students": fields.List(fields.nested(student_model))
})

course_input_model = api.model("CourseInput", {
  "name": fields.String
})

student_input_model = api.model("StudentInput", {
  "name": fields.String,
  "course_id": fields.Integar
})
