print("\nString test:")
string = 'Python'
print(r'C:\app\name')
# End with \ to avoid blank line
print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""", end="")
print("string[-2] = " + string[-2])
# +---+---+---+---+---+---+
# | P | y | t | h | o | n |
# +---+---+---+---+---+---+
# 0   1   2   3   4   5   6
#-6  -5  -4  -3  -2  -1
print("string[2:5] = " + string[2:5])
