import re

target_string = "JessaJ Erriika"
# This '\w' matches any single character
# and then its repetitions (\1*) if any.
matcher = re.compile(r"(\w)\1*")

for match in matcher.finditer(target_string):
    print(match.group(), end=", ")
