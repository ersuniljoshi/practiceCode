# GeeksforGeeks
# Find minimum difference between any two elements
# Given an unsorted array, find the minimum difference between any pair in given array.
import sys

# arr = [1, 5, 3, 19, 18, 25]
arr = [30, 5, 20, 9]
#  arr = [1, 19, -4, 31, 38, 25, 100]
arr.sort()
diff = sys.maxint
print "Sorted Array: {}".format(arr)
for i in range(len(arr)-2):
    if (arr[i+1]-arr[i] < diff):
        diff = arr[i+1]-arr[i]
        x = i

print "Minimum difference is between {0} and {1} is {2}".format(arr[x+1], arr[x], diff)
