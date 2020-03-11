def canThreePartsEqualSum(A):
    s = sum(A)
    if s % 3 != 0:
        return False
    i, j, l = 0, 0, len(A)
    target = s // 3
    s_l = 0
    while i < l:
        s_l += A[i]
        if s_l == target:
            break
        i += 1
    if s_l != target:
        return False
    j = i + 1
    while j + 1 < l:
        s_l += A[j]
        if s_l == target * 2:
            return True
        j += 1
    return False


if __name__ == '__main__':
    print(canThreePartsEqualSum([18, 12, -18, 18, -19, -1, 10, 10]))
