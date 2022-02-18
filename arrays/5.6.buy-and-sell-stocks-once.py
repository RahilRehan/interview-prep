def buy_and_sell_stock_once(prices: List[float]) -> float:
    maxProfit = 0.0
    minStockPriceSoFar = float('inf')

    for price in prices:
        todaysMaxProfit = price - minStockPriceSoFar
        maxProfit = max(todaysMaxProfit, maxProfit)
        minStockPriceSoFar = min(minStockPriceSoFar, price)

    return maxProfit