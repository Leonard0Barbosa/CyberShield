import tkinter as tk

from fases import fase1
from fases import fase2
from fases import fase3

# ============================================================
# FASE 1
# ============================================================

def iniciar_fase_1():

    root = tk.Tk()

    fase1.executar(
        root,
        lambda: iniciar_fase_2(root)
    )

    root.mainloop()


# ============================================================
# FASE 2
# ============================================================

def iniciar_fase_2(janela_anterior):

    # Fecha a janela da Fase 1
    janela_anterior.destroy()

    # Cria a janela da Fase 2
    root = tk.Tk()

    fase2.executar(
        root,
        lambda: iniciar_fase_3(root)
    )

    root.mainloop()


# ============================================================
# FASE 3
# ============================================================

def iniciar_fase_3(janela_anterior):

    # Fecha a janela da Fase 2
    janela_anterior.destroy()

    # Cria a janela da Fase 3
    root = tk.Tk()

    fase3.executar(
        root,
        lambda: finalizar_jogo(root)
    )

    root.mainloop()

# ============================================================
# FASE 4
# ============================================================

def iniciar_fase_4():

    root = tk.Tk()

    fase1.executar(
        root,
        lambda: iniciar_fase_2(root)
    )

    root.mainloop()

# ============================================================
# FINALIZAR
# ============================================================

def finalizar_jogo(janela_atual):

    # Fecha a janela da Fase 36
    janela_atual.destroy()

    print("Jogo finalizado!")


# ============================================================
# INICIAR
# ============================================================

iniciar_fase_1()