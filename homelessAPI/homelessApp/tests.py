from django.test import TestCase, Client
import json


class ListDisabilityTest(TestCase): 
    fixtures = ["APP_FIXTURE"]

    def setUp(self):
        self.c = Client()

    def test_get_request_sends_200(self):
        response = self.c.get("/homeless/disability/")
        self.assertEqual(response.status_code, 200)

    def test_response_returns_correct_objects(self):
        response = self.c.get("/homeless/disability/?format=json")
        json_content = json.loads(response.content.decode('utf-8'))

        # 45 records in disability fixture
        self.assertEqual(len(json_content), 45)


class ListEthnicityTest(TestCase):
    fixtures = ["APP_FIXTURE"]

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


class RootAPITest(TestCase):

    def setUp(self):
        self.c = Client()

    def test_get_request_sends_200(self):
        response = self.c.get("/homeless/")
        self.assertEqual(response.status_code, 200)


 










