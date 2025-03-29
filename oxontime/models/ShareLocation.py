import requests

# Define the URL
url = "https://oxontime.com/pwi/getShareLocations"

# Make a request to the URL
response = requests.get(url)

# Parse the JSON response
data = response.json()

# Define a class to hold the data
class ShareLocation:
    def __init__(self, location_id, location_code, location_name, bearing, locality_code, locality_name, latitude, longitude, operator_code):
        self.location_id = location_id
        self.location_code = location_code
        self.location_name = location_name
        self.bearing = bearing
        self.locality_code = locality_code
        self.locality_name = locality_name
        self.latitude = latitude
        self.longitude = longitude
        self.operator_code = operator_code
# Example function to create instances of ShareLocation from the data
def create_share_locations(data):
    locations = []
    for item in data:
        location = ShareLocation(
            location_id=item.get("location_id"),
            location_code=item.get("location_code"),
            location_name=item.get("location_name"),
            bearing=item.get("bearing"),
            locality_code=item.get("locality_code"),
            locality_name=item.get("locality_name"),
            latitude=item.get("latitude"),
            longitude=item.get("longitude"),
            operator_code=item.get("operator_code"),
        )
        locations.append(location)
    return locations

# Create instances of ShareLocation
share_locations = create_share_locations(data)

# Print the created objects to verify
for location in share_locations:
    print(f"Location ID: {location.location_id}, Location Code: {location.location_code} , Location Name: {location.location_name}, Bearing: {location.bearing}, Locality Code: {location.locality_code}, Locality Name: {location.locality_name}, Latitude: {location.latitude}, Longitude: {location.longitude}, Operator Code: {location.operator_code}")