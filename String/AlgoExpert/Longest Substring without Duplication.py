# Hash Table | O(N) and O(min(N, L))
def longestSubstringWithoutDuplication(string):
    # Write your code here.
    longest = [0, 1]
    start = 0
    char_dict = {}
    for i, val in enumerate(string):
        if val in char_dict:
            start = max(start, char_dict[val] + 1)

        if longest[1] - longest[0] < i + 1 - start:
            longest = [start, i + 1]
        char_dict[val] = i
    return string[longest[0]:longest[1]]


# O(N^2) and O(min(N, L)) solution
# def longestSubstringWithoutDuplication(string):
#     # Write your code here.
#     output = ''
#     temp = ''
#     char_dict = {}
#     i = 0
#
#     while i < len(string):
#         if string[i] not in char_dict:
#             char_dict[string[i]] = i
#             temp += string[i]
#         else:
#             if len(temp) > len(output):
#                 output = temp
#             temp = ''
#             i = char_dict[string[i]]
#             char_dict = {}
#
#         i += 1
#         if len(temp) > len(output):
#             output = temp
#     return output


str1 = 'clementisacap'

print(longestSubstringWithoutDuplication(str1))
