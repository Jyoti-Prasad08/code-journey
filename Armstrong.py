number = int(input("Enter a number: "))
power = len(str(number))

sum_of_number_after_power = 0

for num in str(number):
    sum_of_number_after_power+= int(num)**int(power)
    
if sum_of_number_after_power ==number:
    print(f"{number} is a Armstrong Number!")
else:
    print(f"{number} is not an Armstrong Number!")