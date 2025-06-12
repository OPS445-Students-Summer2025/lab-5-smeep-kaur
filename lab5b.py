#!/usr/bin/env python3
# Author ID: Smeep-kaur@myseneca.ca

def read_file_string(file_name):
    f = open(file_name, 'r')
    content = f.read()
    f.close()
    return content

def read_file_list(file_name):
    f = open(file_name, 'r')
    lines = f.readlines()
    f.close()
    result = []
    for line in lines:
        result.append(line.strip())
    return result
def append_file_string(file_name, string_of_lines):
    f = open(file_name, 'a')            # open in append mode
    f.write(string_of_lines)            # write the entire string
    f.close()

def write_file_list(file_name, list_of_lines):
    f = open(file_name, 'w')            # open in write mode
    for line in list_of_lines:
        f.write(line + '\n')            # write each item on its own line
    f.close()

def copy_file_add_line_numbers(file_name_read, file_name_write):
    f1 = open(file_name_read, 'r')      # read from this file
    lines = f1.readlines()              # read all lines
    f1.close()

    f2 = open(file_name_write, 'w')     # write to this file
    line_number = 1
    for line in lines:
        line = line.strip()             # remove \n
        f2.write(str(line_number) + ':' + line + '\n')
        line_number += 1
    f2.close()

if __name__ == '__main__':
    file1 = 'seneca1.txt'
    file2 = 'seneca2.txt'
    file3 = 'seneca3.txt'
    string1 = 'First Line\nSecond Line\nThird Line\n'
    list1 = ['Line 1', 'Line 2', 'Line 3']
    append_file_string(file1, string1)
    print(read_file_string(file1))
    write_file_list(file2, list1)
    print(read_file_string(file2))
    copy_file_add_line_numbers(file2, file3)
    print(read_file_string(file3))

