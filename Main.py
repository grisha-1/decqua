import tkinter as tk


class NotStr(Exception):
    def __init__(self, message="It's not str"):
        self.message = message
        # переопределяется конструктор встроенного класса `Exception()`
        super().__init__(self.message)


class SignFirstPlace(Exception):
    def __init__(self, message="The sign cannot be placed in the first place"):
        self.message = message
        # переопределяется конструктор встроенного класса `Exception()`
        super().__init__(self.message)


class EquallyEndPlace(Exception):
    def __init__(self, message="The equally cannot be placed in the end"):
        self.message = message
        # переопределяется конструктор встроенного класса `Exception()`
        super().__init__(self.message)


class UnknownChar(Exception):
    def __init__(self, message="What is this?"):
        self.message = message
        # переопределяется конструктор встроенного класса `Exception()`
        super().__init__(self.message)


class ManySteps(Exception):
    def __init__(self, message="Please, use only 1 or 2 steps!"):
        self.message = message
        # переопределяется конструктор встроенного класса `Exception()`
        super().__init__(self.message)


class ZeroStep(Exception):
    def __init__(self, message="Please, use only 1 or 2 steps!"):
        self.message = message
        # переопределяется конструктор встроенного класса `Exception()`
        super().__init__(self.message)


class InvalidStep(Exception):
    def __init__(self, message="Sorry, 2 step is only '+'"):
        self.message = message
        # переопределяется конструктор встроенного класса `Exception()`
        super().__init__(self.message)


