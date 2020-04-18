cost_value =input("Please enter cost value (in dollar) : ")
sell_value =input("Please enter sell value (in dollar) : ")
inventory = input("Please enter inventory              : ")


sales = {
  "cost_value": float(cost_value),
  "sell_value": float(sell_value),
  "inventory": int(inventory)
}  

profit = (sales['sell_value']-sales['cost_value'])*sales['inventory']
print(f"Your profit is ${round(profit)}")