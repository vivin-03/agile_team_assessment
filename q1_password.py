import re

passwords = input("Enter comma separated passwords: ").split(",")

valid = []
for p in passwords:
    if (6 <= len(p) <= 12 and
        re.search("[a-z]", p) and
        re.search("[A-Z]", p) and
        re.search("[0-9]", p) and
        re.search("[$#@]", p)):
        valid.append(p)

print(",".join(valid))
