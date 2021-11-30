import argparse

parser = argparse.ArgumentParser()

"""..."""

parser.add_argument('--method', '-m',
                    action='store',
                    help='Method to make request',
                    default='GET')

parser.add_argument('--url', '-u',
                    action='store',
                    help='Url to make request to',
                    required=True)

parser.add_argument('--true','-t',
                    action='store_true',
                    help='True of false param',
                    required=False)

parser.add_argument('--save','-s',
                    action='append_const',
                    const='const_to_save',
                    dest='const_collection',
                    default=[],
                    help='Store param in list',
                    required=False)

args = parser.parse_args()

print(args)