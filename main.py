import tkinter as tk

from fases import fase1
from fases import fase2
from fases import fase3
from fases import fase4


# ============================================================
# FASE 1
# ============================================================

def iniciar_fase_1():

    root = tk.Tk()

    fase1.executar(
        root,
        lambda: trocar_fase(
            root,
            iniciar_fase_2
        )
    )

    root.mainloop()


# ============================================================
# FASE 2
# ============================================================

def iniciar_fase_2():

    root = tk.Tk()

    fase2.executar(
        root,
        lambda: trocar_fase(
            root,
            iniciar_fase_3
        )
    )

    root.mainloop()


# ============================================================
# FASE 3
# ============================================================

def iniciar_fase_3():

    root = tk.Tk()

    fase3.executar(
        root,
        lambda: trocar_fase(
            root,
            iniciar_fase_4
        )
    )

    root.mainloop()


# ============================================================
# FASE 4
# ============================================================

def iniciar_fase_4():

    root = tk.Tk()

    fase4.executar(
        root,
        lambda: finalizar_jogo(root)
    )

    root.mainloop()


# ============================================================
# TROCAR DE FASE
# ============================================================

def trocar_fase(janela_atual, proxima_fase):

    janela_atual.destroy()

    proxima_fase()


# ============================================================
# FINALIZAR
# ============================================================

def finalizar_jogo(janela_atual):

    janela_atual.destroy()

    print("Jogo finalizado!")


# ============================================================
# INICIAR JOGO
# ============================================================

iniciar_fase_1()