def equation(value):
    steps = 0
    UnknownNumber = None
    equally_ = None
    sign = []

    situation = None
    CharNumber = 0
    if not isinstance(value, str):
        raise NotStr()
    # All chars
    for char in value:
        if char == '+':
            if CharNumber == 0:
                raise SignFirstPlace()
            sign.append(['+', CharNumber])
            steps += 1
        elif char == '.':
            pass
        elif char == '-':
            if CharNumber == 0:
                raise SignFirstPlace()
            sign.append(['-', CharNumber])
            steps += 1
        elif char == '*':
            if CharNumber == 0:
                raise SignFirstPlace()
            sign.append(['*', CharNumber])
            steps += 1
        elif char == '/':
            if CharNumber == 0:
                raise SignFirstPlace()
            sign.append(['/', CharNumber])
            steps += 1
        elif char == '0' or char == '1' or char == '2' or char == '3' or char == '4' or char == '5' or char == '6' or \
                char == '7' or char == '8' or char == '9':
            pass
        elif char == '=':
            equally_ = CharNumber
        elif char == 'x':
            UnknownNumber = CharNumber
        else:
            raise UnknownChar

        CharNumber += 1
    if CharNumber == equally_ + 1:
        raise EquallyEndPlace()
    if steps == 0:
        raise ZeroStep()
    if steps != 1 and steps != 2:
        raise ManySteps()

    # Situations
    if UnknownNumber == 0:
        if sign[0][0] == '+':
            situation = 0
        elif sign[0][0] == '-':
            situation = 1
        elif sign[0][0] == '*':
            situation = 2
        elif sign[0][0] == '/':
            situation = 3
    elif UnknownNumber + 1 == CharNumber:
        if sign[0][0] == '+':
            situation = 4
        elif sign[0][0] == '-':
            situation = 5
        elif sign[0][0] == '*':
            situation = 6
        elif sign[0][0] == '/':
            situation = 7
    elif steps == 1 or steps == 2 and UnknownNumber == sign[0][1] + 1:
        if sign[0][0] == '+':
            situation = 8
        elif sign[0][0] == '-':
            situation = 9
        elif sign[0][0] == '*':
            situation = 10
        elif sign[0][0] == '/':
            situation = 11
    elif steps == 2:
        if UnknownNumber == sign[1][1] + 1:
            if sign[0][0] == '+':
                situation = 12
            elif sign[0][0] == '-':
                situation = 13
            elif sign[0][0] == '*':
                situation = 14
            elif sign[0][0] == '/':
                situation = 15

    # counting
    if steps == 1:
        if situation == 0:
            FirstNumber = value[2: equally_]
            SecondNumber = value[equally_ + 1: len(value)]
            return f'x = {float(SecondNumber) - float(FirstNumber)}'
        elif situation == 1:
            FirstNumber = value[2: equally_]
            SecondNumber = value[equally_ + 1: len(value)]
            return f'x = {float(SecondNumber) + float(FirstNumber)}'
        elif situation == 2:
            FirstNumber = value[2: equally_]
            SecondNumber = value[equally_ + 1: len(value)]
            return f'x = {float(SecondNumber) / float(FirstNumber)}'
        elif situation == 3:
            FirstNumber = value[2: equally_]
            SecondNumber = value[equally_ + 1: len(value)]
            return f'x = {float(SecondNumber) * float(FirstNumber)}'

        elif situation == 4:
            FirstNumber = value[0: sign[0][1]]
            SecondNumber = value[sign[0][1] + 1: equally_]
            return f'x = {float(SecondNumber) + float(FirstNumber)}'
        elif situation == 5:
            FirstNumber = value[0: sign[0][1]]
            SecondNumber = value[sign[0][1] + 1: equally_]
            return f'x = {float(FirstNumber) - float(SecondNumber)}'
        elif situation == 6:
            FirstNumber = value[0: sign[0][1]]
            SecondNumber = value[sign[0][1] + 1: equally_]
            return f'x = {float(SecondNumber) * float(FirstNumber)}'
        elif situation == 7:
            FirstNumber = value[0: sign[0][1]]
            SecondNumber = value[sign[0][1] + 1: equally_]
            return f'x = {float(FirstNumber) / float(SecondNumber)}'

        elif situation == 8:
            FirstNumber = value[0: sign[0][1]]
            SecondNumber = value[equally_ + 1: len(value)]
            return f'x = {float(SecondNumber) - float(FirstNumber)}'
        elif situation == 9:
            FirstNumber = value[0: sign[0][1]]
            SecondNumber = value[equally_ + 1: len(value)]
            return f'x = {float(FirstNumber) - float(SecondNumber)}'
        elif situation == 10:
            FirstNumber = value[0: sign[0][1]]
            SecondNumber = value[equally_ + 1: len(value)]
            return f'x = {float(SecondNumber) / float(FirstNumber)}'
        elif situation == 11:
            FirstNumber = value[0: sign[0][1]]
            SecondNumber = value[equally_ + 1: len(value)]
            return f'x = {float(FirstNumber) / float(SecondNumber)}'
    elif steps == 2:
        if sign[1][0] == '+':
            if situation == 0:
                FirstNumber = value[2: sign[1][1]]
                SecondNumber = value[sign[1][1] + 1: equally_]
                ThirdNumber = value[equally_ + 1: len(value)]
                return f'x = {float(ThirdNumber) - float(SecondNumber) - float(FirstNumber)}'
            elif situation == 1:
                FirstNumber = value[2: sign[1][1]]
                SecondNumber = value[sign[1][1] + 1: equally_]
                ThirdNumber = value[equally_ + 1: len(value)]
                return f'x = {float(ThirdNumber) - float(SecondNumber) + float(FirstNumber)}'
            elif situation == 2:
                FirstNumber = value[2: sign[1][1]]
                SecondNumber = value[sign[1][1] + 1: equally_]
                ThirdNumber = value[equally_ + 1: len(value)]
                return f'x = {(float(ThirdNumber) - float(SecondNumber)) / float(FirstNumber)}'
            elif situation == 3:
                FirstNumber = value[2: sign[1][1]]
                SecondNumber = value[sign[1][1] + 1: equally_]
                ThirdNumber = value[equally_ + 1: len(value)]
                return f'x = {(float(ThirdNumber) - float(SecondNumber)) * float(FirstNumber)}'

            elif situation == 4:
                FirstNumber = value[0: sign[0][1]]
                SecondNumber = value[sign[0][1] + 1: sign[1][1]]
                ThirdNumber = value[sign[1][1] + 1: equally_]
                return f'x = {float(SecondNumber) + float(FirstNumber) + float(ThirdNumber)}'
            elif situation == 5:
                FirstNumber = value[0: sign[0][1]]
                SecondNumber = value[sign[0][1] + 1: sign[1][1]]
                ThirdNumber = value[sign[1][1] + 1: equally_]
                return f'x = {float(FirstNumber) - float(SecondNumber) + float(ThirdNumber)}'
            elif situation == 6:
                FirstNumber = value[0: sign[0][1]]
                SecondNumber = value[sign[0][1] + 1: sign[1][1]]
                ThirdNumber = value[sign[1][1] + 1: equally_]
                return f'x = {float(FirstNumber) * float(SecondNumber) + float(ThirdNumber)}'
            elif situation == 7:
                FirstNumber = value[0: sign[0][1]]
                SecondNumber = value[sign[0][1] + 1: sign[1][1]]
                ThirdNumber = value[sign[1][1] + 1: equally_]
                return f'x = {float(FirstNumber) / float(SecondNumber) + float(ThirdNumber)}'

            elif situation == 8:
                FirstNumber = value[0: sign[0][1]]
                SecondNumber = value[sign[1][1] + 1: equally_]
                ThirdNumber = value[equally_ + 1: len(value)]
                return f'x = {float(ThirdNumber) - float(SecondNumber) - float(FirstNumber)}'
            elif situation == 9:
                FirstNumber = value[0: sign[0][1]]
                SecondNumber = value[sign[1][1] + 1: equally_]
                ThirdNumber = value[equally_ + 1: len(value)]
                return f'x = {float(FirstNumber) - (float(ThirdNumber) - float(SecondNumber))}'
            elif situation == 10:
                FirstNumber = value[0: sign[0][1]]
                SecondNumber = value[sign[1][1] + 1: equally_]
                ThirdNumber = value[equally_ + 1: len(value)]
                return f'x = {(float(ThirdNumber) - float(SecondNumber)) / float(FirstNumber)}'
            elif situation == 11:
                FirstNumber = value[0: sign[0][1]]
                SecondNumber = value[sign[1][1] + 1: equally_]
                ThirdNumber = value[equally_ + 1: len(value)]
                return f'x = {float(FirstNumber) / (float(ThirdNumber) - float(SecondNumber))}'

            elif situation == 12:
                FirstNumber = value[0: sign[0][1]]
                SecondNumber = value[sign[0][1] + 1: sign[1][1]]
                ThirdNumber = value[equally_ + 1: len(value)]
                return f'x = {float(ThirdNumber) - (float(FirstNumber) + float(SecondNumber))}'
            elif situation == 13:
                FirstNumber = value[0: sign[0][1]]
                SecondNumber = value[sign[0][1] + 1: sign[1][1]]
                ThirdNumber = value[equally_ + 1: len(value)]
                return f'x = {float(ThirdNumber) - (float(FirstNumber) - float(SecondNumber))}'
            elif situation == 14:
                FirstNumber = value[0: sign[0][1]]
                SecondNumber = value[sign[0][1] + 1: sign[1][1]]
                ThirdNumber = value[equally_ + 1: len(value)]
                return f'x = {float(ThirdNumber) - (float(FirstNumber) * float(SecondNumber))}'
            elif situation == 15:
                FirstNumber = value[0: sign[0][1]]
                SecondNumber = value[sign[0][1] + 1: sign[1][1]]
                ThirdNumber = value[equally_ + 1: len(value)]
                return f'x = {float(ThirdNumber) - (float(FirstNumber) / float(SecondNumber))}'

        elif sign[1][0] == '-':
            if situation == 0:
                FirstNumber = value[2: sign[1][1]]
                SecondNumber = value[sign[1][1] + 1: equally_]
                ThirdNumber = value[equally_ + 1: len(value)]
                return f'x = {float(ThirdNumber) + float(SecondNumber) - float(FirstNumber)}'
            elif situation == 1:
                FirstNumber = value[2: sign[1][1]]
                SecondNumber = value[sign[1][1] + 1: equally_]
                ThirdNumber = value[equally_ + 1: len(value)]
                return f'x = {float(ThirdNumber) + float(SecondNumber) + float(FirstNumber)}'
            elif situation == 2:
                FirstNumber = value[2: sign[1][1]]
                SecondNumber = value[sign[1][1] + 1: equally_]
                ThirdNumber = value[equally_ + 1: len(value)]
                return f'x = {(float(ThirdNumber) + float(SecondNumber)) / float(FirstNumber)}'
            elif situation == 3:
                FirstNumber = value[2: sign[1][1]]
                SecondNumber = value[sign[1][1] + 1: equally_]
                ThirdNumber = value[equally_ + 1: len(value)]
                return f'x = {(float(ThirdNumber) + float(SecondNumber)) * float(FirstNumber)}'

            elif situation == 4:
                FirstNumber = value[0: sign[0][1]]
                SecondNumber = value[sign[0][1] + 1: sign[1][1]]
                ThirdNumber = value[sign[1][1] + 1: equally_]
                return f'x = {float(SecondNumber) + float(FirstNumber) - float(ThirdNumber)}'
            elif situation == 5:
                FirstNumber = value[0: sign[0][1]]
                SecondNumber = value[sign[0][1] + 1: sign[1][1]]
                ThirdNumber = value[sign[1][1] + 1: equally_]
                return f'x = {float(FirstNumber) - float(SecondNumber) - float(ThirdNumber)}'
            elif situation == 6:
                FirstNumber = value[0: sign[0][1]]
                SecondNumber = value[sign[0][1] + 1: sign[1][1]]
                ThirdNumber = value[sign[1][1] + 1: equally_]
                return f'x = {float(FirstNumber) * float(SecondNumber) - float(ThirdNumber)}'
            elif situation == 7:
                FirstNumber = value[0: sign[0][1]]
                SecondNumber = value[sign[0][1] + 1: sign[1][1]]
                ThirdNumber = value[sign[1][1] + 1: equally_]
                return f'x = {float(FirstNumber) / float(SecondNumber) - float(ThirdNumber)}'

            elif situation == 8:
                FirstNumber = value[0: sign[0][1]]
                SecondNumber = value[sign[1][1] + 1: equally_]
                ThirdNumber = value[equally_ + 1: len(value)]
                return f'x = {float(ThirdNumber) + float(SecondNumber) - float(FirstNumber)}'
            elif situation == 9:
                FirstNumber = value[0: sign[0][1]]
                SecondNumber = value[sign[1][1] + 1: equally_]
                ThirdNumber = value[equally_ + 1: len(value)]
                return f'x = {float(FirstNumber) - float(SecondNumber) - float(ThirdNumber)}'
            elif situation == 10:
                FirstNumber = value[0: sign[0][1]]
                SecondNumber = value[sign[1][1] + 1: equally_]
                ThirdNumber = value[equally_ + 1: len(value)]
                return f'x = {(float(ThirdNumber) + float(SecondNumber)) / float(FirstNumber)}'
            elif situation == 11:
                FirstNumber = value[0: sign[0][1]]
                SecondNumber = value[sign[1][1] + 1: equally_]
                ThirdNumber = value[equally_ + 1: len(value)]
                return f'x = {float(FirstNumber) / (float(ThirdNumber) + float(SecondNumber))}'

            elif situation == 12:
                FirstNumber = value[0: sign[0][1]]
                SecondNumber = value[sign[0][1] + 1: sign[1][1]]
                ThirdNumber = value[equally_ + 1: len(value)]
                return f'x = {float(SecondNumber) + (float(FirstNumber) - float(ThirdNumber))}'
            elif situation == 13:
                FirstNumber = value[0: sign[0][1]]
                SecondNumber = value[sign[0][1] + 1: sign[1][1]]
                ThirdNumber = value[equally_ + 1: len(value)]
                return f'x = {float(FirstNumber) - float(SecondNumber) - float(ThirdNumber)}'
            elif situation == 14:
                FirstNumber = value[0: sign[0][1]]
                SecondNumber = value[sign[0][1] + 1: sign[1][1]]
                ThirdNumber = value[equally_ + 1: len(value)]
                return f'x = {float(FirstNumber) * float(SecondNumber) - float(ThirdNumber)}'
            elif situation == 15:
                FirstNumber = value[0: sign[0][1]]
                SecondNumber = value[sign[0][1] + 1: sign[1][1]]
                ThirdNumber = value[equally_ + 1: len(value)]
                return f'x = {float(FirstNumber) / float(SecondNumber) - float(ThirdNumber)}'
        elif sign[1][0] == '*':
            if situation == 0:
                FirstNumber = value[2: sign[1][1]]
                SecondNumber = value[sign[1][1] + 1: equally_]
                ThirdNumber = value[equally_ + 1: len(value)]
                return f'x = {float(ThirdNumber) - float(FirstNumber) * float(SecondNumber)}'
            elif situation == 1:
                FirstNumber = value[2: sign[1][1]]
                SecondNumber = value[sign[1][1] + 1: equally_]
                ThirdNumber = value[equally_ + 1: len(value)]
                return f'x = {float(ThirdNumber) + float(FirstNumber) * float(SecondNumber)}'
            elif situation == 2:
                FirstNumber = value[2: sign[1][1]]
                SecondNumber = value[sign[1][1] + 1: equally_]
                ThirdNumber = value[equally_ + 1: len(value)]
                return f'x = {float(ThirdNumber) / (float(SecondNumber) * float(FirstNumber))}'
            elif situation == 3:
                FirstNumber = value[2: sign[1][1]]
                SecondNumber = value[sign[1][1] + 1: equally_]
                ThirdNumber = value[equally_ + 1: len(value)]
                return f'x = {float(FirstNumber) * (float(ThirdNumber) / float(SecondNumber))}'

            elif situation == 4:
                FirstNumber = value[0: sign[0][1]]
                SecondNumber = value[sign[0][1] + 1: sign[1][1]]
                ThirdNumber = value[sign[1][1] + 1: equally_]
                return f'x = {float(FirstNumber) + float(SecondNumber) * float(ThirdNumber)}'
            elif situation == 5:
                FirstNumber = value[0: sign[0][1]]
                SecondNumber = value[sign[0][1] + 1: sign[1][1]]
                ThirdNumber = value[sign[1][1] + 1: equally_]
                return f'x = {float(FirstNumber) - float(SecondNumber) * float(ThirdNumber)}'
            elif situation == 6:
                FirstNumber = value[0: sign[0][1]]
                SecondNumber = value[sign[0][1] + 1: sign[1][1]]
                ThirdNumber = value[sign[1][1] + 1: equally_]
                return f'x = {float(FirstNumber) * float(SecondNumber) * float(ThirdNumber)}'
            elif situation == 7:
                FirstNumber = value[0: sign[0][1]]
                SecondNumber = value[sign[0][1] + 1: sign[1][1]]
                ThirdNumber = value[sign[1][1] + 1: equally_]
                return f'x = {float(FirstNumber) / float(SecondNumber) * float(ThirdNumber)}'

            elif situation == 8:
                FirstNumber = value[0: sign[0][1]]
                SecondNumber = value[sign[1][1] + 1: equally_]
                ThirdNumber = value[equally_ + 1: len(value)]
                return f'x = {(float(ThirdNumber) - float(FirstNumber)) / float(SecondNumber)}'
            elif situation == 9:
                FirstNumber = value[0: sign[0][1]]
                SecondNumber = value[sign[1][1] + 1: equally_]
                ThirdNumber = value[equally_ + 1: len(value)]
                return f'x = {(float(FirstNumber) - float(ThirdNumber)) / float(SecondNumber)}'
            elif situation == 10:
                FirstNumber = value[0: sign[0][1]]
                SecondNumber = value[sign[1][1] + 1: equally_]
                ThirdNumber = value[equally_ + 1: len(value)]
                return f'x = {float(ThirdNumber) / float(SecondNumber) / float(FirstNumber)}'
            elif situation == 11:
                FirstNumber = value[0: sign[0][1]]
                SecondNumber = value[sign[1][1] + 1: equally_]
                ThirdNumber = value[equally_ + 1: len(value)]
                return f'x = {float(FirstNumber) / (float(ThirdNumber) / float(SecondNumber))}'

            elif situation == 12:
                FirstNumber = value[0: sign[0][1]]
                SecondNumber = value[sign[0][1] + 1: sign[1][1]]
                ThirdNumber = value[equally_ + 1: len(value)]
                return f'x = {(float(ThirdNumber) - float(FirstNumber)) / float(SecondNumber)}'
            elif situation == 13:
                FirstNumber = value[0: sign[0][1]]
                SecondNumber = value[sign[0][1] + 1: sign[1][1]]
                ThirdNumber = value[equally_ + 1: len(value)]
                return f'x = {((float(FirstNumber) - float(ThirdNumber)) / float(SecondNumber)) * -1}'
            elif situation == 14:
                FirstNumber = value[0: sign[0][1]]
                SecondNumber = value[sign[0][1] + 1: sign[1][1]]
                ThirdNumber = value[equally_ + 1: len(value)]
                return f'x = {float(ThirdNumber) / float(SecondNumber) / float(FirstNumber)}'
            elif situation == 15:
                FirstNumber = value[0: sign[0][1]]
                SecondNumber = value[sign[0][1] + 1: sign[1][1]]
                ThirdNumber = value[equally_ + 1: len(value)]
                return f'x = {float(ThirdNumber) / (float(FirstNumber) / float(SecondNumber))}'

        elif sign[1][0] == '/':
            if situation == 0:
                FirstNumber = value[2: sign[1][1]]
                SecondNumber = value[sign[1][1] + 1: equally_]
                ThirdNumber = value[equally_ + 1: len(value)]
                return f'x = {float(ThirdNumber) - float(FirstNumber) / float(SecondNumber)}'
            elif situation == 1:
                FirstNumber = value[2: sign[1][1]]
                SecondNumber = value[sign[1][1] + 1: equally_]
                ThirdNumber = value[equally_ + 1: len(value)]
                return f'x = {float(ThirdNumber) + float(FirstNumber) / float(SecondNumber)}'
            elif situation == 2:
                FirstNumber = value[2: sign[1][1]]
                SecondNumber = value[sign[1][1] + 1: equally_]
                ThirdNumber = value[equally_ + 1: len(value)]
                return f'x = {float(ThirdNumber) * (float(SecondNumber) / float(FirstNumber))}'
            elif situation == 3:
                FirstNumber = value[2: sign[1][1]]
                SecondNumber = value[sign[1][1] + 1: equally_]
                ThirdNumber = value[equally_ + 1: len(value)]
                return f'x = {float(ThirdNumber) * float(FirstNumber) * float(SecondNumber)}'

            elif situation == 4:
                FirstNumber = value[0: sign[0][1]]
                SecondNumber = value[sign[0][1] + 1: sign[1][1]]
                ThirdNumber = value[sign[1][1] + 1: equally_]
                return f'x = {float(SecondNumber) / float(ThirdNumber) + float(FirstNumber)}'
            elif situation == 5:
                FirstNumber = value[0: sign[0][1]]
                SecondNumber = value[sign[0][1] + 1: sign[1][1]]
                ThirdNumber = value[sign[1][1] + 1: equally_]
                return f'x = {float(FirstNumber) - float(SecondNumber) / float(ThirdNumber)}'
            elif situation == 6:
                FirstNumber = value[0: sign[0][1]]
                SecondNumber = value[sign[0][1] + 1: sign[1][1]]
                ThirdNumber = value[sign[1][1] + 1: equally_]
                return f'x = {float(FirstNumber) * float(SecondNumber) / float(ThirdNumber)}'
            elif situation == 7:
                FirstNumber = value[0: sign[0][1]]
                SecondNumber = value[sign[0][1] + 1: sign[1][1]]
                ThirdNumber = value[sign[1][1] + 1: equally_]
                return f'x = {float(FirstNumber) / float(SecondNumber) / float(ThirdNumber)}'

            elif situation == 8:
                FirstNumber = value[0: sign[0][1]]
                SecondNumber = value[sign[1][1] + 1: equally_]
                ThirdNumber = value[equally_ + 1: len(value)]
                return f'x = {float(ThirdNumber) * float(SecondNumber) - float(FirstNumber)}'
            elif situation == 9:
                FirstNumber = value[0: sign[0][1]]
                SecondNumber = value[sign[1][1] + 1: equally_]
                ThirdNumber = value[equally_ + 1: len(value)]
                return f'x = {float(FirstNumber) - float(ThirdNumber) * float(SecondNumber)}'
            elif situation == 10:
                FirstNumber = value[0: sign[0][1]]
                SecondNumber = value[sign[1][1] + 1: equally_]
                ThirdNumber = value[equally_ + 1: len(value)]
                return f'x = {float(ThirdNumber) / float(FirstNumber)* float(SecondNumber) }'
            elif situation == 11:
                FirstNumber = value[0: sign[0][1]]
                SecondNumber = value[sign[1][1] + 1: equally_]
                ThirdNumber = value[equally_ + 1: len(value)]
                return f'x = {float(FirstNumber) / (float(ThirdNumber) * float(SecondNumber))}'

            elif situation == 12:
                FirstNumber = value[0: sign[0][1]]
                SecondNumber = value[sign[0][1] + 1: sign[1][1]]
                ThirdNumber = value[equally_ + 1: len(value)]
                return f'x = {float(SecondNumber) / (float(ThirdNumber) - float(FirstNumber))}'
            elif situation == 13:
                FirstNumber = value[0: sign[0][1]]
                SecondNumber = value[sign[0][1] + 1: sign[1][1]]
                ThirdNumber = value[equally_ + 1: len(value)]
                return f'x = {float(SecondNumber) / (float(FirstNumber) - float(ThirdNumber))}'
            elif situation == 14:
                FirstNumber = value[0: sign[0][1]]
                SecondNumber = value[sign[0][1] + 1: sign[1][1]]
                ThirdNumber = value[equally_ + 1: len(value)]
                return f'x = {float(FirstNumber) * float(SecondNumber) / float(ThirdNumber)}'
            elif situation == 15:
                FirstNumber = value[0: sign[0][1]]
                SecondNumber = value[sign[0][1] + 1: sign[1][1]]
                ThirdNumber = value[equally_ + 1: len(value)]
                return f'x = {float(FirstNumber) / float(SecondNumber) / float(ThirdNumber)}'
        else:
            raise InvalidStep()


