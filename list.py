#list
alist=["HUZAIFA" , "SAIM" , "PAKISTAN"]#initializing list
#index  0            1         2 
print("Element of list are",alist)#accessing element of list
print(alist)#another way of ascessingelement of list
#floating points list
Floatlist=[1.2,3.5,6.6]
print(Floatlist)
print("index 1 value:",alist[1])#Acesing list members through index no
print("list 2 index 2:",Floatlist[2])
fruits=["Apple","mango","banana"]
len(fruits)
print("before Appending",fruits)#using 'Append' function to add membersto list
fruits.append("orange")
print("After appending",fruits)
fruits.insert(0,"melon")#insert function 
print(fruits)
#extend function to add more than one value in the list
fruits.extend(["Watermelon","blueberry","chery","orange"])
print(fruits)
#count function that how many times valueis present in the list
print(fruits.count("orange"))
#index function :tells the index no of entered value
print(fruits.index("mango"))
#copy function
fruits2=fruits.copy()#by value
print(fruits2)
print(fruits)
fruit3=fruits#copy by reference
fruits.append("newfruit")
print(fruit3)
#remove function
del fruits[3]
print(fruits)
fruits.remove("mango")
print(fruits)
#pop function
deleted=fruits.pop()
print(fruits)
print(deleted)
deleted=fruits.pop(3)
print(deleted)
#sort function
fruits.sort()#ascending order sorting
print(fruits)
fruits.sort(reverse=True)#descending order sorting
print(fruits)
#reverse function
fruits.reverse()
print(fruits)
c=len(fruits)
print("Length of listis:",c)
#clear function:remove all items from list
print(fruits.clear())




