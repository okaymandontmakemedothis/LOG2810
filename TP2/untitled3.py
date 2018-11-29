import sys
import time
for i in range(10):
    print("Loading" + "." * i)
    sys.stdout.write("\033[F") # Cursor up one line
    time.sleep(1)