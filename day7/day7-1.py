"""
$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k
"""

from rich import print
from copy import copy

def get_input():
    with open("./day7.input") as directory_listing:
        return directory_listing.read().split("\n")


def get_sizes(directory_tree):
    directory_sizes = []
    current_dict = copy(directory_tree)
    for name, struct in current_dict.items():
        if type(struct) == dict:
            _directory_tree, _directory_sizes = copy(get_sizes(struct))
            if "_size" in current_dict:
                size = _directory_tree["_size"]
                directory_tree["_size"] = size
            else:
                size = 0
            directory_sizes.append({name: size})
            directory_sizes += _directory_sizes
            continue

        directory_tree["_size"] += struct

    # fix the outer most _size this could probably be done above but I can't
    # figure out what im doing wrong
    if "_size" in directory_tree:
        total_size = 0

        for key, _struct in directory_tree.items():
            if type(_struct) == dict:
                total_size += _struct["_size"]
                continue
            if key != "_size":
                total_size += _struct

        directory_tree["_size"] = total_size

    return directory_tree, directory_sizes


def get_directory_tree(directory_listing):
    location = []
    directory_tree = {}
    current_directory = directory_tree
    for line in directory_listing:
        if line.startswith("$ cd .."):
            # ["/", "b", "c"]
            location = location[:-1]
            # ["/", "b"]
            key_references = "['" + "']['".join(location) + "']"
            current_directory = eval(f"directory_tree{key_references}")
            # current_directory = directory_tree["/"]["b"]
            continue

        if line.startswith("$ cd "):
            _, _, directory = line.split(" ")
            current_directory[directory] = {"_size": 0}
            location.append(directory)
            current_directory = current_directory[directory]
            continue

        if line.startswith("$ ls"):
            continue

        # can assume its either a file or directory
        if line.startswith("dir "):
            _, directory = line.split(" ")
            current_directory[directory] = {"_size": 0}
            continue

        size, filename = line.split(" ")
        current_directory[filename] = int(size)

    return directory_tree


def calculate_score(directory_sizes):
    score = 0
    dirs = []
    for directory in directory_sizes:
        size = list(directory.values())[0]
        if size < 100000:
            score += size
            dirs.append(directory)

    return score, dirs



input = get_input()
directory_tree = get_directory_tree(input)

directory_tree, directory_sizes = get_sizes(directory_tree)
print(directory_sizes)
print(directory_tree)
print(calculate_score(directory_sizes))