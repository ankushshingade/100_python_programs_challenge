import sys

sys.path.insert(0, "../src")
from course_tools import check, check_output


raw = "  ADA Lovelace  "

clean = raw.strip().title()
print(clean)


# Getting help on methods:

help("".split)

string = "   python IS fun   "

new_string = string.strip().title()

print(new_string)
