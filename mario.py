row, col = map(int, input().split())

mat = [['0' for _ in range(col)] for _ in range(row)]
for i in range(row):
    s = input()
    for j in range(col):
        mat[i][j] = s[j]

res = 0
for i in range(col):
    temp = row
    for j in range(row):
        if mat[j][i] == 'C':
            temp = row - j - 1
            break
        elif mat[j][i] == 'H':
            if temp != 0:
                continue
            else:
                temp = row - j
        elif mat[j][i] == '0':
            temp = 0
    res += temp

coin = 0
for i in range(row):
    for j in range(col):
        if mat[i][j] == 'C':
            coin += 1

print(coin, res * 2, end="")