flag = 0
runcount = 0


dict = {'CHANDLER': 'ABSENT',
        'BERGHOFF': 'ABSENT',
        'BOWLES': 'ABSENT',
        'COLE': 'ABSENT',
        'JAMBAM': 'ABSENT',
        'DANNER': 'ABSENT',
        'DULL': 'ABSENT',
        'FERGUSON': 'ABSENT',
        'WEILAND': 'ABSENT'}

while flag == 0:
    
    lastname = input("Who's here bro: ")

    for key in dict:
        if lastname == key:
            runcount += 1

    if lastname == 'missing':
        print("\n" + "Absentees:")
        for value in dict:
            if dict[value] == 'ABSENT':
                print(value)
        print("\n")

    for key in dict:
        if lastname == key:
            dict[key] = 'PRESENT'

    if runcount == len(dict):
        flag = 1
        print("ALL ACCOUNTED FOR")
    


    
            
