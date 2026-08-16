import tkinter as tk
import random


# ============================================================
# CYBERSHIELD — FASE 10
# BOSS FINAL
# ============================================================


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

    def __init__(self, root, proxima_fase=None):

        self.root = root
        self.proxima_fase = proxima_fase

        self.root.title(
            "CYBERSHIELD — FASE 10 — BOSS FINAL"
        )

        # ====================================================
        # TELA CHEIA
        # ====================================================

        self.root.attributes(
            "-fullscreen",
            True
        )

        self.root.configure(
            bg=BG
        )

        # ESC sai do modo tela cheia
        self.root.bind(
            "<Escape>",
            self.sair_fullscreen
        )

        # ====================================================
        # STATUS DA BATALHA
        # ====================================================

        self.vida_jogador = 100
        self.vida_boss = 100

        self.questao_atual = 0
        self.respondida = False

        # Guarda se a fase já terminou
        self.fase_finalizada = False

        # ====================================================
        # TELA INICIAL
        # ====================================================

        self.tela_inicial()


    # ========================================================
    # SAIR DO FULLSCREEN
    # ========================================================

    def sair_fullscreen(self, event=None):

        self.root.attributes(
            "-fullscreen",
            False
        )


    # ========================================================
    # LIMPAR JANELA
    # ========================================================

    def limpar_janela(self):

        for widget in self.root.winfo_children():
            widget.destroy()


    # ========================================================
    # TELA INICIAL
    # ========================================================

    def tela_inicial(self):

        self.limpar_janela()

        self.root.configure(
            bg=BG
        )

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
            font=("Consolas", 15, "bold"),
            fg=RED,
            bg=BG
        ).pack(
            pady=(80, 20)
        )

        tk.Label(
            self.frame_inicio,
            text="☠",
            font=("Arial", 80, "bold"),
            fg=RED,
            bg=BG
        ).pack()

        tk.Label(
            self.frame_inicio,
            text="BOSS FINAL",
            font=("Consolas", 40, "bold"),
            fg=RED,
            bg=BG
        ).pack(
            pady=5
        )

        tk.Label(
            self.frame_inicio,
            text="CYBERSHIELD // FASE 10",
            font=("Consolas", 16, "bold"),
            fg=WHITE,
            bg=BG
        ).pack()

        tk.Label(
            self.frame_inicio,
            text="UMA AMEAÇA CRÍTICA FOI DETECTADA.",
            font=("Consolas", 13, "bold"),
            fg=GRAY,
            bg=BG
        ).pack(
            pady=(30, 5)
        )

        tk.Label(
            self.frame_inicio,
            text="O SISTEMA DEPENDE DE VOCÊ.",
            font=("Consolas", 13, "bold"),
            fg=RED,
            bg=BG
        ).pack()

        tk.Frame(
            self.frame_inicio,
            bg=RED,
            height=2,
            width=600
        ).pack(
            pady=30
        )

        self.btn_iniciar = tk.Button(
            self.frame_inicio,
            text="⚔  INICIAR BATALHA",
            font=("Consolas", 14, "bold"),
            fg=WHITE,
            bg=RED_DARK,
            activeforeground=WHITE,
            activebackground=RED_HOVER,
            relief="flat",
            padx=45,
            pady=14,
            cursor="hand2",
            takefocus=False,
            command=self.iniciar
        )

        self.btn_iniciar.pack()

        tk.Label(
            self.frame_inicio,
            text="⚠ ÚLTIMA LINHA DE DEFESA ⚠",
            font=("Consolas", 10, "bold"),
            fg="#660000",
            bg=BG
        ).pack(
            pady=30
        )

        tk.Label(
            self.frame_inicio,
            text="ESC — SAIR DA TELA CHEIA",
            font=("Consolas", 8),
            fg="#441111",
            bg=BG
        ).pack()


    # ========================================================
    # INICIAR
    # ========================================================

    def iniciar(self):

        self.vida_jogador = 100
        self.vida_boss = 100

        self.questao_atual = 0
        self.respondida = False
        self.fase_finalizada = False

        # Garante que continue em tela cheia
        self.root.attributes(
            "-fullscreen",
            True
        )

        self.criar_interface()

        self.carregar_questao()


    # ========================================================
    # INTERFACE
    # ========================================================

    def criar_interface(self):

        self.limpar_janela()

        self.root.configure(
            bg=BG
        )

        tk.Label(
            self.root,
            text="☠  CYBERSHIELD // BOSS FINAL  ☠",
            font=("Consolas", 22, "bold"),
            fg=RED,
            bg=BG
        ).pack(
            pady=(20, 3)
        )

        tk.Label(
            self.root,
            text="SISTEMA EM ESTADO CRÍTICO",
            font=("Consolas", 10, "bold"),
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
            padx=100,
            pady=20
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
            padx=20
        )

        tk.Label(
            self.player_frame,
            text="🛡 PLAYER",
            font=("Consolas", 11, "bold"),
            fg=CYAN,
            bg=BG
        ).pack(
            anchor="w"
        )

        self.player_bar_bg = tk.Canvas(
            self.player_frame,
            width=350,
            height=22,
            bg="#260909",
            highlightthickness=1,
            highlightbackground="#521010"
        )

        self.player_bar_bg.pack(
            pady=5
        )

        self.player_bar = self.player_bar_bg.create_rectangle(
            0,
            0,
            350,
            22,
            fill=CYAN,
            outline=""
        )

        self.player_hp = tk.Label(
            self.player_frame,
            text="100 / 100 HP",
            font=("Consolas", 9, "bold"),
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
            padx=20
        )

        tk.Label(
            self.boss_frame,
            text="☠ BOSS",
            font=("Consolas", 11, "bold"),
            fg=RED,
            bg=BG
        ).pack(
            anchor="e"
        )

        self.boss_bar_bg = tk.Canvas(
            self.boss_frame,
            width=350,
            height=22,
            bg="#260909",
            highlightthickness=1,
            highlightbackground="#521010"
        )

        self.boss_bar_bg.pack(
            pady=5
        )

        self.boss_bar = self.boss_bar_bg.create_rectangle(
            0,
            0,
            350,
            22,
            fill=RED,
            outline=""
        )

        self.boss_hp = tk.Label(
            self.boss_frame,
            text="100 / 100 HP",
            font=("Consolas", 9, "bold"),
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
            padx=100,
            pady=20
        )


        self.lbl_numero = tk.Label(
            self.card,
            text="",
            font=("Consolas", 11, "bold"),
            fg=RED,
            bg=CARD
        )

        self.lbl_numero.pack(
            pady=(25, 8)
        )


        self.lbl_questao = tk.Label(
            self.card,
            text="",
            font=("Segoe UI", 15, "bold"),
            fg=WHITE,
            bg=CARD,
            wraplength=1000,
            justify="center"
        )

        self.lbl_questao.pack(
            pady=15
        )


        self.frame_opcoes = tk.Frame(
            self.card,
            bg=CARD
        )

        self.frame_opcoes.pack(
            fill="x",
            padx=150,
            pady=20
        )


        self.lbl_evento = tk.Label(
            self.card,
            text="",
            font=("Consolas", 11, "bold"),
            fg=WHITE,
            bg=CARD
        )

        self.lbl_evento.pack(
            pady=10
        )


        self.btn_proxima = tk.Button(
            self.card,
            text="PRÓXIMA RODADA  ➜",
            font=("Consolas", 11, "bold"),
            fg=WHITE,
            bg=RED_DARK,
            activeforeground=WHITE,
            activebackground=RED_HOVER,
            relief="flat",
            padx=30,
            pady=10,
            cursor="hand2",
            takefocus=False,
            command=self.proxima
        )


    # ========================================================
    # CARREGAR QUESTÃO
    # ========================================================

    def carregar_questao(self):

        self.respondida = False

        dados = QUESTOES[
            self.questao_atual
        ]

        self.lbl_numero.config(
            text=(
                f"AMEAÇA "
                f"{self.questao_atual + 1} / "
                f"{len(QUESTOES)}"
            )
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


        for i, opcao in enumerate(
            dados["opcoes"]
        ):

            botao = tk.Button(
                self.frame_opcoes,
                text=opcao,
                font=("Segoe UI", 11, "bold"),
                fg=WHITE,
                bg=BUTTON,
                activeforeground=WHITE,
                activebackground=BUTTON_HOVER,
                relief="flat",
                anchor="w",
                padx=15,
                pady=10,
                cursor="hand2",
                takefocus=False,
                command=lambda indice=i:
                self.responder(indice)
            )

            botao.pack(
                fill="x",
                pady=5
            )


    # ========================================================
    # RESPONDER
    # ========================================================

    def responder(self, escolha):

        if self.respondida:
            return

        if self.fase_finalizada:
            return

        self.respondida = True

        dados = QUESTOES[
            self.questao_atual
        ]

        botoes = self.frame_opcoes.winfo_children()

        for botao in botoes:

            botao.config(
                state="disabled"
            )


        # ====================================================
        # ACERTO
        # ====================================================

        if escolha == dados["correta"]:

            dano = random.randint(
                22,
                34
            )

            critico = (
                random.random() < 0.15
            )

            if critico:

                dano += random.randint(
                    8,
                    15
                )

                self.lbl_evento.config(
                    text=(
                        f"💥 ACERTO CRÍTICO!  "
                        f"BOSS -{dano} HP"
                    ),
                    fg=YELLOW
                )

            else:

                self.lbl_evento.config(
                    text=(
                        f"⚡ ATAQUE EFETIVO!  "
                        f"BOSS -{dano} HP"
                    ),
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

            dano = random.randint(
                18,
                32
            )

            self.vida_jogador -= dano

            self.lbl_evento.config(
                text=(
                    f"☠ CONTRA-ATAQUE!  "
                    f"PLAYER -{dano} HP"
                ),
                fg=RED
            )

            botoes[escolha].config(
                bg=RED_DARK
            )

            botoes[
                dados["correta"]
            ].config(
                bg=GREEN,
                fg="#001B0B"
            )

            self.animar_player()


        # ====================================================
        # ATUALIZAR STATUS
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
            pady=8
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
            lambda: (
                self.card.winfo_exists()
                and self.card.config(
                    bg=CARD
                )
            )
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
            lambda: self.root.configure(
                bg=BG
            )
        )


    # ========================================================
    # ATUALIZAR STATUS
    # ========================================================

    def atualizar_status(self):

        self.vida_jogador = max(
            0,
            min(
                100,
                self.vida_jogador
            )
        )

        self.vida_boss = max(
            0,
            min(
                100,
                self.vida_boss
            )
        )


        # ====================================================
        # PLAYER
        # ====================================================

        largura_player = (
            350 *
            (
                self.vida_jogador /
                100
            )
        )

        self.player_bar_bg.coords(
            self.player_bar,
            0,
            0,
            largura_player,
            22
        )

        self.player_hp.config(
            text=(
                f"{self.vida_jogador} / 100 HP"
            )
        )


        # ====================================================
        # BOSS
        # ====================================================

        largura_boss = (
            350 *
            (
                self.vida_boss /
                100
            )
        )

        self.boss_bar_bg.coords(
            self.boss_bar,
            0,
            0,
            largura_boss,
            22
        )

        self.boss_hp.config(
            text=(
                f"{self.vida_boss} / 100 HP"
            )
        )


    # ========================================================
    # PRÓXIMA RODADA
    # ========================================================

    def proxima(self):

        if self.fase_finalizada:
            return

        if self.vida_jogador <= 0:

            self.derrota()

            return

        if self.vida_boss <= 0:

            self.vitoria()

            return


        self.questao_atual += 1


        # ====================================================
        # TODAS AS QUESTÕES TERMINARAM
        # ====================================================

        if self.questao_atual >= len(QUESTOES):

            self.questao_atual = 0

            self.lbl_evento.config(
                text=(
                    "☠ O BOSS AINDA ESTÁ DE PÉ! "
                    "A BATALHA CONTINUA!"
                ),
                fg=RED
            )


        self.carregar_questao()


    # ========================================================
    # VITÓRIA
    # ========================================================

    def vitoria(self):

        if self.vida_boss > 0:
            return

        if self.fase_finalizada:
            return

        self.fase_finalizada = True

        self.limpar_janela()

        self.root.configure(
            bg="#001A0A"
        )


        tk.Label(
            self.root,
            text="🏆",
            font=("Arial", 80),
            fg=GREEN,
            bg="#001A0A"
        ).pack(
            pady=(120, 10)
        )


        tk.Label(
            self.root,
            text="BOSS DERROTADO",
            font=("Consolas", 40, "bold"),
            fg=GREEN,
            bg="#001A0A"
        ).pack()


        tk.Label(
            self.root,
            text="CYBERSHIELD FOI SALVO",
            font=("Consolas", 17, "bold"),
            fg=WHITE,
            bg="#001A0A"
        ).pack(
            pady=15
        )


        tk.Label(
            self.root,
            text=(
                "A ameaça foi contida.\n"
                "A infraestrutura está segura."
            ),
            font=("Segoe UI", 14),
            fg=GRAY,
            bg="#001A0A",
            justify="center"
        ).pack(
            pady=20
        )


        # ====================================================
        # PRÓXIMA FASE
        # ====================================================

        if self.proxima_fase is not None:

            tk.Button(
                self.root,
                text="CONTINUAR ➜",
                font=("Consolas", 12, "bold"),
                fg=WHITE,
                bg="#075C2B",
                activeforeground=WHITE,
                activebackground="#0A7A3A",
                relief="flat",
                padx=40,
                pady=10,
                takefocus=False,
                cursor="hand2",
                command=self.proxima_fase
            ).pack(
                pady=20
            )

        else:

            tk.Label(
                self.root,
                text="🏆 MISSÃO CONCLUÍDA",
                font=("Consolas", 12, "bold"),
                fg=GREEN,
                bg="#001A0A"
            ).pack(
                pady=15
            )


        tk.Label(
            self.root,
            text="ESC — SAIR DA TELA CHEIA",
            font=("Consolas", 8),
            fg="#285C3A",
            bg="#001A0A"
        ).pack(
            pady=10
        )


    # ========================================================
    # DERROTA
    # ========================================================

    def derrota(self):

        if self.vida_jogador > 0:
            return

        if self.fase_finalizada:
            return

        self.fase_finalizada = True

        self.limpar_janela()

        self.root.configure(
            bg="#080000"
        )


        tk.Label(
            self.root,
            text="☠",
            font=("Arial", 80),
            fg=RED,
            bg="#080000"
        ).pack(
            pady=(120, 10)
        )


        tk.Label(
            self.root,
            text="SISTEMA COMPROMETIDO",
            font=("Consolas", 36, "bold"),
            fg=RED,
            bg="#080000"
        ).pack()


        tk.Label(
            self.root,
            text="BOSS FINAL — DERROTA",
            font=("Consolas", 17, "bold"),
            fg=WHITE,
            bg="#080000"
        ).pack(
            pady=15
        )


        tk.Label(
            self.root,
            text=(
                "A defesa falhou.\n"
                "A infraestrutura foi comprometida."
            ),
            font=("Segoe UI", 14),
            fg=GRAY,
            bg="#080000",
            justify="center"
        ).pack(
            pady=20
        )


        # ====================================================
        # TENTAR NOVAMENTE
        # ====================================================

        tk.Button(
            self.root,
            text="TENTAR NOVAMENTE",
            font=("Consolas", 12, "bold"),
            fg=WHITE,
            bg=RED_DARK,
            activeforeground=WHITE,
            activebackground=RED_HOVER,
            relief="flat",
            padx=40,
            pady=10,
            takefocus=False,
            cursor="hand2",
            command=self.iniciar
        ).pack(
            pady=20
        )


        tk.Label(
            self.root,
            text="ESC — SAIR DA TELA CHEIA",
            font=("Consolas", 8),
            fg="#441111",
            bg="#080000"
        ).pack(
            pady=10
        )


# ============================================================
# FUNÇÃO EXECUTAR
# PADRÃO DO MAIN.PY
# ============================================================

def executar(
    root,
    proxima_fase
):

    BossFinal(
        root,
        proxima_fase
    )


# ============================================================
# EXECUÇÃO INDIVIDUAL
# ============================================================

if __name__ == "__main__":

    root = tk.Tk()

    executar(
        root,
        None
    )

    root.mainloop()