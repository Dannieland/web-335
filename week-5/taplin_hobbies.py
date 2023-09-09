# taplin_hobbies.py
# Danielle Taplin
# 9/07/23
# list of hobbies using python conditionals, lists, and loops

#create python list with hobbies
hobby_list = ["sleeping", "working out", "computer gaming", "cooking", "dancing"]

#create list with the days of the week
day_list = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

#print all hobbies in list to console
for x in hobby_list:
    print(x)

#for each day in list
for d in day_list:
    #create message variable for printing the status of that day
    day_message = d
    #if day is saturday or sunday
    if d == 'Sunday' or d == 'Saturday':
        #concatenate message stating that current day is for hobby enjoyment
        day_message += " is a day for enjoying hobbies"
    else:
        #else, concatenate message stating that current day is a working day
        day_message += " is a work day"

    #print day_message
    print(day_message)