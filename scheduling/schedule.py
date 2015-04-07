from course import Course

def make_schedule(required_courses, taken_courses=[]):
	"""Given a list of required course CRN's, and taken course CRN's
	return a list of courses to take or False if it's not possible"""
	# First, remove taken courses from required courses
	required_courses = [item for item in required_courses if item not in taken_courses]
	
	# Sort required by the number of courses offered (fewer courses offered = more constrained)
	sorted(required_courses, cmp=lambda a, b: len(Course.get_all_by_crn(a)) < len(Course.get_all_by_crn(b)))
	
	def __make_schedule(required_courses, current_schedule):
		if len(required_courses) == 0:
			return current_schedule
		
		course = required_courses[0]
		required_courses = required_courses[1:]
		
		# If we can't take this course, let the rest of the schedule be made and try again
		if len(Course.get_all_by_crn(course)) > 0 and \
			not Course.get_all_by_crn(course)[0].can_take(current_schedule):
			current_schedule = __make_schedule(required_courses, current_schedule)
			if current_schedule == False:
				return False
			if not Course.get_all_by_crn(course)[0].can_take(current_schedule):
				return False
		
		for c in Course.get_all_by_crn(course):
			# Check to see if this course conflicts with anything
			conflicts = False
			for c2 in current_schedule:
				if c.timeslot.conflicts(c2.timeslot):
					conflicts = True
					break
			
			if not conflicts:
				schedule = __make_schedule(required_courses, current_schedule + [c])
				if schedule != False:
					return schedule
		return False
	
	return __make_schedule(required_courses, taken_courses)
		
		
