num1=int(input('Enter the numbers= '))

for i in range(1,num1,1):
    if(i%3==0) and(i%5==0):
        print('fizzbuzz')
        continue
    
    elif(i%3==0):
        print('fizz')
        continue
    elif(i%5==0):
        print('buzz')
        continue
    else:
        print(i)




