if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    max_score = max(arr)
    arr = [arr for arr in arr if arr != max_score]

    runner_up = max(arr)
    print(runner_up)
