import unittest

from timeslot import *

class TestTimeslotMethods(unittest.TestCase):
	def test_no_conflict_semester(self):
		slot1 = Timeslot('FA12', {'M': ['09:00', '11:00'], 'R': ['09:00', '11:00']})
		slot2 = Timeslot('FA13', {'M': ['09:00', '11:00'], 'R': ['09:00', '11:00']})
		
		self.assertFalse(slot1.conflicts(slot2))
		
	def test_no_conflict_day(self):
		slot1 = Timeslot('FA12', {'M': ['09:00', '11:00'], 'R': ['09:00', '11:00']})
		slot2 = Timeslot('FA12', {'T': ['09:00', '11:00'], 'F': ['09:00', '11:00']})
		
		self.assertFalse(slot1.conflicts(slot2))
		
	def test_no_conflict_hours(self):
		slot1 = Timeslot('FA12', {'M': ['09:00', '11:00'], 'R': ['09:00', '11:00']})
		slot2 = Timeslot('FA12', {'M': ['12:00', '14:00'], 'R': ['12:00', '14:00']})
		
		self.assertFalse(slot1.conflicts(slot2))
		
	def test_no_conflict_hours_exact(self):
		slot1 = Timeslot('FA12', {'M': ['09:00', '11:00'], 'R': ['09:00', '11:00']})
		slot2 = Timeslot('FA12', {'M': ['11:00', '14:00'], 'R': ['11:00', '14:00']})
		
		self.assertFalse(slot1.conflicts(slot2))
		
	def test_conflict_hours(self):
		slot1 = Timeslot('FA12', {'M': ['09:00', '11:00'], 'R': ['09:00', '11:00']})
		slot2 = Timeslot('FA12', {'M': ['09:00', '14:00'], 'R': ['09:00', '14:00']})
		
		self.assertTrue(slot1.conflicts(slot2))
		
	def test_conflict_hours_inclusive(self):
		slot1 = Timeslot('FA12', {'M': ['09:00', '11:00'], 'R': ['09:00', '11:00']})
		slot2 = Timeslot('FA12', {'M': ['10:00', '14:00'], 'R': ['10:00', '14:00']})
		
		self.assertTrue(slot1.conflicts(slot2))
		
	def test_conflict_hours_inclusive2(self):
		slot1 = Timeslot('FA12', {'M': ['09:00', '12:00'], 'R': ['09:00', '12:00']})
		slot2 = Timeslot('FA12', {'M': ['10:00', '11:00'], 'R': ['10:00', '11:00']})
		
		self.assertTrue(slot2.conflicts(slot1))
	
	def test_compare_semesters(self):
		self.assertEqual(Timeslot.compare_semesters("FA12", "FA13"), -1)
		self.assertEqual(Timeslot.compare_semesters("FA12", "FA12"), 0)
		self.assertEqual(Timeslot.compare_semesters("FA13", "FA12"), 1)
		
		self.assertEqual(Timeslot.compare_semesters("SP12", "FA12"), -1)
		self.assertEqual(Timeslot.compare_semesters("FA12", "FA12"), 0)
		self.assertEqual(Timeslot.compare_semesters("FA12", "SU12"), 1)
