import requests
import json


class GoRestAPIFunction:
    def __init__(self, url):
        self.url = url

    def api_status_code(self):
        # Method to fetch the API status code to ensure API is accessible
        response = requests.get(self.url, headers=headers).status_code
        return response

    def fetch_api_data(self):
        # Fetch and return the API data in JSON format if status code is 200
        if self.api_status_code() == 200:
            response = requests.get(self.url, headers=headers)
            json_data = response.json()  # Convert response to JSON
            return json_data
        else:
            return "Error: Could Not Fetch API Data"

    def fetch_api_data_pretty(self):
        # Fetch and return API data in a formatted JSON string
        if self.api_status_code() == 200:
            response = requests.get(self.url, headers=headers)
            json_data = response.json()  # Convert response to JSON
            print("API Response Data:")
            json_str = json.dumps(json_data, indent=4)  # Pretty print JSON data
            return json_str
        else:
            return "Error: Could Not Fetch API Data"

    def fetch_header(self):
        # Fetch and return the API response headers as a dictionary
        if self.api_status_code() == 200:
            response = requests.get(self.url, headers=headers)
            json_header_data = dict(response.headers)  # Convert headers to dictionary
            return json_header_data
        else:
            return "Error: Could not fetch headers"

    def fetch_header_pretty(self):
        # Fetch and return the API headers in a formatted JSON string
        if self.api_status_code() == 200:
            response = requests.get(self.url, headers=headers)
            json_header_data = dict(response.headers)
            json_str_data = json.dumps(json_header_data, indent=4)  # Pretty print headers
            return json_str_data
        else:
            return "Error: Could not fetch headers"

    def fetch_data_by_id(self, id):
        # Fetch user data by ID from the API if status code is 200
        if self.api_status_code() == 200:
            response = requests.get(self.url, headers=headers).json()
            user_id = id
            # Iterate through the response data to find the specific user by ID
            for data in response:
                if data['id'] == user_id:
                    return data['id'], data['name'], data['email'], data['gender'], data['status']
            print("ID not found in response")
        return None

    def insert_data(self, data):
        # Insert new user data into the API if status code is 200
        status_code = self.api_status_code()
        print(f"API Status Code: {status_code}")
        if status_code == 200:
            # Send POST request to insert data
            response = requests.post(self.url, json=data, headers=headers)
            print(f"Response Status Code: {response.status_code}")
            json_data = response.json()
            json_str = json.dumps(json_data, indent=4)  # Pretty print the response
            print(json_str)
            return response.status_code == 201  # Return True if insertion is successful
        else:
            return "Error in Inserting Data"

    def update_data(self, id):
        # Update user data by ID if status code is 200
        status_code = self.api_status_code()
        print(f"API Status Code: {status_code}")
        if status_code == 200:
            # Send PUT request to update data
            response = requests.put(f"{self.url}/{id}", json=updated_data, headers=headers)
            print(f"Response Status Code: {response.status_code}")
            json_data = response.json()  # Display the updated data
            print(json_data)
            return response.status_code == 200  # Return True if update is successful

    def delete_data(self, id):
        # Delete user data by ID if status code is 200
        status_code = self.api_status_code()
        print(f"API Status Code: {status_code}")
        if status_code == 200:
            # Send DELETE request to delete data by ID
            delete_url = f"{self.url}/{id}"
            response = requests.delete(delete_url, headers=headers)
            print(f"\nDelete Response: {response.status_code}, {response.text}")

            if response.status_code == 204:
                return True  # Return True if deletion is successful
            else:
                print(f"Unexpected status code during deletion: {response.status_code}")
                return False

        else:
            print("Unable to Delete Data. API not accessible")
        return False


# Base URL and endpoint
base_url = "https://gorest.co.in/"
ext_url = "/public/v2/users"
url = base_url + ext_url  # Complete API URL

# API authorization token and headers
auth_token = "a936a3cfe1225c457665df965ed20117e2b359b5521d3fe37311e8c18ffa7bae"
headers = {
    "Authorization": f"Bearer {auth_token}"
}

# Data to be used for inserting or updating users
data = {
    "name": "Suraj Rai",
    "email": "suraj@gmail.com",
    "gender": "female",
    "status": "active"
}
updated_data = {
    "name": "Sanjay Gandhi",
    "email": "sanjayga@gmail.com",
    "gender": "male",
    "status": "active"}

# Creating an instance of GoRestAPIFunction and calling methods
api = GoRestAPIFunction(url)
print(api.api_status_code())
print(api.fetch_api_data())
print(api.fetch_api_data_pretty())
print(api.fetch_header_pretty())
print(api.fetch_data_by_id(7411239))
print(api.insert_data(data))
print(api.update_data(7411238))
print(api.delete_data(7411288))
