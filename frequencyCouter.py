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


# frequency counter with return the highest time occurring word

# output = happy

def most_freq_word(sentance):
    
    words = sentance.split()

    freq = {}

    for word in words:
        if word in freq:
            freq[word] = freq[word] + 1
        else: 
            freq[word] = 1

    max_word = ""
    max_count = 0 

    for word in freq: 
        if freq[word] > max_count:
            max_count = freq[word]
            max_word = word

    return max_word


sentance= "happy happy friday happy friday"
print(most_freq_word(sentance))

