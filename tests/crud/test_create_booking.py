import pytest
import allure

from src.constants.api_constants import APIConstants
from src.helpers.api_requests_wrapper import post_request
from src.helpers.common_verifications import *
from src.helpers.payload_manager import payload_create_booking
from src.utils.utils import Util

class TestCreateBooking(object):

    @pytest.mark.positive
    @allure.title("Verify that create booking status and booking ID aren't null")
    @allure.description("Creating a booking from payload and verify that booking ID isn't null and status code is 200 "
                        "for correct payload")
    def test_create_booking_positive(self):
        payload = payload_create_booking()
        response = post_request(url=APIConstants.url_create_booking(),
                                auth=None,
                                headers=Util().common_headers_json(),
                                payload=payload_create_booking(),in_json=False)
        booking_id = response.json()["bookingid"]
        verify_http_status_code(response_data=response,expect_data=200)
        verify_json_key_for_not_null(booking_id)

    @pytest.mark.negative
    @allure.title("Verify that create booking doesn't work with empty payload")
    @allure.description("Creating a booking from empty payload and verify that status code is 500 "
                        "for incorrect payload")
    def test_create_booking_negative(self):
        # URL, Headers, Payload,
        response = post_request(url=APIConstants.url_create_booking(), auth=None,
                                headers=Util.common_headers_json(self),
                                 payload={}, in_json=False)
        verify_http_status_code(response, 500)



