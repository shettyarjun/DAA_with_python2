import time
import numpy as np
import matplotlib.pyplot as plt

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L, M = arr[:mid], arr[mid:]
        merge_sort(L)
        merge_sort(M)
        arr[:] = sorted(L + M)

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = min(range(i, len(arr)), key=arr.__getitem__)
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def read_input():
    n = int(input("Enter the number of TV Channels: "))
    return [int(input(f"Enter the number of viewers for TV Channel {i+1}: ")) for i in range(n)]

def time_analysis(sorting_func, label_data):
    elements, times = [], []
    
    print("********** Running Time Analysis **********")
    for i in range(1, 10):
        arr = np.random.randint(0, 1000 * i, 1000 * i)
        start = time.time()
        sorting_func(arr)
        end = time.time()
        print(len(arr), "Elements Sorted by", label_data, end - start)
        elements.append(len(arr))
        times.append(end - start)
    
    plt.xlabel('List Length')
    plt.ylabel('Time Complexity')
    plt.plot(elements, times, label=label_data)
    plt.grid()
    plt.legend()
    plt.show()

def main():
    print("1. Merge Sort 2. Quick Sort 3. Selection Sort 4. Insertion Sort")
    choice = int(input("Enter the Choice: "))

    if choice == 1:
        arr = read_input()
        arr = merge_sort(arr)
        print('Sorted Array:', arr)
        time_analysis(merge_sort, "Merge Sort")
    elif choice == 2:
        arr = read_input()
        arr = quick_sort(arr)
        print('Sorted Array:', arr)
        time_analysis(lambda arr: quick_sort(arr), "Quick Sort")
    elif choice == 3:
        arr = read_input()
        selection_sort(arr)
        print('Sorted Array:', arr)
        time_analysis(selection_sort, "Selection Sort")
    elif choice == 4:
        arr = read_input()
        insertion_sort(arr)
        print('Sorted Array:', arr)
        time_analysis(insertion_sort, "Insertion Sort")
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()
