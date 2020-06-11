#List

#1.Creating and accessing a list

numbers=[1,2,3,4,5,6,7,8,9,10]

# we can access each element in list
print(numbers[1])

# we can use the list like string for like slicing operation
print(numbers[1:])

# we can print entire list like
print(numbers)

#Basic List Operations

l1=[1,2,3]
l2=[4,5,6]
l3=l1+l2
print(l3)

#length
print(len(l3))

#max
print(max(l3))
#min
print(min(l3))

print('a' in ['a','e'])

print('c' in ['a','e'])

#delete list
del(l1)

#sort list
print(sorted(l2,reverse=True))

#sum list
print(sum(l2))
