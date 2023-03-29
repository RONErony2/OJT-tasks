# 25.Define a logic to print the combinations from the two the below input data 
# Input :
# {'Department“: ['Bakkt’, 'Cisco'],
# ’Team’: [’Red’, ’Yellow’, ’Black’]}

# Output :

# [{ ’Department“: ‘Bakkt’, ’Team“: ’Red’},

# { ’Department“: ‘Bakkt’, 'Team“: ’Yellow’},

# { ’Department“: ‘Bakkt’, 'Team“: ’Block’},

# { ’Department“: ‘Cisco’, ’Team“: ’Red’},

# { ’Department“: ‘Cisco’, ’Team“: ’Block’},

# { ’Department“: ‘Cisco’, ’Team': ’Yellow’}]

input_data = {
    'Department': ['Bakkt', 'Cisco'],
    'Team': ['Red', 'Yellow', 'Black']
    }

combinations = []
for department in input_data['Department']:
    for team in input_data['Team']:
        combinations.append({'Department':department, 'Team': team})

print(combinations)
