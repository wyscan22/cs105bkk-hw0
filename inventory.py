"""HW0: a game inventory. Practises Session 1: names and objects, defaults, *args, comprehensions."""


def add_item(inventory, item, count=1):
    """Return a new inventory with count more of item. Do not change inventory. """
    inventory_new = inventory.copy()
    if item not in inventory.keys():
        inventory_new[item] = count
    else:
        inventory_new[item] += count
    return inventory_new
    raise NotImplementedError("core: return a new inventory with the item added")


def total_items(*inventories):
    """Return how many items there are in all the inventories together."""
    total = 0
    for inventory in inventories:
        for count in inventory.values():
            if type(count) == str: raise TypeError(count)
            total += count
    return total
    raise NotImplementedError("core: add up the items in every inventory")


def running_low(inventory, limit=2):
    """Return the names of items with fewer than limit left, sorted A to Z."""
    my_list = []
    for item in inventory.keys():
        if inventory[item] < limit:
            my_list.append(item)
        my_list.sort()
    return my_list
    raise NotImplementedError("core: list the items running low")

a
