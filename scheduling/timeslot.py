class Timeslot:
	def __init__(self, semester, day_time):
		"""Expects semester to look like:
			- "FA12"
			- "SP12"
			- "SU12"
		and day_time to look like:
			- {'M': ['05:00', '07:00'], 'R': ['05:00', '07:00']}
		with the day being one of {Monday, Tuesday, Wednesday, thuRsday, Friday, Saturday, sUnday}
		The hours should be encoded in military time (24 hr)
		"""
		self.semester = semester
		self.day_time = day_time
	
	def __compare_times(self, time1, time2):
		"""Returns -1 if time 1 is before time 2, 0 if they are the same time
		and 1 if time 2 is before time 1"""
		h1, m1 = map(lambda n: int(n), time1.split(':'))
		h2, m2 = map(lambda n: int(n), time2.split(':'))
		if h1 < h2:
			return -1
		if h2 < h1:
			return 1
		else:
			if m1 < m2:
				return -1
			if m2 < m1:
				return 1
		return 0
	
	def conflicts(self, other):
		"""Given another timeslot, returns true if there is a schedule
		conflict with this timeslot, false otherwise"""
		if other.semester != self.semester:
			return False
		
		for key, value in self.day_time.iteritems():
			if key in other.day_time:
				start1 = value[0]
				start2 = other.day_time[key][0]
				
				end1 = value[1]
				end2 = other.day_time[key][1]
				
				# Check if there is any overlap
				# Start time is between end and start time of the other, or vice versa
				if self.__compare_times(start1, start2) == -1 and \
					self.__compare_times(start2, end1) == -1:
					return True
				if self.__compare_times(start2, start1) == -1 and \
					self.__compare_times(start1, end2) == -1:
					return True
				
				# If they start at the same time, there is a conflict
				#  (but if one ends just as the next starts, fine)
				if self.__compare_times(start1, start2) == 0:
					return True
		return False
