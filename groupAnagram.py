def group_anagrams(words):

    groups = {}

    for word in words:

        key = "".join(sorted(word))

        if key not in groups:
            groups[key] = []

        groups[key].append(word)

    return list(groups.values())

words = ["eat","tea","tan","ate","nat","bat"]

print(group_anagrams(words))



# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         combinations = []

#         while len(strs) > 0:
#             list_hold = [strs[0]]
#             for i in range(1, len(strs)):
#                 element_comp = strs[0]

#                 if sorted(element_comp) == sorted(strs[i]):    
#                     list_hold.append(strs[i])
            
#             for i in list_hold:
#                 strs.remove(i)
#             combinations.append(list_hold)

            
                
#         return combinations



class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) # mapping charCount to list of anagrams

        for s in strs:
            count = [0] * 26 # a ... z

            for c in s: 
                count[ord(c) - ord("a")] += 1

            res[tuple(count)].append(s)

        return list(res.values())

