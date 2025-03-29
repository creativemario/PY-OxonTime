import requests

# Define a class to hold the data
class DepartureBoard:
    def __init__(self, timestamp, location_id, description, atco_code, naptan_code, time, calls, messages):
        self.timestamp = timestamp
        self.location_id = location_id
        self.description = description
        self.atco_code = atco_code
        self.naptan_code = naptan_code
        self.time = time
        self.calls = calls
        self.messages = messages


class Call:
    def __init__(self, route_code, direction, direction_name, visit_number, trip_no, service_description, origin_ref, origin_name, ttb_date_id, destination_ref, destination_name, destination_locality, destination, origin_aimed_departure_time, monitored, tvl_fact_id, prediction_id, operator_code, vehicle_code, sequence, stop_point_name, aimed_arrival_time, expected_arrival_time, aimed_departure_time, expected_departure_time, countdown_dep_arr, sort_time, display_time, gps_time, gpslat, gpslong, bay_no, wheelchair_access, trip_status):
        self.route_code = route_code
        self.direction = direction
        self.direction_name = direction_name
        self.visit_number = visit_number
        self.trip_no = trip_no
        self.service_description = service_description
        self.origin_ref = origin_ref
        self.origin_name = origin_name
        self.ttb_date_id = ttb_date_id
        self.destination_ref = destination_ref
        self.destination_name = destination_name
        self.destination_locality = destination_locality
        self.destination = destination
        self.origin_aimed_departure_time = origin_aimed_departure_time
        self.monitored = monitored
        self.tvl_fact_id = tvl_fact_id
        self.prediction_id = prediction_id
        self.operator_code = operator_code
        self.vehicle_code = vehicle_code
        self.sequence = sequence
        self.stop_point_name = stop_point_name
        self.aimed_arrival_time = aimed_arrival_time
        self.aimed_departure_time = aimed_departure_time
        self.expected_arrival_time = expected_arrival_time
        self.aimed_departure_time = aimed_departure_time
        self.expected_departure_time = expected_departure_time
        self.countdown_dep_arr = countdown_dep_arr
        self.sort_time = sort_time
        self.display_time = display_time
        self.gps_time = gps_time
        self.gpslat = gpslat
        self.gpslong = gpslong
        self.bay_no = bay_no
        self.wheelchair_access = wheelchair_access
        self.trip_status = trip_status

    def __str__(self):
        return f"Route Code: {self.route_code}, Direction: {self.direction}, Direction Name: {self.direction_name}, Visit Number: {self.visit_number}, Trip No: {self.trip_no}, Service Description: {self.service_description}, Origin Ref: {self.origin_ref}, Origin Name: {self.origin_name}, Destination Ref: {self.destination_ref}, Destination Name: {self.destination_name}, Destination Locality {self.destination_locality}, Destination {self.destination}, Origin Aimed Departure Time {self.origin_aimed_departure_time}, Monitored {self.monitored}, TVL Fact ID {self.tvl_fact_id}, Prediction ID {self.prediction_id}, Operator Code {self.operator_code}, Vehicle Code {self.vehicle_code}, Sequence {self.sequence}, Stop Point Name {self.stop_point_name}, Aimed Arrival Time {self.aimed_arrival_time}, Aimed Departure Time {self.aimed_departure_time}, Expected Arrival Time {self.expected_arrival_time}, Expected Departure Time {self.expected_departure_time}, Countdown Dep Arr {self.countdown_dep_arr}, Sort Time {self.sort_time}, Display Time {self.display_time}, GPSTime {self.gps_time}, GPSLat {self.gpslat}, GPSLong {self.gpslong}, Bay No {self.bay_no}, Wheelchair Access {self.wheelchair_access}, Trip Status {self.trip_status}"

    def __repr__(self):
        return self.__str__()
# Example function to create instances of Operator from the data
def create_departure_board(data):
    departure_board = None
    for key, data in data.items():
        departure_board = DepartureBoard(
            timestamp=data["timestamp"],
            location_id=data["location_id"],
            description=data["description"],
            atco_code=data["atco_code"],
            naptan_code=data["naptan_code"],
            time=data["time"],
            calls=create_calls(data["calls"]),
            messages=data["messages"]
        )
    return departure_board

def create_calls(data):
    calls = []
    for item in data:
        call = Call(
            route_code=item["route_code"],
            direction=item["direction"],
            direction_name=item["direction_name"],
            visit_number=item["visit_number"],
            trip_no=item["trip_no"],
            service_description=item["service_description"],
            origin_ref=item["origin_ref"],
            origin_name=item["origin_name"],
            ttb_date_id=item["ttb_date_id"],
            destination_ref=item["destination_ref"],
            destination_name=item["destination_name"],
            destination_locality=item["destination_locality"],
            destination=item["destination"],
            origin_aimed_departure_time=item["origin_aimed_departure_time"],
            monitored=item["monitored"],
            tvl_fact_id=item["tvl_fact_id"],
            prediction_id=item["prediction_id"],
            operator_code=item["operator_code"],
            vehicle_code=item["vehicle_code"],
            sequence=item["sequence"],
            stop_point_name=item["stop_point_name"],
            aimed_arrival_time=item["aimed_arrival_time"],
            expected_arrival_time=item["expected_arrival_time"],
            aimed_departure_time=item["aimed_departure_time"],
            expected_departure_time=item["expected_departure_time"],
            countdown_dep_arr=item["countdown_dep_arr"],
            sort_time=item["sort_time"],
            display_time=item["display_time"],
            gps_time=item["gps_time"],
            gpslat=item["gpslat"],
            gpslong=item["gpslong"],
            bay_no=item["bay_no"],
            wheelchair_access=item["wheelchair_access"],
            trip_status=item["trip_status"]
        )
        calls.append(call)
    return calls


def get_departure_board(departure_board_id):
    # Define the URL
    url = "https://oxontime.com/pwi/departureBoard/" + str(departure_board_id)

    # Make a request to the URL
    response = requests.get(url)

    # Parse the JSON response
    data = response.json()

    # Create instances of Operator
    departure_board = create_departure_board(data)

    # Print the created objects to verify
    print(f"Timestamp: {departure_board.timestamp}, Location ID: {departure_board.location_id}, Descriptiion: {departure_board.description}, ACTO Code: {departure_board.atco_code}, NAPTAN Code: {departure_board.naptan_code}, Time: {departure_board.time}, Calls: {str(departure_board.calls)}, Messages: {departure_board.messages}")

    return departure_board