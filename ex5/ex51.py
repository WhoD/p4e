tot = 0
cnt = 0
avg = None
num = None
while num != "done":
	num = input("Enter a number: ")
	try:
		num = float(num)
		tot = tot + num
		cnt = cnt + 1
		avg = tot/cnt
	except:
		if num != "done":
			print("Invalid input")
		continue
print(tot, cnt, avg)