<<<<<<< Updated upstream
=======
import tkinter as tk
import random


# ============================================================
# CORES
# ============================================================

BG = "#090000"
CARD = "#1A0505"
RED = "#FF1744"
RED_DARK = "#8B0000"
RED_HOVER = "#C4112F"
WHITE = "#FFFFFF"
GRAY = "#BDBDBD"
CYAN = "#00E5FF"
GREEN = "#00E676"
YELLOW = "#FFD600"
BUTTON = "#350909"
BUTTON_HOVER = "#5A1111"


# ============================================================
# QUESTÕES
# ============================================================

QUESTOES = [

    {
        "questao": "ACESSO SUSPEITO DETECTADO NA CONTA ADMINISTRADOR.",
        "opcoes": [
            "A) Ignorar o alerta",
            "B) Publicar o incidente na rede",
            "C) Bloquear as credenciais comprometidas",
            "D) Apagar todos os arquivos"
        ],
        "correta": 2
    },

    {
        "questao": "ATAQUE DE INJEÇÃO SQL DETECTADO NO SERVIDOR.",
        "opcoes": [
            "A) Isolar o servidor da rede",
            "B) Mudar o plano de fundo",
            "C) Ignorar os logs",
            "D) Reiniciar todos os computadores"
        ],
        "correta": 0
    },

    {
        "questao": "VULNERABILIDADE ZERO-DAY SENDO EXPLORADA!",
        "opcoes": [
            "A) Esperar o ataque terminar",
            "B) Criar regras de contenção no WAF/Firewall",
            "C) Ignorar os alertas",
            "D) Compartilhar a informação publicamente"
        ],
        "correta": 1
    },

    {
        "questao": "UM FUNCIONÁRIO RECEBEU UM E-MAIL COM LINK SUSPEITO.",
        "opcoes": [
            "A) Clicar no link para verificar",
            "B) Encaminhar para toda a empresa",
            "C) Reportar o e-mail e não abrir o link",
            "D) Responder pedindo a senha"
        ],
        "correta": 2
    },

    {
        "questao": "RANSOMWARE DETECTADO EM UMA ESTAÇÃO CORPORATIVA.",
        "opcoes": [
            "A) Isolar imediatamente o computador da rede",
            "B) Desativar o antivírus",
            "C) Compartilhar os arquivos infectados",
            "D) Ignorar o incidente"
        ],
        "correta": 0
    },

    {
        "questao": "VÁRIAS TENTATIVAS DE LOGIN FORAM DETECTADAS NA CONTA ADMIN.",
        "opcoes": [
            "A) Liberar mais tentativas",
            "B) Desativar os logs",
            "C) Investigar e aplicar bloqueio/rate limiting",
            "D) Compartilhar a conta"
        ],
        "correta": 2
    },

    {
        "questao": "QUAL MEDIDA AUMENTA A SEGURANÇA DE UMA CONTA ADMINISTRATIVA?",
        "opcoes": [
            "A) Usar a mesma senha em todos os sistemas",
            "B) Ativar autenticação multifator (MFA)",
            "C) Compartilhar a senha pelo chat",
            "D) Usar uma senha simples"
        ],
        "correta": 1
    },

    {
        "questao": "TRÁFEGO ANORMAL FOI DETECTADO PELO FIREWALL.",
        "opcoes": [
            "A) Analisar os logs e investigar o tráfego",
            "B) Apagar os logs",
            "C) Desativar o firewall",
            "D) Liberar o endereço suspeito"
        ],
        "correta": 0
    }

]


# ============================================================
# BOSS FINAL
# ============================================================

