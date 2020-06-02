# time = [1,0,2,3,0,4,5,0]
time = [1,2,3]

# for (int i = 3; i >= 0; i--) {
#     intArray[i + 1] = intArray[i];
# }
# count = len(time)
#
# for i in count:
#     if time[i] == 2:
#         time.insert(i+1,0)
#         time.pop()
#         count += 1
i = len(time) - 1

while i >= 0:
    if time[i] == 0:
        time.insert(i+1, 0)
        time.pop()
    i -= 1




print(time)


