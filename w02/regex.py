import re
name = "regex_sum_413796.txt"
handle = open(name)
sum = 0
for line in handle:
    lst = re.findall("[0-9]+", line)
    if len(lst) < 1:
        continue
    for i in lst:
        sum += int(i)
print(sum)
