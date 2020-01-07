import sys

class Arguments:

    def __init__(self):
        self.argument = sys.argv[1]

    def get_argument(self):
        return self.argument
