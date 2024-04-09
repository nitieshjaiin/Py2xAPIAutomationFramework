# Read the CSV or excel file
# Create a function of create token which can take values from the excel file
# Verify the expected result

# to read the excel file - import openpyxl

import openpyxl
from src.constants.api_constants import APIConstants
from src.helpers.api_requests_wrapper import *
from src.helpers.common_verifications import *
from src.helpers.payload_manager import *
from src.utils.utils import Util

def read_cred_from_excel(file_path):
    cred = []
    workbook = openpyxl.load_workbook(filename=file_path)
    sheet = workbook.active
    for row in sheet.iter_rows(min_row=2, values_only=True):
        username, password = row
        cred.append(({
            "username": username,
            "password": password
        }))
    return cred


def create_auth_req(user,pwd):
    create_auth_payload = {
        "username": user,
        "password": pwd
    }
    response = post_request(url=APIConstants.url_create_token(),
                            headers=Util.common_headers_json(str),
                            auth=None,
                            payload=create_auth_payload,
                            in_json=False
                            )
    return response


def test_create_auth_with_excel():
    file_path = ("C:\\Users\\nitishjain8\Py2xAPIAutomationFramework\pythonProject\\tests\datadriventesting"
                 "\\testdata_dtt_123.xlsx")
    credentials = read_cred_from_excel(file_path=file_path)
    print(credentials)
    for user_cred in credentials:
        username = user_cred["username"]
        password = user_cred["password"]
        print(username, password)
        response = create_auth_req(user=username,pwd=password)
        print(response.status_code)
