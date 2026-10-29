import sys

sys.path.insert(0, "../src")
from course_tools import check, check_output


messy = "                  too much space                     "

print("["+messy.strip()+"]")
print("["+messy.lstrip()+"]")
print("["+messy.rstrip()+"]")
print("xxxxxxxxxHello...!!!xxxxxxxxxxxxxxxx".strip("x"))
