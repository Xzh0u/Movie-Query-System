li = []
for i in range(2, 251):
    li.append("app/data/comments/" + str(i) + ".csv")

for i in range(2, 251):
    f = open(li[i], "w")
    f.write("createdAt,author,content,ip")
    f.close()