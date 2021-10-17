import unittest
import rss_reader


class SimpleTest(unittest.TestCase):

    # returns True or False
    def test(self):
        self.assertTrue(True)
    
    def test_console(self): 
        rss_reader.get_console_input([
                                    "https://news.yahoo.com/rss/",
                                    
                                    ]) # error: L is required
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()