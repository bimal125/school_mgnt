import json
from django.urls import reverse
from rest_framework.test import APITestCase
from schools.models import School
from schools.serializers.SchoolSerializer import SchoolSerializer


class TestSchoolViewTestCase(APITestCase):

    url = '/api/v1/schools/'

    def setUp(self):
        self.name = "Radiant Science Campus"
        self.max_students = 200
        self.school = School.objects.create(
                              name       = self.name,
                              max_students     = self.max_students,
                            )
    def test_can_create_school(self):
        response = self.client.post(self.url, {
            "name" : "Amrit Science Campus",
            "max_students" : 100,
            })
        self.assertEqual(201, response.status_code)

    def test_can_get_school(self):
        url = self.url+str(self.school.id)+'/'
        response = self.client.get(self.url)
        self.assertTrue(200 == response.status_code)

    def test_can_update_school(self):
        url = self.url+str(self.school.id)+'/'
        response = self.client.put(url, {"name": "updated school"})
        response_data = json.loads(response.content)
        self.assertEqual("updated school", response_data.get("name"))


    def test_can_partial_update_school(self):
        url = self.url+str(self.school.id)+'/'
        response = self.client.patch(url, {"name": "updated school"})
        response_data = json.loads(response.content)
        self.assertEqual("updated school", response_data.get("name"))


    def test_can_delete_school(self):
        url = self.url+str(self.school.id)+'/'
        response = self.client.delete(url)
        self.assertEqual(204, response.status_code)





