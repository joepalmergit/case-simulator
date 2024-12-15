import random

items = ["Blue", "Purple", "Pink", "Red", "Gold"]
odds = [79.92, 15.98, 3.2, 0.64, 0.26]

random_item = random.choices(items, odds, k=1)[0]
print(random_item)
