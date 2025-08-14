"""
Given an array, arr[] of n integers, and an integer element x, find whether element x is present in the array. Return the index of the first occurrence of x in the array, or -1 if it doesn't exist.

Input: arr[] = [1, 2, 3, 4], x = 3
Output: 2
Explanation: There is one test case with array as [1, 2, 3 4] and element to be searched as 3. Since 3 is present at index 2, the output is 2.

Input: arr[] = [10, 8, 30, 4, 5], x = 5
Output: 4
Explanation: For array [10, 8, 30, 4, 5], the element to be searched is 5 and it is at index 4. So, the output is 4.

Input: arr[] = [10, 8, 30], x = 6
Output: -1
Explanation: The element to be searched is 6 and its not present, so we return -1.
"""


def linear_search(arr, x):
    
    for index, num in enumerate(arr):
        if num == x:
            return index

    return -1    


if __name__ == "__main__":
    test1, x1, output1 = [1, 2, 3, 4], 3, 2
    test2, x2, output2 = [10, 8, 30, 4, 5], 5, 4
    test3, x3, output3 = [10, 8, 30], 6, -1

    test = [test1, test2, test3]
    x = [x1, x2, x3]
    output = [output1, output2, output3]

    for t, s, o in zip(test, x, output):
        assert linear_search(t, s) == o
    
    print("All tests passed")
