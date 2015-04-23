import unittest

from load_available_courses import *

class LoadAvailableCoursesTests(unittest.TestCase):
    # Test check_time
    def test_invalid_minutes(self):
        self.assertRaises(Exception, check_time, '11:5')
    def test_invalid_hours(self):
        self.assertRaises(Exception, check_time, '13:50')
    def test_invalid_time(self):
        self.assertRaises(Exception, check_time, 'TBA')

    # Test decide_am_pm
    def test_can_fix_am_pm(self):
        start_time, end_time = decide_am_pm('11:00', '1:00', 'PM')
        self.assertEquals('11:00AM', start_time)
        self.assertEquals('1:00PM', end_time)
    def test_can_fix_am_pm2(self):
        start_time, end_time = decide_am_pm('11:00', '12:50', 'PM')
        self.assertEquals('11:00AM', start_time)
        self.assertEquals('12:50PM', end_time)
    def test_can_fix_pm_pm(self):
        start_time, end_time = decide_am_pm('12:00', '1:50', 'PM')
        self.assertEquals('12:00PM', start_time)
        self.assertEquals('1:50PM', end_time)
    def test_can_fix_less_than_hour(self):
        start_time, end_time = decide_am_pm('11:30', '12:29', 'PM')
        self.assertEquals('11:30AM', start_time)
        self.assertEquals('12:29PM', end_time)
    def test_can_fix_pm_am(self):
        start_time, end_time = decide_am_pm('11:30', '12:30', 'AM')
        self.assertEquals('11:30PM', start_time)
        self.assertEquals('12:30AM', end_time)
    def test_can_fix_am_am(self):
        start_time, end_time = decide_am_pm('12:00', '1:50', 'AM')
        self.assertEquals('12:00AM', start_time)
        self.assertEquals('1:50AM', end_time)

    # Test convert_time
    def test_can_convert_am1(self):
        self.assertEquals('00:01', convert_time('12:01AM'))
    def test_can_convert_am2(self):
        self.assertEquals('11:00', convert_time('11:00AM'))
    def test_can_convert_pm(self):
        self.assertEquals('13:00', convert_time('1:00PM'))
    def test_can_convert_pm2(self):
        self.assertEquals('12:01', convert_time('12:01PM'))
	
if __name__ == '__main__':
    unittest.main()
