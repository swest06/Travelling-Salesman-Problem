import pytest

from cities import*


def test_print_cities():
    road_map = [('Alabama', 'Montgomery', 32.361538, -86.279118), ('Alaska', 'Juneau', 58.301935, -134.41974), ('Arizona', 'Phoenix', 33.448457, -112.073844)]
    print_city = ['Montgomery 32.36 -86.28', 'Juneau 58.3 -134.42', 'Phoenix 33.45 -112.07']

    assert print_city == print_cities(road_map)


def test_compute_total_distance():
    co_ordinates = [("state", "city", 1, 2), ("state", "city", 2, 2), ("state", "city", 3, 2)]
    total = 2.0
    assert total == round(compute_total_distance(co_ordinates), 2)
