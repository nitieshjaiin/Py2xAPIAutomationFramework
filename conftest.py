import pytest
import allure

from src.constants.api_constants import APIConstants
from src.helpers.api_requests_wrapper import *
from src.helpers.common_verifications import *
from src.helpers.payload_manager import *
from src.utils.utils import Util


@pytest.fixture(scope="session")
def create_token():
    response = post_request(url=APIConstants.url_create_token(),
                            headers=Util.common_headers_json(str),
                            auth=None,
                            payload=payload_create_token(),
                            in_json=False
                            )
    verify_http_status_code(response_data=response, expect_data=200)
    verify_json_key_for_not_null_token(response.json()["token"])
    return response.json()["token"]


@pytest.fixture(scope="session")
def get_booking_id():
    payload = payload_create_booking()
    response = post_request(url=APIConstants.url_create_booking(),
                            auth=None,
                            headers=Util().common_headers_json(str),
                            payload=payload_create_booking(), in_json=False)
    booking_id = response.json()["bookingid"]
    verify_http_status_code(response_data=response, expect_data=200)
    verify_json_key_for_not_null(booking_id)
    return response.json()["bookingid"]
