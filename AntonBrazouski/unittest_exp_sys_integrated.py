import argparse
import unittest

class SweepTestCase(unittest.TestCase):
    """ Tests that the parse class works correctly """

    def setUp(self):
        self.parser=argparse.ArgumentParser()
        self.parser.add_argument(
            "-c", "--color",
            type=str,
            choices=["yellow", "blue"],
            required=True)

        self.parser.add_argument(
                    'link',
                    metavar='L',
                    type=str,
                    help='link for rss feed'
                    )
        
    def test_required_unknown(self):
        """ Try to perform sweep on something that isn't an option """
        args = ["--color", "NASA"]
        with self.assertRaises(SystemExit):
            self.parser.parse_args(args)

    def test_argparse(self):
        args = ["link", "-c", "blue"]
        x = self.parser.parse_args(args)
        print(x)

    # def test_something_new(self):
    #     args = ["-c", "yellow"]
    #     x = self.parser.parse_args(args)
    #     # print(x)
    #     # assert x == 'yellow', 'yellow'

    # def test_yellow(self):
    #     args = ['--color', 'yellow']
    #     x =self.parser.parse_args(args)
    #     print(x)

    # def test_something_bad(self):
    #     args = ["-f", "bad input"]
    #     self.parser.parse_args(args)


if __name__ == '__main__':
    unittest.main()