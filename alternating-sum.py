a,b,term_count=map(int,input().split())
total = 0
for index in range(term_count):
    if index % 2 == 0:
        total += a
    else:
        total += b
print(total)

