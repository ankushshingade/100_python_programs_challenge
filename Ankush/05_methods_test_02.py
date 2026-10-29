import sys

sys.path.insert(0, "../src")
from course_tools import check, check_output

text = "hELLo wORLD..!!!"

print(text.upper(),"\n")
print(text.lower(),"\n")
print(text.title(),"\n")
print(text.capitalize(),"\n")
print(text.swapcase(),"\n")

