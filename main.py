import tkinter as tk

from fases import fase1
from fases import fase2
from fases import fase3


def iniciar_fase_1():
    root = tk.Tk()
    fase1.executar(root, iniciar_fase_2)
    root.mainloop()


def iniciar_fase_2():
    root = tk.Tk()
    fase2.executar(root, iniciar_fase_3)
    root.mainloop()


def iniciar_fase_3():
    root = tk.Tk()
    fase3.executar(root, finalizar_jogo)
    root.mainloop()


def finalizar_jogo():
    print("Jogo finalizado!")


iniciar_fase_1()