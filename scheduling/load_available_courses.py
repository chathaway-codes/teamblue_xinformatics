import csv

from course import Course
from timeslot import Timeslot

def load_available_courses(csv_file_name):
    # Opens available courses file
    f = open(csv_file_name)

    csv_f = csv.DictReader(f)

    available_crn = parse_csv(csv_f)

    f.close()

    return available_crn

def parse_csv(csv_file):
    crn = []
    
    for row in csv_file:
        # If meridian is not 'AM' or 'PM' set to 'AM'
        m = row['']
        if m != 'AM' and m != 'PM':
            m = 'AM'

        # If not in HH:MM format set to empty string
        st = check_time(row['start_time'])
        if st != '':
            st = st + m
        et = check_time(row['end_time'])
        if et != '':
            et = et + m
        
        ts = parse_time(row['days'], st, et)

        # Create course
        # Initializing with no prereqs (need database with prereqs)
        c = Course(row['crn?'], ts, None, row['credit_hours'])
        
        crn.append(c)

    return crn

def check_time(time):
    if ':' not in time:
        return ''
    else:
        hours = time.split(':')[0]
        minutes = time.split(':')[1]
        # Validate hours
        if ((len(hours) == 1 or len(hours) == 2) and \
            (int(hours) > 0 and int(hours) < 13)):
            # Validate minutes
            if (len(minutes) == 2 and \
                (int(minutes) > -1 and int(minutes) < 60)):
                return time
            else:
                return ''
        else:
            return ''

def parse_time(days, start_time, end_time):
    # Convert times from 12 hr to 24 hr
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

def convert_time(time):
    # Assumes time is in one of the following formats H:MMAM, H:MMPM,
    #     HH:MMAM, HH:MMPM
    if time[-2:] == 'AM':
        # Checks if hours is 2 digits, then truncates meridian
        if len(time.split(':')[0]) == 2:
            time = time.split('AM')[0]
        # If hour is 1 digit, add 0 before hour and truncate meridian
        else:
            time = '0' + time.split('AM')[0]
    # Changes PM times to correct 24 hr format and truncates meridian
    elif time[-2:] == 'PM':
        hours = int(time.split(':')[0])
        if hours != 12:
            hours += 12
        time = str(hours) + ':' + time.split(':')[1].split('PM')[0]
    return time

if __name__ == "__main__":
    load_available_courses('sis_class_schedule_fall_2014_CSCI.csv')

### For testing purposes
##available_crn = load_available_courses('sis_class_schedule_fall_2014_CSCI.csv')
##for c in available_crn:
##    print c.CRN, c.timeslot.semester, c.timeslot.day_time, c.prereqs, c.credit_hours
