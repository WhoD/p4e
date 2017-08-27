def computepay(hours, rate):
	if hours > 40:
		pay = (hours - 40) * 1.5 * rate + 40 * rate
	else:
		pay = hours*rate
	return(pay)

try:
	hours = input("Enter Hours: ")
	hours = float(hours)
	rate = input("Enter Rate:")
	rate = float(rate)
	pay = computepay(hours, rate)
	print("Pay: ", pay)
except: 
	print("Error; Enter valid numbers")