sc = tk.Tk()
# Настройки окна
photo = tk.PhotoImage(file='icon.png')  # иконка окна загруженная в переменную
sc.iconphoto(False, photo)  # Изменение иконки
sc.title('decque')  # Изменение названия окна
sc.geometry('500x300+100+100')  # Размеры окна и отступы от краёв
sc.minsize(500, 300)  # Минимальные размеры окна
sc.maxsize(500, 300)  # Максимальные размеры окна
sc.resizable(False, False)  # Разрешение и блокировка на изменение размеров окна


# Функции для элементов


def count():
    value = TextArea_1.get()
    try:
        result = equation(value)
        result = str(result)
    except:
        result = 'ERROR'
    TextArea_1.delete(0, 'end')
    TextArea_1.insert(0, result)


def one():
    TextArea_1.insert('end', '1')


def two():
    TextArea_1.insert('end', '2')


def three():
    TextArea_1.insert('end', '3')


def four():
    TextArea_1.insert('end', '4')


def five():
    TextArea_1.insert('end', '5')


def six():
    TextArea_1.insert('end', '6')


def seven():
    TextArea_1.insert('end', '7')


def eight():
    TextArea_1.insert('end', '8')


def nine():
    TextArea_1.insert('end', '9')


def zero():
    TextArea_1.insert('end', '0')


