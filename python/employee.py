# 21.Imagine a scenario where you are required to fetch the employee names who joined after 
# 02 Sep 2022 and location is Hyderabad
# empIoyee_ data = {“priya”:{“location”	: “Hyderabad”, “joining_date '. “05/09/2022”},
# “mahi”: {“location”	: “Bangalore”, “joining_date ': “20/02/2023”},
# “raja”: {“location”	: “Hyderabad”, “joining_date ': “14/10/2022”},
# “prabhu”:{“location”	: “Bangalore” “joining_date ': “02/01/2023”}}

employee_data = {
    "priya":{
    "location": "hyderabad",
    "joining_date":"05/09/2022"
    },
    "mahi":{
    "location": "bangalore",
    "joining_date":"20/02/2023"
    },
    "raja":{
    "location": "hyderabad",
    "joining_date":"14/10/2022"
    },
    "prabhu":{
    "location": "bangalore",
    "joining_date":"02/01/2023"
    },
    "kumar":{
    "location": "hyderabad",
    "joining_date":"01/01/2023"
    },
}

res = []
for k,v in employee_data.items():
    if v["location"] == "hyderabad":
        day, month, year = [int(i) for i in v["joining_date"].split("/")]
        if year > 2022:
            res.append(k)
        elif year == 2022 and month >= 9 and day > 2:
            res.append(k)
        
print(res)

