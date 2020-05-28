var starttime = new Date();

// get the project from a prompt

// wait for the end time

var endtime = new Date();
var totalTime = endtime.getTime() - starttime.getTime();

// get days
var myDays = totalTime / (1000 * 60 * 60 * 24);
myDays = Math.floor(myDays);
// get hours
var myHours = totalTime - (myDays * 1000 * 60 * 60 * 24);
myHours = Math.floor(myHours);
// get minutes
var myMinutes = totalTime - (myDays * 1000 * 60 * 60 * 24) - (myHours * 1000 * 60 * 60)
myMinutes = Math.floor(myMinutes)
// get seconds

// print out to user what their time today was

// open CSV
// if project nonexistant, create it
// log milliseconds towards project 
// add milliseconds to total time

// print out how much total time has been spent in that project
// print out total time 