def plus():
    TextArea_1.insert('end', '+')


def minus():
    TextArea_1.insert('end', '-')


def multiply():
    TextArea_1.insert('end', '*')


def division():
    TextArea_1.insert('end', '/')


def equally():
    TextArea_1.insert('end', '=')


def x():
    TextArea_1.insert('end', 'x')


def delete():
    TextArea_1.delete(len(TextArea_1.get()) - 1, 'end')


def point():
    TextArea_1.insert('end', '.')


# Объекты окна
# Бирки с текстом
label_1 = tk.Label(sc, text='Решение уравнений',
                   bg='#222222',
                   fg='white',
                   font=('Arial', 20, 'bold'))

label_2 = tk.Label(sc, text='''Данное приложение предназначено для решения уравнений в одно или в два действия без 
                            скобок. В уравнении могут применяться всего 4 арифметических знака: "+", "-", "*", "/".''',
                   bg='#222222',
                   fg='white',
                   font=('Times new Roman', 10, 'bold'),
                   padx=100,
                   anchor='e')

label_3 = tk.Label(sc, text='               ', bg='#222222')
label_4 = tk.Label(sc, text='               ', bg='#222222')
label_5 = tk.Label(sc, text='               ', bg='#222222')
label_6 = tk.Label(sc, text='               ', bg='#222222')
label_7 = tk.Label(sc, text='               ', bg='#222222')
label_8 = tk.Label(sc, text='               ', bg='#222222')
label_9 = tk.Label(sc, text='               ', bg='#222222')
label_10 = tk.Label(sc, text=' ', bg='#222222', font=('Arial', 2, 'bold'))
label_11 = tk.Label(sc, text=' ', bg='#222222', font=('Arial', 2, 'bold'))
label_12 = tk.Label(sc, text=' ', bg='#222222', font=('Arial', 2, 'bold'))
label_13 = tk.Label(sc, text=' ', bg='#222222', font=('Arial', 2, 'bold'))
label_14 = tk.Label(sc, text=' ', bg='#222222', font=('Arial', 2, 'bold'))
label_15 = tk.Label(sc, text=' ', bg='#222222', font=('Arial', 2, 'bold'))

