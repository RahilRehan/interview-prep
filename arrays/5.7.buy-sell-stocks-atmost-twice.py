def buy_and_sell_stock_twice(prices: List[float]) -> float:
    
    maxTotalProfit = 0
    minPiceSoFar = float("inf")
    stockProfits = [0]*len(prices)

    # forwards pass, store profits at each day in dp(stockProfits array)
    for i in range(len(prices)):
        minPiceSoFar = min(minPiceSoFar, prices[i])
        maxTotalProfit = max(maxTotalProfit, prices[i] - minPiceSoFar)
        stockProfits[i] = maxTotalProfit

    # traverse back to find if you can make two transactions to achieve max profit.
    maxPriceSoFar = float("-inf")
    for i in range(len(prices)-1, 0, -1):
        maxPriceSoFar = max(maxPriceSoFar, prices[i])
        maxTotalProfit = max(maxTotalProfit, stockProfits[i-1] + (maxPriceSoFar - prices[i]))

    return maxTotalProfit