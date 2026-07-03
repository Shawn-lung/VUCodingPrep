from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(PROJECT_ROOT))

from finance_toolkit import TwoAssetPortfolioAnalysis
prices_a = [100, 102, 101, 105, 107]
prices_b = [50, 49, 51, 50, 52]    
weight_a = 0.6
weight_b = 0.4
portfolio = TwoAssetPortfolioAnalysis(prices_a, prices_b, weight_a, weight_b)
print(portfolio.run_analysis())