# keeps track of my hours in coding
import csv
import time

'''
def stopWatch(value):
    valueD = (((value/365)/24)/60)
    days = int(valueD)

    valueH = (valueD - days) * 365
    hours = int(valueH)

    valueM = (valueH - hours) * 24
    minutes = int(valueM)

    valueS = (valueM - minutes) * 60
    seconds = int(valueS)

    return days, hours, minutes, seconds
'''
'''
def parser(n):
    totalInSeconds = math.floor(n)
    secondsLeftOver = totalInSeconds % 60
    minutes = math.floor(totalInSeconds/60)
    hours = math.floor(totalInSeconds / 3600)
    minutesLeftOver = minutes - (hours * 60)

    print(f"\nYou have been working for a total of {totalInSeconds} seconds.")
    print(f"\nThat's {minutes} minutes and {secondsLeftOver} seconds.")
    print(f"\nThat's {hours} hours, {minutesLeftOver} minutes, and {secondsLeftOver} seconds.")

    return hours, minutesLeftOver, secondsLeftOver
'''

start = time.time()


print("Welcome, Mr. Gelok. Which project are you working on today?")
todaysProject = input("> ")
print("\n"*8)
print("Please hit Enter when finished.")
input("> ")

end = time.time()
readerTime = end - start         
timeToday = stopWatch(readerTime)
totalTime = 0

r = csv.reader(open('timer.csv'))
lines = list(r)

testlist = []
for line in lines:
    testlist.append(line[0])
if todaysProject not in testlist:
    newline = [todaysProject,0]
    lines.append(newline)

for line in lines:
    if line[0] == todaysProject:
        sofar = float(line[1])
        line[1] = sofar + readerTime
    
    if line[0] == 'total':
        sofar = float(line[1])
        cumulativeTime = sofar + readerTime
        totalTime = cumulativeTime
        line[1] = cumulativeTime

writer = csv.writer(open('timer.csv', 'w'))
writer.writerows(lines)

grandTotal = stopWatch(totalTime)

print("\n\nToday's time is {} days, {} hours, {} minutes, and {} seconds.".format(timeToday[0], timeToday[1], timeToday[2], timeToday[3]))
print(f"Today's time has been logged to {todaysProject}.")
print("\n\nYour TOTAL CODING time is {} days, {} hours, {} minutes, and {} seconds.".format(grandTotal[0], grandTotal[1], grandTotal[2], grandTotal[3]))
print("\n"*2)

