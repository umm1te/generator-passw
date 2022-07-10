import random 


chars = 'abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'

nazv = input ('от чего пароль?')
dlina = input("Длину пароля:"+ "\n")

number = input('Сколько надо паролей:'+ "\n")
dlina = int(dlina)
number = int(number)

for n in range(number):
    password = ''
    for i in range(dlina):
        password += random.choice(chars)
    print(password)

    file = open( "password.txt", 'a')
    file.write( "\n" + password + ' пароль от ' + nazv )
    file.close()
