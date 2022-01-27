from tkinter import ttk
from tkinter import *
import numpy
from numpy import ndarray
from scipy import stats
from scipy.stats.stats import ModeResult

class Statistics():
    def __init__(self):
        self.window = Tk()
        self.window.title('Estadistica')
        self.window.iconbitmap('calculadora.ico')
        self.window.geometry('300x150')
        self.window.minsize(300, 150)

        # Frame datos
        frame = Frame(self.window, pady=10)
        frame.pack()

        Label(frame, text='Ingresa los datos a calcular:').grid(row=1, column=0)
        self.numbers = Entry(frame)
        self.numbers.grid(row=1, column=1)
        self.numbers.focus()

        btn = ttk.Button(frame, text="Calcular", command=self.calculate).grid(row=2, column=1)

        rFrame = LabelFrame(self.window, text='Resultados', pady=5, padx=20)
        rFrame.pack()

        Label(rFrame, text="Media", anchor=CENTER).grid(row=3, column=0, padx=10)
        self.media = Label(rFrame, text='')
        self.media.grid(row=4, column=0)

        Label(rFrame, text="Mediana", anchor=CENTER).grid(row=3, column=2, padx=10)
        self.mediana = Label(rFrame, text='')
        self.mediana.grid(row=4, column=2)

        Label(rFrame, text="Moda", anchor=CENTER).grid(row=3, column=4, padx=10)
        self.moda = Label(rFrame, text='')
        self.moda.grid(row=4, column=4)

        self.window.bind('<Key>', lambda i: self.on_enter(i))

        self.window.mainloop()
    
    def calculate(self):
        text = self.numbers.get() + ' '

        if len(text) <= 1:
            return
        
        text = text.strip().replace(' ', ',')
        text = text + ','

        numberlist = []
        number_char = ''
        for c in text:
            if c.isnumeric():
                number_char = number_char + c
            
            if c == ',':
                numberlist.append(int(number_char))
                number_char = ''

        media = self.calculate_media(numberlist)
        mediana = self.calculate_mediana(numberlist)
        moda = self.calculate_moda(numberlist)

        self.media["text"] = str(media)
        self.mediana["text"] = str(mediana)
        self.moda["text"] = moda

    def on_enter(self, key):
        keycode = key.keycode
        if keycode == 13:
            self.calculate()
    
    def calculate_media(self, numbers = []):
        return numpy.mean(numbers)

    def calculate_mediana(self, numbers = []):
        numbers.sort()
        nlen = len(numbers)
        if ispar(nlen):
            # Es par
            if nlen > 2:
                newlist = numbers[int((nlen/2)-1):int((nlen/2)+1)]
                result = (newlist[0] + newlist[1]) / 2
            else:
                result = (numbers[0] + numbers[1]) / 2
            return result

        else:
            # Es impar
            result = numbers[int(nlen/2)]
            return result

    def calculate_moda(self, numbers = []):
        result = stats.mode(numbers)
        return f"{result[0][0]} ({result[1][0]})"

def ispar(num):
    if num % 2 == 0:
        return True
    else:
        return False