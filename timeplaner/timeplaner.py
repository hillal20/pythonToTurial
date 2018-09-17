# Implement a time planner that receives the availability
#  of two people and a duration. The time planner should return 
#  the earliest time slot that matches the given duration where both 
#  people have availability. If there is no common time slot that satisfies 
#  these requirements, return None.

# Each person's availability will be a list of tuples, with the first tuple 
# element representing the start time of a time slot, and the second tuple element
#  representing the end time of that time slot. The input variable dur is a positive 
#  integer that represents the duration of a meeting in seconds.
#  The output should be a tuple with the appropriate start time and end time.

# Examples:

# input: a = [(10, 50), (60, 120), (140, 210)]         
#        b = [(0, 15), (60, 70)]         
#        dur = 8 
# output: (60, 68)  

# input: a = [(10, 50), (60, 120), (140, 210)]         
#        b = [(0, 15), (60, 70)]         
#        dur = 12 
# output: None # since there is no common slot

# These example inputs are obviously not realistic input numbers
#  for representing meeting times. Ideally the inputs would consist
#   of Unix epoch timestamps, but those are very large numbers to have to 
#   type out over and over again, so we're just going to fake that part. 
#   If your function works with these faux inputs, it will work just fine with
#    Unix timestamps. 

def time_planner(a, b, dur):
    
   
    valid = []
   
    for i in a:
       for j in b:
            if ( i[1] - i[0] >= dur and j[1] - j[0] >= dur):
                if ( i[0] == j[0]):
                   valid.append(i)
                elif (i[0]>= j[0] and i[0]+dur <= j[1]):
                   valid.append(i)
            else:
                print('none')
                return None    
         
    print(valid[0][0]) 
    print(valid[0][0] + dur) 
    return (valid[0][0],valid[0][0] + dur)
    
time_planner([(10, 50)],[(0, 30)] ,8)