# filename = input("Enter file name: ")
# filehand = open(filename)
# lst = list()
# for line in filehand:
#     line.rstrip()
#     words = line.split()
#     for word in words:
#         if word not in lst:
#             lst.append(word)
# lst.sort()
# print(lst)


fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
count = 0
for line in fh:
    if line.startswith("From:"):
        new = line.split()
        print(new[1])
        count = count + 1

print("There were", count, "lines in the file with From as the first word")
