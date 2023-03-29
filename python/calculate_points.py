# 17. Create a function that takes the number of wins, draws and losses and calculates the 
# number of points obtained so far for 'n' number of ipl teams . 
# Print the winner team in the end .
# wins get +3 points, draws get +1 point, losses get -1 points . 
# I/p: Team1(3, 4, 2) ## calculation : 33 +41 + 2(-1) = 11
# Team2(5, 0, 2) ## calculation : 53 + 01 + 2(-1) = 13 
# Team3(0, 0, 1) ## calculation : 03 + 01 + 1(-1) = -1 
# O/p: Winner: Team2 

def CalculatePoints(*teams):
    points_table = {}
    
    for team in teams:
        name = team[0]
        win = team[1]
        draw = team[2]
        losses = team[3]

        total = (win*3)+draw-losses

        points_table[name] = total

    winner =  max(points_table, key=points_table.get)

    return f"{points_table} \nThe winner is {winner} with {points_table[winner]} points."

print(CalculatePoints(['CSK', 3, 4, 2], ['RCB', 5, 0, 2], ['MI', 0, 0, 1]))
