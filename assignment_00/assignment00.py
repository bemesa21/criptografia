import fileinput

def read_input():
    lines = []
    for line in fileinput.input():
        lines.append(float(line.strip()))
    return lines

values = read_input()
print(sum(values))