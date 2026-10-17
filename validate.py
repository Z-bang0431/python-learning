import re

email = input("what's your email?").strip()

# if "@" in email and "." in email:
#     print("Valid")
# else:
#     print("Invalid")

# username, domain = email.split("@")

# if username and "." in domain:
#     print("Valid")
# else:
#     print("Invalid")

if re.search("@", email):
    print("Valid")
else:
    print("Invalid")

if re.search(r"^[^@]+@[^@]+\.edu$", email):
    print("Valid")
else:
    print("Invalid")

if re.search(r"^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.edu$", email):
    print("Valid")
else:
    print("Invalid")