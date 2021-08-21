if __name__ == '__main__':
    N = int(input())
    ourList = []

    for i in range(N):
        N = input().split()
        process = N[0]
        if process == "append":
            ourList.append(int(N[1]))
        elif process == "insert":
            ourList.insert(int(N[1]),int(N[2]))
        elif process == "remove":
            ourList.remove(int(N[1]))
        elif process == "print":
            print(ourList)
        elif process == "sort":
            ourList.sort()
        elif process == "pop":
            ourList.pop()
        elif process == "reverse":
            ourList.reverse()
        elif process == "count":
            ourList.count(int(N[1]))


