import csv

from course import Course
from timeslot import Timeslot

def load_available_courses(csv_file_name):
    # Open available courses file
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

        # Read in start and end time
        st = check_time(row['start_time'])
        et = check_time(row['end_time'])

        # Give start time correct meridian
        st, et = decide_am_pm(st, et, m)

        # Create a timeslot 
        ts = parse_time(row['days'], st, et)

        # Create course
        # Initialize with no prereqs (need database with prereqs)
        c = Course(row['crn?'], ts, None, row['credit_hours'])
        
        crn.append(c)

    return crn

def check_time(time):
    if ':' not in time:
        raise Exception('Invalid time string')
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
                raise Exception('Invalid minutes')
        else:
            raise Exception('Invalid hours')

def decide_am_pm(time1, time2, me):
    h1 = int(time1.split(':')[0])
    h2 = int(time2.split(':')[0])

    if h2 < h1 or h2 == 12:
        if me == 'AM':
            if h1 == 12:
                yield time1 + 'AM'
            else:
                yield time1 + 'PM'
        else:
            if h1 == 12:
                yield time1 + 'PM'
            else:
                yield time1 + 'AM'
    else:
        yield time1 + me
    yield time2 + me

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
    # Hard-code semester (should be read in somehow)
    return Timeslot("FA14", d)

def convert_time(time):
    # time should be in one of the following formats:
    #     H:MMAM, H:MMPM, HH:MMAM, HH:MMPM
    h = int(time.split(':')[0])
    me = time[-2:].upper()
    m = int(time.split(':')[1].split(me)[0])

    if me == '':
        raise Exception('No AM or PM specified')

    # Change 12AM to correct 24 hr format
    if me == 'AM' and h == 12:
        h = 0
    # Change PM time to correct 24 hr format
    elif me == 'PM':
        if h != 12:
            h += 12
    
    return "%02d:%02d" % (h, m)

if __name__ == "__main__":
    load_available_courses('sis_class_schedule_fall_2014_CSCI.csv')

# For testing purposes
##available_crn = load_available_courses('sis_class_schedule_fall_2014_CSCI.csv')
##for c in available_crn:
##    print c.CRN, c.timeslot.semester, c.timeslot.day_time, c.prereqs, c.credit_hours
