import sys
import random as rn
import check as ch


def lineal_search(arr, search_num):
    for i in arr:
        if i == search_num:
            return True
    return False


def main():
    """
        Main code calls necesary functions
    """
    if len(sys.argv) != 5 or sys.argv[1] != "-size" or sys.argv[3] != "-search_num":
        print("The number of arguments is incorrect.\n Correct execution is:\npython3 Insert_sort.py -size (100) -search_num (100)")
        exit()
    try:
        arr_len = int(sys.argv[2])
        search_num = int(sys.argv[4])
    except:
        print("Last argument must be a number")
        exit()
    arr = [rn.randint(1, arr_len) for i in range(1, 1+arr_len)]
    print(f"Permuted array: {arr}")
    arr.sort()
    print(f"Sorted array: {arr}")
    if lineal_search(arr, search_num) == True and ch.check(arr, search_num) == True:
        print("The number was found on the list")
    else:
        print("The number was NOT found in the list")


if __name__ == "__main__":
    main()
    exit()
