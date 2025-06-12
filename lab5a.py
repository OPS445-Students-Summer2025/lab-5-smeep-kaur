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

if __name__ == '__main__':
    file_name = 'data.txt'
    print(read_file_string(file_name))
    print(read_file_list(file_name))
