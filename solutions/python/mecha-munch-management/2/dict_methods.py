"""Functions to manage a users shopping cart items."""


def add_item(current_cart, items_to_add):
    """Add items to shopping cart.

    :param current_cart: dict - the current shopping cart.
    :param items_to_add: iterable - items to add to the cart.
    :return: dict - the updated user cart dictionary.
    """

    for item_quantity_add in items_to_add:
        current_cart[item_quantity_add] = current_cart.get(item_quantity_add, 0) + 1
    return current_cart

def read_notes(notes):
    """Create user cart from an iterable notes entry.

    :param notes: iterable of items to add to cart.
    :return: dict - a user shopping cart dictionary.
    """

    new_shopping_cart = {}
    return new_shopping_cart.fromkeys(notes, 1)


def update_recipes(ideas, recipe_updates):
    """Update the recipe ideas dictionary.

    :param ideas: dict - The "recipe ideas" dict.
    :param recipe_updates: iterable -  with updates for the ideas section.
    :return: dict - updated "recipe ideas" dict.
    """
    ideas |= recipe_updates
    return ideas


def sort_entries(cart):
    """Sort a users shopping cart in alphabetically order.

    :param cart: dict - a users shopping cart dictionary.
    :return: dict - users shopping cart sorted in alphabetical order.
    """

    return dict(sorted(cart.items()))


def send_to_store(cart, aisle_mapping):
    """Combine users order to aisle and refrigeration information.

    :param cart: dict - users shopping cart dictionary.
    :param aisle_mapping: dict - aisle and refrigeration information dictionary.
    :return: dict - fulfillment dictionary ready to send to store.
    """

    combined_cart = {}
    for item_name, item_info in sorted(aisle_mapping.items(), reverse=True):
        quantity = cart.get(item_name, 0)
        if  quantity !=0:
            new_item_info = [quantity] + item_info
            combined_cart[item_name] = new_item_info
    return combined_cart


def update_store_inventory(fulfillment_cart, store_inventory):
    """Update store inventory levels with user order.

    :param fulfillment cart: dict - fulfillment cart to send to store.
    :param store_inventory: dict - store available inventory
    :return: dict - store_inventory updated.
    """

    for item_name, item_info in store_inventory.items():
        inventory_quantity = item_info[0]
        consume_quantity = fulfillment_cart.get(item_name, [0])[0]
        inventory_quantity -= consume_quantity
        if inventory_quantity > 0:
            item_info[0] = inventory_quantity
        else:
            item_info[0] = 'Out of Stock'

    return store_inventory
