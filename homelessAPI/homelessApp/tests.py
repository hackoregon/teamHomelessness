from django.test import TestCase, Client


class ListVeteransTest(TestCase):
    # fixtures = ["homelessApp/fixtures/disability_fixture.json"]

    def setUp(self):
        self.c = Client()

    def test_get_request_sends_200(self):
        response = self.c.get("/homeless/veterans/")
        self.assertEqual(response.status_code, 200)
