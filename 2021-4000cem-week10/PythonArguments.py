import sys
n = len(sys.argv)
print("Length of argv: ", n)
for i in range(n):
	if i==0:
		print("File Name: ", sys.argv[i])
	else:
		print("Argument " + str(i), sys.argv[i], type(sys.argv[i]))
