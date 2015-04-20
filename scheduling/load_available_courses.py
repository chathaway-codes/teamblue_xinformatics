import csv

from course import Course
from timeslot import Timeslot

def load_available_courses(csv_file_name):
    # Opens available courses file
    f = open(csv_file_name) #('sis_class_schedule_fall_2014_CSCI.csv')

    csv_f = csv.DictReader(f)

    available_crn = parse_csv(csv_f)

    f.close()

    return available_crn

def parse_time(days, start_time, end_time):
    # Need to convert times from 12 hr to 24 hr
    start_time = convert_time(start_time)
    end_time = convert_time(end_time)
 
    # Read in the times for the course
    d = {}
    if 'M' in days:
        d['M'] = [start_time, end_time]
    if 'T' in days:
        d['T'] = [start_time, end_time]
    if 'W' in days:
        d['W'] = [start_time, end_time]
    if 'R' in days:
        d['R'] = [start_time, end_time]
    if 'F' in days:
        d['F'] = [start_time, end_time]
 
    # Create timeslot for the course
    # Hard-coded semester (should be read in somehow)
    return Timeslot("FA14", d)

def parse_csv(csv_file):
    crn = []
    
    # Should add a way to skip the header line
    for row in csv_file:
        # Make sure AM and PM are in correct format
        # Assume that if meridian is not 'AM' or 'PM'
        #     set to 'AM'
        m = row['']
        if m != 'AM' and m != 'PM':
            m = 'AM'

        # Make sure HH:MM is in the correct format
        st = row['start_time']
        if st == '** TBA **':
            st = ''
        et = row['end_time']
        if et == '** TBA **':
            et = ''
        
        ts = parse_time(row['days'], st + m, et + m)

        # Create a new course
        # Initializing with no prereqs (need database with prereqs)
        c = Course(row['crn?'], ts, None, row['credit_hours'])
        
        crn.append(c)

    return crn

# There is an issue '10:00AM' & '11:00AM' times.
# Printing out as '010:00' & '011:00'
def convert_time(time):
    if time[-2:] == 'AM':
        if len(time.split(':')[0]) == 2:
            time = time[-len(time):-2]
        else:
            time = '0' + time[-len(time):-2]
    elif time[-2:] == 'PM':
        size = len(time)
        hours = int(time[-size:size - 5])
        if hours != 12:
            hours += 12
        time = str(hours) + time[-5:-2]
    return time

if __name__ == "__main__":
    load_available_courses('sis_class_schedule_fall_2014_CSCI.csv')

### For testing purposes
available_crn = load_available_courses('sis_class_schedule_fall_2014_CSCI.csv')
for c in available_crn:
    print c.CRN, c.timeslot.semester, c.timeslot.day_time, c.prereqs, c.credit_hours
