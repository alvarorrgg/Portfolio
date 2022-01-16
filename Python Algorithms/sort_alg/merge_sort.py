import perm as pm
import sys
import time
import check


def merge_sort(arr, P, U):

    M = (U+P)/2
    if P > U:
        return False
    if P == U:
        return True
    merge_sort(arr, P, int(M))
    merge_sort(arr, int(M+1), U)
    return merge(arr, int(P), int(M), U)


def merge(arr, P, M, U):
    T = [0 for i in range(U-P+1)]
    i = P
    j = M+1
    k = 0
    while i <= M and j <= U:
        if arr[i] < arr[j]:
            T[k] = arr[i]
            i += 1
        else:
            T[k] = arr[j]
            j += 1
        k += 1
    if i > M:
        while j <= U:
            T[k] = arr[j]
            k += 1
            j += 1
    elif j > U:
        while i <= M:
            T[k] = arr[i]
            k += 1
            i += 1
    arr[P:U+1] = T[0:U+1]
    return


def main():
    """
        Main code calls necesary functions
    """
    if len(sys.argv) != 3 or sys.argv[1] != "-size":
        print("The number of arguments is incorrect.\n Correct execution is:\npython3 merge_sort.py -size (100)")
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
    merge_sort(arr, 0, arr_len-1)
    print(f"Sorted array: {arr} \n")
    if(check.check(arr) == True):
        print("The array is correctly sorted")
    else:
        print("The array is not correctly sorted")


if __name__ == "__main__":
    main()
    exit()
