prices_a = [100, 102, 101, 105, 107]

returns_a = []

for i in range(1, len(prices_a)):
    today_price = prices_a[i]
    yesterday_price = prices_a[i - 1]
    r = today_price / yesterday_price - 1
    
    print("i =", i)
    print("today price =", today_price)
    print("yesterday price =", yesterday_price)
    print("return =", r)
    print("---")
    
    returns_a.append(r)

print("returns_a:", returns_a)
print("======")

total_return = 0

for r in returns_a:
    print("before adding:", total_return)
    print("new return:", r)
    
    total_return += r
    
    print("after adding:", total_return)
    print("---")

mean_return_a = total_return / len(returns_a)

print("total_return:", total_return)
print("number of returns:", len(returns_a))
print("mean_return_a:", mean_return_a)