# import sys
# import time

# while True:
# 	a = 0  
# 	for x in range (0,3):  
# 	    a = a + 1  
# 	    b = ("Loading" + "." * a)
# 	    # \r prints a carriage return first, so `b` is printed on top of the previous line.
# 	    sys.stdout.write('\r'+b)
# 	    time.sleep(0.5)
# print (a)

import sys
import time

def delete_last_line():
    "Use this function to delete the last line in the STDOUT"

    #cursor up one line
    sys.stdout.write('\x1b[1A')

    #delete last line
    sys.stdout.write('\x1b[2K')


########## FOR DEMO ################
if __name__ == "__main__":
    print("hello")
    print("this line will be delete after 2 seconds")
    time.sleep(2)
    delete_last_line()
####################################