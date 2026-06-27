def calculate_returns(prices:list):
    returns=[]
    for i in range(1, len(prices)):
        returns.append(prices[i]/prices[i-1]-1)
    
    return returns

def calculate_mean(values):
    if not len(values):
        raise ValueError("values must not be empty")
    total = 0
    for value in values:
        total+=value
    mean = total/len(values)
    
    return mean

def calculate_portfolio_returns(returns_a, returns_b, weight_a, weight_b):    
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
import pandas as pd
import matplotlib.pyplot as plt


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

summary_table = pd.DataFrame({"Assets": ["Asset A", "Asset B", "Portfolio"], "Mean Return": [mean_return_a, mean_return_b, mean_portfolio_return], 
                              "Std Dev": [std_a, std_b, portfolio_std], "Sharpe Ratio": [sharpe_a, sharpe_b, sharpe_portfolio]})
summary_table = summary_table.round(4)
print(summary_table)

fig, ax = plt.subplots(figsize = (8, 2.1))
ax.axis("off")
ax.set_title("Lesson 1 Summary Table", pad=12)

table = ax.table(
    cellText=summary_table.values, 
    colLabels=summary_table.columns,
    loc="center",
    cellLoc="center"
)
table.auto_set_font_size("False")
table.set_fontsize(10)
table.scale(1, 1.4)

plt.tight_layout()
plt.savefig("lesson_01_summary_table.png", dpi=300, bbox_inches="tight")
plt.show()