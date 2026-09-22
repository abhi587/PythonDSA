def longest_subString(s):

    longest = ""

    for i in range(len(s)):
        current = ""

        for j in range(i, len(s)):
            if s[j] in current:
                break

            current += s[j]

        if len(current) > len(longest):
            longest = current

    return longest

s = 'abcabcdab'
res = longest_subString(s)

result = len(res)

print(result)

