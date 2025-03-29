import requests
import json

# Define the URL
url = "https://oxontime.com/pwi/getLocalityServices"

# Make a request to the URL
response = requests.get(url)
# Parse the JSON response
data = response.json()

# Define a class to hold the data
class LocalityService:
    def __init__(self, locality_code, services):
        self.locality_code = locality_code
        self.services = services

# Example function to create instances of LocalityService from the data
def create_locality_services(data):
    services = []

    for key, data in data.items():
        service = LocalityService(
            locality_code=key,
            services=data.get("services").split(","),
        )
        services.append(service)
    return services

# Create instances of LocalityService
locality_services = create_locality_services(data)

# Print the created objects to verify
for service in locality_services:
    print(f"Locality Code: {service.locality_code}, Services: {service.services}")