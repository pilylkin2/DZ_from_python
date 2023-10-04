import pyttsx3
import random
import time,os

def func_decoratore(func):
    def wrapper(*args, **kwargs): #Принимаем произвольное число фактических и формальных параметров
        #print("Выыод до  вызова функции")
        st = time.time()
        res = func(*args, **kwargs)
        #print("Вывод после вызова функции")
        en = time.time()
        dt = en - st
        print(f"Затраченное время: {dt}")
        os.system("PAUSE")
        return res

    return wrapper


class question_varible:

    def __init__(self,vopros,answer_1,answer_2,answer_3) -> None:
        '''Конструктор для создания класса "Вопрос с несколькими вариантами ответа"'''
        self.vopros = vopros
        self.answer_1 = answer_1
        self.answer_2 = answer_2
        self.answer_3 = answer_3

    @func_decoratore
    def question(self):
        '''Метод задания вопроса и проверки ответа на него'''
        print(self.vopros)
        print("Выберите ответ")
        print("1 -",self.answer_1)
        print("2 -",self.answer_2)
        print("3 - ",self.answer_3)
        i = input()
        match i:
            case '1':
                return 0
            case '2':
                return 1
            case '3':
                return 0
            case _:
                print("Введен некоректный символ, пока")
                return 0


class question_audio:
    def __init__(self, vopros,answer) -> None:
        '''Конструктор для создания класса "музыкальный вопрос"'''
        self.vopros = vopros
        self.answer = answer
    @func_decoratore
    def question(self):
        '''Метод задания вопроса и проверки ответа на него'''
        e = pyttsx3.init()
        e.say(self.vopros)
        e.runAndWait()
        i = input("Введите ответ на вопрос: ")
        if i!=self.answer:
            return 0
        else:
            return 1
        

# e = input("Вопрос: ")
# e1 = input("Ответ: ")

# q = question_audio(e,e1)
# question_list = []
# question_list.append(q)
# for i in question_list:
#     k = i.question()


class question_comparison:
    
    def __init__(self, list) -> None:
        '''Конструктор для создания класса "Вопрос-сопостовление"'''
        self.list = list
    @func_decoratore
    def question(self):
        '''Метод формированиявопроса и  провери ответа на вопросы'''
        l = len(self.list)
        copy_list = dict.copy(self.list)
        self.list1 = list(dict.keys(self.list))
        self.list2 = list(self.list.values())
        random.shuffle(self.list2)
        print("Сопоставить")
        for i in self.list1:
            print(i,end='   ')
        print('\n')
        for i in self.list2:
            print(i,end='   ')
        print('\n')
        for i in copy_list:
            print("Введите ответ на вопрос: ", i)
            copy_list[i] = input()
        #print(copy_list)
        l = 1/l
        bals = 0
        for i in self.list:
            if self.list[i] == copy_list[i]:
                #print(self.list[i], copy_list[i])
                bals += l
        return bals
    
