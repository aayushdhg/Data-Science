n=int(input("How many elements would you like on the list? "))
meow=[]
for i in range (n):
    a = input (f"Enter element {i+1}: ")
    meow.append(a)

checked=set()
new_list=[]
for element in meow: #operators for iterables
    if element not in checked:
        new_list.append(element)
        checked.add(element)

print (new_list)

print(set(meow))