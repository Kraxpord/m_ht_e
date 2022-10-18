try:
    num1 = int(input("Перше число - "))
    num2 = int(input("Друге число - "))
    for i in range(1,11):
        for g in range(num1,num2+1):
            print(f'{g}*{i}={i*g}',end='\t\t')
        print()
except Exception as ex:
    print(f'Eror information: {ex}')