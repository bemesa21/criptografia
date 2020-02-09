import fileinput

def read_input():
    lines = []
    for line in fileinput.input():
        lines.append(convert_num(line.strip()))
    return lines

def convert_num(num):
    try:
        return int(num)
    except ValueError:
        return float(num)

values = read_input()
print(sum(values))