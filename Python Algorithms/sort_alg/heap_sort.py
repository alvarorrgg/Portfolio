import perm as pm
import sys
import check
import math as m


def max_heap_check(heap, P, U):
    # We convert the heal to a max heap so its easier to sort
    n_fathers = int(m.log2(len(heap)))
    for i in range((2**n_fathers)-1):
        try:
            if heap[i] < heap[2*i+1] or heap[i] < heap[2*i+2]:
                return False
        except:
            break
    return True


def heapify(heap, ind):
    while True:
        try:
            if heap[2*ind+1] > heap[2*ind+2]:
                if heap[ind] > heap[2*ind+1]:
                    break
                else:
                    heap[ind], heap[2*ind+1] = heap[2*ind+1], heap[ind]
                    ind = 2*ind + 1
            else:
                if heap[ind] > heap[2*ind+2]:
                    break
                else:
                    heap[ind], heap[2*ind+2] = heap[2*ind+2], heap[ind]
                    ind = 2*ind + 2

        except:
            try:
                if heap[ind] > heap[2*ind+1]:
                    break
                else:
                    heap[ind], heap[2*ind+1] = heap[2*ind+1], heap[ind]
                    ind = 2*ind + 1
            except:
                break


def convert_max_heap(heap, P, U):
    # To convert we will aply a simple algorithm
    if U % 2 != 0:
        length = int(U/2) + 1
    else:
        length = int(U/2)
    for i in range(length):
        heapify(heap, length-1-i)


def heap_sort(heap, P, U):
    heap_aux = []
    for i in range(U+1):
        heap[0], heap[U-i] = heap[U-i], heap[0]
        heap_aux.insert(0, heap.pop(U-i))
        heapify(heap, 0)
    return heap_aux


def heap_alg(heap, P, U):
    """
        This algorithm sorts the array using heap_sort method.
        heap sort method is a local sorting algorithm. This means it sorts a max of 1 element on each loop.
    """
    # We check if heap is a max_heap
    if not max_heap_check(heap, P, U):
        convert_max_heap(heap, P, U)
        heap = heap_sort(heap, P, U)
    else:
        heap = heap_sort(heap, P, U)
    return heap


def main():
    """
        Main code calls necesary functions
    """
    if len(sys.argv) != 3 or sys.argv[1] != "-size":
        print("The number of arguments is incorrect.\n Correct execution is:\npython3 heap_sort.py -size (100)")
        exit()
    try:
        arr_len = int(sys.argv[2])
    except:
        print("Last argument must be a number")
        exit()

    heap = [i for i in range(1, 1+arr_len)]
    print(f"New Array: {heap} \n")
    pm.perm(heap, arr_len)
    print(f"Permuted Array: {heap} \n")
    heap = heap_alg(heap, 0, arr_len-1)
    print(f"Sorted array: {heap} \n")

    if(check.check(heap) == True):
        print("The array is correctly sorted")
    else:
        print("The array is not correctly sorted")


if __name__ == "__main__":
    main()
    exit()
