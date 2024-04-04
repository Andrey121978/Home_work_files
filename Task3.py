line_file1 = []
line_file2 = []
line_file3 = []


def append_line_in_file(line1,line_file):
    with open('result.txt', 'a', encoding='utf8') as f:
        f.write(line1 + '\n')
        f.write(str(len(line_file)) + '\n')
        for line in line_file:
            f.write(line + '\n')


with open('1.txt', encoding='utf8') as f:
    for line in f:
        line_file1.append(line.strip())

with open('2.txt', encoding='utf8') as f:
    for line in f:
        line_file2.append(line.strip())

with open('3.txt', encoding='utf8') as f:
    for line in f:
        line_file3.append(line.strip())

print(len(line_file1))
print(len(line_file2))
print(len(line_file3))
if len(line_file1) > len(line_file2) and len(line_file1) > len(line_file3):
    if len(line_file2) > len(line_file3):
        append_line_in_file('1.txt',line_file1)
        append_line_in_file('2.txt', line_file2)
        append_line_in_file('3.txt', line_file3)
    else:
        append_line_in_file('1.txt', line_file1)
        append_line_in_file('3.txt', line_file3)
        append_line_in_file('2.txt', line_file2)
elif len(line_file2) > len(line_file1) and len(line_file2) > len(line_file3):
    if len(line_file1) > len(line_file3):
        append_line_in_file('2.txt', line_file2)
        append_line_in_file('1.txt', line_file1)
        append_line_in_file('3.txt', line_file3)
    else:
        append_line_in_file('2.txt', line_file2)
        append_line_in_file('3.txt', line_file3)
        append_line_in_file('1.txt', line_file1)
elif len(line_file3) > len(line_file1) and len(line_file3) > len(line_file2):
    if len(line_file1) > len(line_file2):
        append_line_in_file('3.txt', line_file3)
        append_line_in_file('1.txt', line_file1)
        append_line_in_file('2.txt', line_file2)
    else:
        append_line_in_file('3.txt', line_file3)
        append_line_in_file('2.txt', line_file2)
        append_line_in_file('1.txt', line_file1)
