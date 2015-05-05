from course import Course

class Requirement:
	"""Represents a single requirement; if any of the courses are satisfied,
	the requirement is complete"""
	def __init__(self, valid_courses):
		self.valid_courses = valid_courses

	def get_worst_crn(self):
		lowest = self.valid_courses[0]
		for c in self.valid_courses[1:]:
			if len(Course.get_all_by_crn(c)) < len(Course.get_all_by_crn(lowest)):
				lowest = c
		return len(Course.get_all_by_crn(lowest))

	def satisfies(self, course):
		return course in self.valid_courses

	def satisfied(self, list_of_courses):
		for course in self.valid_courses:
			if course in list_of_courses:
				return True
		return False


	def __repr__(self):
		return repr(self.valid_courses)
