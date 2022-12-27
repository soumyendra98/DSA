# 223, Simple Area Calculation | O(1) and O(1)

def computeArea(ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
    area_a = abs(ax1 - ax2) * abs(ay1 - ay2)
    area_b = abs(bx1 - bx2) * abs(by1 - by2)

    if ax1 <= bx1 < ax2:
        cx = abs(bx1 - min(ax2, bx2))
    elif bx1 <= ax1 < bx2:
        cx = abs(ax1 - min(ax2, bx2))
    else:
        return area_a + area_b

    if ay1 <= by1 < ay2:
        cy = abs(by1 - min(ay2, by2))
    elif by1 <= ay1 < by2:
        cy = abs(ay1 - min(ay2, by2))
    else:
        return area_a + area_b

    return area_a + area_b - (cy * cx)