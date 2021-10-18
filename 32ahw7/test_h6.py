import unittest
from h6 import count_absences, count_words_by_sentiment

class TestHomework6(unittest.TestCase):
    def test_count_absences_case1(self):
        seating_chart = [["Carly","Sam","Freddy","Drake","Josh"], ["Homer","Bart","Marge","Lisa","Maggie"], ["Robin","Starfire","Raven","Cyborg","Beast Boy"]]
        attendance = [["Carly","","Freddy","","Josh"], ["Homer","","Marge","Lisa","Maggie"], ["Starfire","Robin","Raven","Beast Boy","Cyborg"]]
        output = count_absences(seating_chart, attendance)
        self.assertEqual(output, 7)
    def test_count_absences_case2(self):
        seating_chart = [["Carly","Sam","Freddy","Drake","Josh"], ["Homer","Bart","Marge","Lisa","Maggie"], ["Robin","Starfire","Raven","Cyborg","Beast Boy"]]
        attendance = [["Sam","Carly","Freddy","","Josh"], ["Homer","","Marge","Lisa",""], ["Batman","Luna","Nevermore","Cyclops","Beast Man"]]
        output = count_absences(seating_chart, attendance)
        self.assertEqual(output, 10)

    def test_count_words_by_sentiment_case1(self):
        output = count_words_by_sentiment("I am glad to have this much fun")
        self.assertEqual(output, (2,0))

    def test_count_words_by_sentiment_case2(self):
        output = count_words_by_sentiment("I think it is wrong to win by dirty means.")
        self.assertEqual(output, (1,2))
        
    def test_count_words_by_sentiment_case3(self):
        output = count_words_by_sentiment("You are not mad. I am madly mad")
        self.assertEqual(output, (0, 2))

if __name__ == '__main__':
    unittest.main(verbosity=2)

