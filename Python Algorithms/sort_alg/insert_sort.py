import perm as pm
import sys
import check


def insert_sort(arr, P, U):
    """
        This algorithm sorts the array using insert_sort method.
        insert sort method is a local sorting algorithm. This means it sorts a max of 1 element on each loop.
    """
    for i in range(P+1, U+1):
        j = i-1
        a = arr[i]
        while arr[j] > a and j >= P:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = a


def main():
    """
        Main code calls necesary functions
    """
    if len(sys.argv) != 3 or sys.argv[1] != "-size":
        print("The number of arguments is incorrect.\n Correct execution is:\npython3 Insert_sort.py -size (100)")
        exit()
    try:
        arr_len = int(sys.argv[2])
    except:
        print("Last argument must be a number")
        exit()

    arr = [i for i in range(1, 1+arr_len)]
    print(f"New Array: {arr} \n")
    pm.perm(arr, arr_len)
    print(f"Permuted Array: {arr} \n")
    insert_sort(arr, 0, arr_len-1)
    print(f"Sorted array: {arr} \n")
    if(check.check(arr) == True):
        print("The array is correctly sorted")
    else:
        print("The array is not correctly sorted")


if __name__ == "__main__":
    main()
    exit()
