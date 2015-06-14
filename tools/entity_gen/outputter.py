class Indent(object):
    def __init__(self, size = 4):
        self.size = size

class Unindent(object):
    pass

class BlankLine(object):
    pass

class Outputter(object):
    def __init__(self, out):
        self.out = out
        self.indent = [0]

    def __call__(self, item):
        if isinstance(item, Indent):
            self.indent.append(self.indent[-1] + item.size)
        elif isinstance(item, Unindent):
            self.indent.pop()
        elif isinstance(item, BlankLine):
            print >>self.out
        else:
            print >>self.out, " " * self.indent[-1] + item
