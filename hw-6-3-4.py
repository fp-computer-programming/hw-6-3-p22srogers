# Author: SMR (AMDG) 11/14/21
list_1 = input("Please enter a list of numbers or letters: ")
list_1.split()
question = input("Would you like the middle or ends of this list? ")
if(question == "ends"):
    ends = str(list_1[0:1]) + str(list_1[-1])
    print("The end is: " + ends)
elif(question == "middle"):
    middle = str(list_1[1:-1])
    print("The middle is: " + middle)


