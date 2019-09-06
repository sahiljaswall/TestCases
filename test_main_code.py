import unittest

import main_code


class TestCaseMainCode(unittest.TestCase):
    def test_case_1(self):
        result = main_code.page_work('India')  # String with first uppercase alphabet
        self.assertTrue('New Delhi', result)

    def test_case_2(self):
        result = main_code.page_work('india')  # String with lowercase alphabets
        self.assertTrue('New Delhi', result)

    def test_case_3(self):
        result = main_code.page_work('INDIA')  # String with all uppercase alphabets
        self.assertTrue('New Delhi', result)

    def test_case_4(self):
        result = main_code.page_work('InDiA')  # String with uppercase and lowercase alphabets
        self.assertTrue('New Delhi', result)

    def test_case_5(self):
        result = main_code.page_work('Sri Lanka')  # String with two or more letters & Starting with  uppercase alphabets
        self.assertTrue('Colombia', result)

    def test_case_6(self):
        result = main_code.page_work('sri lanka')  # String with two or more letters & with all lowercase alphabets
        self.assertTrue('Colombia', result)

    def test_case_7(self):
        result = main_code.page_work('SRI LANKA')  # String with two or more letters & with all uppercase alphabets
        self.assertTrue('Colombia', result)

    def test_case_8(self):
        result = main_code.page_work('Srilanka')  # String with Invalid Country Name or Spelling Mistake
        self.assertTrue('Invalid Country Spelling Mistake', result)


if __name__ == '__main__':
    unittest.main()
