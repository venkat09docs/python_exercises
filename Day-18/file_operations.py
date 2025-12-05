# File Opertaions

# Open the file and Read the content
    # Read the content Line by Line
# Open the file and Writing the content
    # First Line
    # Appending Content

# File Content Type
    # text based file content UTF-8
    # Binary file content (PDF, Image, Audio, Video) (0 / 1)

# Opening AND READING FILES

f = open('config/configuration.txt')
content = f.read()
# print(content)

print(f.closed)
f.close()
print(f.closed)

print('#' * 50)

# ABSOLUTE AND RELATIVE PATHS -

# Absolute Path - E:\projects\Day-18

f = open('E:/projects/Day-18/config/configuration.txt')
content = f.read()
# print(content)
f.close()

print('#' * 50)

# . - Current Directory
# .. - Parent Directory

f = open('./config/configuration.txt')
content = f.read()
# print(content)
f.close()


f = open('./config/configuration.txt')
content = f.read(8)
print(content)

content = f.read(4)
print(content)

content = f.read(4)
print(content)

print(f.tell())
f.seek(2)
content = f.read(2)
print(content)

f.seek(0)
content = f.read(8)
print(content)

f.close()

with open('./config/configuration.txt') as f:
    content = f.read()
    print(content)

print(f.closed)
# f.read()

print('#' * 100)

# READING FILES INTO A LIST

with open('./config/configuration.txt') as f:
    content = f.read().splitlines()
    print(content)
    print(type(content))

    # for line in content:
    #     print(line)

print('#' * 100)

with open('./config/configuration.txt') as f:
    content = f.readlines()
    print(content)

print('#' * 100)

with open('./config/configuration.txt', 'rt') as f:
    content = f.readline()
    content1 = f.readline()
    print(content,end='')
    print(content1,end='')

# WRITING TO TEXT FILES

with open('myfile.txt', 'w') as f:
    f.write('Just a 1st line.\n')
    f.write('Just a 2nd line.\n')
    f.write('Just a 3rd line.\n')

with open('myfile.txt', 'a') as f:
    f.write('Just a 4th line.\n')
    f.write('Just a 5th line.\n')

# --------------------------------------------------------
