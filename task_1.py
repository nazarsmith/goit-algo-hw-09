def greedy_algorithm(coins: list, total_sum: int):
    total_coins = {}
    for coin in coins:
        num_coins = total_sum // coin
        total_sum -= coin * num_coins
        total_coins.update({coin : num_coins})
    return total_coins

def dynamic_programming(coins: list, total_sum: int):
    n = len(coins)

    K = [[0 for c in range(total_sum + 1)] for i in range(n + 1)]

    for i in range(n + 1):
        for w in range(total_sum + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif coins[i - 1] <= w:
                K[i][w] = max(K[i - 1][w - coins[i - 1]], K[i - 1][w])
            else:
                K[i][w] = K[i - 1][w]
    for i in K:
        print(i)
    return K[n][total_sum]

if __name__ == "__main__":
    coins = [50, 25, 10, 5, 2, 1]
    
    total_coins_greedy = greedy_algorithm(coins, 131)
    print("Total coins (GREEDY):", total_coins_greedy)

    total_coins_dynamic = dynamic_programming(coins, 131)
    print("Total calories (DYNAMIC):", total_coins_dynamic)