print("\t\t\t\t:::USEFUL FUNCTIONS:::\n\n\n")
print("\t\t\t\t::STRING FUNCTIONS::\n\n")
print("1. join - joins a list of strings with anoher string as a seprator.\n2. replace - replaces one substring in a string with other substring.\n3. startswith and endswith - dtermine if there is a substring at the start and end of string, respectively.\n4. lower and upper - To change the case of a string.\n5. split - split is the opposite of the join.\n")
print("Examples:-\n")
#using join
print("Using join")
print(", ".join(["Car", "Bus", "Train"]))
print("\n\n")
#using replace
print("Using replace")
print("Hello Satyam!".replace("Satyam!", "World"))
print("\n\n")
#using startswith
print("Using startswith")
print("Yo Yo Honey Singh!".startswith("Yo"))
print("\n\n")
#using endswith
print("Using endswith")
print("Yo Yo Honey Singh!".endswith("Singh!"))
print("\n\n")
#using upper
print("Using upper")
print("all in caps sentence.".upper())
print("\n\n")
#using lower
print("Using lower")
print("ALL IN SMALL.".lower())
print("\n\n")
#using split
print("Using split")
print("Car, bike, scooter".split(", "))
print("\n\n\n")

print("\t\t\t\t::NUMERIC FUNCTIONS::\n\n")
print("To find maximum or minimum of some numbers or a list, you can use max or min.\nTp find the distance of a number from zero(its absolute value), use abs.\nTo round a number to a certain number of decimal place use round.\nTo find total of a list, use sum.")
print("Examples:-")

print(min([i*2 for i in range(10)] ))
print(max([i*2 for i in range(10)] ))
print(abs(10000101001010155254254212))
print(abs(-8558))
print(sum([i for i in range(10)]))
print(round(1.5254581))

print("\n\n\n")
a = min([sum([11,22]),max(abs(-30),2)])
print(a)



print("\n\n\n\n\n")
print("\t\t\t\t::LIST FUNCTIONS::\n\n")
print("Often used in conditional statements, all and any take a list as an argument,\nand return true if all or any(respectively) of their arguments evaluate to true and false.\nThe function enumerate can be used used to iterate through the values and indices of a list simlutaneously.\n")
nums = [55,44,33,22,11]

if all([i > 5 for i in nums ]):
    print("All are greater than 5.")


if any([i % 2 == 0 for i in nums]):
    print("At least one is even.")


for v in enumerate(nums):
    print(v)

