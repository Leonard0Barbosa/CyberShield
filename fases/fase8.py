import tkinter as tk
from tkinter import messagebox


# ==============================================================================
# FASE 8 — DESENVOLVIMENTO SEGURO
# CyberShield: Academia do Hacker Ético
# ==============================================================================


# ==============================================================================
# CORES — CYBER NETWORK
# ==============================================================================

COLOR_BG_TOP = "#030D22"
COLOR_BG_BOTTOM = "#0A2542"

COLOR_CARD_BG = "#0D1F38"
COLOR_CARD_BORDER = "#144574"

COLOR_CYAN_GLOW = "#00F0FF"

COLOR_BTN_BG = "#0F3356"
COLOR_BTN_HOVER = "#0077B6"

COLOR_TEXT_MAIN = "#FFFFFF"
COLOR_TEXT_MUTED = "#8ECAE6"

COLOR_HEALTH = "#00F5D4"
COLOR_CORRECT = "#00E676"
COLOR_INCORRECT = "#FF3366"
COLOR_WARNING = "#FFD166"


# ==============================================================================
# BANCO DE PERGUNTAS — FASE 8
# ==============================================================================

QUIZ_FASE_8 = [

    {
        "category": "🛠️ VALIDAÇÃO DE ENTRADAS",

        "question":
            "Durante o desenvolvimento de um sistema, "
            "foi identificada uma falha relacionada aos dados "
            "enviados pelos usuários.\n\n"
            "Qual medida é mais adequada para reduzir esse risco?",

        "options": [
            "A) Aumentar a velocidade do servidor",
            "B) Desativar o firewall",
            "C) Validar e tratar adequadamente as entradas",
            "D) Armazenar todos os dados em texto puro"
        ],

        "answer": 2,

        "explanations": [
            "❌ INCORRETO: Aumentar a velocidade do servidor "
            "não corrige falhas de validação. Um servidor mais rápido "
            "continuará vulnerável se aceitar entradas maliciosas.",

            "❌ INCORRETO: Desativar o firewall reduziria ainda mais "
            "a segurança e não corrige o problema relacionado "
            "à validação das entradas.",

            "✅ CORRETO! A validação e o tratamento adequado das entradas "
            "ajudam a impedir que dados maliciosos sejam aceitos "
            "pelo sistema.",

            "❌ INCORRETO: Armazenar dados em texto puro pode aumentar "
            "o risco de exposição e vazamento de informações."
        ],

        "tip":
            "💡 Dica: Nunca confie automaticamente nos dados enviados "
            "pelo usuário. Valide formato, tamanho, tipo e conteúdo."
    },


    {
        "category": "🧹 SANITIZAÇÃO DE DADOS",

        "question":
            "Qual é o principal objetivo da sanitização de entradas "
            "em uma aplicação?",

        "options": [
            "A) Aumentar a capacidade do armazenamento",
            "B) Remover ou neutralizar elementos potencialmente perigosos",
            "C) Desligar os mecanismos de autenticação",
            "D) Tornar todos os usuários administradores"
        ],

        "answer": 1,

        "explanations": [
            "❌ INCORRETO: Sanitização não tem como objetivo aumentar "
            "a capacidade de armazenamento.",

            "✅ CORRETO! A sanitização busca remover, escapar ou neutralizar "
            "elementos que poderiam ser interpretados de forma perigosa "
            "pela aplicação.",

            "❌ INCORRETO: A sanitização não deve desativar autenticação "
            "ou outros mecanismos de segurança.",

            "❌ INCORRETO: Tornar usuários administradores seria uma "
            "grave violação do princípio do menor privilégio."
        ],

        "tip":
            "💡 Dica: Validação verifica se o dado está no formato esperado; "
            "sanitização ajuda a tornar a entrada mais segura para processamento."
    },


    {
        "category": "🌐 CROSS-SITE SCRIPTING — XSS",

        "question":
            "Uma aplicação exibe diretamente um texto fornecido por um usuário "
            "em uma página web sem realizar o tratamento adequado. "
            "Qual vulnerabilidade pode surgir?",

        "options": [
            "A) XSS — Cross-Site Scripting",
            "B) DHCP Spoofing obrigatoriamente",
            "C) Falha física no processador",
            "D) Apenas lentidão no monitor"
        ],

        "answer": 0,

        "explanations": [
            "✅ CORRETO! XSS pode ocorrer quando dados fornecidos pelo usuário "
            "são inseridos em páginas web sem o devido tratamento, "
            "permitindo que conteúdo não confiável seja interpretado "
            "pelo navegador.",

            "❌ INCORRETO: DHCP Spoofing é um ataque relacionado à infraestrutura "
            "de rede e não é a consequência direta descrita na situação.",

            "❌ INCORRETO: A falha descrita está relacionada ao processamento "
            "de conteúdo web, não ao processador físico.",

            "❌ INCORRETO: O problema apresentado é uma questão de segurança "
            "da aplicação, não simplesmente de desempenho."
        ],

        "tip":
            "💡 Dica: Dados vindos do usuário devem ser tratados como "
            "não confiáveis até serem devidamente validados e processados."
    },


    {
        "category": "🔒 PRINCÍPIO DE DEFESA EM PROFUNDIDADE",

        "question":
            "O que significa aplicar Defesa em Profundidade "
            "(Defense in Depth) no desenvolvimento seguro?",

        "options": [
            "A) Utilizar apenas um firewall muito poderoso",
            "B) Utilizar várias camadas independentes de proteção",
            "C) Desativar controles para melhorar o desempenho",
            "D) Confiar exclusivamente na senha do usuário"
        ],

        "answer": 1,

        "explanations": [
            "❌ INCORRETO: Um único mecanismo pode falhar. "
            "A segurança não deve depender de apenas uma barreira.",

            "✅ CORRETO! Defesa em Profundidade utiliza várias camadas "
            "de segurança, como autenticação, autorização, validação, "
            "criptografia, logs e monitoramento.",

            "❌ INCORRETO: Desativar controles reduz a segurança "
            "e não representa defesa em profundidade.",

            "❌ INCORRETO: Uma senha sozinha não representa uma estratégia "
            "completa de defesa em profundidade."
        ],

        "tip":
            "💡 Dica: Se uma camada falhar, outras devem continuar protegendo "
            "o sistema."
    },


    {
        "category": "🧪 SECURE BY DESIGN",

        "question":
            "O conceito de Secure by Design recomenda que a segurança:",

        "options": [
            "A) Seja adicionada somente depois que o sistema estiver pronto",
            "B) Seja considerada desde as primeiras etapas do desenvolvimento",
            "C) Seja responsabilidade exclusiva do usuário final",
            "D) Seja ignorada durante a fase de testes"
        ],

        "answer": 1,

        "explanations": [
            "❌ INCORRETO: Corrigir segurança apenas no final pode tornar "
            "as correções mais caras e deixar vulnerabilidades durante "
            "grande parte do desenvolvimento.",

            "✅ CORRETO! Secure by Design significa considerar segurança "
            "desde a arquitetura, requisitos e desenvolvimento até os testes "
            "e manutenção.",

            "❌ INCORRETO: Segurança é responsabilidade de toda a equipe "
            "envolvida no desenvolvimento e operação do sistema.",

            "❌ INCORRETO: Testes de segurança são fundamentais para "
            "identificar problemas antes da implantação."
        ],

        "tip":
            "💡 Dica: Segurança não deve ser um 'remendo' colocado "
            "depois que o sistema já está pronto."
    }
]


