from timeslot import *

class Course:
	__courses_by_crn = {}
	
	def __init__(self, CRN, timeslot, prereqs=None):
		self.CRN = CRN
		self.timeslot = timeslot
		
		if prereqs != None:
			self.prereqs = prereqs
		else:
			self.prereqs = []
		
		if CRN in Course.__courses_by_crn:
			Course.__courses_by_crn[CRN] += [self]
		else:
			Course.__courses_by_crn[CRN] = [self]
	
	def can_take(self, courses):
		for r in self.prereqs:
			found = False
			for c in courses:
				# If we find a matching course, and it occured before this one
				if r == c.CRN and Timeslot.compare_semesters(c.timeslot.semester, self.timeslot.semester) == -1:
					found = True
					break
			if not found:
				return False
		return True
	
	@staticmethod
	def get_all_by_crn(CRN):
		return Course.__courses_by_crn[CRN]
	
	@staticmethod
	def reset_crn():
		Course.__courses_by_crn = {}
