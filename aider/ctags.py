import os
import json
import sys

from aider.dump import dump

def print_tags_info(filename):
    tags = sorted(get_tags(filename))

    last = [None] * len(tags[0])
    tab = ' '
    for tag in tags:
        tag = list(tag)
        common_prefix = [
            tag_i for tag_i,last_i in zip(tag,last)
            if tag_i == last_i
        ]
        num_common = len(common_prefix)
        indent = tab * num_common
        rest = tag[num_common:]
        for item in rest:
            print(indent + item)
            indent += tab
        last = tag


def get_tags(filename):
    with open(filename, "r") as tags_file:
        for line in tags_file:
            tag = json.loads(line)
            path = tag.get("path")
            scope = tag.get("scope")
            kind = tag.get("kind")
            name = tag.get("name")
            signature = tag.get("signature")

            last = name
            if signature:
                last += ' ' + signature

            path = os.path.relpath(path, os.getcwd())

            res = []
            if scope:
                res.append(scope)
            res += [kind, last]

            yield res


if __name__ == "__main__":
    for filename in sys.argv[1:]:
        print_tags_info(filename)