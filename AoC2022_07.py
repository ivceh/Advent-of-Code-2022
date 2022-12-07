class Dir:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.objects = []

    def insert(self, obj):
        self.objects.append(obj)

    def size(self):
        if hasattr(self, "size_mem"):
            return self.size_mem

        size_mem = sum(o.size() for o in self.objects)
        return size_mem

class File:
    def __init__(self, name, size):
        self.name = name
        self.size_attr = size

    def size(self):
        return self.size_attr

def sum_le_100000(d):
    if d.size() <= 100000:
        s = d.size()
    else:
        s = 0
    s += sum(sum_le_100000(child) for child in d.objects
             if isinstance(child, Dir))
    return s

def smallest_bigger_than_x(d, x):
    if d.size() >= x:
        r = d.size()
    else:
        r = float("inf")

    for child in d.objects:
        if isinstance(child, Dir):
            y = smallest_bigger_than_x(child, x)
            if y < r:
                r = y
    return r

def day07(infile):
    #memorizing directory structure from input
    with open(infile, "r") as file:
        for line in file.read().splitlines():
            words = line.split(" ")
            if words[0] == '$':
                if words[1] == 'cd':
                    if words[2] == '/':
                        root = Dir('/', None)
                        current_dir = root
                    elif words[2] == "..":
                        current_dir = current_dir.parent
                    else:
                        current_dir = next(obj for obj in current_dir.objects
                                           if obj.name == words[2])
            elif words[0] == "dir":
                current_dir.insert(Dir(name=words[1], parent=current_dir))
            else:
                current_dir.insert(File(name=words[1], size=int(words[0])))

    # solving Part One
    print("Part One: ", sum_le_100000(root))

    # solving Part Two
    space_needed = root.size() - 40000000
    print("Part Two: ", smallest_bigger_than_x(root, space_needed))