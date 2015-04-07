from requirement import *
from timeslot import *
from course import *
from schedule import *

humel1 = Requirement(['HUM101', 'HUM102', 'HUM103', 'HUM104'])
humel2 = Requirement(['HUM201', 'HUM202', 'HUM203', 'HUM204'])
humel3 = Requirement(['HUM301', 'HUM302', 'HUM303', 'HUM304'])
humel4 = Requirement(['HUM401', 'HUM402', 'HUM403', 'HUM404'])

mathel1 = Requirement(['MAT 2000', 'MAT 2020', 'MAT 2030', 'MAT 2040'])
mathel2 = Requirement(['MAT 2100', 'MAT 2120', 'MAT 2130', 'MAT 2140'])

required_courses = [
	humel1,
	"CSCI 1100",
	"MATH 1010",
	"PHYS 1100",
	humel2,
	"CSCI 1200",
	"MATH 1020",
	"MATH 2800",
	humel3,
	"BIOL 1010",
	"CSCI 2300",
	"CSCI 2500",
	mathel1,
	mathel2,
	humel4,
	"CSCI 2400"
]

# Contruct a list of courses and when they're offered... We have 6 time slots a semester
semesters = ["FA16", "SP17", "FA17", "SP18"]
time_slots = [ 
	{'M': ['09:00', '11:00'], 'R': ['09:00', '11:00']},
	{'T': ['09:00', '11:00'], 'F': ['09:00', '11:00']},
	{'M': ['13:00', '14:00'], 'R': ['13:00', '14:00']},
	{'T': ['13:00', '14:00'], 'F': ['13:00', '14:00']},
	{'M': ['14:00', '16:00'], 'R': ['14:00', '16:00']},
	{'T': ['14:00', '16:00'], 'F': ['14:00', '16:00']}
]

timeslots = []

for s in semesters:
	for t in time_slots:
		timeslots += [Timeslot(s, t)]

courses = [
	Course("CSCI 1100", timeslots[0], credit_hours=4),
	Course("MATH 1010", timeslots[1], credit_hours=4),
	Course("PHYS 1100", timeslots[2], credit_hours=4),
	Course("CSCI 1200", timeslots[6], credit_hours=4),
	Course("MATH 1020", timeslots[7], credit_hours=4),
	Course("MATH 2800", timeslots[8], credit_hours=4),
	Course("BIOL 1010", timeslots[12], credit_hours=4),
	Course("CSCI 2300", timeslots[13], credit_hours=4),
	Course("CSCI 2500", timeslots[14], credit_hours=4),
	Course("CSCI 2400", timeslots[18], credit_hours=4),
	
	Course("HUM101", timeslots[3], credit_hours=4),
	Course("HUM102", timeslots[4], credit_hours=4),
	Course("HUM103", timeslots[5], credit_hours=4),
	Course("HUM104", timeslots[1], credit_hours=4),
	
	Course("HUM201", timeslots[9], credit_hours=4),
	Course("HUM202", timeslots[10], credit_hours=4),
	Course("HUM203", timeslots[11], credit_hours=4),
	Course("HUM204", timeslots[12], credit_hours=4),
	
	Course("HUM301", timeslots[15], credit_hours=4),
	Course("HUM302", timeslots[16], credit_hours=4),
	Course("HUM303", timeslots[17], credit_hours=4),
	Course("HUM304", timeslots[15], credit_hours=4),
	
	Course("HUM401", timeslots[19], credit_hours=4),
	Course("HUM402", timeslots[20], credit_hours=4),
	Course("HUM403", timeslots[21], credit_hours=4),
	Course("HUM404", timeslots[22], credit_hours=4),
	
	Course("MAT 2000", timeslots[19], credit_hours=4),
	Course("MAT 2020", timeslots[20], credit_hours=4),
	Course("MAT 2030", timeslots[21], credit_hours=4),
	Course("MAT 2040", timeslots[22], credit_hours=4),
	
	Course("MAT 2100", timeslots[19], credit_hours=4),
	Course("MAT 2120", timeslots[20], credit_hours=4),
	Course("MAT 2130", timeslots[21], credit_hours=4),
	Course("MAT 2140", timeslots[22], credit_hours=4),
]

# Once all the courses have been setup, computer the schedule
my_schedule = make_schedule(required_courses, [], max_credits=16)

for s in semesters:
	print "============================"
	print s
	print "============================"
	for c in my_schedule:
		if c.timeslot.semester == s:
			print c.CRN, c.timeslot.day_time
	print ""

