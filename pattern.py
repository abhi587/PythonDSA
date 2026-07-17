n = 5


#################( 1 )############################


# * * * * *
# * * * * *
# * * * * *
# * * * * *
# * * * * *

# for i in range(n):
#     for j in range(n):
#         print("*", end=" ")
#     print()


#######################(  2) ######################


# * 
# * * 
# * * * 
# * * * * 
# * * * * * 

# for i in range(n):
#     for j in range(i+1):
#         print("*", end = " ")
#     print()


###################( 3 )##########################


# 1 
# 1 2 
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

# for i in range(n):
#     for j in range(i+1):
#         print(j+1, end = " ")
#     print()


####################( 4 )#######################


# 1 
# 2 2 
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5

# for i in range(n):
#     for j in range(i+1):
#         print(i+1, end=" ")
#     print()


######################( 5 )######################


# * * * * * 
# * * * * 
# * * *
# * *
# *

# for i in range(n):
#     for j in range(n-i):
#         print("*", end = " ")
#     print()


#####################( 6 )#####################


# 1 2 3 4 5 
# 1 2 3 4 
# 1 2 3
# 1 2
# 1

# for i in range(n):
#     for j in range(n-i):
#         print(j+1, end = " ")
#     print()


#######################( 7 )##################


#         * 
#       * * * 
#     * * * * *
#   * * * * * * *
# * * * * * * * * *

# for i in range(n):
#     for j in range(n-i-1):
#         print(" ", end=" ")
#     for j in range(2*i+1):
#         print("*", end = " ")
#     print()


####################( 8 )##################


# * * * * * * * 
#   * * * * * 
#     * * *
#       *

# for i in range(n):
#     for j in range(i):
#         print(" ", end = " ")
#     for j in range(2*(n-i-1)-1):
#         print("*", end= " ")
#     print()


#####################( 9 )##################


#         * 
#       * * * 
#     * * * * *
#   * * * * * * *
# * * * * * * * * *
#   * * * * * * *
#     * * * * *
#       * * *
#         *

# for i in range(n):
#     for j in range(n-i-1):
#         print(" ", end=" ")
#     for j in range(2*i+1):
#         print("*", end = " ")
#     print()

# for i in range(n):
#     for j in range(i+1):
#         print(" ", end = " ")
#     for j in range(2*(n-i-1)-1):
#         print("*", end= " ")
#     print()



######################( 10 )###################


# * 
# * * 
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *

# for i in range(n):
#     for j in range(i+1):
#         print("*", end = " ")
#     print()
# for i in range(n):
#     for j in range(n-i-1):
#         print("*", end = " ")
#     print()


####################( 11 )#####################

# 1 
# 0 1 
# 1 0 1
# 0 1 0 1
# 1 0 1 0 1

# for i in range(n):
#     for j in range(i+1):
#         if (i+j)%2==0:
#             print("1", end = " ")
#         else:
#             print("0", end = " ")
#     print()


#####################( 12 )####################


# 1                 1 
# 1 2             2 1 
# 1 2 3         3 2 1
# 1 2 3 4     4 3 2 1
# 1 2 3 4 5 5 4 3 2 1

# for i in range(1, n+1):
#     for j in range(1, i+1):
#         print(j, end = " ")
#     for j in range(2*(n-i)):
#         print(" ", end=" ")
#     for j in range(i, 0, -1):
#         print(j, end = " ")
#     print()


#################### ( 13 ) ####################


# 1 
# 2 3 
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15

# num =1

# for i in range(n):
#     for j in range(i+1):
#         print(num, end = " ")
#         num += 1
#     print()


#################### ( 14 ) ##################

# A 
# A B 
# A B C
# A B C D
# A B C D E

# for i in range(n):
#     for j in range(i+1):
#         print(chr(65+j), end = " ")
#     print()


##################### ( 15 ) ######################


# A B C D E 
# A B C D 
# A B C
# A B
# A

# for i in range(n):
#     for j in range(n-i):
#         print(chr(65+j), end = " ")
#     print()


######################## ( 16 ) #####################

# A 
# B B 
# C C C
# D D D D
# E E E E E

# for i in range(n):
#     for j in range(i+1):
#         print(chr(65+i), end = " ")
#     print()

####################### ( 17 ) #######################


#         A 
#       A B A 
#     A B C B A
#   A B C D C B A
# A B C D E D C B A

# for i in range(n):
#     for j in range(n-i-1):
#         print(" ", end= " ")
#     for j in range(i+1):
#         print(chr(65+j), end = " ")
#     for j in range(i-1, -1, -1):
#         print(chr(65+j), end = " ")
#     print()


###################### ( 18 ) #########################


# E 
# D E 
# C D E
# B C D E
# A B C D E

# for i in range(n):
#     for j in range(i+1):
#         print(chr(65+n-i-1+j), end= " ")
#     print()


###################### ( 19 ) #########################


# * * * * * * * * * * 
# * * * *     * * * * 
# * * *         * * *
# * *             * *
# *                 *
# *                 *
# * *             * *
# * * *         * * *
# * * * *     * * * *
# * * * * * * * * * *

# for i in range(n):
#     for j in range(n-i):
#         print("*", end=" ")
#     for j in range(2*i):
#         print(" ", end= " ")
#     for j in range(n-i):
#         print("*", end=" ")
#     print()

# for i in range(n):
#     for j in range(i+1):
#         print("*", end = " ")
#     for j in range(2*(n-i-1)):
#         print(" ", end=" ")
#     for j in range(i+1):
#         print("*", end=" ")
#     print()


#################### ( 20 ) ############################


# *        *
# **      **
# ***    ***
# ****  ****
# **********
# ****  ****
# ***    ***
# **      **
# *        *

# for i in range(1, n + 1):
#     stars = i
#     spaces = 2 * (n - i)

#     print("*" * stars + " " * spaces + "*" * stars)

# for i in range(n - 1, 0, -1):
#     stars = i
#     spaces = 2 * (n - i)

#     print("*" * stars + " " * spaces + "*" * stars)


####################### ( 21 ) #########################

# *****
# *   *
# *   *
# *   *
# *****

# for i in range(n):
#     for j in range(n):
#         if i == 0 or i == n-1 or j == 0 or j == n-1:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()


#################### ( 22 ) ######################


# 5 5 5 5 5 5 5 5 5 
# 5 4 4 4 4 4 4 4 5 
# 5 4 3 3 3 3 3 4 5
# 5 4 3 2 2 2 3 4 5
# 5 4 3 2 1 2 3 4 5
# 5 4 3 2 2 2 3 4 5
# 5 4 3 3 3 3 3 4 5
# 5 4 4 4 4 4 4 4 5
# 5 5 5 5 5 5 5 5 5

# size = 2* n-1

# for i in range(size):
#     for j in range(size):
#         val = n-min(i,j,size-1-i,size-1-j)
#         print(val, end=" ")
#     print()
