s = "anagram"
t = "nagaram"

def is_anagram(s, t):

    if len(s) != len(t):
        return False

    countS = {}
    countT = {}

    for i in range(len(s)):

        if s[i] in countS:
            countS[s[i]] += 1
        else:
            countS[s[i]] = 1

        if t[i] in countT:
            countT[t[i]] += 1
        else:
            countT[t[i]] = 1

    return countS == countT

print(is_anagram(s,t))