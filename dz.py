import os,sys
import random
import time
#import pyttsx3
from question_types.module_dz import *



class interviewee:
    def __init__(self, name, statistic) -> None:
        '''Конструктор для создания класса "Опрашиваемый"'''
        self.name = name
        self.statistic = statistic


class question:

    def __init__(self, vopros , answer) -> None:
        '''Конструктор для создания класса "Вопрос с коротким ответтом"'''
        self.vopros = vopros
        self.answer = answer

    @func_decoratore
    def question(self):
        '''Метод задания вопроса и проверки ответа на него'''
        print(self.vopros)
        print("Введите ответ")
        i = input()
        if i == self.answer:
            return 1
        else:
            return 0

q = question("2+2=", '4')


class opros:
    
    def menu():
        question_list = []
        question_list.append(q) # создания списка вопросов
        question_comparison_list = dict() # создание словаря для вормирования вопроса типа 'вопрос сопоставление'
        st = 0
        n = 0
        coll = 0
        name = input("Введите имя опрашиваемого: ")
        interviewee_1 = interviewee(name,0)
        interviewee_sl = {name:interviewee_1} # создание словаря опрашиваемых
        inw = interviewee_1
        os.system('cls')
        while(True):
            print("Имя потзователя: ",inw.name,' Статистика: ',inw.statistic)
            print("Выберите действие")
            print("1 - Пройти опрос ")
            print("2 - Добавить вопрос")
            print("3 - Добавить опрашиваемого")
            print("4 - Выбор опрашиваемого")
            print("Любой символ - Выход")
            i = input()
            match i:
                case '1':
                    os.system('cls')
                    print('Опрос')
                    random.shuffle(question_list)
                    for i in question_list:
                        k = i.question()
                        os.system('cls')
                        if k != 0:
                            st+=k
                        else:
                            st+=0
                        #print(st)
                        coll+=1
                    #os.system('PAUSE')
                    os.system('cls')
                    st_l = lambda st,coll : st/coll *100
                    inw.statistic = st_l(st,coll)
                    st = coll = 0
                case '2':
                    os.system('cls')
                    print("Какой тип вопроса вы хотите создать?")
                    print("1 - Открытый вопрос с коротким ответом")
                    print("2 - Вопрос с выбором правильного ответа из списка")
                    print("3 - Музыкальный вопрос")
                    print("4 - Вопрос-сопостовление")
                    print("Все что угодно - выход")
                    j = input()
                    match j:
                        case '1':
                            vopros = input('Введите вопрос ')
                            answer = input("Введите ответ : ")
                            b = question(vopros,answer)                    
                            question_list.append(b)
                            os.system('cls')
                        case '2':
                            vopros = input('Введите вопрос ')
                            answer_1 = input("Введите ответ : ")
                            answer_2 = input("Введите правильный ответ : ")
                            answer_3 = input("Введите ответ : ")
                            b = question_varible(vopros,answer_1,answer_2,answer_3)                    
                            question_list.append(b)
                            os.system('cls')
                        case '3':
                            vopros = input('Введите вопрос ')
                            answer = input("Введите ответ : ")
                            b = question_audio(vopros,answer)                    
                            question_list.append(b)
                            os.system('cls')
                        case '4':
                            while(n!="Нет"):
                                vopros = input("Ведите вопрос: ")
                                question_comparison_list[vopros] = input("Введите ответ: ")
                                n = input("Добавить еще вопросы?: ")
                            question_list.append(question_comparison(question_comparison_list))
                            os.system('cls')
                        case _:
                            break
                case '3':
                        os.system('cls')
                        print("Добавление пользователей")
                        name = input('Введите имя: ')
                        interviewee_2 = interviewee(name,0)
                        interviewee_sl[name] = interviewee_2
                        os.system('cls')
                case '4': 
                        os.system('cls')
                        print("Выбор опрашиваемого")
                        b = input("Введите имя опрашиваемого: ")
                        inw = interviewee_sl[b]           
                        os.system('cls')          
                case _:
                    print("пока")
                    return False
        
c = opros
c = c.menu()

