import tkinter as tk

from fases import fase1
from fases import fase2
from fases import fase3
from fases import fase4


# ============================================================
# LIMPAR A JANELA ATUAL
# ============================================================

def limpar_janela(root):

    for widget in root.winfo_children():
        widget.destroy()


# ============================================================
# TROCAR DE FASE
# ============================================================

def trocar_fase(root, proxima_fase_func):

    limpar_janela(root)

    # Pequeno atraso para garantir que o Tkinter
    # terminou de destruir os widgets anteriores.
    root.after(
        50,
        lambda: proxima_fase_func(root)
    )


# ============================================================
# FASE 1
# ============================================================

def iniciar_fase_1(root):

    fase1.executar(
        root,
        lambda: trocar_fase(
            root,
            iniciar_fase_2
        )
    )


# ============================================================
# FASE 2
# ============================================================

def iniciar_fase_2(root):

    fase2.executar(
        root,
        lambda: trocar_fase(
            root,
            iniciar_fase_3
        )
    )


# ============================================================
# FASE 3
# ============================================================

def iniciar_fase_3(root):

    fase3.executar(
        root,
        lambda: trocar_fase(
            root,
            iniciar_fase_4
        )
    )


# ============================================================
# FASE 4
# ============================================================

def iniciar_fase_4(root):

    fase4.executar(
        root,
        lambda: finalizar_jogo(root)
    )


# ============================================================
# FINALIZAR JOGO
# ============================================================

def finalizar_jogo(root):

    limpar_janela(root)

    print("================================")
    print("JOGO FINALIZADO!")
    print("================================")

    root.destroy()


# ============================================================
# INICIAR JOGO
# ============================================================

if __name__ == "__main__":

    root = tk.Tk()

    iniciar_fase_1(root)

    root.mainloop()
