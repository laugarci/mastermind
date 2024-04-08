import tkinter as tk
import random
from game import *

num = resultNum()
noNum = checkIncorrectNums(num)
oneNumWrongPlace = oneNumCorrectWrongPlace(num)
oneNumWrongPlace2 = oneNumCorrectWrongPlace(num)
oneNumCorrectPlace = oneNumCorrectCorrectPlace(num)
oneNumCorrectPlace2 = oneNumCorrectCorrectPlace(num)
twoNumIncorrectPlace = twoNumsCorrectWrongPlace(num)

print(num)
print(noNum)
print(oneNumWrongPlace)
print(oneNumWrongPlace2)
print(oneNumCorrectPlace)
print(oneNumCorrectPlace2)
print(twoNumIncorrectPlace)

root = tk.Tk()
root.title("Números Generados")

def reiniciar_juego():
    global num, noNum, oneNumWrongPlace, oneNumWrongPlace2, oneNumCorrectPlace, oneNumCorrectPlace2, twoNumIncorrectPlace
    num = resultNum()
    noNum = checkIncorrectNums(num)
    oneNumWrongPlace = oneNumCorrectWrongPlace(num)
    oneNumWrongPlace2 = oneNumCorrectWrongPlace(num)
    oneNumCorrectPlace = oneNumCorrectCorrectPlace(num)
    oneNumCorrectPlace2 = oneNumCorrectCorrectPlace(num)
    twoNumIncorrectPlace = twoNumsCorrectWrongPlace(num)
    resultado.config(text="")
    mostrar_numeros()

def mostrar_numeros():
    for i, (numero, descripcion) in enumerate([(noNum, "Todos los números son incorrectos"),
                                                (oneNumWrongPlace, "Un número es correcto pero en el lugar incorrecto"),
                                                (oneNumWrongPlace2, "Un número es correcto pero en el lugar incorrecto"),
                                                (oneNumCorrectPlace, "Un número es correcto y en el lugar correcto"),
                                                (twoNumIncorrectPlace, "Dos números son correctos pero en el lugar incorrecto"),
                                                (oneNumCorrectPlace2, "Un numero es correcto y el en lugar correcto")]):
        tk.Label(root, text=descripcion).grid(row=i, column=0, padx=5, pady=5)
        for j, digit in enumerate(str(numero)):
            button_digit = tk.Button(root, text=digit, font=("Helvetica", 16), width=6, height=2, command=lambda d=digit: marcar_numero(d))
            button_digit.grid(row=i, column=j+1, padx=5, pady=5)

mostrar_numeros()

entrada = tk.Entry(root, font=("Helvetica", 20), justify="center")
entrada.grid(row=8, column=0, columnspan=2, padx=5, pady=5)

def verificar_respuesta(resultado):
    respuesta_usuario = entrada.get()
    if (respuesta_usuario == str(num)):
        resultado.config(text="Correcto!")
    else:
        resultado.config(text=f"Incorrecto, el numero era {num}")

def marcar_numero(numero):
    for widget in root.winfo_children():
        if isinstance(widget, tk.Button) and widget.cget("text") == numero:
            widget.config(text="X", state="disabled")


boton_verificar = tk.Button(root, text="Verificar", command=lambda: verificar_respuesta(resultado))
boton_verificar.grid(row=10, column=0, columnspan=2, padx=5, pady=5)

boton_reiniciar = tk.Button(root, text="Reiniciar Juego", command=reiniciar_juego)
boton_reiniciar.grid(row=11, column=0, columnspan=2, padx=5, pady=5)

resultado = tk.Label(root, text="", font=("Helvetica", 16))
resultado.grid(row=12, column=0, columnspan=2, padx=5, pady=5)

root.mainloop()

