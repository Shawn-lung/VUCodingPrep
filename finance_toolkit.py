class TwoAssetPortfolioAnalysis:
    def __init__(self, prices_a, prices_b, weight_a, weight_b, risk_free_rate=0.001):
        if len(prices_a) != len(prices_b):
            raise ValueError("Both assets must have the same number of price observations.")
        
        if len(prices_a) < 2 or len(prices_b) < 2:
            raise ValueError("Each asset must have at least two prices.")
        
        if abs((weight_a + weight_b) - 1) > 1e-12:
            raise ValueError("Portfolio weights must sum to 1.")
        
        for price in prices_a:
            if price <= 0:
                raise ValueError("All prices in Asset A must be positive.")

        for price in prices_b:
            if price <= 0:
                raise ValueError("All prices in Asset B must be positive.")
        self.prices = {
            "A": prices_a,
            "B": prices_b
        }
        self.weight_a = weight_a
        self.weight_b = weight_b
        self.risk_free_rate = risk_free_rate

    def calculate_returns(self, asset):
        if asset not in self.prices:
            raise ValueError("asset must be 'A' or 'B'")
        
        prices = self.prices[asset]
        returns = []

        for i in range(1, len(prices)):         
            returns.append(prices[i] / prices[i - 1] - 1)

        return returns

    def calculate_portfolio_returns(self):
        returns_a = self.calculate_returns("A")
        returns_b = self.calculate_returns("B")

        portfolio_returns = []

        for i in range(len(returns_a)):
            portfolio_returns.append(
                self.weight_a * returns_a[i] + self.weight_b * returns_b[i]
            )

        return portfolio_returns

    def get_returns(self, asset):
        if asset == "Portfolio":
            return self.calculate_portfolio_returns()
        
        if asset in self.prices:
            return self.calculate_returns(asset)
        
        raise ValueError("asset must be 'A', 'B', or 'Portfolio'")

    def calculate_mean(self, values):
        if len(values) == 0:
            raise ValueError("values must not be empty")
        
        total = 0
        for value in values:
            total += value
        
        return total / len(values)

    def calculate_mean_return(self, asset):
        returns = self.get_returns(asset)
        return self.calculate_mean(returns)

    def calculate_variance(self, asset):
        returns = self.get_returns(asset)
        mean_returns = self.calculate_mean(returns)

        total_squared_deviation = 0

        for r in returns:
            total_squared_deviation += (r - mean_returns) ** 2

        return total_squared_deviation / len(returns)

    def calculate_standard_deviation(self, asset):
        return self.calculate_variance(asset) ** 0.5

    def calculate_sharpe_ratio(self, asset):
        standard_deviation = self.calculate_standard_deviation(asset)
        mean_return = self.calculate_mean_return(asset)

        if standard_deviation == 0:
            raise ValueError("standard_deviation must not be zero")
        
        excess_return = mean_return - self.risk_free_rate
        return excess_return / standard_deviation
    def run_analysis(self):
        assets = ["A", "B", "Portfolio"]
        analysis_dict = {}
        for asset in assets:
            mean_return = self.calculate_mean_return(asset)
            standard_deviation = self.calculate_standard_deviation(asset)
            sharpe_ratio = self.calculate_sharpe_ratio(asset)
            analysis_dict[asset] = {
                "mean_return":mean_return, 
                "standard_deviation":standard_deviation, 
                "sharpe_ratio":sharpe_ratio
            }
        return analysis_dict
    
if __name__ == "__main__":
    prices_a = [100, 102, 101, 105, 107]
    prices_b = [50, 49, 51, 50, 52]    
    weight_a = 0.6
    weight_b = 0.4
    analysis = TwoAssetPortfolioAnalysis(prices_a, prices_b, weight_a, weight_b)
    print(analysis.run_analysis())