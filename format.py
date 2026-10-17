import re

# name = input("ehat's your name?").strip()
# if "," in name:
#     last, first = name.split(",?")
#     name = f"{first} {last}"
#     print(F"hello, {name}")

name = input("what's your name?").strip()
matches = re.search(r"^(.+), (.+)$", name)
if matches:
    last, first = matches.groups()
    name = f"{first} {last}"
print(f"hello, {name}")