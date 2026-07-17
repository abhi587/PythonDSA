# arr = [ 1,2,3,4,2,1,4,3,0,6,2]
# arr = "abhishek"

# freq = {}

# for num in arr:

#     if num in freq:
#         freq[num] += 1
#     else:
#         freq[num] = 1

# print(freq)


# count the number of fruits
text = "apple orange orange apple mango pineapple"

words = text.split()
freq = {}

for word in words:
    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1

print(freq)