import hashlib
import argparse

def hash_item(item):
    encoded_item = item.encode('utf-8')
    hash_obj = hashlib.sha256(encoded_item)
    hex_dig = hash_obj.hexdigest()
    return hex_dig

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--item')
    args = parser.parse_args()
    print(hash_item(args.item))
