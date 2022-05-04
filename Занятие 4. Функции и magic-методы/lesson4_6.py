file = open("demo.txt", "w")

s1 = [1, 2, 3]
s2 = ["vasya", "masha", "peter"]
s3 = ["dfs", "fdsf", "fdsf"]
# file.write("\n".join(s2))
for i in range(len(s1)):
    file.write(str(s1[i]) + " " + s2[i] + " " + s3[i] + "\n")