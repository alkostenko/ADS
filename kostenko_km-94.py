import random

def counting_sort(l, max):
    m = max + 1
    count = [0] * m                
    
    for a in l:
        count[a] += 1             
    i = 0
    for a in range(m):            
        for c in range(count[a]):  
            l[i] = a
            i += 1
    return l

print("Костенко КМ-94")
print("'Сортування підрахунком'")
restart="так"

while restart=="так":
    n=int(input("Введіть кількість елементів списку: "))
    l=[]
    i=0
    vidp=input("Використати масив з випадкових чисел? (Відповіть має бути 'так' або 'ні'): ")
    if vidp=="так":
        for i in range(n):
            l.append(random.randint(0,50))
    else:
        for i in range(n):
            x=int(input("Введіть "+str(i+1)+ "-ий елемент масиву: "))
            l.append(x)
            
    print("Початковий список:")
    print(l)
    i=0
    max=-1
    for i in range(n):
        if l[i]>max:
            max=l[i]

    print("Відстортований список:")
    print(counting_sort( l, max ))
    restart=input("Перезапустити програму? (Відповіть має бути 'так' або 'ні'): ")