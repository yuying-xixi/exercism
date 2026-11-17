"""Functions which helps the locomotive engineer to keep track of the train."""


def get_list_of_wagons(*wagons_id):
    """Return a list of wagons.

    :param: arbitrary number of wagons.
    :return: list - list of wagons.
    """
    return list(wagons_id)


def fix_list_of_wagons(each_wagons_id, missing_wagons):
    """Fix the list of wagons.

    :param each_wagons_id: list - the list of wagons.
    :param missing_wagons: list - the list of missing wagons.
    :return: list - list of wagons.
    """
    wagon1, wagon2, locomotive, *remanent_each_wagon= each_wagons_id
    return [locomotive] + missing_wagons + remanent_each_wagon + [wagon1, wagon2]


def add_missing_stops(route, **stops):
    """Add missing stops to route dict.

    :param route: dict - the dict of routing information.
    :param: arbitrary number of stops.
    :return: dict - updated route dictionary.
    """
    stops_list = list(stops.values())
    route['stops'] = stops_list
    return route


def extend_route_information(route, more_route_information):
    """Extend route information with more_route_information.

    :param route: dict - the route information.
    :param more_route_information: dict -  extra route information.
    :return: dict - extended route information.
    """
    return_extend_route = {}
    return_extend_route = route | more_route_information
    return return_extend_route


def fix_wagon_depot(wagons_rows):
    """Fix the list of rows of wagons.

    :param wagons_rows: list[list[tuple]] - the list of rows of wagons.
    :return: list[list[tuple]] - list of rows of wagons.
    """

    return [list(row) for row in zip(*wagons_rows)]
