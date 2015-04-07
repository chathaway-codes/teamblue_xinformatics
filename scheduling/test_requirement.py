import unittest

from requirement import *

class TestRequirementMethods(unittest.TestCase):
	def test_satisfies(self):
		r = Requirement(['CS101', 'CS201'])
		
		self.assertTrue(r.satisfies('CS101'))
		self.assertFalse(r.satisfies('CS102'))
		
	def test_satisfied(self):
		r = Requirement(['CS101', 'CS201'])
		
		self.assertTrue(r.satisfied(['CS101']))
		self.assertFalse(r.satisfied(['CS102']))
