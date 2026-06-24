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
    if standard_deviation == 0:
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

print(f"Asset A mean return:{mean_return_a}")
print(f"Asset A standard deviation:{std_a}")
print(f"Asset A Sharpe ratio:{sharpe_a}")
print(f"Asset B mean return:{mean_return_b}")
print(f"Asset B standard deviation:{std_b}")
print(f"Asset B Sharpe ratio:{sharpe_b}")
print(f"Portfolio mean return:{mean_portfolio_return}")
print(f"Portfolio standard deviation:{portfolio_std}")
print(f"Portfolio Sharpe ratio:{sharpe_portfolio}")

sharpe_scores = {"Asset A": sharpe_a, "Asset B": sharpe_b, "Portfolio": sharpe_portfolio}
best_sharpe = max(sharpe_scores.values())
tolerance = 1e-12

best_choice = []

for name, sharpe in sharpe_scores.items():
    if abs(sharpe-best_sharpe) < tolerance:
        best_choice.append(name)

if len(best_choice) == 1:
    print(f"Best risk-adjusted choice:{best_choice[0]}")
else:
    print(f"Tie between:{", ".join(best_choice)}")