import argparse
import urllib.request
import re
import json


def get_console_input():
    """ return 'argparse.Namespace' """

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
                        version='RSS reader, version 0.2',
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
    """ print RSS news to console """
    url = args.link
    limit = args.limit

    if args.limit and args.verbose:
        print(f"\t * Showing {args.limit} news items")

    # --verbose
    if args.verbose:
        print(f"\t * Parsing rss link: {args.link}")

    # urllib --> vars

    
    # request n response --> bytes
    request_url = urllib.request.urlopen(url)
    resp_data = request_url.read()

    # print(type(resp_data))
    # print()


    # catch rss version
    rss_tag = re.findall(r'<rss(.*?)>',str(resp_data))[0]
    # if not rss_tag:
    #     print('\t * Link is fully supported RSS feed')
    # print(rss_tag)
    rss_version = re.findall(r'version="(.*?)"', str(rss_tag))[0]
    
    if args.verbose:
        print(f"\t * RSS {rss_version}")

    # print(rss_tag)
    is_rss_version_2 = '2.0' in rss_tag
    # print(is_rss_version_2)

    # channel info
    channel = re.findall(r'<title>(.*?)</title>', str(resp_data))[0]
    if args.verbose:
        print(f"\t * {channel}")

    # news items --limit
    items = re.findall(r'<item>(.*?)</item>', str(resp_data))[0:limit]

    pub_date = re.findall(r'<pubDate>(.*?)</pubDate>', str(resp_data))[0]
    if args.verbose:
        print(f"\t * Updated: {pub_date}")
    
    # db list and item dict
    data = []
    data_dict = {}

    # news to data list of dicts
    for each_item in items:
        # print('\n' + each_item)
        item = str(each_item)
        title = re.findall(r'<title>(.*?)</title>', str(each_item))[0]
        link = re.findall(r'<link>(.*?)</link>', item)[0]
        pub_date = re.findall(r'<pubDate>(.*?)</pubDate>', item)[0]
        # title = re.sub(r'[\xe2]', '', title)
        data_dict['title'] = title
        data_dict['link'] = link
        data_dict['pub_date'] = pub_date

        data.append(data_dict)
        # print(data_dict)
        data_dict = {} # empty and reuse

    # json mode
    if args.json:
        if args.verbose:
            print('\t * JSON mode is ON')
        data_json = json.dumps(data)
        print(data_json)

    # default news output - titles 
    else:
        for item in data:
            if args.verbose:
                print(f"{item['title']} -- {item['pub_date']}")
                print(f"\t{item['link']}")
            else:
                print(f"{item['title']}")



if __name__ == '__main__':
    user = get_console_input()
    print_news_from_argparse_namespase(user)

