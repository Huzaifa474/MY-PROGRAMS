#slicing:extracting one or more values from list
#index    0        1       2       3       4
students=["Ali","Faisal","Saleem","faraz","Hamza"]
#index   -5       -4         -3      -2       -1
#to ascess single value
print(students[0])
print(students[-5])
#list have double index
#listname[start;end+1]
a=students[0:2+1]
print(a)
#passing negative index
b=students[-5:-4+1]
print(a)
#giving no end
c=students[3:]
print(c)
nums=[1,2,3,4,5,6,7,8,9,0,21,12,13,14,15,16,17,18,19,20]
d=nums[0:15+1]
print(d)
e=nums[0:15:2]
print(e)#where '2'is the step
f=nums[0::5]
print(f)
