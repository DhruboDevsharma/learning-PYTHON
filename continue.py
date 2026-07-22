n = int(input())

i = 1
while i < n:
    if i == 5:
        i += 1   # এখানে i বাড়াতে হবে, না হলে infinite loop হবে
        continue
    print(i)
    i += 1
print("end")
