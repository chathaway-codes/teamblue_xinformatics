from course import Course
from requirement import Requirement

def make_schedule(requirements, taken_courses=[], max_credits=15):
	"""Given a list of required course CRN's (or requirements), and taken course CRN's
	return a list of courses to take or False if it's not possible"""
	# Turn non-requirements into requirements
	for i, item in enumerate(requirements):
		if isinstance(item, basestring):
			requirements[i] = Requirement([item])

	# Remove taken courses from required courses
	requirements = [item for item in requirements if not item.satisfied(taken_courses)]

	# Sort required by the number of courses offered (fewer courses offered = more constrained)
	sorted(requirements, cmp=lambda a, b: a.get_worst_crn() < b.get_worst_crn())

	print "requirements: ", requirements
	print "taken_courses: ", taken_courses

	def __make_schedule(requirements, current_schedule):
		if len(requirements) == 0:
			return current_schedule

		requirement = requirements[0]
		requirements = requirements[1:]

		for course in requirement.valid_courses:
			if len(Course.get_all_by_crn(course)) == 0:
				raise Exception("No class in catalog; %s" % course)
			for c in Course.get_all_by_crn(course):
				# Check to see if this course conflicts with anything
				conflicts = False
				for c2 in current_schedule:
					if c.timeslot.conflicts(c2.timeslot):
						conflicts = True
						break

				if not conflicts:
					# Make sure we can take it, then recurse
					schedule = []
					if not c.can_take(current_schedule, credit_hour_limit=max_credits):
						schedule =  __make_schedule(requirements, current_schedule)
						if schedule == False:
							continue
						# If we still can't take it, continue
						if not c.can_take(schedule, credit_hour_limit=max_credits):
							continue
						schedule += [c]
					else:
						schedule = __make_schedule(requirements, current_schedule + [c])
					if schedule != False:
						return schedule
		return False

	return __make_schedule(requirements, [])
