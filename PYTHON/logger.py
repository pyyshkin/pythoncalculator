from data_create import name_data,surname_data,phone_data,address_data,newname_data,newsurname_data,newphone_data,newaddress_data

def input_data():
    name = name_data()
    surname = surname_data()
    phone = phone_data()
    address = address_data()
    var = int(input(f"В каком формате записать данные \n\n"
    f"1 Вариант: \n"
    f"{name}\n{surname}\n{phone}\n{address}\n\n"
    f"2 Вариант: \n"
    f"{name};{surname};{phone};{address} \n"
    f"Выберите вариант: "))

    while var!= 1 and var!=2:
        print('Неправильный ввод')
        var = int(input("Введите число "))

    if var == 1:
        with open('data_first_variant.csv','a', encoding="utf-8") as f:
            f.write(f"{name}\n{surname}\n{phone}\n{address}\n\n")
    elif var == 2:
        with open('data_second_variant.csv','a', encoding="utf-8") as f:        
            f.write(f"{name};{surname};{phone};{address} \n\n")


def print_data():
    print("Вывожу данные из 1 файла: \n")
    with open('data_first_variant.csv','r', encoding="utf-8") as f:
        data_first = f.readlines()
        data_first_list=[]
        j=0
        for i in range(len(data_first)):
            if data_first[i] == '\n' or i == len(data_first)-1:
                data_first_list.append(''.join(data_first[j:i+1]))
                j=i
        print(''.join(data_first_list))
    
    print("Вывожу данные из 2 файла: \n")
    with open('data_second_variant.csv','r', encoding="utf-8") as f:
        data_second = f.readlines()
        print(*data_second)

