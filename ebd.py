from objs.Arguments import Arguments
from commands import infos, count
import sys

arguments = Arguments()

if not arguments.were_provided():
    print("No argument provided. Sorry")
    exit()

getattr(sys.modules[__name__], arguments.get_argument())()

