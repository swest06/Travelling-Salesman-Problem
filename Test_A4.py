
import math
from cities import *


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
#swap_adjacent_cities(co_ordinates, 2)
swap_cities(co_ordinates, 1, 2)

if __name__ == "__main__":
    main()
