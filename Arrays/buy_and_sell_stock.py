def maxProfit(prices):
    # Initialize total profit to zero
    total_profit = 0

    # Loop over each price (starting from the second one)
    for i in range(1, len(prices)):
        # If today's price is higher than yesterday's, we have a profit opportunity
        if prices[i] > prices[i - 1]:
            # Accumulate the profit from this opportunity
            total_profit += prices[i] - prices[i - 1]

    return total_profit


# Example usage:
prices = [7, 1, 5, 3, 6, 4]
print(maxProfit(prices))  # Output: 7