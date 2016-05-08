#HelloWorld.py
import sys
def Hello(name):
    print("Hello," + name + "!")

if len(sys.argv) > 1: #You can write as many names as you like.
    for arg in sys.argv[1: ]:
        Hello(arg)
else :
    print("Hello World!")
