from timeslot import *

class Course:
	__courses_by_crn = {}
	initialized = False

	def __init__(self, CRN, timeslot, prereqs=None, credit_hours=3):
		self.CRN = CRN
		self.timeslot = timeslot
		self.credit_hours = credit_hours

		Course.initialized = True

		if prereqs != None:
			self.prereqs = prereqs
		else:
			self.prereqs = []

		if CRN in Course.__courses_by_crn:
			Course.__courses_by_crn[CRN] += [self]
		else:
			Course.__courses_by_crn[CRN] = [self]

	def can_take(self, courses, credit_hour_limit=15):
		for r in self.prereqs:
			if r == '':
				continue
			found = False
			for c in courses:
				# If we find a matching course, and it occured before this one
				if r == c.CRN and Timeslot.compare_semesters(c.timeslot.semester, self.timeslot.semester) == -1:
					found = True
					break
			if not found:
				return False
		# Do we exceed credit hour limit?
		credits_so_far = self.credit_hours
		for c in courses:
			if c.timeslot.semester == self.timeslot.semester:
				credits_so_far += c.credit_hours
		if credits_so_far > credit_hour_limit:
			return False
		return True

	@staticmethod
	def get_all_by_crn(CRN):
		return Course.__courses_by_crn[CRN]

	@staticmethod
	def reset_crn():
		Course.__courses_by_crn = {}
		Course.initialized = False
