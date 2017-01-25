def get_array(): return map(int, input().strip().split())
s,t = get_array()
a,b = get_array()
m,n = get_array()
apples = get_array()
oranges = get_array()

def fell_on_house(item, tree): return (item + tree) >= s and (item + tree) <= t
apple_count = sum([1 if fell_on_house(apple, a) else 0 for apple in apples])
orange_count = sum([1 if fell_on_house(orange, b) else 0 for orange in oranges])
print(apple_count)
print(orange_count)
