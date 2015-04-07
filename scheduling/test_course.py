import unittest

from course import Course

class TestCourseMethods(unittest.TestCase):
	def setUp(self):
		Course.__courses_by_crn = {}
	
	def test_get_courses_by_crn(self):
		# Timeslot can be empty for this
		c1 = Course("CSCI2121", None)
		c2 = Course("CSCI2121", None)
		c3 = Course("CSCI2121", None)
		c4 = Course("CSCI2122", None)
		
		self.assertEquals(3, len(Course.get_all_by_crn("CSCI2121")))
