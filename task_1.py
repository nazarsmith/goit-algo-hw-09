import time

def greedy_algorithm(coins: list, total_sum: int):
    total_sum_original = total_sum
    total_coins = {}
    for coin in coins:
        num_coins = total_sum // coin # <-- very easy to optimize
        total_sum -= coin * num_coins
        total_coins.update({coin : num_coins})
    print("Total change assembled GREEDY:", total_sum_original - total_sum)
    return total_coins

def dynamic_programming(coins: list, total_sum: int):
    original_coins = coins
    while sum(coins) < total_sum:
        coins.extend(original_coins)
        coins = sorted(coins, reverse = True)
    n = len(coins)

    K = [[0 for c in range(total_sum + 1)] for i in range(n + 1)]

    for w in range(total_sum + 1):
        
        for i in range(n + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif coins[i - 1] <= w:
                print(coins[i - 1], K[i - 1][w - coins[i - 1]], K[i - 1][w])
                mx = max(coins[i - 1] + K[i - 1][w - coins[i - 1]], K[i - 1][w]) # <-- extremely difficult to optimize
                K[i][w] = mx
            else:
                K[i][w] = K[i - 1][w]

    dyn_total = K[n][total_sum]
    print("Total change assembled DYNAMIC:", dyn_total)
    total_coins = {}
    n = 0
    while coins:
        num_coins = dyn_total // coins[n]
        total_coins.update({coins[n] : num_coins})
        dyn_total -= num_coins * coins[n]
        coins = [c for c in coins if c != coins[n]]
    return total_coins

if __name__ == "__main__":
    coins = [50, 25, 10, 5, 2, 1]

    time_now = time.time()
    total_coins_greedy = greedy_algorithm(coins, 87)
    print("Total coins (GREEDY):", total_coins_greedy)
    print("Execution time (GREEDY):", time.time() - time_now)

    time_now = time.time()
    total_coins_dynamic = dynamic_programming(coins, 87)
    print("Total coins (DYNAMIC):", total_coins_dynamic)
    print("Execution time (DYNAMIC):", time.time() - time_now)