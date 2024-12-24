
def print_specific_elements():
    arr = [10, 20, 30, 40, 50]
    print(arr[2], arr[4])


def print_odd_indexed_elements():
    N = int(input())
    arr = [int(input()) for _ in range(N)]
    for i in range(1, N, 2):
        print(arr[i])


def double_elements():
    arr = [int(input()) for _ in range(10)]
    doubled = [x * 2 for x in arr]
    print(doubled)


def reverse_array():
    N = int(input())
    arr = [int(input()) for _ in range(N)]
    print(arr[::-1])


def swap_and_print():
    N = int(input())
    arr = [int(input()) for _ in range(N)]
    arr[0], arr[-1] = arr[-1], arr[0]
    print(arr)
