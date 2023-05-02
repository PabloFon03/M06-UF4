import re


def AskYesNo(question):
    while True:
        answer = input(question + " [Y/N] ").lower()
        if answer == 'y' or answer == 'n':
            return answer == 'y'
        else:
            print("Respuesta inválida. Debes responder con Y (Yes) o N (No).")


def AskNumber(question, min, max):
    while True:
        answer = input(question)
        if answer.isdecimal():
            n = int(answer)
            if n >= min and n <= max:
                return n
            else:
                print(f"El número debe estar entre {min} y {max}.")
        else:
            print("La entrada no es un número válido.")


def AskDecimalNumber(question, min, max):
    while True:
        answer = input(question)
        if re.match(r"^\d+(\.\d+)?$", answer):
            n = float(answer)
            if n >= min and n <= max:
                return n
            else:
                print(f"El número debe estar entre {min} y {max}.")
        else:
            print("La entrada no es un número válido.")


def AskAlphaNum(question, min, max):
    while True:
        answer = input(question)
        if answer.isalnum():
            if len(answer) >= min and len(answer) <= max:
                return answer
            else:
                print(f"La cadena debe medir entre {min} y {max} caracteres.")
        else:
            print("Sólo se permiten caracteres alfanuméricos.")
