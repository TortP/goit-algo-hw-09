import time

# Жадібний алгоритм для видачі решти


def find_coins_greedy(amount):
    coins = [50, 25, 10, 5, 2, 1]
    result = {}

    for coin in coins:
        if amount >= coin:
            count = amount // coin
            amount -= count * coin
            result[coin] = count

    return result

# Алгоритм динамічного програмування для знаходження мінімальної кількості монет


def find_min_coins(amount):
    coins = [1, 2, 5, 10, 25, 50]
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0  # Для суми 0 потрібна 0 монет

    coin_count = [{} for _ in range(amount + 1)]

    for coin in coins:
        for i in range(coin, amount + 1):
            if dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                coin_count[i] = coin_count[i - coin].copy()
                coin_count[i][coin] = coin_count[i].get(coin, 0) + 1

    return coin_count[amount]

# Функція для вимірювання часу виконання і виведення результатів


def measure_time(func, amount, algorithm_name):
    start = time.time()
    result = func(amount)
    end = time.time()
    print(f"{algorithm_name} для суми {amount}:")
    print(f"Час виконання: {end - start:.6f} секунд")
    print(f"Результат: {result}")
    print(f"Кількість монет: {sum(result.values())}\n")
    return end - start

# Функція для порівняння двох алгоритмів на різних сумах


def compare_algorithms(amounts):
    for amount in amounts:
        print(f"=== Порівняння для суми {amount} ===")
        greedy_time = measure_time(
            find_coins_greedy, amount, "Жадібний алгоритм")
        dp_time = measure_time(find_min_coins, amount,
                               "Динамічне програмування")

        print(f"Час виконання жадібного алгоритму: {greedy_time:.6f} секунд")
        print(f"Час виконання алгоритму динамічного програмування: {
              dp_time:.6f} секунд")
        print("===================================\n")


if __name__ == "__main__":
    # Тестування на малих і великих сумах
    amounts = [113, 1387, 54367, 10947, 54679]  # Суми для порівняння
    compare_algorithms(amounts)
