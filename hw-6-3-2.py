# Author: SMR (AMDG) 11/14/21
list_inp = input("Please type a sequence of numbers: ")
list_sort = list(list_inp)
list_sort.sort()
if(list_sort == list(list_inp)):
    print("The numbers",list_inp, "are sorted.")
else:
    print("The numbers", list_inp, "are not sorted.")