def apply () :
    age = input('Enter your age: ')
    age = int(age)
    if age < 18 :
        print('you are too young')
    elif age <= 22 :
        print('welcome to Egypt scolarship program')
    else:
        print('you are too old')
count = 0
while count < 1000:
    apply()
    count +=1
