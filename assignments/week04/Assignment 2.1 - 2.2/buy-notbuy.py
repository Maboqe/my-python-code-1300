items = []
for i in range(6):
    price = int(input(f"Enter price of 6 item {i+1}: "))
    items.append(price)
print()

budget = int(input("Enter total budget: "))

total = 0
bought = []
for i in range(6):
    if total + items[i] <= budget:
        print(f"Item {i+1} = {items[i]} can buy")
        total += items[i]
        bought.append(items[i])
    else:
        print(f"Item {i+1} = {items[i]} cant buy")
    print(f"Current total = {total}")

print(f"Bount items: {bought}")
print(f"Total spent: {total}")
print(f"Remain budget: {budget - total}")