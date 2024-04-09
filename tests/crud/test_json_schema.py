# Get the response
# Create the JSON schema from https://www.jsonschema.net/
# save that schema into the name.json file
# If you want to validate the json schema - https://www.jsonschemavalidator.net/

from jsonschema import validate
from jsonschema.exceptions import ValidationError
import pytest
import allure

from src.constants.api_constants import APIConstants
from src.helpers.api_requests_wrapper import *
from src.helpers.common_verifications import *
from src.helpers.payload_manager import *
from src.utils.utils import Util
import os


class TestCreateBookingJSONSchema(object):

    def load_schema(self, file_name):
        with open(file_name, 'r') as file:
            return json.load(file)

    def test_create_booking_jsonschema(self):
        payload = payload_create_booking()
        response = post_request(url=APIConstants.url_create_booking(),
                                auth=None,
                                headers=Util().common_headers_json(),
                                payload=payload_create_booking(), in_json=False)
        booking_id = response.json()["bookingid"]
        verify_http_status_code(response_data=response, expect_data=200)
        verify_json_key_for_not_null(booking_id)

        # file_path = os.getcwd()+"\\create_booking_schema.json"
        file_path = "C:\\Users\\nitishjain8\Py2xAPIAutomationFramework\pythonProject\\tests\crud\create_booking_schema.json"
        schema = self.load_schema(file_name=file_path)

        try:
            validate(instance=response.json(), schema=schema)
        except ValidationError as E:
            print(E.message)
