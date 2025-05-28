import unittest
from name import formatted_name
class NameTestCase(unittest.TestCase):
	def test_first_last_name(self):
		fname=formatted_name('manoj','kumar')
		self.assertEqual(fname,'manoj kumar')
	def test_first_middle_last_name(self):
		fname=formatted_name('amit','yadav','kumar')
		self.assertEqual(fname,'amit kumar yadav')
if __name__ =='__main__':
	unittest.main()
