import tkinter as tk

from fases import fase1
from fases import fase2
from fases import fase3
from fases import fase4
from fases import fase5
from fases import fase6
from fases import fase7
from fases import fase8
from fases import fase9
from fases import fase10


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
        lambda: trocar_fase(
            root,
            iniciar_fase_5
        )
    )


# ============================================================
# FASE 5
# ============================================================

def iniciar_fase_5(root):

    fase5.executar(
        root,
        lambda: trocar_fase(
            root,
            iniciar_fase_6
        )
    )


# ============================================================
# FASE 6
# ============================================================

def iniciar_fase_6(root):

    fase6.executar(
        root,
        lambda: trocar_fase(
            root,
            iniciar_fase_7
        )
    )


# ============================================================
# FASE 7
# ============================================================

def iniciar_fase_7(root):

    fase7.executar(
        root,
        lambda: trocar_fase(
            root,
            iniciar_fase_8
        )
    )


# ============================================================
# FASE 8
# ============================================================

def iniciar_fase_8(root):

    fase8.executar(
        root,
        lambda: trocar_fase(
            root,
            iniciar_fase_9
        )
    )


# ============================================================
# FASE 9
# ============================================================

def iniciar_fase_9(root):

    fase9.executar(
        root,
        lambda: trocar_fase(
            root,
            iniciar_fase_10
        )
    )


# ============================================================
# FASE 10
# ============================================================

def iniciar_fase_10(root):

    fase10.executar(
        root,
        lambda: finalizar_jogo(root)
    )


# ============================================================
# FINALIZAR JOGO
# ============================================================

def finalizar_jogo(root):

    limpar_janela(root)

    print("================================")
    print("CYBERSHIELD FINALIZADO!")
    print("TODAS AS 10 FASES CONCLUÍDAS!")
    print("================================")

    root.destroy()


# ============================================================
# INICIAR JOGO
# ============================================================

if __name__ == "__main__":

    root = tk.Tk()

    iniciar_fase_1(root)

    root.mainloop()
