import sys

if len(sys.argv) != 2:
    print(f"{sys.argv[0]} expected exactly one argument.")
    sys.exit(1)

password = sys.argv[1]
is_valid = False

# Do all the requirement checks here.
checks = [False, False, False, False, False]
for c in password:
    if c.isupper():
        checks[0] = True
    if c.islower():
        checks[1] = True
    if c.isnumeric():
        checks[2] = True
    if c in "$#@":
        checks[3] = True
    if len(password) < 17 and len(password) >= 6:
        checks[4] = True
if checks.count(True) == 5:
    print(is_valid)
