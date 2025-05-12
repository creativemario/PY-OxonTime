import requests



# Define a class to hold the data
class Operator:
    def __init__(self, operator_id, operator_code, legal_name, address01, address02, address03, address04, short_name, loc_prefix, tel_travel, tel_enquiry, text, value):
        self.operator_id = operator_id
        self.operator_code = operator_code
        self.legal_name = legal_name
        self.address01 = address01
        self.address02 = address02
        self.address03 = address03
        self.address04 = address04
        self.short_name = short_name
        self.loc_prefix = loc_prefix
        self.tel_travel = tel_travel
        self.tel_enquiry = tel_enquiry
        self.text = text
        self.value = value

    def __str__(self):
        return(f"[Operator ID: {self.operator_id}, Operator Code: {self.operator_code}, Legal Name: {self.legal_name}, Text: {self.text}, Value: {self.value}]")

    def __repr__(self):
        return self.__str__()

# Example function to create instances of Operator from the data
def update_operators():
    # Define the URL
    url = "https://oxontime.com/pwi/getOperators"

    # Make a request to the URL
    response = requests.get(url)

    # Parse the JSON response
    data = response.json()

    operators = []
    for item in data:
        operator = Operator(
            operator_id=item.get("operator_id"),
            operator_code=item.get("operator_code"),
            legal_name=item.get("legal_name"),
            address01=item.get("address01"),
            address02=item.get("address02"),
            address03=item.get("address03"),
            address04=item.get("address04"),
            short_name=item.get("short_name"),
            loc_prefix=item.get("loc_prefix"),
            tel_travel=item.get("tel_travel"),
            tel_enquiry=item.get("tel_enquiry"),
            text=item.get("text"),
            value=item.get("value")
        )
        operators.append(operator)
    return operators