def updatedelete():
    var = int(input(f"Выберите функцию: \n\n"
    f"1 Изменение данных: \n"
    f"2 Удаление данных: \n"
    f"Выберите вариант: "))
    
    while var!= 1 and var!=2:
        print('Неправильный ввод')
        var = int(input("Введите число "))

    if var == 1: 
        var = int(input(f"Выберите формат поиска для изменения контакта: \n\n"
        f"1 Поиск по имени: \n"
        f"2 Поиск по фамилии: \n"
        f"3 Поиск по номеру телефона: \n"
        f"4 Поиск по адресу: \n"
        f"Выберите вариант: "))

        while var!= 1 and var!=2 and var!=3 and var!=4:
            print('Неправильный ввод')
            var = int(input("Введите число "))

        if var == 1:
            name = input("Введите имя контакта: ")
            with open('data_first_variant.csv','r', encoding="utf-8") or open('data_second_variant.csv','r', encoding="utf-8") as f:
                for i in f:
                    if name in i:
                        print('Введите новые данные: ')
                        newname=newname_data()
                        newsurname = newsurname_data()
                        newphone = newphone_data()
                        newaddress = newaddress_data()
                        var = int(input(f"В каком формате записать данные \n\n"
                        f"1 Вариант: \n"
                        f"{newname}\n{newsurname}\n{newphone}\n{newaddress}\n\n"
                        f"2 Вариант: \n"
                        f"{newname};{newsurname};{newphone};{newaddress} \n"
                        f"Выберите вариант: "))
                        
                        while var!= 1 and var!=2:
                            print('Неправильный ввод')
                            var = int(input("Введите число "))

                        if var == 1:
                            with open('data_first_variant.csv','a', encoding="utf-8") as f:
                                f.write(f"{newname}\n{newsurname}\n{newphone}\n{newaddress}\n\n")
                        elif var == 2:
                            with open('data_second_variant.csv','a', encoding="utf-8") as f:        
                                f.write(f"{newname};{newsurname};{newphone};{newaddress} \n\n")
                    else: 
                        print("Таких данных не существует!")           

        if var == 2:
            surname = input("Введите фамилию контакта: ")
            with open('data_first_variant.csv','r', encoding="utf-8") or open('data_second_variant.csv','r', encoding="utf-8") as f:
                for i in f:
                    if surname in i:
                        print('Введите новые данные: ')
                        newname=newname_data()
                        newsurname = newsurname_data()
                        newphone = newphone_data()
                        newaddress = newaddress_data()
                        var = int(input(f"В каком формате записать данные \n\n"
                        f"1 Вариант: \n"
                        f"{newname}\n{newsurname}\n{newphone}\n{newaddress}\n\n"
                        f"2 Вариант: \n"
                        f"{newname};{newsurname};{newphone};{newaddress} \n"
                        f"Выберите вариант: "))

                        while var!= 1 and var!=2:
                            print('Неправильный ввод')
                            var = int(input("Введите число "))

                        if var == 1:
                            with open('data_first_variant.csv','a', encoding="utf-8") as f:
                                f.write(f"{newname}\n{newsurname}\n{newphone}\n{newaddress}\n\n")
                        elif var == 2:
                            with open('data_second_variant.csv','a', encoding="utf-8") as f:        
                                f.write(f"{newname};{newsurname};{newphone};{newaddress} \n\n")
                    else: 
                        print("Таких данных не существует!") 

        if var == 3:
            phone = input("Введите номер контакта: ")
            with open('data_first_variant.csv','r', encoding="utf-8") or open('data_second_variant.csv','r', encoding="utf-8") as f:
                for i in f:
                    if phone in i:
                        print('Введите новые данные: ')
                        newname=newname_data()
                        newsurname = newsurname_data()
                        newphone = newphone_data()
                        newaddress = newaddress_data()
                        var = int(input(f"В каком формате записать данные \n\n"
                        f"1 Вариант: \n"
                        f"{newname}\n{newsurname}\n{newphone}\n{newaddress}\n\n"
                        f"2 Вариант: \n"
                        f"{newname};{newsurname};{newphone};{newaddress} \n"
                        f"Выберите вариант: "))

                        while var!= 1 and var!=2:
                            print('Неправильный ввод')
                            var = int(input("Введите число "))

                        if var == 1:
                            with open('data_first_variant.csv','a', encoding="utf-8") as f:
                                f.write(f"{newname}\n{newsurname}\n{newphone}\n{newaddress}\n\n")
                        elif var == 2:
                            with open('data_second_variant.csv','a', encoding="utf-8") as f:        
                                f.write(f"{newname};{newsurname};{newphone};{newaddress} \n\n")
                    else: 
                        print("Таких данных не существует!") 

        if var == 4:
            address = input("Введите адрес контакта: ")
            with open('data_first_variant.csv','r', encoding="utf-8") or open('data_second_variant.csv','r', encoding="utf-8") as f:
                for i in f:
                    if address in i:
                        print('Введите новые данные: ')
                        newname=newname_data()
                        newsurname = newsurname_data()
                        newphone = newphone_data()
                        newaddress = newaddress_data()
                        var = int(input(f"В каком формате записать данные \n\n"
                        f"1 Вариант: \n"
                        f"{newname}\n{newsurname}\n{newphone}\n{newaddress}\n\n"
                        f"2 Вариант: \n"
                        f"{newname};{newsurname};{newphone};{newaddress} \n"
                        f"Выберите вариант: "))

                        while var!= 1 and var!=2:
                            print('Неправильный ввод')
                            var = int(input("Введите число "))

                        if var == 1:
                            with open('data_first_variant.csv','a', encoding="utf-8") as f:
                                f.write(f"{newname}\n{newsurname}\n{newphone}\n{newaddress}\n\n")
                        elif var == 2:
                            with open('data_second_variant.csv','a', encoding="utf-8") as f:        
                                f.write(f"{newname};{newsurname};{newphone};{newaddress} \n\n")
                    else: 
                        print("Таких данных не существует!")
            
    if var == 2: 
        var = int(input(f"Выберите формат поиска для удаления контакта: \n\n"
        f"1 Поиск по имени: \n"
        f"2 Поиск по фамилии: \n"
        f"3 Поиск по номеру телефона: \n"
        f"4 Поиск по адресу: \n"
        f"Выберите вариант: "))

        while var!= 1 and var!=2 and var!=3 and var!=4:
            print('Неправильный ввод')
            var = int(input("Введите число "))

        if var == 1:
            name = input("Введите имя контакта: ")
            with open('data_first_variant.csv','r+', encoding="utf-8") or open('data_second_variant.csv','r+', encoding="utf-8") as f:
                lines = f.readlines()
                f.seek(0)
                for i in lines:
                    if name.lower() not in i.lower():
                        f.write(i)
                        print("Контакт удален.")

        if var == 2:
            surname = input("Введите фамилию контакта: ")
            with open('data_first_variant.csv','r+', encoding="utf-8") or open('data_second_variant.csv','r+', encoding="utf-8") as f:
                lines = f.readlines()
                f.seek(0)
                for i in lines:
                    if surname.lower() not in i.lower():
                        f.write(i)
                        print("Контакт удален.")

        if var == 3:
            phone = input("Введите номер контакта: ")
            with open('data_first_variant.csv','r+', encoding="utf-8") or open('data_second_variant.csv','r+', encoding="utf-8") as f:
                lines = f.readlines()
                f.seek(0)
                for i in lines:
                    if phone.lower() not in i.lower():
                        f.write(i)
                        print("Контакт удален.")

        if var == 3:
            address = input("Введите адрес контакта: ")
            with open('data_first_variant.csv','r+', encoding="utf-8") or open('data_second_variant.csv','r+', encoding="utf-8") as f:
                lines = f.readlines()
                f.seek(0)
                for i in lines:
                    if address.lower() not in i.lower():
                        f.write(i)
                        print("Контакт удален.")

