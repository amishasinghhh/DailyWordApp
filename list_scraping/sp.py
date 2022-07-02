with open('spwords.txt') as f:
    lines = f.readlines()
new = []

for line in lines:
    for i in range(len(line)):
        if line[i] == "(":
            new.append(line[:i])
            break

with open('sp.txt', 'w') as f:
    for line in new:
        f.write(line)
        f.write('\n')