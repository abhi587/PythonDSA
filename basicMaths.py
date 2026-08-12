# Example 1:
# Input:N = 12345
# Output:5
# Explanation:  The number 12345 has 5 digits.

# Example 2:
# Input:N = 7789              
# Output: 4
# Explanation: The number 7789 has 4 digits.


# n = 123456

# cnt = 0
# while n > 0:
#     cnt = cnt + 1
#     n = n // 10
# print(cnt)


################### REVERSE A NUMBER ####################

# n = 12345

# revNum = 0

# while n>0:
#     #Get the last digit
#     lastDigit = n %10
#     #append it to the reversed number
#     revNum = revNum*10+lastDigit
#     #remove the last digit forn number
#     n=n//10

# print(revNum)


##################  PALINDROME OR NOT  #####################

# n = 4554
# original = n

# rev = 0

# while n > 0:
#     lastDigit = n%10
#     rev = rev*10+lastDigit
#     n = n//10

# if(rev == original):
#     print("is palindrome")
# else:
#     print("not a palindrome")



###################  GCD  #######################

# Example 1:
# Input: N1 = 9, N2 = 12

# Output: 3
# Explanation:
# Factors of 9: 1, 3, 9
# Factors of 12: 1, 2, 3, 4, 6, 12
# Common Factors: 1, 3
# Greatest common factor: 3 (GCD)

# Example 2:
# Input: N1 = 20, N2 = 15

# Output: 5
# Explanation:
# Factors of 20: 1, 2, 4, 5, 10, 20
# Factors of 15: 1, 3, 5, 15
# Common Factors: 1, 5
# Greatest common factor: 5 (GCD)

# a = 20
# b = 15

# while b != 0:
#     a,b = b,a%b

# print(a)



############### Armstrong Number or not ##############


# Example 1:
# Input:N = 153
# Output:True
# Explanation: 1^3+5^3+3^3 = 1 + 125 + 27 = 153
                                        
# Example 2:
# Input:N = 371                
# Output: True
# Explanation: 3^3+7^3+1^3 = 27 + 343 + 1 = 371

# n = 153
# original = n 

# digits = len(str(n))
# sum_val = 0

while n>0:
    last = n%10
    sum_val += last ** digits
    n = n//10

if sum_val == original:
    print("True")
else:
    print("False")



###################### Print all Divisors of a given Number ######################


# Input: N = 36
# Output: [1, 2, 3, 4, 6, 9, 12, 18, 36]  
# Explanation: The divisors of 36 are 1, 2, 3, 4, 6, 9, 12, 18, 36.
# Input: N = 12
# Output: [1, 2, 3, 4, 6, 12]
# Explanation: The divisors of 12 are 1, 2, 3, 4, 6, 12.


# # Method 1
# n = 36
# arr = []

# for i in range(1, n+1):
#     if n % i == 0:
#         arr.append(i)

# print(arr)

# # Method 2
# n = 36
# arr = []

# for i in range(1, int(n ** 0.5)+1):
#     if n%i==0:
#         arr.append(i)

#     if i != n//i:
#         arr.append(n//i)

# arr.sort()
# print(arr)


############## Number is Prime or Not #################

# Example 1:
# Input:N = 2
# Output:True
# Explanation: 2 is a prime number because it has two divisors: 1 and 2 (the number itself).
                                        
# Example 2:
# Input:N =10                
# Output: False
# Explanation: 10 is not prime, it is a composite number because it has 4 divisors: 1, 2, 5 and 10.                          

##Method 1
# n = 2
# count = 0

# for i in range(1, n+1):
#     if n%i == 0:
#         count += 1

# if count == 2:
#     print("True")
# else:
#     print("False")


## Method 2
# n = 2

# if n <= 1:
#     print("False")
# else:
#     is_prime = True

#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             is_prime = False
#             break

#     print(is_prime)