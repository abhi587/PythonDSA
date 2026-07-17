###########   Print Name N times using Recursion  ########


# Input: N = 3
# Output: Ashish Ashish Ashish 
# Explanation: Name is printed 3 times.
# Input: N = 1
# Output: Ashish 
# Explanation: Name is printed once.


# n = 3

# for i in range(n):
#     print("abhishek", end=" ")


#########  Print 1 to N using Recursion  ######

# Input: N = 4
# Output: 1, 2, 3, 4
# Explanation: All the numbers from 1 to 4 are printed.
# Input: N = 1
# Output: 1 
# Explanation: This is the base case.

# def print_1_to_n(n):
#     if n == 0:
#         return
#     print_1_to_n(n-1)
#     print(n, end=" ")

# print_1_to_n(4)


########  Print N to 1 using Recursion  #######

# Input: N = 4
# Output: 4, 3, 2, 1
# Explanation: All the numbers from 4 to 1 are printed.
# Input: N = 1
# Output: 1 
# Explanation: This is the base case.

# def print_number(n):
#     if n == 0:
#         return 
#     print(n, end= " ")

#     print_number(n-1)

# print_number(4)


##########  Sum of first N Natural Numbers  #########


# Input: N=5
# Output: 15
# Explanation: 1+2+3+4+5=15

# Input: N=6
# Output: 21
# Explanation: 1+2+3+4+5+6=15

# def find_sum(n):
#     if n == 0:
#         return 0 
#     return n + find_sum(n-1)

# print(find_sum(5))


##########  Factorial of a Number : Iterative and Recursive ########

# # Example 1:
# # Input:
# #  X = 5
# # Output:
# #  120
# # Explanation:
# #  5! = 5*4*3*2*1

# # Example 2:
# # Input:
# #  X = 3
# # Output:
# #  6
# # Explanation:
# #  3!=3*2*1

# def Factorial(n):
#     if n==0 or n==1:
#         return 1
    
#     return n*Factorial(n-1)

# print(Factorial(5))


# # Loop method

# n = 5
# fact = 1

# for i in range(1, n + 1):
#     fact *= i

# print(fact)


###########  Reverse a given Array ###############

# Input: N = 5, arr[] = {5,4,3,2,1}
# Output: {1,2,3,4,5}
# Explanation: Since the order of elements gets reversed the first element will occupy the fifth position, the second element occupies the fourth position and so on.

# Input: N=6 arr[] = {10,20,30,40}
# Output: {40,30,20,10}
# Explanation: Since the order of elements gets reversed the first element will occupy the fifth position, the second element occupies the fourth position and so on.

# def reverse( arr, left , right):
#     if left >= right:
#         return

#     arr[left], arr[right] = arr[right], arr[left]

#     reverse(arr, left+1, right-1)

# arr = [5,4,3,2,1]

# reverse(arr, 0, len(arr)-1)

# print(arr)


###########  Check if String is Palindrome or Not  #########


# class Solution:    
#     def palindromeCheck(self, s):
#         #your code goes here
#         rev = s[::-1]

#         if rev == s:
#             return True
#         else:
#             return False


############  Print Fibonacci Series up to Nth term   ########


# Example 1:
# Input: N = 5
# Output: 0 1 1 2 3 5
# Explanation: 0 1 1 2 3 5 is the fibonacci series up to 5th term.(0 based indexing)

# Example 2:
# Input: 6
# Output: 0 1 1 2 3 5 8
# Explanation: 0 1 1 2 3 5 8 is the fibonacci series upto 6th term.(o based indexing)


# class Solution:
#     def fib(self, n: int) -> int:
#         a = 0
#         b = 1

#         for i in range(n+1):
#             print(a, end = " ")

#             c = a+b
#             a = b
#             b = c


# Recursion solution

def fibonacci(n):

    if n == 0:
        return 0

    if n == 1:
        return 1

    return fibonacci(n-1) + fibonacci(n-2)


n = 5

for i in range(n + 1):
    print(fibonacci(i), end=" ")