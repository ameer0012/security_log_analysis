from django.test import TestCase

from django.test import TestCase
from django.urls import reverse


class LogParsingTestCase(TestCase):
    # Add your test cases here
    pass


class ReceiveLogsTestCase(TestCase):
    def test_receive_logs_post_json(self):
        # Create a JSON log data string to simulate the request body
        log_data = '{"message": "This is a log message"}'

        # Make a POST request to the receive_logs view with the JSON log data
        response = self.client.post(reverse('receive_logs'), data=log_data, content_type='application/json')

        # Assert that the response status code is 200
        self.assertEqual(response.status_code, 200)

        # Add any additional assertions to validate the response if needed

    def test_receive_logs_post_csv(self):
        # Create a CSV log data string to simulate the request body
        log_data = 'timestamp,message\n2022-01-01 12:00:00,This is a log message'

        # Make a POST request to the receive_logs view with the CSV log data
        response = self.client.post(reverse('receive_logs'), data=log_data, content_type='text/csv')

        # Assert that the response status code is 200
        self.assertEqual(response.status_code, 200)

        # Add any additional assertions to validate the response if needed

    def test_receive_logs_invalid_content_type(self):
        # Create an invalid content type
        content_type = 'application/xml'

        # Make a POST request to the receive_logs view with an invalid content type
        response = self.client.post(reverse('receive_logs'), content_type=content_type)

        # Assert that the response status code is 400
        self.assertEqual(response.status_code, 400)

        # Add any additional assertions to validate the response if needed

    def test_receive_logs_get_request(self):
        # Make a GET request to the receive_logs view
        response = self.client.get(reverse('receive_logs'))

        # Assert that the response status code is 405 (Method Not Allowed)
        self.assertEqual(response.status_code, 405)

        # Add any additional assertions to validate the response if needed