class BossFinal:

    def __init__(self, root):

        self.root = root

        self.root.title("CYBERSHIELD — BOSS FINAL")
        self.root.geometry("800x600")
        self.root.resizable(False, False)
        self.root.configure(bg=BG)

        # ====================================================
        # BLOQUEAR TECLADO
        # ====================================================
        # Impede que ESPAÇO ou ENTER acionem botões
        # automaticamente.
        self.root.bind_all("<space>", self.bloquear_tecla)
        self.root.bind_all("<Return>", self.bloquear_tecla)

        self.vida_jogador = 100
        self.vida_boss = 100

        self.questao_atual = 0
        self.respondida = False

        self.tela_inicial()


    # ========================================================
    # BLOQUEAR TECLAS
    # ========================================================

    def bloquear_tecla(self, event):
        return "break"


    # ========================================================
    # TELA INICIAL
    # ========================================================

    def tela_inicial(self):

        self.frame_inicio = tk.Frame(
            self.root,
            bg=BG
        )

        self.frame_inicio.pack(
            fill="both",
            expand=True
        )

        tk.Label(
            self.frame_inicio,
            text="⚠  ALERTA DE SEGURANÇA MÁXIMO  ⚠",
            font=("Consolas", 11, "bold"),
            fg=RED,
            bg=BG
        ).pack(pady=(35, 12))

        tk.Label(
            self.frame_inicio,
            text="☠",
            font=("Arial", 55, "bold"),
            fg=RED,
            bg=BG
        ).pack()

        tk.Label(
            self.frame_inicio,
            text="BOSS FINAL",
            font=("Consolas", 32, "bold"),
            fg=RED,
            bg=BG
        ).pack(pady=2)

        tk.Label(
            self.frame_inicio,
            text="CYBERSHIELD // FASE 10",
            font=("Consolas", 13, "bold"),
            fg=WHITE,
            bg=BG
        ).pack()

        tk.Label(
            self.frame_inicio,
            text="UMA AMEAÇA CRÍTICA FOI DETECTADA.",
            font=("Consolas", 10, "bold"),
            fg=GRAY,
            bg=BG
        ).pack(pady=(22, 3))

        tk.Label(
            self.frame_inicio,
            text="O SISTEMA DEPENDE DE VOCÊ.",
            font=("Consolas", 10, "bold"),
            fg=RED,
            bg=BG
        ).pack()

        tk.Frame(
            self.frame_inicio,
            bg=RED,
            height=2,
            width=480
        ).pack(pady=22)

        self.btn_iniciar = tk.Button(
            self.frame_inicio,
            text="⚔  INICIAR BATALHA",
            font=("Consolas", 12, "bold"),
            fg=WHITE,
            bg=RED_DARK,
            activeforeground=WHITE,
            activebackground=RED_HOVER,
            relief="flat",
            padx=35,
            pady=11,
            cursor="hand2",
            takefocus=False,
            command=self.iniciar
        )

        self.btn_iniciar.pack()

        tk.Label(
            self.frame_inicio,
            text="⚠ ÚLTIMA LINHA DE DEFESA ⚠",
            font=("Consolas", 8, "bold"),
            fg="#660000",
            bg=BG
        ).pack(pady=25)


    # ========================================================
    # INICIAR
    # ========================================================

    def iniciar(self):

        self.frame_inicio.destroy()

        self.criar_interface()

        self.carregar_questao()


    # ========================================================
    # INTERFACE
    # ========================================================

    def criar_interface(self):

        tk.Label(
            self.root,
            text="☠  CYBERSHIELD // BOSS FINAL  ☠",
            font=("Consolas", 17, "bold"),
            fg=RED,
            bg=BG
        ).pack(pady=(10, 2))

        tk.Label(
            self.root,
            text="SISTEMA EM ESTADO CRÍTICO",
            font=("Consolas", 8, "bold"),
            fg=RED,
            bg=BG
        ).pack()


        # ====================================================
        # STATUS
        # ====================================================

        self.status = tk.Frame(
            self.root,
            bg=BG
        )

        self.status.pack(
            fill="x",
            padx=25,
            pady=8
        )


        # ====================================================
        # PLAYER
        # ====================================================

        self.player_frame = tk.Frame(
            self.status,
            bg=BG
        )

        self.player_frame.pack(
            side="left",
            fill="x",
            expand=True,
            padx=8
        )

        tk.Label(
            self.player_frame,
            text="🛡 PLAYER",
            font=("Consolas", 9, "bold"),
            fg=CYAN,
            bg=BG
        ).pack(anchor="w")

        self.player_bar_bg = tk.Canvas(
            self.player_frame,
            width=280,
            height=18,
            bg="#260909",
            highlightthickness=1,
            highlightbackground="#521010"
        )

        self.player_bar_bg.pack(pady=3)

        self.player_bar = self.player_bar_bg.create_rectangle(
            0,
            0,
            280,
            18,
            fill=CYAN,
            outline=""
        )

        self.player_hp = tk.Label(
            self.player_frame,
            text="100 / 100 HP",
            font=("Consolas", 8, "bold"),
            fg=WHITE,
            bg=BG
        )

        self.player_hp.pack()


        # ====================================================
        # BOSS
        # ====================================================

        self.boss_frame = tk.Frame(
            self.status,
            bg=BG
        )

        self.boss_frame.pack(
            side="right",
            fill="x",
            expand=True,
            padx=8
        )

        tk.Label(
            self.boss_frame,
            text="☠ BOSS",
            font=("Consolas", 9, "bold"),
            fg=RED,
            bg=BG
        ).pack(anchor="e")

        self.boss_bar_bg = tk.Canvas(
            self.boss_frame,
            width=280,
            height=18,
            bg="#260909",
            highlightthickness=1,
            highlightbackground="#521010"
        )

        self.boss_bar_bg.pack(pady=3)

        self.boss_bar = self.boss_bar_bg.create_rectangle(
            0,
            0,
            280,
            18,
            fill=RED,
            outline=""
        )

        self.boss_hp = tk.Label(
            self.boss_frame,
            text="100 / 100 HP",
            font=("Consolas", 8, "bold"),
            fg=WHITE,
            bg=BG
        )

        self.boss_hp.pack()


        # ====================================================
        # CARD
        # ====================================================

        self.card = tk.Frame(
            self.root,
            bg=CARD,
            highlightbackground=RED_DARK,
            highlightthickness=2
        )

        self.card.pack(
            fill="both",
            expand=True,
            padx=30,
            pady=8
        )


        self.lbl_numero = tk.Label(
            self.card,
            text="",
            font=("Consolas", 9, "bold"),
            fg=RED,
            bg=CARD
        )

        self.lbl_numero.pack(pady=(10, 3))


        self.lbl_questao = tk.Label(
            self.card,
            text="",
            font=("Segoe UI", 11, "bold"),
            fg=WHITE,
            bg=CARD,
            wraplength=650,
            justify="center"
        )

        self.lbl_questao.pack(pady=5)


        self.frame_opcoes = tk.Frame(
            self.card,
            bg=CARD
        )

        self.frame_opcoes.pack(
            fill="x",
            padx=60,
            pady=8
        )


        self.lbl_evento = tk.Label(
            self.card,
            text="",
            font=("Consolas", 9, "bold"),
            fg=WHITE,
            bg=CARD
        )

        self.lbl_evento.pack(pady=4)


        self.btn_proxima = tk.Button(
            self.card,
            text="PRÓXIMA RODADA  ➜",
            font=("Consolas", 9, "bold"),
            fg=WHITE,
            bg=RED_DARK,
            activeforeground=WHITE,
            activebackground=RED_HOVER,
            relief="flat",
            padx=22,
            pady=6,
            cursor="hand2",
            takefocus=False,
            command=self.proxima
        )


    # ========================================================
    # CARREGAR QUESTÃO
    # ========================================================

    def carregar_questao(self):

        self.respondida = False

        dados = QUESTOES[self.questao_atual]

        self.lbl_numero.config(
            text=f"AMEAÇA {self.questao_atual + 1} / {len(QUESTOES)}"
        )

        self.lbl_questao.config(
            text=dados["questao"]
        )

        self.lbl_evento.config(
            text=""
        )

        self.btn_proxima.pack_forget()


        for widget in self.frame_opcoes.winfo_children():
            widget.destroy()


        for i, opcao in enumerate(dados["opcoes"]):

            botao = tk.Button(
                self.frame_opcoes,
                text=opcao,
                font=("Segoe UI", 9, "bold"),
                fg=WHITE,
                bg=BUTTON,
                activeforeground=WHITE,
                activebackground=BUTTON_HOVER,
                relief="flat",
                anchor="w",
                padx=12,
                pady=7,
                cursor="hand2",

                # Impede foco pelo teclado.
                takefocus=False,

                command=lambda indice=i: self.responder(indice)
            )

            botao.pack(
                fill="x",
                pady=3
            )


    # ========================================================
    # RESPONDER
    # ========================================================

    def responder(self, escolha):

        if self.respondida:
            return

        self.respondida = True

        dados = QUESTOES[self.questao_atual]

        botoes = self.frame_opcoes.winfo_children()

        for botao in botoes:
            botao.config(
                state="disabled"
            )


        # ====================================================
        # ACERTO
        # ====================================================

        if escolha == dados["correta"]:

            dano = random.randint(22, 34)

            critico = random.random() < 0.15

            if critico:

                dano += random.randint(8, 15)

                self.lbl_evento.config(
                    text=f"💥 ACERTO CRÍTICO!  BOSS -{dano} HP",
                    fg=YELLOW
                )

            else:

                self.lbl_evento.config(
                    text=f"⚡ ATAQUE EFETIVO!  BOSS -{dano} HP",
                    fg=GREEN
                )

            self.vida_boss -= dano

            botoes[escolha].config(
                bg=GREEN,
                fg="#001B0B"
            )

            self.animar_boss()


        # ====================================================
        # ERRO
        # ====================================================

        else:

            dano = random.randint(18, 32)

            self.vida_jogador -= dano

            self.lbl_evento.config(
                text=f"☠ CONTRA-ATAQUE!  PLAYER -{dano} HP",
                fg=RED
            )

            botoes[escolha].config(
                bg=RED_DARK
            )

            botoes[dados["correta"]].config(
                bg=GREEN,
                fg="#001B0B"
            )

            self.animar_player()


        # ====================================================
        # ATUALIZA STATUS
        # ====================================================

        self.atualizar_status()


        # ====================================================
        # DERROTA
        # ====================================================

        if self.vida_jogador <= 0:

            self.root.after(
                700,
                self.derrota
            )

            return


        # ====================================================
        # VITÓRIA
        # ====================================================

        if self.vida_boss <= 0:

            self.root.after(
                700,
                self.vitoria
            )

            return


        # ====================================================
        # CONTINUAR
        # ====================================================

        self.btn_proxima.pack(
            pady=4
        )


    # ========================================================
    # ANIMAÇÃO BOSS
    # ========================================================

    def animar_boss(self):

        self.card.config(
            bg="#5C0000"
        )

        self.root.after(
            100,
            lambda: self.card.config(bg=CARD)
        )


    # ========================================================
    # ANIMAÇÃO PLAYER
    # ========================================================

    def animar_player(self):

        self.root.configure(
            bg="#550000"
        )

        self.root.after(
            100,
            lambda: self.root.configure(bg=BG)
        )


    # ========================================================
    # ATUALIZAR STATUS
    # ========================================================

    def atualizar_status(self):

        self.vida_jogador = max(
            0,
            min(100, self.vida_jogador)
        )

        self.vida_boss = max(
            0,
            min(100, self.vida_boss)
        )


        # PLAYER

        largura_player = 280 * (
            self.vida_jogador / 100
        )

        self.player_bar_bg.coords(
            self.player_bar,
            0,
            0,
            largura_player,
            18
        )

        self.player_hp.config(
            text=f"{self.vida_jogador} / 100 HP"
        )


        # BOSS

        largura_boss = 280 * (
            self.vida_boss / 100
        )

        self.boss_bar_bg.coords(
            self.boss_bar,
            0,
            0,
            largura_boss,
            18
        )

        self.boss_hp.config(
            text=f"{self.vida_boss} / 100 HP"
        )


    # ========================================================
    # PRÓXIMA RODADA
    # ========================================================

    def proxima(self):

        # Segurança contra estados inválidos

        if self.vida_jogador <= 0:
            self.derrota()
            return

        if self.vida_boss <= 0:
            self.vitoria()
            return


        self.questao_atual += 1


        # Se acabaram as perguntas,
        # volta para a primeira.
        # Isso NÃO gera vitória.

        if self.questao_atual >= len(QUESTOES):

            self.questao_atual = 0

            self.lbl_evento.config(
                text="☠ O BOSS AINDA ESTÁ DE PÉ! A BATALHA CONTINUA!",
                fg=RED
            )


        self.carregar_questao()


    # ========================================================
    # VITÓRIA
    # ========================================================

    def vitoria(self):

        if self.vida_boss > 0:
            return

        for widget in self.root.winfo_children():
            widget.destroy()

        self.root.configure(
            bg="#001A0A"
        )

        tk.Label(
            self.root,
            text="🏆",
            font=("Arial", 55),
            fg=GREEN,
            bg="#001A0A"
        ).pack(pady=(70, 5))

        tk.Label(
            self.root,
            text="BOSS DERROTADO",
            font=("Consolas", 30, "bold"),
            fg=GREEN,
            bg="#001A0A"
        ).pack()

        tk.Label(
            self.root,
            text="CYBERSHIELD FOI SALVO",
            font=("Consolas", 13, "bold"),
            fg=WHITE,
            bg="#001A0A"
        ).pack(pady=10)

        tk.Label(
            self.root,
            text="A ameaça foi contida.\nA infraestrutura está segura.",
            font=("Segoe UI", 11),
            fg=GRAY,
            bg="#001A0A",
            justify="center"
        ).pack(pady=15)

        tk.Button(
            self.root,
            text="SAIR",
            font=("Consolas", 10, "bold"),
            fg=WHITE,
            bg="#075C2B",
            relief="flat",
            padx=30,
            pady=8,
            takefocus=False,
            command=self.root.destroy
        ).pack(pady=15)


    # ========================================================
    # DERROTA
    # ========================================================

    def derrota(self):

        if self.vida_jogador > 0:
            return

        for widget in self.root.winfo_children():
            widget.destroy()

        self.root.configure(
            bg="#080000"
        )

        tk.Label(
            self.root,
            text="☠",
            font=("Arial", 55),
            fg=RED,
            bg="#080000"
        ).pack(pady=(70, 5))

        tk.Label(
            self.root,
            text="SISTEMA COMPROMETIDO",
            font=("Consolas", 27, "bold"),
            fg=RED,
            bg="#080000"
        ).pack()

        tk.Label(
            self.root,
            text="BOSS FINAL — DERROTA",
            font=("Consolas", 13, "bold"),
            fg=WHITE,
            bg="#080000"
        ).pack(pady=10)

        tk.Label(
            self.root,
            text="A defesa falhou.\nA infraestrutura foi comprometida.",
            font=("Segoe UI", 11),
            fg=GRAY,
            bg="#080000",
            justify="center"
        ).pack(pady=15)

        tk.Button(
            self.root,
            text="SAIR",
            font=("Consolas", 10, "bold"),
            fg=WHITE,
            bg=RED_DARK,
            relief="flat",
            padx=30,
            pady=8,
            takefocus=False,
            command=self.root.destroy
        ).pack(pady=15)


# ============================================================
# EXECUTAR
# ============================================================

if __name__ == "__main__":

    root = tk.Tk()

    jogo = BossFinal(root)

    root.mainloop()
>>>>>>> Stashed changes
