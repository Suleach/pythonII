logins = ['111', '222', '333']
passwords = ['444', '555', '666']

inp_login = str(input('Login: '))
inp_pass = str(input('Password: '))

for i in range(len(logins)):

    if inp_login == logins[i]:

        if inp_pass == passwords[i]:
            print('Hello', logins[i])
            break

        else: 
            print('Incorrect password')
            break