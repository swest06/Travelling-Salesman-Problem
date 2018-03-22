import pytest
from cities import*


# def test_print_cities():
#     road_map = [('Alabama', 'Montgomery', 32.361538, -86.279118), ('Alaska', 'Juneau', 58.301935, -134.41974), ('Arizona', 'Phoenix', 33.448457, -112.073844)]
#     print_city = ['Montgomery 32.36 -86.28', 'Juneau 58.3 -134.42', 'Phoenix 33.45 -112.07']
#
#     assert print_city == print_cities(road_map)


def test_compute_total_distance():
    co_ordinates = [("state A", "city A", 0, 0), ("state B", "city B", 0, 1), ("state C", "city C", 0, 2)]
    total = 276.18

    assert total == round(compute_total_distance(co_ordinates), 2)


def test_swap_adjacent_cities():
    co_ordinates = [("state A", "city A", 1, 2), ("state B", "city B", 2, 2), ("state C", "city C", 3, 2)]
    index = 0
    new_co_ordinates = [("state B", "city B", 2, 2), ("state A", "city A", 1, 2), ("state C", "city C", 3, 2)]
    result = (new_co_ordinates, compute_total_distance(new_co_ordinates))

    assert result == swap_adjacent_cities(co_ordinates, index)


def test_swap_cities():
    co_ordinates = [("state A", "city A", 1, 2), ("state B", "city B", 2, 2), ("state C", "city C", 3, 2)]
    new_co_ordinates = [("state C", "city C", 3, 2), ("state B", "city B", 2, 2), ("state A", "city A", 1, 2)]
    index1 = 0
    index2 = 2

    result1 = (new_co_ordinates, compute_total_distance(new_co_ordinates))
    result2 = (co_ordinates, compute_total_distance(co_ordinates))

    assert result1 == swap_cities(co_ordinates, index1, index2)
    assert result2 == swap_cities(co_ordinates, index1, index1)


def test_find_best_cycle():
    road_map = [('Alabama', 'Montgomery', 32.361538, -86.279118), ('Alaska', 'Juneau', 58.301935, -134.41974), ('Arizona', 'Phoenix', 33.448457, -112.073844)]
    assert (compute_total_distance(find_best_cycle(road_map)) < compute_total_distance(road_map))
