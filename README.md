# Scheduling for 60 people
The program reads the list of surnames from the excel file, and on its equipment draws up a work schedule for employees and writes a report.xlsx file with the schedule.
## Installation
The program is written in Python 3.7 and it is expected that it is already installed
In case of conflict with Python2, use pip3. Install the necessary modules:

pip install -r requirements.txt

## Use
the program has a console and graphical version.
To use the console version of the program, type:
`` ``
	sh-5.0 $ python3.7 grafic.py
	usage: grafic.py [-h] [-link LINK]

	optional arguments:
	-h, --help show this help message and exit
	-link LINK Enter link to file from list families
`` ``
That is: if there is a -link switch and the path to the file with the list behind it, then it processes it and writes the result to the report.xlsx file.
If it is not, then the graphical version of the program is launched.
An additional condition: on weekdays, there should be 15 people, and on weekends - 22 people.
If the program cannot process the files, the files are of the wrong structure or an exception occurs, then everything will be written to the report.log file
## Project Description
This project was written for training purposes by the module pandas, logging, argparse
