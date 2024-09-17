import pytest
import requests

from gorestapifunction.api_function import GoRestAPIFunction
from gorestapifunction.mock_data import TestData


class TestGoRestAPI:
    @pytest.fixture(autouse=True)
    def setup(self):
        # Set up the API object with base URL and authentication details
        self.url = "https://gorest.co.in/public/v2/users"
        self.api_function = GoRestAPIFunction(self.url)

    def test_api_status_code(self):
        # Test case to check if the API is reachable and returns a status code
        assert self.api_function.api_status_code() == 200

    def test_fetch_api_data(self):
        # Test case to verify if API data is fetched correctly
        assert self.api_function.fetch_api_data() == TestData.mock_data

    def test_fetch_header(self):

        header = self.api_function.fetch_header()
        assert header['Connection'] == 'keep-alive'

    def test_fetch_data_by_id(self):
        result = self.api_function.fetch_data_by_id(7411239)
        assert result == TestData.mock_new_data

    def test_insert_data(self):
        # Test case to insert new data into the API and verify success
        new_data = {'name': 'Ajit Agarwal', 'email': 'ajith@gmail.com', 'gender': 'male', 'status': 'active'}
        assert self.api_function.insert_data(new_data) == True  # Check if insertion is successful

    def test_update_data(self):
        assert self.api_function.update_data(7411238) == True

    def test_delete_data(self):
        # Test case to delete a user by ID and verify deletion success
        assert self.api_function.delete_data(7411288) == True  # Check if deletion was successful
