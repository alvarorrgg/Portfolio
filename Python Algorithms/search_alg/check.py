def check(arr, num):
    if num in arr:
        return True
    return False


def main():
    num = 4
    arr = [1, 2, 3, 4, 5]
    print(f"Number is: {num} ")
    print(f"Array is: {arr}")
    print(f"Is number in array: {check(arr,num)}")
    num = 100
    print(f"New num is {num}")
    print(f"Array is: {arr}")
    print(f"Is number in array: {check(arr,num)}")


if __name__ == "__main__":
    main()
    exit()
