# Declare variables
mylist = [10,2,5,20,31,7,8,4,3,12,11,1,2]   # Our inputs to the program
has_duplicates = False # initialize as false (why?)

#  Sort 'mylist' (Why do we sort first?)
mylist.sort()

#  Loop through 'mylist' with a for-Loop
print()
for index in range(len(mylist) - 1):
    print(index)
    print(mylist[index], mylist[index + 1])
    #  Check if adjacent elements of 'mylist' are the same
    if mylist[index] == mylist[index + 1]:
        #  if they are the same, set has_duplicates to True
        has_duplicates = True
        #  Exit out of the for-loop (no need to check rest of list)
        break
print(has_duplicates) # Our outputs of the program
