from django.test import TestCase, Client
import json


class BasicEndpointsTest(TestCase):
    fixtures = ["APP_FIXTURE"]

    def setUp(self):
        self.c = Client()

    def test_disability_get_request_sends_200(self):
        response = self.c.get("/homeless/disability/")
        self.assertEqual(response.status_code, 200)

    def test_disability_get_request_works_with_query_param(self):
        response = self.c.get("/homeless/disability/?year=2015")
        self.assertEqual(response.status_code, 200)
        json_content = json.loads(response.content.decode('utf-8'))
        years = [item["year"] for item in json_content]

        for year in years:
            self.assertEqual(year, 2015)

    def test_disability_response_returns_correct_objects(self):
        response = self.c.get("/homeless/disability/?format=json")
        json_content = json.loads(response.content.decode('utf-8'))
        # 45 records in disability fixture
        self.assertEqual(len(json_content), 45)

    def test_ethnicity_get_request_sends_200(self):
        response = self.c.get("/homeless/ethnicity/")
        self.assertEqual(response.status_code, 200)

    def test_ethnicity_get_request_works_with_query_param(self):
        response = self.c.get("/homeless/ethnicity/?year=2015")
        self.assertEqual(response.status_code, 200)
        json_content = json.loads(response.content.decode('utf-8'))
        years = [item["year"] for item in json_content]

        for year in years:
            self.assertEqual(year, 2015)

    def test_individuals_get_request_sends_200(self):
        response = self.c.get("/homeless/individuals/")
        self.assertEqual(response.status_code, 200)

    def test_individuals_get_request_works_with_query_param(self):
        response = self.c.get("/homeless/individuals/?year=2015")
        self.assertEqual(response.status_code, 200)
        json_content = json.loads(response.content.decode('utf-8'))
        years = [item["year"] for item in json_content]

        for year in years:
            self.assertEqual(year, 2015)

    def test_gender_get_request_sends_200(self):
        response = self.c.get("/homeless/gender/")
        self.assertEqual(response.status_code, 200)

    def test_gender_get_request_works_with_query_param(self):
        response = self.c.get("/homeless/gender/?year=2015")
        self.assertEqual(response.status_code, 200)
        json_content = json.loads(response.content.decode('utf-8'))
        years = [item["year"] for item in json_content]

        for year in years:
            self.assertEqual(year, 2015)

    def test_geolocation_get_request_sends_200(self):
        response = self.c.get("/homeless/geolocation/")
        self.assertEqual(response.status_code, 200)

    def test_geolocation_get_request_works_with_query_param(self):
        response = self.c.get("/homeless/geolocation/?year=2015")
        self.assertEqual(response.status_code, 200)
        json_content = json.loads(response.content.decode('utf-8'))
        years = [item["year"] for item in json_content]

        for year in years:
            self.assertEqual(year, 2015)

    def test_veterans_get_request_sends_200(self):
        response = self.c.get("/homeless/veterans/")
        self.assertEqual(response.status_code, 200)

    def test_veterans_get_request_works_with_query_param(self):
        response = self.c.get("/homeless/veterans/?year=2015")
        self.assertEqual(response.status_code, 200)
        json_content = json.loads(response.content.decode('utf-8'))
        years = [item["year"] for item in json_content]

        for year in years:
            self.assertEqual(year, 2015)

    def test_sleeping_get_request_sends_200(self):
        response = self.c.get("/homeless/sleeping/")
        self.assertEqual(response.status_code, 200)

    def test_sleeping_get_request_works_with_query_param(self):
        response = self.c.get("/homeless/sleeping/?year=2015")
        self.assertEqual(response.status_code, 200)
        json_content = json.loads(response.content.decode('utf-8'))
        years = [item["year"] for item in json_content]

        for year in years:
            self.assertEqual(year, 2015)

    def test_length_get_request_sends_200(self):
        response = self.c.get("/homeless/length/")
        self.assertEqual(response.status_code, 200)

    def test_length_get_request_works_with_query_param(self):
        response = self.c.get("/homeless/length/?year=2015")
        self.assertEqual(response.status_code, 200)
        json_content = json.loads(response.content.decode('utf-8'))
        years = [item["year"] for item in json_content]

        for year in years:
            self.assertEqual(year, 2015)

    def test_domesticviolence_get_request_sends_200(self):
        response = self.c.get("/homeless/domesticviolence/")
        self.assertEqual(response.status_code, 200)

    def test_domesticviolence_get_request_works_with_query_param(self):
        response = self.c.get("/homeless/domesticviolence/?year=2015")
        self.assertEqual(response.status_code, 200)
        json_content = json.loads(response.content.decode('utf-8'))
        years = [item["year"] for item in json_content]

        for year in years:
            self.assertEqual(year, 2015)

    def test_chronic_get_request_sends_200(self):
        response = self.c.get("/homeless/chronic/")
        self.assertEqual(response.status_code, 200)

    def test_chronic_get_request_works_with_query_param(self):
        response = self.c.get("/homeless/chronic/?year=2015")
        self.assertEqual(response.status_code, 200)
        json_content = json.loads(response.content.decode('utf-8'))
        years = [item["year"] for item in json_content]

        for year in years:
            self.assertEqual(year, 2015)

    def test_agehousecomp_get_request_sends_200(self):
        response = self.c.get("/homeless/agehousecomp/")
        self.assertEqual(response.status_code, 200)

    def test_agehousecomp_get_request_works_with_query_param(self):
        response = self.c.get("/homeless/agehousecomp/?year=2015")
        self.assertEqual(response.status_code, 200)
        json_content = json.loads(response.content.decode('utf-8'))
        years = [item["year"] for item in json_content]

        for year in years:
            self.assertEqual(year, 2015)

    def test_acsage_get_request_sends_200(self):
        response = self.c.get("/homeless/acsage/")
        self.assertEqual(response.status_code, 200)

    def test_acsage_get_request_works_with_query_param(self):
        response = self.c.get("/homeless/acsage/?year=2015")
        self.assertEqual(response.status_code, 200)
        json_content = json.loads(response.content.decode('utf-8'))
        years = [item["year"] for item in json_content]

        for year in years:
            self.assertEqual(year, 2015)

    def test_acsdisability_get_request_sends_200(self):
        response = self.c.get("/homeless/acsdisability/")
        self.assertEqual(response.status_code, 200)

    def test_acsdisability_get_request_works_with_query_param(self):
        response = self.c.get("/homeless/acsdisability/?year=2015")
        self.assertEqual(response.status_code, 200)
        json_content = json.loads(response.content.decode('utf-8'))
        years = [item["year"] for item in json_content]

        for year in years:
            self.assertEqual(year, 2015)

    def test_acsrace_get_request_sends_200(self):
        response = self.c.get("/homeless/acsrace/")
        self.assertEqual(response.status_code, 200)

    def test_acsrace_get_request_works_with_query_param(self):
        response = self.c.get("/homeless/acsrace/?year=2015")
        self.assertEqual(response.status_code, 200)
        json_content = json.loads(response.content.decode('utf-8'))
        years = [item["year"] for item in json_content]

        for year in years:
            self.assertEqual(year, 2015)

    def test_acsveteran_get_request_sends_200(self):
        response = self.c.get("/homeless/acsveteran/")
        self.assertEqual(response.status_code, 200)

    def test_acsveteran_get_request_works_with_query_param(self):
        response = self.c.get("/homeless/acsveteran/?year=2015")
        self.assertEqual(response.status_code, 200)
        json_content = json.loads(response.content.decode('utf-8'))
        years = [item["year"] for item in json_content]

        for year in years:
            self.assertEqual(year, 2015)

    def test_root_get_request_sends_200(self):
        response = self.c.get("/homeless/")
        self.assertEqual(response.status_code, 200)
