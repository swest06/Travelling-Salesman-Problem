import math

def read_cities(file_name):
    """
    Read in the cities from the given `file_name`, and return 
    them as a list of four-tuples: 

      [(state, city, latitude, longitude), ...]
    """
    cities = []
    with open(file_name) as f:
        for line in f.readlines():
            x = line.split("\t")
            cities.append((str(x[0]), str(x[1]), eval(x[2]), eval(x[3])))

    return cities

  
def print_cities(road_map):
    """
    Prints a list of cities, along with their locations. 
    Print only one or two digits after the decimal point.
    """
    list = []
    for i in road_map:
        x = round(i[2], 2)
        y = round(i[3], 2)
        elem = '{} {} {}'.format(i[1], x, y)
        list.append(elem)
    return list

def compute_total_distance(road_map):
    """
    Returns, as a floating point number, the sum of the distances of all 
    the connections in the `road_map`. Remember that it's a cycle, so that 
    (for example) in the initial `road_map`, Wyoming connects to Alabama...
    """
    total = 0.0

    for i, e in enumerate(road_map):
        print(i)
        x1 = road_map[i][2]
        y1 = road_map[i][3]
        print(str(x1) + str(y1))

        if i + 1 == len(road_map):
            x2 = road_map[0][2]
            y2 = road_map[0][3]
        else:
            x2 = road_map[i+1][2]
            y2 = road_map[i+1][3]
        print(str(x2) + str(y2))



def swap_adjacent_cities(road_map, index):
    """
    Take the city at location `index` in the `road_map`, and the city at 
    location `index+1` (or at `0`, if `index` refers to the last element 
    in the list), swap their positions in the `road_map`, compute the 
    new total distance, and return the tuple 

        (new_road_map, new_total_distance)
    """
    pass

def swap_cities(road_map, index1, index2):
    """
    Take the city at location `index` in the `road_map`, and the 
    city at location `index2`, swap their positions in the `road_map`, 
    compute the new total distance, and return the tuple 

        (new_road_map, new_total_distance)

    Allow for the possibility that `index1=index2`,
    and handle this case correctly.
    """
    pass

def find_best_cycle(road_map):
    """
    Using a combination of `swap_cities` and `swap_adjacent_cities`, 
    try `10000` swaps, and each time keep the best cycle found so far. 
    After `10000` swaps, return the best cycle found so far.
    """
    pass

def print_map(road_map):
    """
    Prints, in an easily understandable format, the cities and 
    their connections, along with the cost for each connection 
    and the total cost.
    """
    pass

def main():
    """
    Reads in, and prints out, the city data, then creates the "best"
    cycle and prints it out.
    """
    file = input("Type txt file: ")
    road_map = read_cities(file)
    print(road_map)
    print("")
    # x = print_cities(road_map)
    # print(x)
    compute_total_distance(road_map)


if __name__ == "__main__":
    main()
