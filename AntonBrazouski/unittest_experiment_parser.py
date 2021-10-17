import argparse
import sys



def parse_args(args):
    parser = argparse.ArgumentParser()

    # parser.add_argument(
    #                 'link',
    #                 metavar='L',
    #                 type=str,
    #                 help='link for rss feed'
    #                 )

    parser.add_argument(                        
                        '--version',
                        action='version',
                        version='RSS reader, version 0.1',
                        help="Print version info"
                        )
    
    return parser.parse_args(args) 


parser = parse_args(sys.argv[1:])
