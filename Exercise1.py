print("Hello World")
age = 20
print(age)
price = 19.95
print(price)
first_name = 'marilyn'
print(first_name)
is_online = False
name = input('What is your Name? ')
print('Hello ' + name)
### sum
first = float(input('First Number: '))
second = float(input('second Number: '))
sum = first + second
print('sum:'+str(sum))




lista = [2, 4, 6, 8]
contiguos = []

#iteramos en el rango del tamaño de la lista -1
for element in range(len(lista)-1):
    #un numero es contiguo con otro si sumado o restado 1 son iguales
    if lista[element] == lista[element+1]-1:
        contiguos.append((lista[element],lista[element+1]))
print(contiguos)




#Generates a new  user password
import random

chars = "abcdefghijklmnopqrstuvwxzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
newPassword = []
for x in range(8):
    newPassword.append(random.choice(chars))
    finalPassword = ''.join(map(str, newPassword))
print("\nThis is your new password: ",finalPassword)
new_password = input("Please enter your New Password: ")

problem = input("\nEnter description of problem: ")

############################
