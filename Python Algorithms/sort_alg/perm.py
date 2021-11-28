import random as rn


def perm(arr, arr_len):
    """
        Simple code to permutate an array.
    """
    n = rn.randint(1, arr_len-1)
    for i in range(n):
        k = rn.randint(0, arr_len-1)
        arr[i], arr[k] = arr[k], arr[i]
    return True


def main():
    arr = [1, 2, 3, 4, 5]
    print(f"Arr is: {arr}")
    perm(arr, len(arr))
    print(f"Permuted Arr is: {arr}")


if __name__ == "__main__":
    main()
    exit()
