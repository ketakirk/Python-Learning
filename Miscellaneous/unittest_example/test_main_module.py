import main_module as mm
import unittest

class TestMainModule(unittest.TestCase):
	def test_seconds_to_isotimestamp_typical(self):
		ts_in = 1443323282
		expected = "2015-09-26 20:08:02"
		returned = mm.seconds_to_isotimestamp(ts_in)
		self.assertEqual(
			expected, 
			returned,
			"Expected: %s, returned %s" %(expected, returned)
		)

	def test_seconds_to_isotimestamp_millis(self):
		ts_in = 1443323282555
		self.assertRaises(ValueError, mm.seconds_to_isotimestamp, ts_in)		
		
	def test_remove_vowels_typical(self):
		str_in = "Hello my Name is Mr President"
		expected = "Hll my Nm s Mr Prsdnt"
		returned = mm.remove_vowels(str_in)
		self.assertEqual(
			expected, 
			returned,
			"Expected: %s, returned %s" %(expected, returned)
		)
	
	def test_remove_vowels_allvowels(self):
		str_in = "AEIOUaeiou"
		expected = ""
		returned = mm.remove_vowels(str_in)
		self.assertEqual(
			expected, 
			returned,
			"Expected: %s, returned %s" %(expected, returned)
		)

	def test_remove_vowels_novowels(self):
		str_in = "Strskyzzz"
		expected = "Strskyzzz"
		returned = mm.remove_vowels(str_in)
		self.assertEqual(
			expected, 
			returned,
			"Expected: %s, returned %s" %(expected, returned)
		)		
	
	def test_remove_odds_typical(self):
		list_in = range(100)
		expected = range(0, 100, 2)
		returned = mm.remove_odds(list_in)
		self.assertEqual(
			expected, 
			returned,
			"Expected: %s, returned %s" %(expected, returned)
		)	

	def test_remove_odds_allevens(self):
		list_in = range(0, 100, 2)
		expected = range(0, 100, 2)
		returned = mm.remove_odds(list_in)
		self.assertEqual(
			expected, 
			returned,
			"Expected: %s, returned %s" %(expected, returned)
		)					

	def test_remove_odds_allodds(self):
		list_in = range(1, 101, 2)
		expected = []
		returned = mm.remove_odds(list_in)
		self.assertEqual(
			expected, 
			returned,
			"Expected: %s, returned %s" %(expected, returned)
		)

if __name__ == '__main__':
	unittest.main()
