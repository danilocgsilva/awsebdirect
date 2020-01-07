import sys

class Arguments:

    def __init__(self):
        try:
            self.argument = sys.argv[1]
        except IndexError as ie:
            self.argument = ''


    def get_argument(self):
        return self.argument
