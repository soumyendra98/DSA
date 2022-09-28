# 557, Split and Reverse | O(N) and O(N)
def reverseWords(s: str) -> str:
    s_arr = s.split(" ")

    for idx in range(len(s_arr)):
        s_arr[idx] = s_arr[idx][::-1]

    return " ".join(s_arr)
