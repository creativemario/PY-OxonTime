from datetime import datetime

class call:
    def __init__(self, call):
        self.route_code = call["route_code"]
        self.direction = call["direction"]
        self.direction_name = call["direction_name"]
        self.visit_number = call["visit_number"]
        self.trip_no = call["trip_no"]
        self.service_description = call["service_description"]
        self.origin_ref = call["origin_ref"]
        self.origin_name = call["origin_name"]
        self.ttb_date_id = call["ttb_date_id"]
        self.destination_ref = call["destination_ref"]
        self.destination_name = call["destination_name"]
        self.destination_locality = call["destination_locality"]
        self.destination = call["destination"]
        self.origin_aimed_departure_time = call["origin_aimed_departure_time"]
        self.monitored = call["monitored"]
        self.tvl_fact_id = call["tvl_fact_id"]
        self.prediction_id = call["prediction_id"]
        self.operator_code = call["operator_code"]
        self.vehicle_code = call["vehicle_code"]
        self.sequence = call["sequence"]
        self.stop_point_name = call["stop_point_name"]
        self.aimed_arrival_time = call["aimed_arrival_time"]
        self.expected_arrival_time = call["expected_arrival_time"]
        self.aimed_departure_time = call["aimed_departure_time"]
        self.expected_departure_time = call["expected_departure_time"]
        self.countdown_dep_arr = call["countdown_dep_arr"]
        self.sort_time = call["sort_time"]
        self.display_time = call["display_time"]
        self.gps_time = call["gps_time"]
        self.gpslat = call["gpslat"]
        self.gpslong = call["gpslong"]
        self.bay_no = call["bay_no"]
        self.wheelchair_access = call["wheelchair_access"]
        self.trip_status = call["trip_status"]
        
    def getETA(self):
        date_format = "%Y-%m-%d %H:%M:%S"
        time_expected = datetime.strptime(self.expected_arrival_time, date_format)
        now = datetime.now()
        diff = time_expected - now
        diff_minutes = int(diff.total_seconds() / 60)
        
        if (diff_minutes == 0):
            return "Due"
        elif(diff_minutes <=-1):
            return "Late"
        else:
            return str(diff_minutes) + " Mins"
        
        
        
    def __str__(self):
        formattedString = ""
        stopTitle = ""
        
        stopTitle = "Call (" + self.route_code +"): \t(P) " + self.aimed_arrival_time
        if(self.monitored):
            stopTitle += " | (T) ETA: " + self.getETA() + " (" + self.expected_arrival_time + ")"
            stopTitle += "\n\t\t\t\t\t\t\t  (" + str(self.gpslat) +"," + str(self.gpslong) + ")\n\t\t\t\t\t\t\t  https://embed.waze.com/iframe?zoom=15&lat="+self.gpslat+"&lon="+self.gpslong+"&pin=1&desc=0"
        formattedString += stopTitle
        return formattedString
        
    
    