import sys

sys.path.insert(0, "../src")
from course_tools import check, check_output


sentence = "Mississippi"

print(sentence.find("ss"))
print(sentence.find("z"))
print(sentence.count("s"))
print(sentence.count("ss"))
print(sentence.count("r"))

print(sentence.startswith("Miss"))
print(sentence.endswith("pi"))

print("12345".isdigit(), "12j324k".isdigit(), "213fv7437h".isalnum())

