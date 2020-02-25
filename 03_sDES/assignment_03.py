import fileinput
from collections import deque

def read_input():
    lines = []
    for line in fileinput.input():
        lines.append(line.strip().replace(" ", ""))
    return lines

def create_keys(number_of_keys, key):
    keys = []
    permuted_values = permutation(key, [2, 4, 1, 6, 3, 9, 0, 8, 7, 5])
    left_half = deque(permuted_values[:5])
    right_half = deque(permuted_values[5:])
    for i in range(1, number_of_keys + 1):
        left_half.rotate(-i) 
        right_half.rotate(-i)
        joined_halfs = join_deques_into_list(left_half, right_half) 
        keys.append(subkey(joined_halfs, [5, 2, 6, 3, 7, 4 ,9 ,8]))
    return keys

def join_deques_into_list(a, b):
    return list(a) + list(b)

def subkey(original_array, index_array):
    some = [original_array[i] for i in index_array]
    return some

def permutation(original_array, permutation_index_array):
    new_list = [0 for i in range(len(original_array))]
    for i in range(len(original_array)):
        new_list[i] = original_array[permutation_index_array[i]]
    return new_list

    

def sDES(text, subkeys):
    subkey_one, subkey_two = subkeys
    initial_permutation = permutation(text, [1, 5,2,0,3,7,4,6])

    left_half = initial_permutation[:4]
    right_half = initial_permutation[4:]

    result_one = feistel_operation(right_half,subkey_one, left_half)
    
    left_half = result_one[4:]
    right_half = result_one[:4]

    result_two = feistel_operation(right_half,subkey_two, left_half)

    final_permutation = permutation(result_two, [3, 0,2,4,6,1,7,5])
    return ''.join([str(elem) for elem in final_permutation])



def feistel_operation(right_half, sub_key, left_half):
    expanded_data = subkey(right_half, [3,0,1,2,1,2,3,0])
    xored_data = xor_lists(expanded_data,sub_key)
    
    s_box_one = s_box(xored_data[:4], [[1,0,3,2],[3,2,1,0],[0,2,1,3],[3,1,3,2]])
    s_box_two = s_box(xored_data[4:], [[0,1,2,3], [2,0,1,3], [3,0,1,0], [2,1,0,3]])
    
    joined_sbox = s_box_one + s_box_two
    permuted_sbox_concatenation = permutation(joined_sbox, [1,3,2,0])

    return xor_lists(permuted_sbox_concatenation, left_half) + right_half

def xor_lists(list1, list2):
    return [list1[i] ^ list2[i] for i in range(0, len(list1))]

def s_box(data, s_box):
    row_bits = [data[0],data[3]]
    column_bits = [data[1],data[2]]
    row = int("".join(str(x) for x in row_bits), 2)
    column = int("".join(str(x) for x in column_bits), 2)
    return format_bin_value(s_box[row][column])

def format_bin_value(value):
    formated_value = bin(value).lstrip("0b")
    if(len(formated_value) == 1):
        formated_value = "0" + formated_value 
    if value == 0:
        formated_value = "00"

    return [int(i) for i in list(formated_value)]




method, key, text = read_input()

subkeys = create_keys(2, [int(i) for i in list(key)])

if(method == "E"):
    print(sDES([int(i) for i in list(text)], subkeys))
else:
    subkeys.reverse()
    print(sDES([int(i) for i in list(text)], subkeys))