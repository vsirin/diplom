
f = open("colorings.txt")
lines = f.readlines()

f2 = open("colorings2.txt", "w")

for line_ in lines:

	if not line_:
		continue

	line = line_.split()

	if not line:
		continue

	n = line[0].split(".")[0]
	k = line[1]
	r1 = line[2]
	r2 = line[3]

	
	f2.write(f"{n:3} & {k} & {r1:19} & {r2:19} \\\\ \n")
	print(n, k, r1, r2)	

f2.close()