n = 32
count = 0
while(n):
    count += n & 1
    n >>= 1
print(count)