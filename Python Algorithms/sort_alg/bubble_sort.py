import perm as pm
import sys
import check

	
def bubble_sort(arr, P, U):
	for i in range(len(arr)-1):
		for j in range(len(arr)-i-1):
			if arr[j] > arr[j+1]:
				arr[j], arr[j+1] = arr[j+1], arr[j]
	
			
			
			
def main():
    """
        Main code calls necesary functions
    """
    if len(sys.argv) != 3 or sys.argv[1] != "-size":
        print("The number of arguments is incorrect.\n Correct execution is:\npython3 bubble_sort.py -size (100)")
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
    bubble_sort(arr, 0, arr_len-1)
    print(f"Sorted array: {arr} \n")
    if(check.check(arr) == True):
        print("The array is correctly sorted")
    else:
        print("The array is not correctly sorted")


if __name__ == "__main__":
    main()
    exit()


	

