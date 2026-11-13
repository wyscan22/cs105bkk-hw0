"""HW0: a game inventory. Practises Session 1: names and objects, defaults, *args, comprehensions."""


def add_item(inventory, item, count=1):
    """Return a new inventory with count more of item. Do not change inventory. """
    if inventory[item] is None:
        inventory[item] = count
        return
    inventory[item] += count
    return
    raise NotImplementedError("core: return a new inventory with the item added")


def total_items(*inventories):
    """Return how many items there are in all the inventories together."""
    total = 0
    for inventory in inventories:
        for count in inventory:
            total += count
    return total
    raise NotImplementedError("core: add up the items in every inventory")


def running_low(inventory, limit=2):
    """Return the names of items with fewer than limit left, sorted A to Z."""
    for item in inventory.keys():
        my_list = []
        if inventory[item] < limit:
            my_list.append(item)
        my_list.sort()
        return my_list
    raise NotImplementedError("core: list the items running low")