# ==============================================================================
# CLASSE PRINCIPAL — FASE 8
# ==============================================================================

class Phase8App:

    def __init__(self, root, proxima_fase):

        self.root = root
        self.proxima_fase = proxima_fase

        self.root.title(
            "CyberShield: Fase 8 — Desenvolvimento Seguro"
        )

        self.root.geometry(
            "700x640"
        )

        self.root.resizable(
            False,
            False
        )

        self.current_q = 0

        self.score = 0

        self.lives = 3

        self.setup_ui()

        self.load_quiz_mode()


    # ==========================================================================
    # INTERFACE
    # ==========================================================================

    def setup_ui(self):

        self.bg_canvas = tk.Canvas(
            self.root,
            width=700,
            height=640,
            highlightthickness=0
        )

        self.bg_canvas.pack(
            fill="both",
            expand=True
        )

        self.draw_cyber_background()


        # ----------------------------------------------------------------------
        # HEADER
        # ----------------------------------------------------------------------

        self.status_frame = tk.Frame(
            self.bg_canvas,
            bg=COLOR_BG_TOP
        )

        self.bg_canvas.create_window(
            350,
            35,
            window=self.status_frame,
            width=660
        )


        self.lbl_header = tk.Label(
            self.status_frame,
            text="🛡️ FASE 8: DESENVOLVIMENTO SEGURO",
            font=("Consolas", 11, "bold"),
            fg=COLOR_HEALTH,
            bg=COLOR_BG_TOP
        )

        self.lbl_header.pack(
            side="left"
        )


        self.lbl_status = tk.Label(
            self.status_frame,
            text="",
            font=("Consolas", 11, "bold"),
            fg=COLOR_CYAN_GLOW,
            bg=COLOR_BG_TOP
        )

        self.lbl_status.pack(
            side="right"
        )


        # ----------------------------------------------------------------------
        # CARD
        # ----------------------------------------------------------------------

        self.card_frame = tk.Frame(
            self.bg_canvas,
            bg=COLOR_CARD_BG,
            highlightbackground=COLOR_CARD_BORDER,
            highlightthickness=2,
            bd=0
        )

        self.bg_canvas.create_window(
            350,
            330,
            window=self.card_frame,
            width=660,
            height=520
        )


    # ==========================================================================
    # FUNDO CYBER
    # ==========================================================================

    def draw_cyber_background(self):

        width = 700
        height = 640

        r1, g1, b1 = self.hex_to_rgb(
            COLOR_BG_TOP
        )

        r2, g2, b2 = self.hex_to_rgb(
            COLOR_BG_BOTTOM
        )


        # ----------------------------------------------------------------------
        # GRADIENTE
        # ----------------------------------------------------------------------

        for y in range(height):

            r = int(
                r1 + (r2 - r1) * (y / height)
            )

            g = int(
                g1 + (g2 - g1) * (y / height)
            )

            b = int(
                b1 + (b2 - b1) * (y / height)
            )

            color = f"#{r:02x}{g:02x}{b:02x}"


            self.bg_canvas.create_line(
                0,
                y,
                width,
                y,
                fill=color
            )


        # ----------------------------------------------------------------------
        # CIRCUITOS
        # ----------------------------------------------------------------------

        line_color = "#0B3254"

        glow_dot = COLOR_CYAN_GLOW


        self.bg_canvas.create_line(
            30,
            25,
            180,
            25,
            230,
            50,
            480,
            50,
            fill=line_color,
            width=1.5
        )

        self.bg_canvas.create_oval(
            177,
            22,
            183,
            28,
            fill=glow_dot,
            outline=""
        )

        self.bg_canvas.create_oval(
            477,
            47,
            483,
            53,
            fill=glow_dot,
            outline=""
        )


        self.bg_canvas.create_line(
            50,
            610,
            200,
            610,
            250,
            590,
            550,
            590,
            fill=line_color,
            width=1.5
        )

        self.bg_canvas.create_oval(
            247,
            587,
            253,
            593,
            fill=glow_dot,
            outline=""
        )


    # ==========================================================================
    # HEX → RGB
    # ==========================================================================

    @staticmethod
    def hex_to_rgb(hex_str):

        hex_str = hex_str.lstrip("#")

        return tuple(
            int(
                hex_str[i:i + 2],
                16
            )
            for i in (0, 2, 4)
        )


    # ==========================================================================
    # LIMPAR CARD
    # ==========================================================================

    def clear_card(self):

        for widget in self.card_frame.winfo_children():

            widget.destroy()


    # ==========================================================================
    # BOTÃO
    # ==========================================================================

    def create_custom_button(
        self,
        parent,
        text,
        command
    ):

        btn = tk.Button(
            parent,
            text=text,
            font=("Segoe UI", 9, "bold"),
            bg=COLOR_BTN_BG,
            fg=COLOR_TEXT_MUTED,
            activebackground=COLOR_BTN_HOVER,
            activeforeground=COLOR_TEXT_MAIN,
            relief="flat",
            cursor="hand2",
            anchor="w",
            padx=15,
            bd=1,
            highlightbackground=COLOR_CARD_BORDER,
            command=command
        )


        btn.bind(
            "<Enter>",
            lambda e, b=btn:
            self.on_hover_enter(b)
        )

        btn.bind(
            "<Leave>",
            lambda e, b=btn:
            self.on_hover_leave(b)
        )


        return btn


    # ==========================================================================
    # HOVER
    # ==========================================================================

    def on_hover_enter(self, btn):

        if btn["state"] == "normal":

            btn.config(
                bg=COLOR_BTN_HOVER,
                fg=COLOR_TEXT_MAIN
            )


    def on_hover_leave(self, btn):

        if btn["state"] == "normal":

            btn.config(
                bg=COLOR_BTN_BG,
                fg=COLOR_TEXT_MUTED
            )


    # ==========================================================================
    # QUIZ
    # ==========================================================================

    def load_quiz_mode(self):

        self.clear_card()


        self.lbl_status.config(
            text=(
                f"QUESTÃO "
                f"{self.current_q + 1}/"
                f"{len(QUIZ_FASE_8)}   |   "
                f"🛡️ FIREWALL: {'█ ' * self.lives}"
                f"   |   SCORE: {self.score}"
            )
        )


        q_data = QUIZ_FASE_8[
            self.current_q
        ]


        # ----------------------------------------------------------------------
        # CATEGORIA
        # ----------------------------------------------------------------------

        lbl_cat = tk.Label(
            self.card_frame,
            text=q_data["category"],
            font=("Segoe UI", 10, "bold"),
            fg=COLOR_CYAN_GLOW,
            bg=COLOR_CARD_BG
        )

        lbl_cat.pack(
            anchor="w",
            padx=20,
            pady=(15, 5)
        )


        # ----------------------------------------------------------------------
        # PERGUNTA
        # ----------------------------------------------------------------------

        lbl_q = tk.Label(
            self.card_frame,
            text=q_data["question"],
            font=("Segoe UI", 10),
            fg=COLOR_TEXT_MAIN,
            bg=COLOR_CARD_BG,
            wraplength=600,
            justify="left"
        )

        lbl_q.pack(
            anchor="w",
            padx=20,
            pady=10
        )


        # ----------------------------------------------------------------------
        # BOTÕES
        # ----------------------------------------------------------------------

        self.quiz_buttons = []


        for i, opt in enumerate(
            q_data["options"]
        ):

            btn = tk.Button(
                self.card_frame,
                text=opt,
                font=("Segoe UI", 9, "bold"),
                bg=COLOR_BTN_BG,
                fg=COLOR_TEXT_MUTED,
                activebackground=COLOR_BTN_HOVER,
                activeforeground=COLOR_TEXT_MAIN,
                relief="flat",
                cursor="hand2",
                anchor="w",
                padx=15,
                bd=1,
                highlightbackground=COLOR_CARD_BORDER,
                command=lambda idx=i:
                self.check_quiz_answer(idx)
            )


            btn.pack(
                fill="x",
                padx=20,
                pady=5,
                ipady=4
            )


            btn.bind(
                "<Enter>",
                lambda e, b=btn:
                self.on_hover_enter(b)
            )

            btn.bind(
                "<Leave>",
                lambda e, b=btn:
                self.on_hover_leave(b)
            )


            self.quiz_buttons.append(btn)


    # ==========================================================================
    # VERIFICAR RESPOSTA
    # ==========================================================================

    def check_quiz_answer(
        self,
        selected_idx
    ):

        q_data = QUIZ_FASE_8[
            self.current_q
        ]

        correct_idx = q_data["answer"]

        selected_btn = self.quiz_buttons[
            selected_idx
        ]


        # ----------------------------------------------------------------------
        # RESPOSTA CORRETA
        # ----------------------------------------------------------------------

        if selected_idx == correct_idx:

            for btn in self.quiz_buttons:

                btn.config(
                    state="disabled"
                )


            selected_btn.config(
                bg=COLOR_CORRECT,
                fg="#000000"
            )


            self.root.update()


            self.score += 100


            messagebox.showinfo(
                "Resposta Correta! 🎯",

                f"{q_data['explanations'][selected_idx]}"
                f"\n\n"
                f"{q_data['tip']}"
                f"\n\n"
                f"+100 PTS"
            )


            self.current_q += 1


            # ------------------------------------------------------------------
            # PRÓXIMA QUESTÃO
            # ------------------------------------------------------------------

            if self.current_q < len(QUIZ_FASE_8):

                self.load_quiz_mode()


            # ------------------------------------------------------------------
            # FASE 8 CONCLUÍDA
            # ------------------------------------------------------------------

            else:

                self.lbl_status.config(
                    text=(
                        f"FASE CONCLUÍDA   |   "
                        f"SCORE FINAL: {self.score}"
                    )
                )


                messagebox.showinfo(
                    "Fase 8 Concluída! 🏆",

                    "Parabéns!\n\n"
                    "Você concluiu o módulo de Desenvolvimento Seguro!\n\n"

                    "• Validação de Entradas\n"
                    "• Sanitização de Dados\n"
                    "• Cross-Site Scripting (XSS)\n"
                    "• Defesa em Profundidade\n"
                    "• Secure by Design\n\n"

                    f"SCORE FINAL: {self.score}\n\n"

                    "Prepare-se para a Fase 9!"
                )


                # ==============================================================
                # IMPORTANTE
                #
                # NÃO destruir a janela.
                #
                # O MAIN será responsável pela transição.
                # ==============================================================

                if self.proxima_fase:

                    self.proxima_fase()


        # ----------------------------------------------------------------------
        # RESPOSTA INCORRETA
        # ----------------------------------------------------------------------

        else:

            self.lives -= 1


            selected_btn.config(
                bg=COLOR_INCORRECT,
                fg="#FFFFFF"
            )


            self.root.update()


            messagebox.showerror(
                "Resposta Incorreta! ⚠️",

                f"{q_data['explanations'][selected_idx]}"
                f"\n\n"
                f"{q_data['tip']}"
                f"\n\n"
                f"🛡️ Firewall restante: {self.lives}"
            )


            # ------------------------------------------------------------------
            # GAME OVER
            # ------------------------------------------------------------------

            if self.lives <= 0:

                self.quiz_buttons[
                    correct_idx
                ].config(
                    bg=COLOR_CORRECT,
                    fg="#000000"
                )


                for btn in self.quiz_buttons:

                    btn.config(
                        state="disabled"
                    )


                self.root.update()


                messagebox.showerror(
                    "GAME OVER 🚨",

                    "O firewall foi completamente comprometido!\n\n"
                    "Você perdeu todas as suas defesas.\n\n"
                    "A Fase 8 será reiniciada."
                )


                # --------------------------------------------------------------
                # REINICIAR FASE 8
                # --------------------------------------------------------------

                self.current_q = 0

                self.score = 0

                self.lives = 3


                self.load_quiz_mode()


            else:

                # --------------------------------------------------------------
                # Mostra a resposta correta e permite tentar novamente
                # --------------------------------------------------------------

                self.quiz_buttons[
                    correct_idx
                ].config(
                    bg=COLOR_CORRECT,
                    fg="#000000"
                )

                self.root.update()

                # Volta para a mesma questão depois da explicação
                self.load_quiz_mode()


# ==============================================================================
# FUNÇÃO EXECUTAR — PADRÃO DO MAIN.PY
# ==============================================================================

def executar(
    root,
    proxima_fase
):

    Phase8App(
        root,
        proxima_fase
    )