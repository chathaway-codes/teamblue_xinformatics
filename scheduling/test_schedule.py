import unittest

from schedule import *
from course import *
from timeslot import *
from requirement import Requirement

class TestSchedule(unittest.TestCase):
	def setUp(self):
		Course.reset_crn()
	
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
	
	def test_simple_schedule_with_prereqs(self):
		ts1 = Timeslot('FA12', {'M': ['09:00', '11:00'], 'R': ['09:00', '11:00']})
		ts2 = Timeslot('FA13', {'M': ['09:00', '11:00'], 'R': ['09:00', '11:00']})
		
		c1 = Course("CS101", ts1)
		c2 = Course("CS201", ts2, ["CS101"])
		
		schedule = make_schedule(["CS101", "CS201"], [])
		
		self.assertTrue(schedule != False)
		
		required_courses = ["CS101", "CS201"]
		self.assertEqual(len(schedule), len(required_courses))
		for c in schedule:
			required_courses.remove(c.CRN)
		self.assertEqual(len(required_courses), 0)

	def test_impossible_schedule_with_prereqs(self):
		ts1 = Timeslot('FA12', {'M': ['09:00', '11:00'], 'R': ['09:00', '11:00']})
		ts2 = Timeslot('FA13', {'M': ['09:00', '11:00'], 'R': ['09:00', '11:00']})
		
		c1 = Course("CS101", ts2)
		c2 = Course("CS201", ts1, ["CS101"])
		
		schedule = make_schedule(["CS101", "CS201"], [])
		
		self.assertTrue(schedule == False)

	def test_schedule_with_prereq_cycle(self):
		ts1 = Timeslot('FA12', {'M': ['09:00', '11:00'], 'R': ['09:00', '11:00']})
		ts2 = Timeslot('FA13', {'M': ['09:00', '11:00'], 'R': ['09:00', '11:00']})
		
		c1 = Course("CS101", ts1, ["CS201"])
		c2 = Course("CS201", ts2, ["CS101"])
		
		schedule = make_schedule(["CS101", "CS201"], [])
		
		self.assertTrue(schedule == False)
	
	def test_simple_schedule_with_prereqs_3_levels(self):
		ts1 = Timeslot('FA12', {'M': ['09:00', '11:00'], 'R': ['09:00', '11:00']})
		ts2 = Timeslot('FA13', {'M': ['09:00', '11:00'], 'R': ['09:00', '11:00']})
		ts3 = Timeslot('FA14', {'M': ['09:00', '11:00'], 'R': ['09:00', '11:00']})
		
		c1 = Course("CS101", ts1)
		c2 = Course("CS201", ts2, ["CS101"])
		c3 = Course("CS301", ts3, ["CS201"])
		
		schedule = make_schedule(["CS101", "CS201", "CS301"], [])
		
		self.assertTrue(schedule != False)
		
		required_courses = ["CS101", "CS201", "CS301"]
		self.assertEqual(len(schedule), len(required_courses))
		for c in schedule:
			required_courses.remove(c.CRN)
		self.assertEqual(len(required_courses), 0)
	
	def test_simple_schedule_with_not_possible_first_schedule(self):
		ts1 = Timeslot('FA12', {'M': ['09:00', '11:00'], 'R': ['09:00', '11:00']})
		ts2 = Timeslot('FA13', {'M': ['09:00', '11:00'], 'R': ['09:00', '11:00']})
		ts3 = Timeslot('FA14', {'M': ['09:00', '11:00'], 'R': ['09:00', '11:00']})
		ts4 = Timeslot('FA11', {'M': ['09:00', '11:00'], 'R': ['09:00', '11:00']})
		
		c4 = Course("CS301", ts4, ["CS201"])
		c1 = Course("CS101", ts1)
		c2 = Course("CS201", ts2, ["CS101"])
		c3 = Course("CS301", ts3, ["CS201"])
		
		schedule = make_schedule(["CS101", "CS201", "CS301"], [])
		
		self.assertTrue(schedule != False)
		
		required_courses = ["CS101", "CS201", "CS301"]
		self.assertEqual(len(schedule), len(required_courses))
		for c in schedule:
			required_courses.remove(c.CRN)
		self.assertEqual(len(required_courses), 0)
	
	def test_simple_schedule_with_electives(self):
		ts1 = Timeslot('FA12', {'M': ['09:00', '11:00'], 'R': ['09:00', '11:00']})
		ts2 = Timeslot('FA13', {'M': ['09:00', '11:00'], 'R': ['09:00', '11:00']})
		ts3 = Timeslot('FA14', {'M': ['09:00', '11:00'], 'R': ['09:00', '11:00']})
		ts4 = Timeslot('FA11', {'M': ['09:00', '11:00'], 'R': ['09:00', '11:00']})
		ts5 = Timeslot('FA11', {'T': ['09:00', '11:00'], 'F': ['09:00', '11:00']})
		ts6 = Timeslot('FA11', {'T': ['09:00', '11:00'], 'F': ['09:00', '11:00']})
		
		c1 = Course("CS101", ts1)
		c2 = Course("CS201", ts2, ["CS101"])
		c3 = Course("CS301", ts3, ["CS201"])
		c4 = Course("CS301", ts4, ["CS201"])
		c5 = Course("HU101", ts5)
		c5 = Course("HU102", ts6)
		
		schedule = make_schedule(["CS101", "CS201", "CS301", Requirement(["HU101", "HU102"])], [])
		
		self.assertTrue(schedule != False)
		
		required_courses = ["CS101", "CS201", "CS301", "HU101"]
		self.assertEqual(len(schedule), len(required_courses))
		for c in schedule:
			required_courses.remove(c.CRN)
		self.assertEqual(len(required_courses), 0)
	
	def test_simple_schedule_with_conflicting_elective(self):
		ts1 = Timeslot('FA12', {'M': ['09:00', '11:00'], 'R': ['09:00', '11:00']})
		ts2 = Timeslot('FA13', {'M': ['09:00', '11:00'], 'R': ['09:00', '11:00']})
		ts3 = Timeslot('FA14', {'M': ['09:00', '11:00'], 'R': ['09:00', '11:00']})
		ts4 = Timeslot('FA11', {'M': ['09:00', '11:00'], 'R': ['09:00', '11:00']})
		ts5 = Timeslot('FA11', {'T': ['09:00', '11:00'], 'F': ['09:00', '11:00']})
		
		c1 = Course("CS101", ts1)
		c2 = Course("CS201", ts2, ["CS101"])
		c3 = Course("CS301", ts3, ["CS201"])
		c4 = Course("CS301", ts4, ["CS201"])
		c5 = Course("HU101", ts1)
		c5 = Course("HU102", ts5)
		
		schedule = make_schedule(["CS101", "CS201", "CS301", Requirement(["HU101", "HU102"])], [])
		
		self.assertTrue(schedule != False)
		
		required_courses = ["CS101", "CS201", "CS301", "HU102"]
		self.assertEqual(len(schedule), len(required_courses))
		for c in schedule:
			required_courses.remove(c.CRN)
		self.assertEqual(len(required_courses), 0)
	
	def test_exceed_credits(self):
		ts1 = Timeslot('FA12', {'M': ['09:00', '11:00'], 'R': ['09:00', '11:00']})
		ts2 = Timeslot('FA12', {'T': ['09:00', '11:00'], 'F': ['09:00', '11:00']})
		ts3 = Timeslot('FA12', {'W': ['09:00', '11:00']})
		
		c1 = Course("CS101", ts1, credit_hours=7)
		c2 = Course("CS201", ts2, credit_hours=7)
		c3 = Course("CS301", ts3, credit_hours=7)
		
		schedule = make_schedule(["CS101", "CS201", "CS301"], [])
		
		self.assertFalse(schedule)
	
	def test_equal_credits(self):
		ts1 = Timeslot('FA12', {'M': ['09:00', '11:00'], 'R': ['09:00', '11:00']})
		ts2 = Timeslot('FA12', {'T': ['09:00', '11:00'], 'F': ['09:00', '11:00']})
		ts3 = Timeslot('FA12', {'W': ['09:00', '11:00']})
		
		c1 = Course("CS101", ts1, credit_hours=3)
		c2 = Course("CS201", ts2, credit_hours=3)
		c3 = Course("CS301", ts3, credit_hours=1)
		
		schedule = make_schedule(["CS101", "CS201", "CS301"], [])
		
		self.assertTrue(schedule)
	
	def test_extended_credits(self):
		ts1 = Timeslot('FA12', {'M': ['09:00', '11:00'], 'R': ['09:00', '11:00']})
		ts2 = Timeslot('FA12', {'T': ['09:00', '11:00'], 'F': ['09:00', '11:00']})
		ts3 = Timeslot('FA12', {'W': ['09:00', '11:00']})
		
		c1 = Course("CS101", ts1, credit_hours=7)
		c2 = Course("CS201", ts2, credit_hours=7)
		c3 = Course("CS301", ts3, credit_hours=7)
		
		schedule = make_schedule(["CS101", "CS201", "CS301"], [], max_credits=21)
		
		self.assertTrue(schedule)
