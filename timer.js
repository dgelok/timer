// get starting time
var starttime = new Date("May 28, 2020 9:00:00");

// get the project from a prompt
var myProject = "Timer";

// wait for the end time

// get ending time
var endtime = new Date("May 28, 2020 10:16:30");
var totalTimeInMs = endtime.getTime() - starttime.getTime();
var value = totalTimeInMs / 1000;

// parse in to hours, minutes, etc.
var nDays = 0;
var nHours = 0;
var nMinutes = 0;
var nSeconds = 0;

if (value > 86400) {
    nDays = Math.floor(value/86400);
    value = value % 86400;
}
if (value > 3600) {
    nHours = Math.floor(value/3600);
    value = value % 3600;
}
if (totalTimeInMs > 60) {
    nMinutes = Math.floor(value/60);
    value = value % 60
}
nSeconds = Math.floor(value);


// log the time to the console
var s = `Today, you spent 
\t${nDays} days, ${nHours} hours, ${nMinutes} minutes, and ${nSeconds} seconds... 
\ton ${myProject}.`
console.log(s);

// open CSV
// if project nonexistant, create it
// log milliseconds towards project 
// add milliseconds to total time

// print out how much total time has been spent in that project
// print out total time 