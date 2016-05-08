import sys

def outName(name):
    print("Hello", name,'!')

if len(sys.argv) > 1:
    for arg in sys.argv[1:]:
        name = sys.argv[1]
        outName(arg)
else:
    print("Hello World!")
