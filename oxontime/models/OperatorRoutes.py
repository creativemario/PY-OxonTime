import requests

# Define the URL
url = "https://oxontime.com/pwi/getOperatorRoutes"

# Make a request to the URL
response = requests.get(url)

# Parse the JSON response
data = response.json()

# Define a class to hold the data
class Route:
    def __init__(self, route_id, operator_id, route_code, description, service_code, inbound_desc, outbound_desc):
        self.route_id = route_id
        self.operator_id = operator_id
        self.route_code = route_code
        self.description = description
        self.service_code = service_code
        self.inbound_desc = inbound_desc
        self.outbound_desc = outbound_desc


# Example function to create instances of Operator from the data
def create_routes(data):
    routes = []
    for item in data:
        count = 0
        for routen in item["routes"]:
            route = Route(
                route_id=routen.get("route_id"),
                operator_id=routen.get("operator_id"),
                route_code=routen.get("route_code"),
                description=routen.get("description"),
                service_code=routen.get("service_code"),
                inbound_desc=routen.get("inbound_desc"),
                outbound_desc=routen.get("outbound_desc")
             )
            routes.append(route)
    return routes

# Create instances of Operator
routes = create_routes(data)

# Print the created objects to verify
for route in routes:
    print(f"Route ID: {route.route_id}, Operator ID: {route.operator_id}, Route Code: {route.route_code}, Description: {route.description}, Service Code: {route.service_code}, Inbound Description {route.inbound_desc}, Outbound Description {route.outbound_desc}")
