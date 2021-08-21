
l = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]

flatten_list = []

for i in range(1):

    flatten_list.append(l[0][1])
    flatten_list.append(l[0][2][0])
    flatten_list.append(l[0][3])
    flatten_list.append(l[1][0][0][0])
    flatten_list.append(l[1][1])
    flatten_list.append(l[0][2])
    flatten_list.append(l[0][3])

print(flatten_list)


