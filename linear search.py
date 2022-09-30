l=[]
x=int(input('enter the size of array'))
print('enter the elements')
for k in range (x):l.append(int(input()))
key=int(input('enter the element that you want to find'))
for k in l:
    if key==k:
        print('your element found at position',l.index(k))
        break
else:print('the element not  found anywhere!!!')

        