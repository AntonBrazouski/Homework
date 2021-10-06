import argparse


parser = argparse.ArgumentParser(description='RSS Parser')
parser.add_argument('link', metavar='L', type=str',
                    help='link for rss feed')