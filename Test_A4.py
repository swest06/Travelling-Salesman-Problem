
import math
from cities import *
from earth_distance import *

def main():
    """
    Reads in, and prints out, the city data, then creates the "best"
    cycle and prints it out.
    """
    # file = input("Type txt file: ")
    # road_map = read_cities(file)
    # print(road_map)
    # print("")
    # # x = print_cities(road_map)
    # # print(x)
    # compute_total_distance(road_map)

co_ordinates = [("state A", "city A", 4, 5), ("state B", "city B", 2, 2), ("state C", "city C", 3, 2)]
co_ordinates2 = [("state B", "city B", 2, 2), ("state A", "city A", 4, 5), ("state C", "city C", 3, 2)]
# print(compute_total_distance(co_ordinates))
#find_best_cycle(co_ordinates)
# new = swap_adjacent_cities(co_ordinates, 2)
# print(co_ordinates)
# print(new)
# print(co_ordinates)
# swap_cities(co_ordinates, 1, 2)
#print(find_best_cycle(co_ordinates))
#print(compute_total_distance(co_ordinates))
#new = swap_cities(co_ordinates, 1, 2)
#print(new is co_ordinates)

a = (distance(0, 0, 0, 1))
b = (distance(0, 1, 0, 2))
c = (distance(0, 2, 0, 0))
sum1 = a + b
sum1 += c
print(a)
print(b)
print(c)
print(sum1)
co_ordinates = [("state A", "city A", 0, 0), ("state B", "city B", 0, 1), ("state C", "city C", 0, 2)]
# Maine	Augusta	44.323535	-69.765261
# Missouri	Jefferson City	38.572954	-92.189283

print_map(co_ordinates)
if __name__ == "__main__":
    main()
