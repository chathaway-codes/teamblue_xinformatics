import csv

from course import Course
from timeslot import Timeslot

def load_available_courses():
    # Opens available courses file
    f = open_csv('sis_class_schedule_fall_2014_CSCI.csv')

    csv_f = csv.DictReader(f)

    crn = read_csv(csv_f)

    f.close()

    return crn

def open_csv(file_name):
    return open(file_name)

def read_csv(csv_file):
    crn = []
    
    # Should add a way to skip the header line
    for row in csv_file:
        # Read in the times for the course
        # Need to make times military time
        t = {}
        days = str(row['days'])
        if 'M' in days:
            t['M'] = [row['start_time'], row['end_time']]
        if 'T' in days:
            t['T'] = [row['start_time'], row['end_time']]
        if 'W' in days:
            t['W'] = [row['start_time'], row['end_time']]
        if 'R' in days:
            t['R'] = [row['start_time'], row['end_time']]
        if 'F' in days:
            t['F'] = [row['start_time'], row['end_time']]

        # Create timeslot for the course
        # Hard-coded semester (should be read in somehow)
        ts = Timeslot("FA14", t)

        # Create a new course
        # Initializing with no prereqs (need database with prereqs)
        c = Course(row['crn?'], ts, None, row['credit_hours'])
        
        crn.append(c)

    return crn

# For testing purposes
available_crn = load_available_courses()
for c in available_crn:
    print c.CRN, c.timeslot.semester, c.timeslot.day_time, c.prereqs, c.credit_hours
