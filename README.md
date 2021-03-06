# Timer

Hello, GitHubbers! 👋 This is my first real (*self-conceived, independently-developed*) project! 

### Description

- `timer.py` keeps track of my independent coding practice.
- As I run it (in terminal), it registers the starting time and asks what I'm working on.
- If my project doesn't exist, it creates it.
- It then prompts me to hit enter when done, at which point it registers the ending time.
- After determining the total time, it tells me how long I spent and logs it to an external file (`timer.csv`).
- It logs it twice; first to the project's header, secondly to the total time.

### Prerequisites

- a Python 3 environment (I'm using Python 3.8)
- both files (`timer.py` and `timer.csv`) in same folder

### Changelog

- Version 1 had some issues; it exported to the csv properly but had inaccuracies recording the time.
- Version 1.1 fixed recording issues, updated README to a .md.

### Next up

- change csv so it becomes human-readable
- add feature to list currently recorded projects and their totals
- add feature to list current day's cumulative time
- rewrite whole thing in JS!
- wire up to a website
