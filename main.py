import tkinter as tk

from fases import fase1
from fases import fase2
from fases import fase3
from fases import fase4


# ============================================================
# TROCAR DE FASE
# ============================================================

def trocar_fase(janela_atual, proxima_fase):
    janela_atual.destroy()
    proxima_fase()


# ============================================================
# FASE 1
# ============================================================

def iniciar_fase_1():
    root = tk.Tk()

    fase1.executar(
        root,
        lambda: trocar_fase(root, iniciar_fase_2)
    )


# ============================================================
# FASE 2
# ============================================================

def iniciar_fase_2():
    root = tk.Tk()

    fase2.executar(
        root,
        lambda: trocar_fase(root, iniciar_fase_3)
    )


# ============================================================
# FASE 3
# ============================================================

def iniciar_fase_3():
    root = tk.Tk()

    fase3.executar(
        root,
        lambda: trocar_fase(root, iniciar_fase_4)
    )


# ============================================================
# FASE 4
# ============================================================

def iniciar_fase_4():
    root = tk.Tk()

    fase4.executar(
        root,
        lambda: finalizar_jogo(root)
    )


# ============================================================
# FINALIZAR JOGO
# ============================================================

def finalizar_jogo(janela):
    janela.destroy()
    print("================================")
    print("JOGO FINALIZADO!")
    print("================================")


# ============================================================
# INICIAR
# ============================================================

iniciar_fase_1()

# APENAS UM MAINLOOP PARA O JOGO INTEIRO
tk.mainloop()
