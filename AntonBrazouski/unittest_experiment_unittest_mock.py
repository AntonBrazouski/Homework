import argparse
from unittest import mock
from unittest_experiment_parser import parse_args

@mock.patch('argparse.ArgumentParser.parse_args',
            return_value=argparse.Namespace(kwarg1='--version'))
def test_command(mock_args):
    res = parse_args()
    assert res == 'version', "--version"

if __name__ == "__main__":
    print(parse_args())