# Кнопки
button_1 = tk.Button(sc, text='1', command=one, bg='orange', activebackground='red', state=tk.NORMAL, height='1',
                     width='6')
button_2 = tk.Button(sc, text='2', command=two, bg='orange', activebackground='red', state=tk.NORMAL, height='1',
                     width='6')
button_3 = tk.Button(sc, text='3', command=three, bg='orange', activebackground='red', state=tk.NORMAL, height='1',
                     width='6')
button_4 = tk.Button(sc, text='4', command=four, bg='orange', activebackground='red', state=tk.NORMAL, height='1',
                     width='6')
button_5 = tk.Button(sc, text='5', command=five, bg='orange', activebackground='red', state=tk.NORMAL, height='1',
                     width='6')
button_6 = tk.Button(sc, text='6', command=six, bg='orange', activebackground='red', state=tk.NORMAL, height='1',
                     width='6')
button_7 = tk.Button(sc, text='7', command=seven, bg='orange', activebackground='red', state=tk.NORMAL, height='1',
                     width='6')
button_8 = tk.Button(sc, text='8', command=eight, bg='orange', activebackground='red', state=tk.NORMAL, height='1',
                     width='6')
button_9 = tk.Button(sc, text='9', command=nine, bg='orange', activebackground='red', state=tk.NORMAL, height='1',
                     width='6')
