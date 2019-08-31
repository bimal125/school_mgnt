import json
from django.urls import reverse
from rest_framework.test import APITestCase
from schools.models import School
from students.models import Student

class TestStudentViewTestCase(APITestCase):

    url = '/api/v1/students/'

    def setUp(self):
        self.fname = "Bimal"
        self.lname = "Pandey"
        self.roll_no = 12
        self.name = "Radiant Science Campus"
        self.max_students = 200
        self.school = School.objects.create(
                              name       = self.name,
                              max_students     = self.max_students,
                            )
        self.student = Student.objects.create(
                              fname  = self.fname,
                              lname  = self.lname,
                              roll_no   = self.roll_no,
                              school = self.school
                            )
                            
    def test_can_list_all_students(self):
        response = self.client.get(self.url)
        self.assertTrue(200 == response.status_code)

    def test_can_create_student(self):
      response = self.client.post(self.url, {
            "fname" : "John",
            "lname" : "Doe",
            "roll_no" : 100,
            "school": self.school.pk
            })
      self.assertEqual(201, response.status_code)

    def test_can_get_student(self):
        url = self.url+str(self.student.id)+'/'
        response = self.client.get(url)
        self.assertTrue(200 == response.status_code)

    def test_can_update_student(self):
        url = self.url+str(self.student.id)+'/'
        response = self.client.put(url, {
          "fname": "updated fname",
          "lname": "updated lname",
          "school":self.school.pk,
          "roll_no": 122
          })
        response_data = json.loads(response.content)
        self.assertEqual("updated fname", response_data.get("fname"))
        self.assertEqual("updated lname", response_data.get("lname"))
        self.assertEqual(self.school.pk, response_data.get("school"))

    def test_can_partial_update_school(self):
        url = self.url+str(self.student.id)+'/'
        response = self.client.patch(url, {
          "fname": "updated fname",
          "lname": "updated lname",
          "school":self.school.pk,
          "roll_no": 122
          })
        response_data = json.loads(response.content)
        self.assertEqual("updated fname", response_data.get("fname"))
        self.assertEqual("updated lname", response_data.get("lname"))
        self.assertEqual(self.school.pk, response_data.get("school"))


    def test_can_delete_school(self):
        url = self.url+str(self.student.id)+'/'
        response = self.client.delete(url)
        self.assertEqual(204, response.status_code)





