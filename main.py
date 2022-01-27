from tkinter import ttk
from tkinter import *
import statistic

version = 'v2.0'

# Application
class Calculator:
    # Constructor
    def __init__(self, window):

        # Config Window
        self.wind = window
        self.wind.title(f'Calculadora {version}')
        self.wind.iconbitmap('calculadora.ico')
        self.wind.geometry('450x300')
        self.wind.minsize(450, 300)

        # Label indicator
        indFrame = LabelFrame(self.wind, text='Operación', pady=10, padx=200)
        #indFrame = LabelFrame(self.wind, text='Operación', width=1000, height=100)
        #indFrame.grid(row=0, column=0, columnspan=3, pady=20)
        indFrame.pack()

        # Label indicator numbers
        self.label = ttk.Label(indFrame, text='')
        self.label.grid(row=0,column=0)

        # Result Label
        self.result_label = ttk.Label(indFrame, text='')
        self.result_label.grid(row=1,column=0)

        # Frame buttons
        frame = Frame(self.wind, pady=20)
        #frame.grid(row=1, column=0, columnspan=3, pady=20)
        frame.pack()

        # Buttons Numbers
        ttk.Button(frame, text='9',command=lambda: self.update_label('9')).grid(row=2,column=2)
        ttk.Button(frame, text='8',command=lambda: self.update_label('8')).grid(row=2,column=1)
        ttk.Button(frame, text='7',command=lambda: self.update_label('7')).grid(row=2,column=0)
        ttk.Button(frame, text='6',command=lambda: self.update_label('6')).grid(row=3,column=2)
        ttk.Button(frame, text='5',command=lambda: self.update_label('5')).grid(row=3,column=1)
        ttk.Button(frame, text='4',command=lambda: self.update_label('4')).grid(row=3,column=0)
        ttk.Button(frame, text='3',command=lambda: self.update_label('3')).grid(row=4,column=2)
        ttk.Button(frame, text='2',command=lambda: self.update_label('2')).grid(row=4,column=1)
        ttk.Button(frame, text='1',command=lambda: self.update_label('1')).grid(row=4,column=0)
        ttk.Button(frame, text='0',command=lambda: self.update_label('0')).grid(row=5,column=0)

        # Habilitamos el poder usar el teclado
        self.wind.bind("<Key>", lambda i: self.check_numpad(i))

        # Buttons specials
        ttk.Button(frame, text='÷', command=lambda: self.add_operation('/')).grid(row=1,column=3)
        ttk.Button(frame, text='x', command=lambda: self.add_operation('*')).grid(row=2,column=3)
        ttk.Button(frame, text='-', command=lambda: self.add_operation('-')).grid(row=3,column=3)
        ttk.Button(frame, text='+', command=lambda: self.add_operation('+')).grid(row=4,column=3)
        ttk.Button(frame, text='=', command=self.operate).grid(row=5,column=3)

        # Button dot '.'
        ttk.Button(frame, text='.').grid(row=5,column=2)

        # Button CE and C
        ttk.Button(frame, text='C', command=self.clear_all).grid(row=1,column=2)
        ttk.Button(frame, text='CE', command=self.clear_number).grid(row=1,column=1)

        # Frame -> Otras opciones/calculos
        optFrame = Frame(self.wind)
        optFrame.pack()

        # Statistic button
        ttk.Button(optFrame, text='Estadistica', command=self.open_statistic).grid(row=1,column=0)
        
        # Declare vars and empty data
        self.label['text'] = ''
        self.operation = 0

    def update_label(self, char):
        # Actualizamos el valor del label que muestra los numeros a operar
        text = self.label.cget('text') + char
        self.label['text'] = text

    def add_operation(self, operator):
        # Configuramos la operacion (1: suma, 2: resta, 3: multiplicacion, 4: division) y lo guardamos en una variable 'self' para que pueda ser usado en todas las funciones
        # dentro de la clase (osea las def que estan dentro de la class Calculator:)
        if operator == '+':
            self.operation = 1
            self.update_label(operator)
        elif operator == '-':
            self.operation = 2
            self.update_label(operator)
        elif operator == '*':
            self.operation = 3
            self.update_label(operator)
        elif operator == '/':
            self.operation = 4
            self.update_label(operator)
    
    def operate(self):
        # Variables
        text = self.label.cget('text')
        first_number = ''
        second_number = ''
        is_first_number = True
        operate = 0
        result = 0
        con_result = False

        # Hacemos un loop para obtener todos los valores que hay en el label de la operacion
        for c in text:
            print(c)
            if c.isnumeric():
                # Si es un numero va guardando los numeros en variables, se guardan en valores tipo string/char
                if is_first_number:
                    # Primer operador
                    first_number = first_number + c
                else:
                    # Segundo operador
                    second_number = second_number + c
            else:
                # Si no es un numero (ya sea porque es el +, -, *, /) empieza a guardar valores en el segundo operador
                #is_first_number = False
                if operate != 0:
                    if operate == 1:
                        if not con_result:
                            result = int(first_number) + int(second_number)
                        else:
                            result = int(result) + int(second_number)
                    elif operate == 2:
                        if not con_result:
                            result = int(first_number) - int(second_number)
                        else:
                            result = int(result) - int(second_number)
                    elif operate == 3:
                        if not con_result:
                            result = int(first_number) * int(second_number)
                        else:
                            result = int(result) * int(second_number)
                    elif operate == 4:
                        if not con_result:
                            result = int(first_number) / int(second_number)
                        else:
                            result = int(result) / int(second_number)

                if c == '+':
                    operate = 1
                elif c == '-':
                    operate = 2
                elif c == '*':
                    operate = 3
                elif c == '/':
                    operate = 4
                
                is_first_number = False

                if result != 0:
                    con_result = True

                print(result, first_number, second_number)

        # Revisamos si ambas variables no estan vacias
        #if first_number == '' or second_number == '': 
            #return

        # Guardamos los numeros totales obtenidos de ambos operadores y los volvemos a guardar en otra variable pero esta vez en un valor tipo int
        #num1 = int(first_number)
        #num2 = int(second_number)

        # Verificamos que operacion queremos hacer (1: suma, 2: resta, 3: multiplicacion, 4: division) y lo guardamos en una variable
        #if self.operation == 1:
        #    result = num1 + num2
        #elif self.operation == 2:
        #    result = num1 - num2
        #elif self.operation == 3:
        #    result = num1 * num2
        #elif self.operation == 4:
        #    result = num1 / num2
        
        # Mostramos el resultado en el label del resultado
        self.result_label['text'] = result

    def clear_all(self):
        # Elimina todo el texto y la operación a realizar
        self.label['text'] = ''
        self.operation = 0

    def clear_number(self):
        # Limpia un sector de la operacion entera, puede ser antes o despues de haber indicado la operacion a realizar
        text = self.label.cget('text')
        clear = False
        clear_text = ''
        # Verificamos si ya se indicó una operación
        if self.operation != 0:
            for c in text:
                # Si hay una operacion buscando el sector de la operación que vamos a eliminar
                if c == '+' or c == '-' or c == '*':
                    # Declaramos esta variable para que empiece a recolectar los valores a eliminar
                    clear = True

                if clear:
                    # Si la variable esta en True guardará los valores a eliminar en 'clear_text'
                    clear_text = clear_text + c

            # Usamos el metodo 'String.replace()' para eliminar los valores que recolectamos con 'clear_text'
            text = text.replace(clear_text, '')
            # Actualizamos el label
            self.label['text'] = text
            self.operation = 0
        else:
            # Si no hay una operación, eliminamos todo el texto
            self.clear_all()

    def check_numpad(self, key):
        print(key)
        keychar = key.char
        keycode = key.keycode
        if keychar == '9' or keychar == '8' or keychar == '7' or keychar == '6' or keychar == '5' or keychar == '4' or keychar == '3' or keychar == '2' or keychar == '1' or keychar == '0':
            # Numero presionado
            self.update_label(keychar)
        if keycode == 13:
            # Enter presionado
            self.operate()
        if keycode == 8:
            # Retroceso presionado
            self.clear_number()
        if keychar == '+' or keychar == '-' or keychar == '*' or keychar == '/':
            self.add_operation(keychar)

    def open_statistic(self):
        statistic.Statistics()


# Funcion principal
if __name__ == '__main__':
    window = Tk()
    app = Calculator(window)
    window.mainloop()