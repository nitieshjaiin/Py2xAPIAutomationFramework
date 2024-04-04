# Create Token
# Create Booking ID
# Update the booking (Put) - Booking ID, TOken
# Delete the booking

# Verify that created booking id when


import pytest
import allure

from src.constants.api_constants import APIConstants
from src.helpers.api_requests_wrapper import post_request
from src.helpers.common_verifications import *
from src.helpers.payload_manager import payload_create_booking
from src.utils.utils import Util

class TestCrudBooking():
    @pytest.fixture
    def create_token(self):
        pass

    @pytest.fixture
    def get_booking_id(self):
        pass

    def test_update_booking(self):
        pass

    def test_delete_booking(self):
        pass
