# 给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。


def generate(numRows):
    if numRows == 0:
        return []
    triangle = [[1]]
    for i in range(1, numRows):
        tmp = [1, 1]
        for j in range(1, i):
            tmp.insert(j, triangle[i-1][j-1] + triangle[i-1][j])
        triangle.append(tmp)
    return triangle


print(generate(5))
