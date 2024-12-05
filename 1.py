with open('input.txt', 'r') as infile:
    data = infile.readlines()

l_1 = []
l_2 = []
for line in data:
    a, b = line.split()
    l_1.append(int(a))
    l_2.append(int(b))

l_1.sort()
l_2.sort()

distance = 0
for idx in range(len(l_1)):
    distance += abs(l_1[idx] - l_2[idx])

print(distance)

final_score = 0
scores = {}
for number in l_1:
    if number in scores:
        final_score += scores[number]
        continue
    scores[number] = number * l_2.count(number)
    final_score += scores[number]

print(final_score)

