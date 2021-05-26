inv = {'gold coin': 42, 'rope': 1}
dragon_loot = ['gold coin', ' dagger', 'gold coin', 'gold coin', 'ruby']


def add_to_inventory(inventory, items):
    for item in items:
         # get count of item in inventory, or 0 if item is not in inventory
         item_count = inventory.get(item, 0)
         # update item count in inventory
         inventory[item] = item_count + 1
    return inventory



inv = add_to_inventory(inv, dragon_loot)
# print(stuff)

def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        print(str(v) + ' ' + k)
        item_total += v
    print("Total number of items: " + str(item_total))


displayInventory(inv)