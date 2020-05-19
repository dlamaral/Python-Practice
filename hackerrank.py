# 123...n integer print
n = int(input())
print(''.join(str(i) for i in range(1, n+1)))

# list compreehension exercise cuboid

x = int(input())
y = int(input())
z = int(input())
n = int(input())
print([[i, j, k] for i in range( x + 1) for j in range( y + 1) for k in range ( z + 1) if ( ( i + j + k ) != n )])

