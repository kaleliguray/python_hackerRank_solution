def split_and_join(line):
    # write your code here
    tempString = line.split(" ")
    print("Split version : ",tempString)
    tempString = "-".join(tempString)
    print("Join version : ",tempString)
    return tempString

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)