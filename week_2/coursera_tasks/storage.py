import os
import json
import argparse
import tempfile


parser = argparse.ArgumentParser()
parser.add_argument("--key", action="store",
                    help="If it is the only argument - then it is used to get "
                         "values for that key. Otherwise it sets the key for "
                         "which the specified value should be stored")
parser.add_argument("--value", action="store",
                    help="Sets a value for the chosen key.")
args = parser.parse_args()
storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
if not os.path.exists(storage_path):
    with open(storage_path, 'w') as f:
        json.dump({}, f)


if args.value is None:
    with open(storage_path, 'r') as f:
        values = json.load(f)
    try:
        print(', '.join(list(map(str, values[args.key]))))
    except KeyError:
        print('None')
else:
    with open(storage_path, 'r') as f:
        values = json.load(f)

    try:
        values[args.key]
    except KeyError:
        values[args.key] = [args.value]
    else:
        values[args.key].append(args.value)

    with open(storage_path, 'w') as f:
        json.dump(values, f)
