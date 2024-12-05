with open('input.txt', 'r') as infile:
    data = infile.readlines()

rules = {}
for idx, line in enumerate(data):
    if line == '\n':
        break
    rules[line.strip()] = True

sum = 0
sum_bad = 0
for line in data[idx+1:]:
    nbrs = line.split(',')
    nbrs[-1] = nbrs[-1].strip()
    bad = False
    for i, left in enumerate(nbrs):
        for j, right in enumerate(nbrs[i+1:]):
            if f'{right}|{left}' in rules:
                bad = True
                nbrs[i] = right
                nbrs[j+i+1] = left
                left = right
    if not bad:
        sum += int(nbrs[int(len(nbrs)/2)])
    else:
        sum_bad += int(nbrs[int(len(nbrs)/2)])
print(sum)
print(sum_bad)