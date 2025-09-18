#  Write a Python program
# 1. to read an entire text file.
import re

if __name__ == '__main__':
    file_path = "C:/Intel/tramy.txt"
    f=open(file_path,'r')
    print("Cau 1: ")
    for line in f:
        print( line, end="")
    f.close()
# 2. to read the first n lines of a file.
if __name__ == '__main__':
    file_path = "C:/Intel/tramy.txt"
    n = int(input("\n2) Enter n: "))
    count = 0
    first_lines = []
    f=open(file_path, 'r')
    for line in f:
        first_lines.append(line)
        count +=1
        if count==n:
            break
    print(f" {n} dong dau:")
    for line in first_lines:
        print(line, end=" ")
    f.close()

# 3. to append text to a file and display the text.
if __name__ == '__main__':
    file_path = "C:/Intel/tramy.txt"
    print("/nCau 3:")
    f=open(file_path, "a")
    f.write("\nDong moi duoc them")
    f.close()

    f=open(file_path, "r")
    print("\nSau khi them:",f.read())
    f.close()
# 4. to read a file line by line and store it into a list.
if __name__ == '__main__':
    file_path = "C:/Intel/tramy.txt"
    f=open(file_path, 'r')
    lines_list = f.readlines()
    print("\n4) Danh sach tung dong: ", lines_list)
    f.close()
# 5. to find the longest words in a file.
words =re.findall()
# 6. to count the frequency of words in a file.
# 7. to copy the contents of a file to another file.
# 8. that takes a text file as input and returns the number of words in a given text file
# 9. generate 100 random numbers then write it to a file with name "numbers.txt". Read this file and summarize these numbers.
#