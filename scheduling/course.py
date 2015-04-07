
class Course:
	__courses_by_crn = {}
	
	def __init__(self, CRN, timeslot):
		self.CRN = CRN
		self.timeslot = timeslot
		
		if CRN in Course.__courses_by_crn:
			Course.__courses_by_crn[CRN] += [self]
		else:
			Course.__courses_by_crn[CRN] = [self]
	
	@staticmethod
	def get_all_by_crn(CRN):
		return Course.__courses_by_crn[CRN]
