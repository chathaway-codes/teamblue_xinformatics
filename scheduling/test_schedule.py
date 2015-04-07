import unittest

from schedule import *
from course import *
from timeslot import *

class TestSchedule(unittest.TestCase):
	def setUp(self):
		Course.__courses_by_crn = {}
	
	def test_simple_schedule(self):
		ts1 = Timeslot('FA12', {'M': ['09:00', '11:00'], 'R': ['09:00', '11:00']})
		ts2 = Timeslot('FA13', {'M': ['09:00', '11:00'], 'R': ['09:00', '11:00']})
		
		c1 = Course("CS101", ts1)
		c2 = Course("CS201", ts2)
		
		schedule = make_schedule(["CS101", "CS201"], [])
		
		self.assertTrue(schedule != False)
		
		required_courses = ["CS101", "CS201"]
		self.assertEqual(len(schedule), len(required_courses))
		for c in schedule:
			required_courses.remove(c.CRN)
		self.assertEqual(len(required_courses), 0)
	
	def test_simple_conflict_schedule(self):
		ts1 = Timeslot('FA12', {'M': ['09:00', '11:00'], 'R': ['09:00', '11:00']})
		ts2 = Timeslot('FA13', {'M': ['11:00', '13:00'], 'R': ['11:00', '13:00']})
		
		c1 = Course("CS101", ts1)
		c2 = Course("CS201", ts1)
		c3 = Course("CS101", ts2)
		c4 = Course("CS201", ts2)
		
		schedule = make_schedule(["CS101", "CS201"], [])
		
		self.assertTrue(schedule != False)
		
		required_courses = ["CS101", "CS201"]
		self.assertEqual(len(schedule), len(required_courses))
		for c in schedule:
			required_courses.remove(c.CRN)
		self.assertEqual(len(required_courses), 0)
	
	def test_impossible_schedule(self):
		ts1 = Timeslot('FA12', {'M': ['09:00', '11:00'], 'R': ['09:00', '11:00']})
		
		c1 = Course("CS101", ts1)
		c2 = Course("CS201", ts1)
		
		schedule = make_schedule(["CS101", "CS201"], [])
		
		self.assertTrue(schedule == False)
