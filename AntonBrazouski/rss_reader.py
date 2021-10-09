import argparse


parser = argparse.ArgumentParser(description='RSS Parser')
parser.add_argument('link', metavar='L', type=str,
                    help='link for rss feed')
parser.add_argument("--version", action="store_true",
                    help="Print version info")

parser.add_argument('-v', "--verbose", action='store_true',
                    help='Outputs verbose status messages')

args = parser.parse_args()

if args.verbose:
    print(f"parsing rss link: {args.link}")