# keeps track of my hours in coding
import csv
import time
import math

def stopWatch(value):
    nDays = 0
    nHours = 0
    nMinutes = 0
    nSeconds = 0

    if value > 86400: #days
        nDays = math.floor(value/86400)
        value = value % 86400 

    if value > 3600: #hours
        nHours = math.floor(value/3600)
        value = value % 3600

    if value > 60: #minutes 
        nMinutes = math.floor(value/60)
        value = value % 60
    
    nSeconds = math.floor(value)

    return nDays, nHours, nMinutes, nSeconds


start = time.time()


print("\nWelcome, Mr. Gelok. Which project are you working on today?")
todaysProject = input("> ")
print("\n"*8)
print("Please hit Enter when finished.")
input("> ")

end = time.time()
readerTime = end - start         
timeToday = stopWatch(readerTime)
totalTime = 0

# Opening the file
r = csv.reader(open('timer.csv'))
# splitting into a list
lines = list(r)

testlist = []
for line in lines:
    if len(line) > 0:
        testlist.append(line[0][0])
if todaysProject not in testlist:
    newline = [todaysProject,0]
    lines.append(newline)


for line in lines:
    if len(line) > 0:
        if line[0] == todaysProject:
            sofar = float(line[1])
            line[1] = sofar + readerTime
        
        if line[0] == 'total':
            sofar = float(line[1])
            line[1] = sofar + readerTime
            totalTime = line[1]


writer = csv.writer(open('timer.csv', 'w', newline=""))
writer.writerows(lines)

grandTotal = stopWatch(totalTime)

print("\n\nToday's time is {} days, {} hours, {} minutes, and {} seconds.".format(timeToday[0], timeToday[1], timeToday[2], timeToday[3]))
print(f"Today's time has been logged to {todaysProject}.")
print("\n\nYour TOTAL CODING time is {} days, {} hours, {} minutes, and {} seconds.".format(grandTotal[0], grandTotal[1], grandTotal[2], grandTotal[3]))
print("\n"*2)

