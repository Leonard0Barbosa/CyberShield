import tkinter as tk
from tkinter import messagebox
import os
import pygame
import sqlite3
from flask import Flask , render_template



con = sqlite3.connect("database.db")

from MENU import introdução
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
# MÚSICA
# ============================================================

CAMINHO_MUSICA = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "assets",
    "AUD-20260817-WA0003.mp3"
)


# ============================================================
# INICIALIZAR ÁUDIO
# ============================================================

try:

    pygame.mixer.init()

    print("🔊 Sistema de áudio inicializado.")

except Exception as erro:

    print("❌ Erro ao inicializar o áudio:")
    print(erro)


# ============================================================
# INICIAR MÚSICA
# ============================================================

def iniciar_musica():

    print("================================")
    print("🎵 TENTANDO INICIAR A MÚSICA")
    print("================================")

    print(
        "Caminho:",
        CAMINHO_MUSICA
    )

    # Verifica se o arquivo realmente existe
    if not os.path.exists(CAMINHO_MUSICA):

        print("❌ MÚSICA NÃO ENCONTRADA!")

        print(
            "Verifique se o arquivo está em:"
        )

        print(
            os.path.join(
                "assets",
                "AUD-20260817-WA0003.mp3"
            )
        )

        return

    print("✅ Arquivo de música encontrado!")

    try:

        pygame.mixer.music.load(
            CAMINHO_MUSICA
        )

        print("✅ Música carregada!")

        pygame.mixer.music.set_volume(
            0.7
        )

        pygame.mixer.music.play(
            loops=-1
        )

        print("🎵 MÚSICA TOCANDO EM LOOP!")

    except Exception as erro:

        print("❌ ERRO AO TOCAR A MÚSICA:")
        print(erro)


# ============================================================
# PARAR MÚSICA
# ============================================================

def parar_musica():

    try:

        pygame.mixer.music.stop()

        print("🔇 Música parada.")

    except Exception as erro:

        print("Erro ao parar música:")
        print(erro)


# ============================================================
# LIMPAR JANELA
# ============================================================

def limpar_janela(root):

    for widget in root.winfo_children():

        widget.destroy()


# ============================================================
# TROCAR DE FASE
# ============================================================


def trocar_fase(root, proxima_fase_func):

    limpar_janela(root)

    def carregar_proxima_fase():

        # Mantém a janela visível
        root.deiconify()

        # Reativa a tela cheia
        root.attributes("-fullscreen", True)

        # Coloca o jogo na frente
        root.lift()

        # Abre a próxima fase
        proxima_fase_func(root)

        # Recupera o foco após carregar os elementos
        root.after(150, recuperar_foco)

    def recuperar_foco():

        root.attributes("-fullscreen", True)
        root.lift()
        root.focus_force()

    root.after(50, carregar_proxima_fase)



# ============================================================
# INTRODUÇÃO
# ============================================================

def iniciar_introdução(root):

    introdução.executar(
        root,
        lambda: trocar_fase(
            root,
            iniciar_fase_1
        )
    )


# ============================================================
# FASE 1
# ============================================================

def iniciar_fase_1(root):

    # ========================================================
    # A MÚSICA COMEÇA EXATAMENTE AQUI
    # ========================================================

    iniciar_musica()

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

    # Para a música ao entrar na Fase 10
    parar_musica()

    fase10.executar(
        root,
        lambda: finalizar_jogo(root)
    )


# ============================================================
# FINALIZAR JOGO
# ============================================================

def finalizar_jogo(root):

    parar_musica()

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

    iniciar_introdução(root)

    root.mainloop()
