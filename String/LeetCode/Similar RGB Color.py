# 800, Using Set and hex() | O(1) and O(1)

def similarRGB(color: str) -> str:
    output = "#"
    hex_set = set()

    for idx in range(16):
        hex_set.add(hex(idx) + hex(idx)[2:])

    for idx in range(1, len(color), 2):
        if color[idx] == color[idx + 1]:
            output += color[idx: idx + 2]
            continue
        min_val = ""
        min_diff = float("inf")
        for val in hex_set:
            diff = abs(int(val, 16) - int(color[idx: idx + 2], 16))
            if diff < min_diff:
                min_val = val
                min_diff = diff

        output += min_val[2:]

    return output