button_0 = tk.Button(sc, text='0', command=zero, bg='orange', activebackground='red', state=tk.NORMAL, height='1',
                     width='6')

button_PLUS = tk.Button(sc, text='+', command=plus, bg='white', activebackground='gray', state=tk.NORMAL, height='1',
                        width='6')
button_MINUS = tk.Button(sc, text='-', command=minus, bg='white', activebackground='gray', state=tk.NORMAL, height='1',
                         width='6')
button_MULTIPLY = tk.Button(sc, text='*', command=multiply, bg='white', activebackground='gray', state=tk.NORMAL,
                            height='1', width='6')
button_DIVISION = tk.Button(sc, text='/', command=division, bg='white', activebackground='gray', state=tk.NORMAL,
                            height='1', width='6')
button_EQUALLY = tk.Button(sc, text='=', command=equally, bg='white', activebackground='gray', state=tk.NORMAL,
                           height='1', width='6')
button_X = tk.Button(sc, text='x', command=x, bg='white', activebackground='gray', state=tk.NORMAL, height='1',
                     width='6')
button_POINT = tk.Button(sc, text='.', command=point, bg='orange', activebackground='red', state=tk.NORMAL, height='1',
                         width='6')
button_result = tk.Button(sc, text='Результат', command=count, bg='orange', activebackground='red', state=tk.NORMAL)
button_delete = tk.Button(sc, text='<-', command=delete, bg='white', activebackground='gray', state=tk.NORMAL,
                          height='1', width='6')

