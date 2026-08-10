prices = (100,200,300,400,500)
total = 0
for price in prices:
    total = total  + price
    average = total / len(prices)
    highest = prices[0]
    for price in prices:
      if price > highest:
        highest = price

lowest = prices[0]

for price in prices:
    if price < lowest:
        lowest = price

print("Item prices:", prices)
print("Total bill:", total)
print("Average price:", average)
print("Highest-priced item:", highest)
print("Lowest-priced item:", lowest)