from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(PROJECT_ROOT))

from finance_toolkit import TwoAssetPortfolioAnalysis

def test_valid_analysis():
    prices_a = [100, 102, 101, 105, 107]
    prices_b = [50, 49, 51, 50, 52]
    weight_a, weight_b = 0.6, 0.4
    analysis = TwoAssetPortfolioAnalysis(prices_a, prices_b, weight_a, weight_b)
    results = analysis.run_analysis()
    assert "A" in results
    assert "B" in results 
    assert "Portfolio" in results 
    assert "mean_return" in results["Portfolio"] 
    assert "standard_deviation" in results["Portfolio"] 
    assert "sharpe_ratio" in results["Portfolio"] 

def test_invalid_weights():
    prices_a = [100, 102, 101, 105, 107]
    prices_b = [50, 49, 51, 50, 52]
    weight_a, weight_b = 0.7, 0.4
    try:
        TwoAssetPortfolioAnalysis(prices_a, prices_b, weight_a, weight_b)
    except ValueError:
        pass
    else:
        raise AssertionError("Invalid weights should raise ValueError")

def test_negative_price():
    prices_a = [100, 102, -101, 105, 107]
    prices_b = [50, 49, 51, 50, 52]
    weight_a, weight_b = 0.6, 0.4
    try:
        TwoAssetPortfolioAnalysis(prices_a, prices_b, weight_a, weight_b)
    except ValueError:
        pass
    else:
        raise AssertionError("Negative prices should raise ValueError")

def test_invalid_asset_name():
    prices_a = [100, 102, 101, 105, 107]
    prices_b = [50, 49, 51, 50, 52]
    weight_a, weight_b = 0.6, 0.4
    analysis = TwoAssetPortfolioAnalysis(prices_a, prices_b, weight_a, weight_b)
    try:
        analysis.calculate_mean_return("C")
    except ValueError:
        pass
    else:
        raise AssertionError("Invalid asset name should raise ValueError")

if __name__ == "__main__":
    test_valid_analysis()
    test_invalid_weights()
    test_negative_price()
    test_invalid_asset_name()
    print("All manual tests passed.")