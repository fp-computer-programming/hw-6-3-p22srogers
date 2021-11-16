# Author: SMR (AMDG) 11/14/21
list_inp = input("Please type a sequence of numbers: ")
list_inp=list_inp.split()
list_2=list_inp.copy()
list_2.sort()
if(list_2 == list(list_inp)):
    print("The numbers",list_inp, "are sorted.")
else:
    print("The numbers", list_inp, "are not sorted.")