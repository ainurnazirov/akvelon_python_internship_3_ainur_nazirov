def fibonacci__for(num):
    if num == 1:
        return 1
    if num == 0:
        return 0
    if num < 0:
        return fibonacci__for(-1 * num) * (-1) ** (num + 1)

    result_last = 0
    result = 1

    for i in range(2, num + 1):
        result, result_last = result + result_last, result

    return result


if __init__ := "__main__":
    print("Fibonacci for 0: ", fibonacci__for(0))
    print("Fibonacci for 100: ", fibonacci__for(100))
    print("Fibonacci for -100: ", fibonacci__for(-100))
