# Given a number find the respective excel column name

n = int(input())
columnName=""
while n > 0:
    pos = (n - 1) % 26
    columnName += chr(pos + ord('A'))
    n = (n - 1) // 26
print(columnName[::-1])