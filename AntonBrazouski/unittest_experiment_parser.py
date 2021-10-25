import argparse
import sys



def parse_args():
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
    
    args = parser.parse_args() 
    print(args)
    return args


parser = parse_args()
