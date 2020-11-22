li = []
for i in range(17, 35):
    li.append("app/data/comments/" + str(i) + ".csv")

for i in range(17, 34):
    f = open(li[i], "w+")
    f.write(", time, username, content")
    f.close()