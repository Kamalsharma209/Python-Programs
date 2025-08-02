
list1 = [9,0,6]
list2 = [6,0,9]

copy_list1 = list1.copy()
copy_list1.reverse()
if(copy_list1 == list1):
    print("It is palindrome")
else:
    print("It is not an palindrome")