import unittest
import warnings
from Project2_1 import get_trending_tweets
from Project2_2 import sample_classify_text


class Test_Get_Trending_Tweets(unittest.TestCase):

    def test_not_empty(self):
        self.assertNotEqual(get_trending_tweets(), '')


class Test_sample_classify_text(unittest.TestCase):

    def test_not_empty(self):
        self.assertNotEqual(sample_classify_text(get_trending_tweets()), '')

    def test_classify_function(self):
        self.assertNotEqual(sample_classify_text("Former president and first lady Donald and Melania Trump attend "
                                                 "Game 4 of the World Series between the Astros and Braves"),
                            '/News/Politics')

    def test_classify_error_case(self):
        self.assertRaises(Exception, sample_classify_text(""))


if __name__ == '__main__':
    warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)
    unittest.main()
