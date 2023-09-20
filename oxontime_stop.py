import oxontime_call
class stop:
    def __init__(self, stop):
        self.timestamp = stop["timestamp"]
        self.location_id = stop["location_id"]
        self.description = stop["description"]
        self.atco_code = stop["atco_code"]
        self.naptan_code = stop["naptan_code"]
        self.time = stop["time"]
        
        self.calls = []
        
        for call in stop["calls"]:
            call_obj = oxontime_call.call(call)
            self.calls.append(call_obj)
    
    def __str__(self):
        formattedString = ""
        
        stopTitle = "OxonTime_Stop:(" + str(self.atco_code) + "):"
        stopLine1 = "\n\tlocation_id: " + str(self.location_id)
        stopLine2 = "\n\tdescription: " + str(self.description)
        stopLine3 = "\n\tatco_code: " + str(self.atco_code)
        stopLine4 = "\n\tnaptan_code: " + str(self.naptan_code)
        stopLine5 = "\n\ttime: " + str(self.time)
        
        calls = "\n\tcalls: \n\t\t"
        for call in self.calls:
            calls += str(call)
            calls += "\n\t\t"
        
        formattedString += stopTitle
        formattedString += stopLine1
        formattedString += stopLine2
        formattedString += stopLine3
        formattedString += stopLine4
        formattedString += stopLine5
        formattedString += calls
        
        return(formattedString)
        
        