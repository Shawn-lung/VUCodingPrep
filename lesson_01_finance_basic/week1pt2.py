def calculate_returns(prices:list):
    #TODO:
    # 1. create empty list
    # 2. loop through prices from index 1
    # 3. calculate simple return
    # 4. append to list
    # 5. return the list

    returns=[]
    for i in range(1, len(prices)):
        returns.append(prices[i]/prices[i-1]-1)
    
    return returns

def calculate_mean(values):
    # TODO:
    # 1. create total = 0
    # 2. loop through values
    # 3. accumulate total
    # 4. divide by length
    # 5. return mean    
    if not len(values):
        raise ValueError("values must not be empty")
    total = 0
    for value in values:
        total+=value
    mean = total/len(values)
    
    return mean

def calculate_portfolio_returns(returns_a, returns_b, weight_a, weight_b):
    # TODO:
    # 1. create empty list
    # 2. loop through return index
    # 3. portfolio return = weight_a * return_a + weight_b * return_b
    # 4. append to list
    # 5. return portfolio returns
    
    if len(returns_a) != len(returns_b):
        raise ValueError("returns_a and returns_b must have the same length")
    return_p=[]
    for i in range(len(returns_a)):
        return_p.append(returns_a[i]*weight_a+returns_b[i]*weight_b)
    
    return return_p

def calculate_variance(returns):
    if not len(returns):
        raise ValueError("values must not be empty")
    total_squared_deviation = 0
    mean_returns = calculate_mean(returns)
    for r in returns:
        total_squared_deviation += (r-mean_returns)**2
    return total_squared_deviation/len(returns)

def calculate_standard_deviation(returns):
    return calculate_variance(returns)**0.5

def calculate_sharpe_ratio(mean_return, standard_deviation, risk_free_rate=0.001):
    if not standard_deviation:
        raise ValueError("standard_deviation must not be zero")
    excess_return = mean_return - risk_free_rate
    sharpe_ratio = excess_return/standard_deviation
    return(sharpe_ratio)

prices_a = [100, 102, 101, 105, 107]
prices_b = [50, 49, 51, 50, 52]    
weight_a = 0.6
weight_b = 0.4

returns_a = calculate_returns(prices_a)
returns_b = calculate_returns(prices_b)

mean_return_a = calculate_mean(returns_a)
mean_return_b = calculate_mean(returns_b)

portfolio_returns = calculate_portfolio_returns(returns_a, returns_b, weight_a, weight_b)
mean_portfolio_return = calculate_mean(portfolio_returns)

variance_a = calculate_variance(returns_a)
variance_b = calculate_variance(returns_b)

std_a = calculate_standard_deviation(returns_a)
std_b = calculate_standard_deviation(returns_b)

portfolio_variance = calculate_variance(portfolio_returns)
portfolio_std = calculate_standard_deviation(portfolio_returns)

sharpe_a = calculate_sharpe_ratio(mean_return=mean_return_a, standard_deviation= std_a)
sharpe_b = calculate_sharpe_ratio(mean_return=mean_return_b, standard_deviation= std_b)
sharpe_portfolio = calculate_sharpe_ratio(mean_return=mean_portfolio_return, standard_deviation= portfolio_std)

print(f"returns_a:{returns_a}")
print(f"returns_b:{returns_b}")
print(f"mean_return_a:{mean_return_a}")
print(f"mean_return_b:{mean_return_b}")
print(f"portfolio_returns:{portfolio_returns}")
print(f"mean_portfolio_return:{mean_portfolio_return}")
print(f"variance_a:{variance_a}")
print(f"variance_b:{variance_b}")
print(f"std_a:{std_a}")
print(f"std_b:{std_b}")
print(f"portfolio_variance:{portfolio_variance}")
print(f"portfolio_std:{portfolio_std}")
print(f"sharpe_a:{sharpe_a}")
print(f"sharpe_b:{sharpe_b}")
print(f"sharpe_portfolio:{sharpe_portfolio}")

if mean_return_a > mean_return_b:
    print("Asset A has higher average return.")
else:
    print("Asset B has higher average return.")

if mean_portfolio_return > 0:
    print("The portfolio has positive average return.")
else:
    print("The portfolio has non-positive average return.")

if std_a > std_b:
    print("Asset A has higher risk")    
else:
    print("Asset B has higher risk")
