hours = input("Enter Hours:")
rate = input("Enter Rate:")
try:
    fhours= float(hours)
    frate= float(rate)
except:
    print("Enter a Valid Number")
    quit()
print(fhours,frate)
if fhours>40:
    eHours= fhours-40
    epay= eHours*(frate*1.5)
    pay = epay+ float(40*frate)
else:
    pay = fhours*frate
print(hours, rate, pay)
