import unittest
from name import formatted_name
class NameTestCase(unittest.TestCase):
	def test_first_last_name(self):
		fname=formatted_name('manoj','kumar')
		self.assertEqual(fname,'manoj kumar')
if __name__ =='__main __':
	unittest.main()
