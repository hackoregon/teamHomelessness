from django.test import TestCase, Client
import json


class ListDisabilityTest(TestCase):
    # 8 fake records in the fixture data 
    fixtures = ["homelessApp/fixtures/disability_fixture.json"]

    def setUp(self):
        self.c = Client()

    def test_get_request_sends_200(self):
        response = self.c.get("/homeless/disability/")
        self.assertEqual(response.status_code, 200)

    def test_response_returns_correct_objects(self):
        response = self.c.get("/homeless/disability/?format=json")
        json_content = json.loads(response.content.decode('utf-8'))

        self.assertEqual(len(json_content), 8)


class ListEthnicityTest(TestCase):
    # 25 fake records need to add better mix of years 
    fixtures = ["homelessApp/fixtures/ethnicity_fixture.json"]

    def setUp(self):
        self.c = Client()

    def test_get_request_sends_200(self):
        response = self.c.get("/homeless/ethnicity/")
        self.assertEqual(response.status_code, 200)


class ListIndividualsTest(TestCase):

    def setUp(self):
        self.c = Client()

    def test_get_request_sends_200(self):
        response = self.c.get("/homeless/individuals/")
        self.assertEqual(response.status_code, 200)


class ListGenderTest(TestCase):

    def setUp(self):
        self.c = Client()

    def test_get_request_sends_200(self):
        response = self.c.get("/homeless/gender/")
        self.assertEqual(response.status_code, 200)


class ListGeolocationTest(TestCase):

    def setUp(self):
        self.c = Client()

    def test_get_request_sends_200(self):
        response = self.c.get("/homeless/geolocation/")
        self.assertEqual(response.status_code, 200)


class ListVeteransTest(TestCase):
    
    def setUp(self):
        self.c = Client()

    def test_get_request_sends_200(self):
        response = self.c.get("/homeless/veterans/")
        self.assertEqual(response.status_code, 200)


 










