def check(arr):
    for i in range(len(arr)-1):
        if(arr[i] > arr[i+1]):
            return False
    return True


def main():
    arr = [1, 2, 3, 4, 5]
    print(f"Arr value is: {arr}")
    print(f"Is array sorted: {check(arr)}")
    arr = [2, 4, 1, 6, 2]
    print(f"New array is: {arr}")
    print(f"Is array sorted: {check(arr)}")


if __name__ == "__main__":
    main()
    exit()
