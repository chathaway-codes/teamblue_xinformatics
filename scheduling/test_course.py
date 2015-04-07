import unittest

from course import Course
from timeslot import Timeslot

class TestCourseMethods(unittest.TestCase):
	def setUp(self):
		Course.reset_crn()
	
	def test_get_courses_by_crn(self):
		# Timeslot can be empty for this
		c1 = Course("CSCI2121", None)
		c2 = Course("CSCI2121", None)
		c3 = Course("CSCI2121", None)
		c4 = Course("CSCI2122", None)
		
		self.assertEquals(3, len(Course.get_all_by_crn("CSCI2121")))

	def test_course_can_take(self):
		ts1 = Timeslot('FA12', {'M': ['09:00', '11:00'], 'R': ['09:00', '11:00']})
		ts2 = Timeslot('FA13', {'M': ['09:00', '11:00'], 'R': ['09:00', '11:00']})
		ts3 = Timeslot('FA14', {'M': ['09:00', '11:00'], 'R': ['09:00', '11:00']})
		
		c1 = Course("CS101", ts1)
		c2 = Course("CS201", ts2, ["CS101"])
		c3 = Course("CS101", ts3)
		
		self.assertFalse(c2.can_take([]))
		
		self.assertTrue(c2.can_take([c1]))
		
		self.assertFalse(c2.can_take([c3]))
