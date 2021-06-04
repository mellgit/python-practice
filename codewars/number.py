# Find the first non-consecutive number


def main():
    print(first_non_consecutive([-7, -6, -5, -4, 8]))

def first_non_consecutive(arr):
    
    

    for i in range(len(arr)-1):
        if arr[i+1] - arr[i] != 1:
            return arr[i+1]

    return None
          
main()

