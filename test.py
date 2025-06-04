import sys
import time
from collections import deque

# sys.stdout.write("Hi")
# sys.stdout.flush()
# sys.stdout.write("Bye")

# import sys
# import time

# sys.stdout.write("\rHi\nGrr")
# sys.stdout.flush()
# time.sleep(1)
# sys.stdout.write("\rBye\nooh")


# queue = deque([], 3)
# for t in range(20):
#     time.sleep(0.5)
#     s = "update %d" % t
#     for _ in range(len(queue)):
#         sys.stdout.write("\x1b[1A\x1b[2K")
#     queue.append(s)
#     for i in range(len(queue)):
#         sys.stdout.write(queue[i] + "\n")

s = ""
for i in range(10):
    s += "123456789\n"
sys.stdout.write(s)
time.sleep(2)
for i in range(10):
    sys.stdout.write("\x1b[1A\x1b[2K")

s2 = ""
for i in range(10):
    s2 += "abcdefghij\n"
sys.stdout.write(s2)
