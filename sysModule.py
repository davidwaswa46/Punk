import sys
#Python sys module stores the command line arguments into a list, we can access it using sys.argv
print(type(sys.argv))
print('The command line arguments are:"q w e t y i"')
for i in sys.argv:
    print(i)
    #Python getopt module is very similar in working as the C getopt() function for parsing command-line parameters. 
    # Python getopt module is useful in parsing command line arguments where we want user to enter some options too.
    import getopt
import sys

argv = sys.argv[1:]
try:
    opts, args = getopt.getopt(argv, 'hm:d', ['help', 'my_file='])
    print(opts)
    print(args)
except getopt.GetoptError:
    # Print a message or do something useful
    print('Something went wrong!')
    sys.exit(2)

    #Python argparse module is the preferred way to parse command line arguments. 
    #It provides a lot of option such as positional arguments, default value for arguments, help message, specifying data type of argument etc
    import argparse
    

parser = argparse.ArgumentParser()
parser.parse_args()