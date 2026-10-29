import sys

sys.path.insert(0, "../src")
from course_tools import check, check_output


words = "the quick brown fox chases white rabbit".split()

print(words)
print(len(words))

a=0
for i in words:
    print("Lentght of '"+words[a]+"' is:",len(words[a]))
    a += 1

print("2026-10-18".split("-"))
print("a,b,,c".split(","))

parts = "2026-10-18".split("-")
print(parts[0])
print(parts[-1])

print("".join(words))
print(" ".join(words))
print("-".join(words))
