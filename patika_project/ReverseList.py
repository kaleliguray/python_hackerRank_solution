array=[[1, 2], [3, 4], [5, 6, 7]]
for i in reversed(array):

    for j in reversed(i):
        list = [j]
        print(list,end=" ")

