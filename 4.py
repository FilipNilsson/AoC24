with open('input.txt', 'r') as infile:
    data = infile.readlines()

for idx, line in enumerate(data):
    data[idx] = '...' + line.strip('\n') + '...'
data.insert(0, '.' * len(data[0]))
data.insert(0, '.' * len(data[0]))
data.insert(0, '.' * len(data[0]))
data.append('.' * len(data[0]))
data.append('.' * len(data[0]))
data.append('.' * len(data[0]))

part_1 = False
if part_1:
    matches = 0
    for row, line in enumerate(data):
        for col, char in enumerate(line):
            if char != 'X':
                continue
            if line[col:col+4] == 'XMAS':  # right
                matches += 1
            if line[col-3:col+1] == 'SAMX':  # left
                matches += 1
            if data[row+1][col] == 'M' and data[row+2][col] == 'A' and data[row+3][col] == 'S':  # down
                matches += 1
            if data[row-1][col] == 'M' and data[row-2][col] == 'A' and data[row-3][col] == 'S':  # up
                matches += 1
            if data[row+1][col+1] == 'M' and data[row+2][col+2] == 'A' and data[row+3][col+3] == 'S':  # down-right
                matches += 1
            if data[row-1][col-1] == 'M' and data[row-2][col-2] == 'A' and data[row-3][col-3] == 'S':  # up-left
                matches += 1
            if data[row+1][col-1] == 'M' and data[row+2][col-2] == 'A' and data[row+3][col-3] == 'S':  # down-left
                matches += 1
            if data[row-1][col+1] == 'M' and data[row-2][col+2] == 'A' and data[row-3][col+3] == 'S':  # up-right
                matches += 1
    print(matches)

else:
    matches = 0
    for row, line in enumerate(data):
        for col, char in enumerate(line):
            if char != 'A':
                continue
            if (data[row-1][col-1] + data[row+1][col+1]) in ('MS', 'SM'):
                if (data[row+1][col-1] + data[row-1][col+1]) in ('MS', 'SM'):
                    matches += 1
    print(matches)