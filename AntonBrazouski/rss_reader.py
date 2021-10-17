import argparse
import urllib.request
import re
import json


def get_console_input():
    """ returns 'argparse.Namespace' """

    parser = argparse.ArgumentParser(description='RSS Parser')
    parser.add_argument(
                        'link',
                        metavar='L',
                        type=str,
                        help='link for rss feed'
                        )
    parser.add_argument(
                        '--version',
                        action='version',
                        version='RSS reader, version 0.1',
                        help="Print version info"
                        )

    parser.add_argument(
                        '--json',
                        action='store_true',
                        help='Print result as JSON in stdout'
    )

    parser.add_argument(
                        '-v', "--verbose",
                        action='store_true',
                        help='Outputs verbose status messages'
                        )

    parser.add_argument(
                        '--limit',
                        metavar='LIMIT',
                        type=int,
                        help='limit feed'
    )
    
    return parser.parse_args()


def print_news_from_argparse_namespase(args):
    """ prints RSS news to console """

    # --verbose
    if args.verbose:
        print(f"\t - Parsing rss link: {args.link}")

    # urllib --> vars
    url = args.link
    limit = args.limit
    
    # request n response --> bytes
    request_url = urllib.request.urlopen(url)
    resp_data = request_url.read()
    # print(type(resp_data))

    # news
    items = re.findall(r'<item>(.*?)</item>', str(resp_data))[0:limit]

    # db list and item dict
    data = []
    data_dict = {}

    # news to db
    for each_item in items:
        item = str(each_item)
        title = re.findall(r'<title>(.*?)</title>', str(each_item))[0]
        link = re.findall(r'<link>(.*?)</link>', item)[0]
        pub_date = re.findall(r'<pubDate>(.*?)</pubDate>', item)[0]
        data_dict['title'] = title
        data_dict['link'] = link
        data_dict['pub_date'] = pub_date

        data.append(data_dict)
        # print(data_dict)
        data_dict = {} # empty and reuse

    # json mode
    if args.json:
        if args.verbose:
            print('\t - JSON mode is ON')
        data_json = json.dumps(data)
        print(data_json)

    # usual news output - titles 
    else:
        for item in data:
            print(f"{item['title']}")



if __name__ == '__main__':
    user = get_console_input()
    print_news_from_argparse_namespase(user)