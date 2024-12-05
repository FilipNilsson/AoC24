with open('input.txt', 'r') as infile:
    data = infile.readlines()[0]

def mul(x, y):
    if not 1 < x < 1000 or not 1 < y < 1000:
        return 0
    if int(x) != x and int(y) != y:
        return 0
    return x*y

window_size = 12
sum = 0
enabled = True
for idx, _ in enumerate(data):
    window = data[idx:idx+window_size]
    if window.startswith("do()"):
        enabled = True
        continue
    if window.startswith("don't()"):
        enabled = False
        continue
    if not enabled:
        continue
    if not window.startswith("mul("):
        continue
    window_rest = window.split(')', 1)
    if len(window_rest) == 1:
        continue
    window = window_rest[0] + ')'
    try:
        sum += eval(window)
    except Exception:
        pass
print(sum)