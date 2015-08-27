size = input("Enter the number of params of function: ")
f1 = []
f2 = []
print("Enter the first function: ")
for i in range(size):
	value = raw_input()
	f1.append(value)
print("Enter the second function: ")
for i in range(size):
	value = raw_input()
	f2.append(value)

print("1st function: " + str(f1))
print("2nd function: " + str(f2))

flag = 0

for j in range(size):
	if(f1[j].isdigit() and f2[j].isdigit()):
		if(f1[j] == f2[j]):
			print("Digits are same")
		else:
			print("Digits are not same so cannot be accepted")
			flag = 1
			break
	elif(f1[j].isalpha() and f2[j].isalpha()):
		if(f1[j] == f2[j]):
			print("Both characters are same")
		else:
			print("Replace " + f1[j] + " with " + f2[j] + " for " + str(j + 1) + " param")
	elif((f1[j].isalpha() and f2[j].isdigit())):
		print("Replace " + f1[j] + " with " + f2[j] + " for " + str(j + 1) + " param")
	elif((f1[j].isdigit() and f2[j].isalpha())):
		print("Replace " + f2[j] + " with " + f1[j] + " for " + str(j + 1) + " param")
			

if(flag == 1):
	print("Functions cannot be unified")
else:
	print("Unification possible using the above repalcements")

''' OUTPUT

student@CC:~/Downloads$ python Uni.py 
Enter the number of params of function: 2
Enter the first function: 
x
2
Enter the second function: 
y
z
1st function: ['x', '2']
2nd function: ['y', 'z']
Replace x with y for 1 param
Replace z with 2 for 2 param
Unification possible using the above repalcements
student@CC:~/Downloads$ python Uni.py 
Enter the number of params of function: 2
Enter the first function: 
x
1
Enter the second function: 
y
2
1st function: ['x', '1']
2nd function: ['y', '2']
Replace x with y for 1 param
Digits are not same so cannot be accepted
Functions cannot be unified
student@CC:~/Downloads$ 

'''	

	
