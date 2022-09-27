# occurs frequently when doing system development
# example
# python3 myscript.py result.txt
# or
# python3 myscript.py -o result.txt -l DEBUG -c


# def my_function(*args, **kwargs):
#     print(args[0])
#     print(args[1])
#     print(args[2])
#     print(args[3])
#     print(kwargs['KEYONE'])
#     print(kwargs['KEYTWO'])


# my_function('hey', True, 19, 'wow', KEYONE="TEST", KEYTWO=7)

import sys
# optional arguments
import getopt

# how argc argv in c looks like
# main(int argc, char** argv)
# can be used to receive the argument in command prompt
# Usage: main.py FILENAME -p 8080 -h localhost
# __filename = sys.argv[1]
# __message = sys.argv[2]
# len(sys.argv)

# file stream
# with open(__filename, 'w+') as f:
#     f.write(__message)


# [1:] everything except the first one
# "f:m:" filename and message (-f -m)
opts, args = getopt.getopt(sys.argv[1:], "f:m:", ['filename', 'message'])


filename = "text.txt"
message = "Hello"

for opt, arg in opts:
    if opt  == '-f':
        filename = arg
    if opt == '-m':
        message = arg

with open(filename, 'w+') as f:
    f.write(message)
