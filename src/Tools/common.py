import os


def ClearConsole():
    os.system('cls' if os.name == 'nt' else 'clear')


def FormatPrice(price):
    return format(price, ".2f") + "€"
