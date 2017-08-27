tot = 0 
cnt = 0
Min = None
Max = None
num = None
while num != "done":
	num = input("Enter a number: ")
	try:
		num = float(num)
		tot = tot + num
		cnt = cnt + 1
		if Min == None or Min > num :
			Min = num
		if Max == None or Max < num :
			Max = num 
	except:
		if num != "done":
			print("Invalid data")
		continue
print(tot, cnt, Min, Max)