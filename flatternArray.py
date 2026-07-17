arr = [[1,3],[2],[6,[12,[14]]],[8,10],[15,18]]
 



# result = []

# for i in range(len(arr)):
#     # print(arr[i])
#     for j in arr[i]:
#         # print(j)
#         result.append(j)


# print(result)


# flattern an array using recursion


def fattern(data):
    result = []
    for item in data:
        if isinstance(item, list):
            result.extend(fattern(item))
        else:
            result.append(item)
    return result

answer = fattern(arr)
print(answer)
