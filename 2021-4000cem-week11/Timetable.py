from Printer import dictPrinter

# Define timetable dictionary
timetable = { ("Mon",9):"121COM", ("Mon", 3):"A.L.L.", ("Wed", 10):"121COM"} 
timetable[("Fri", 6)] = "Party!" 

dictPrinter(timetable)

# Function to say where I should be
def whatNow(day, time):
    task = timetable[ (day, time) ]
    return task
    
whatNow("Mon", 9)
timetable[["Mon", 6]] = "Gym"