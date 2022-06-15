# Create a list of all odd numbers between 1 and a max number. Max number is 
# something you need to take from a user using input() function

print("Write Down Your maximum number of the list")
a=int(input("What Is Your NUmber?"))
gt=[]
for i in range(1,a+1):
    if i%2!=0:
        gt.append(i)


print(gt)
    

