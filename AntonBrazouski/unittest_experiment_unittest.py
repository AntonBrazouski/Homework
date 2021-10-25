import unittest
from unittest_experiment_parser import parse_args

class SimpleTest(unittest.TestCase):

    def test_parser(self):
        
        parser = parse_args()
        self.assertTrue(True)

    def test_parser_2(self):
        parser = parse_args()

        #parser = parse_args('--version')
        #print(dir(parser))
        #print(parser._get_args())
        # parser = parse_args(['--version'])
        # self.assertTrue('RSS reader, version 0.1')
        # self.assertTrue(parser.version)
        # self.assertEqual(parser.version, 'RSS reader, version 0.1' )


if __name__ == '__main__':
    unittest.main()