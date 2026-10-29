import sys

sys.path.insert(0, "../src")
from course_tools import check, check_output

message = "hello, world"

print(message.upper())
print(message.title())
print(message.count("l"))

shout = "quiet"
shout.upper()
print(shout)        # unchanged!

shout = shout.upper()       # store the new string
print(shout)
