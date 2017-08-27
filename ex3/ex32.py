try:
    hrs = input("Enter Hours:")
    fhrs = float(hrs)
    rate = input("Enter Rate:")
    frate = float(rate)
    if fhrs >= 40:
        pay = (fhrs - 40)*1.5*frate + 40*frate  
    else:
        pay =  fhrs*frate
    print('Pay: ' ,  pay)
except:
    print("Error, please enter numeric input")

 

    
