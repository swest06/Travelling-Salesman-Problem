
import math
from cities import *
# a = 32.361538
# b = -86.279118
#
# x = 58.301935
# y = -134.41974
#
# a = 1
# b = 2
#
# x = 2
# y = 2
#
# l = 3
# r = 2
# sum = round(math.sqrt((a-x)**2 + (b-y)**2), 2)
# sum += round(math.sqrt((x-l)**2 + (y-r)**2), 2)
# print(sum)

co_ordinates = [("state", "city", 1, 2), ("state", "city", 2, 2), ("state", "city", 3, 2)]
print(compute_total_distance(co_ordinates))

