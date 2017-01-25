def get_array(): return map(int, input().strip().split())
n,k = get_array()
costs = list(get_array())
charged = int(input().strip())

fair_price = (sum(costs) - costs[k])//2
print("Bon Appetit" if fair_price == charged else str(charged - fair_price))