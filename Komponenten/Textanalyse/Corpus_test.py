import unittest

from Corpus import Corpus
class CorpusTest(unittest.TestCase):
    def setUp(self):
        self.filename = 'test.csv'
        self.corpus = Corpus(self.filename)
    def test_read_csv_file(self):
        rows = self.corpus.read_csv_file()
        expected_rows = [['Ein wunderbarer Tag.'], ['Ich mag Eis.'], ['Das Wetter ist scheisse.']]
        self.assertEqual(rows[:3], expected_rows)




"""class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)  # add assertion here"""


if __name__ == '__main__':
    unittest.main()
