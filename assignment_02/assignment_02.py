import fileinput

def read_input():
    lines = []
    for line in fileinput.input():
        lines.append([ord(char) for char in line.strip()])
    return lines

def key_scheduling_algorithm(key):
    S = [n for n in range(0, 256)]
    j = 0
    for i in range(0, 256):
        j = (j + S[i] + key[i % len(key)]) % 256
        aux = S[i]
        S[i] = S[j]
        S[j] = aux
    
    return S

def pseudo_random_generation_algorithm(S, key, text):
    i =  j = 0
    result = ''
    for m in text:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        aux = S[i]
        S[i] = S[j]
        S[j] = aux
        index = (S[i] + S[j]) % 256
        k = S[index]
        result = result + format_hex_value(k ^ m)
    return result

def format_hex_value(value):
    formated_value = hex(value).lstrip("0x").upper()
    if(len(formated_value) == 1):
        formated_value = "0" + formated_value 
    return formated_value



key, text = read_input()
S = key_scheduling_algorithm(key)
result = pseudo_random_generation_algorithm(S, key, text)
print(result)