# Текстовое поле
TextArea_1 = tk.Entry(sc)
# Размещение объектов окна
sc.config(bg='#222222')  # Разукрашивание заднего фона

label_3.grid(row=0, column=0)
label_4.grid(row=0, column=1)
label_1.grid(row=0, column=2)
label_5.grid(row=0, column=3)
label_6.grid(row=0, column=4)

label_7.grid(row=1, column=0)
TextArea_1.grid(row=2, column=0, columnspan=5, stick='we')
label_8.grid(row=3, column=0)
button_result.grid(row=4, column=0, columnspan=5, stick='we')
label_9.grid(row=5, column=0)
button_1.grid(row=6, column=0, stick='we')
button_2.grid(row=6, column=1, stick='we')
button_3.grid(row=6, column=2, stick='w')
button_PLUS.grid(row=6, column=3, stick='w')
button_delete.grid(row=6, column=4, stick='w')
label_11.grid(row=7, column=0)
button_4.grid(row=8, column=0, stick='we')
button_5.grid(row=8, column=1, stick='we')
button_6.grid(row=8, column=2, stick='w')
button_MINUS.grid(row=8, column=3, stick='w')
button_X.grid(row=8, column=4, stick='w')
label_10.grid(row=9, column=0)
button_7.grid(row=10, column=0, stick='we')
button_8.grid(row=10, column=1, stick='we')
button_9.grid(row=10, column=2, stick='w')
button_MULTIPLY.grid(row=10, column=3, stick='w')
button_EQUALLY.grid(row=10, column=4, stick='sn', rowspan=3)
label_12.grid(row=11, column=0)
button_0.grid(row=12, column=0, stick='we', columnspan=2)
button_POINT.grid(row=12, column=2, stick='w')
button_DIVISION.grid(row=12, column=3, stick='w')

# Цикл
sc.mainloop()  # Цикл приложения
