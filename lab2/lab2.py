# Listy skadane

numbers= [1,2,3,4,5,6]
result= [x**2 for x in numbers if x%2 ==0]

result1= list(map(lambda x:x*2, numbers))
print(result1)

result2= list(filter(lambda x:x%2==0, numbers))
print(result2)