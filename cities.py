import random
from earth_distance import *
from copy import deepcopy


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
    list_cities = []
    for i in road_map:
        x = round(i[2], 2)
        y = round(i[3], 2)

        # Creates new list element to append to list
        elem = '{}  Latitude: {}  Longitude: {}'.format(i[1], x, y)
        list_cities.append(elem)

    print(list_cities)

    return list_cities


def compute_total_distance(road_map):
    """
    Returns, as a floating point number, the sum of the distances of all 
    the connections in the `road_map`. Remember that it's a cycle, so that 
    (for example) in the initial `road_map`, Wyoming connects to Alabama...
    """
    total = 0.0

    for i, e in enumerate(road_map):

        # Assign latitude and longitude values to variables
        lat1 = road_map[i][2]
        long1 = road_map[i][3]

        lat2 = road_map[(i + 1) % len(road_map)][2]
        long2 = road_map[(i + 1) % len(road_map)][3]

        # Calculate total distance
        sum1 = distance(lat1, long1, lat2, long2)

        total += sum1

    return total


def swap_adjacent_cities(road_map, index):
    """
    Take the city at location `index` in the `road_map`, and the city at 
    location `index+1` (or at `0`, if `index` refers to the last element 
    in the list), swap their positions in the `road_map`, compute the 
    new total distance, and return the tuple 

        (new_road_map, new_total_distance)
    """
    # create new list of tuples with original 'road_map'
    new_road_map = deepcopy(road_map)

    # Get indexes of elements
    a = road_map[index]
    b = road_map[(index+1) % len(road_map)]

    new_road_map[index] = b
    new_road_map[(index + 1) % len(road_map)] = a

    # Compute new total distance
    new_total_distance = compute_total_distance(new_road_map)

    result = (new_road_map, new_total_distance)

    return result


def swap_cities(road_map, index1, index2):
    """
    Take the city at location `index` in the `road_map`, and the 
    city at location `index2`, swap their positions in the `road_map`, 
    compute the new total distance, and return the tuple 

        (new_road_map, new_total_distance)

    Allow for the possibility that `index1=index2`,
    and handle this case correctly.
    """
    # create new list of tuples with original 'road_map'
    new_road_map = deepcopy(road_map)

    if index1 == index2:

        pass
    else:
        a = road_map[index1]
        b = road_map[index2]
        new_road_map[index1] = b
        new_road_map[index2] = a

    new_total_distance = compute_total_distance(new_road_map)
    result = (new_road_map, new_total_distance)

    return result


def find_best_cycle(road_map):
    """
    Using a combination of `swap_cities` and `swap_adjacent_cities`, 
    try `10000` swaps, and each time keep the best cycle found so far. 
    After `10000` swaps, return the best cycle found so far.
    """

    swaps = 10000

    # DELETE LATER!
    # for i, e in enumerate(road_map):
    #     print("outer loop")
    #     print(i)
    #     tup1 = swap_adjacent_cities(road_map, i)
    #         dis1 = tup1[1]
    #         print(dis1)
    #
    #         for j, f in enumerate(road_map):
    #             print("inner loop")
    #             print(i, j)
    #             tup2 = swap_cities(road_map, i, j)

    finished = False
    while not finished:

        for i, e in enumerate(road_map):

            num = int(len(road_map) * random.random() // 1)

            # Swap adjacent cities and compute new total distance
            tup1 = swap_adjacent_cities(road_map, i)
            swaps -= 1
            winner = tup1

            if swaps > 0:
                # 2 Opt swap at random
                tup2 = swap_cities(road_map, i, num)
                swaps -= 1

                # Compares swaps and keeps shortest route
                if tup2[1] < tup1[1]:
                    winner = tup2

            # Compares new route with old route and keeps shortest route
            if winner[1] < compute_total_distance(road_map):
                road_map = winner[0]

            if swaps < 1:
                finished = True
                break

    return road_map


def print_map(road_map):
    """
    Prints, in an easily understandable format, the cities and 
    their connections, along with the cost for each connection 
    and the total cost.
    """
    # Assume road_map has been changed and shortest route found
    for i, e in enumerate(road_map):
        # Assign cities to variables
        city1 = road_map[i][1]
        city2 = road_map[(i + 1) % len(road_map)][1]

        # Assign latitude and longitude values to variables
        lat1 = road_map[i][2]
        long1 = road_map[i][3]
        lat2 = road_map[(i + 1) % len(road_map)][2]
        long2 = road_map[(i + 1) % len(road_map)][3]

        # Calculate distance between cities and print
        dist = round(distance(lat1, long1, lat2, long2), 2)
        print("{} to {} = {} miles".format(city1, city2, dist))
        print("")

    print("Total distance = {} miles".format(round(compute_total_distance(road_map), 2)))


def main():
    """
    Reads in, and prints out, the city data, then creates the "best"
    cycle and prints it out.
    """
    # Reads txt file
    file = input("Type txt file: ")
    road_map = read_cities(file)
    print("")

    # Prints cities
    print("City data:")
    print_cities(road_map)
    print("")

    # Finds shortest route and prints it
    road_map = find_best_cycle(road_map)
    print("Best route found:")
    print_map(road_map)


if __name__ == "__main__":
    main()
