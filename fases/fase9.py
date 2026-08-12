import tkinter as tk
from tkinter import messagebox


# ==============================================================================
# --- CYBERSHIELD: FASE 9 — SOC ---
# ==============================================================================

# ==============================================================================
# --- CORES PRINCIPAIS ---
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


# ==============================================================================
# --- CORES DA TELA BOSS ---
# ==============================================================================

COLOR_BOSS_BG = "#050000"
COLOR_BOSS_RED = "#FF1744"
COLOR_BOSS_RED_DARK = "#8B0000"
COLOR_BOSS_RED_GLOW = "#FF0033"
COLOR_BOSS_TEXT = "#FFFFFF"
COLOR_BOSS_MUTED = "#FF8A9B"


# ==============================================================================
# --- DADOS DA FASE 9 ---
# ==============================================================================

QUESTIONS = [

    {
        "category": "🔴 FASE 9 — SOC",

        "question": (
            "Um analista do SOC identificou os seguintes eventos nos logs:\n\n"
            "• 08:41 — 5 falhas de login consecutivas\n"
            "• 08:45 — login realizado com sucesso\n"
            "• 08:47 — acesso originado de uma localização incomum\n"
            "• 08:49 — download de vários arquivos\n\n"
            "Qual é a conclusão mais adequada neste momento?"
        ),

        # ----------------------------------------------------------------------
        # IMPORTANTE:
        # NÃO existem ❌ ou ✅ nas alternativas.
        # A resposta somente aparece depois do clique.
        # ----------------------------------------------------------------------

        "options": [

            "O computador está definitivamente infectado",

            "O servidor está necessariamente desligado",

            "Existe um comportamento suspeito que merece investigação",

            "O usuário esqueceu a senha"
        ],

        # C = índice 2

        "answer": 2,

        # ----------------------------------------------------------------------
        # EXPLICAÇÕES
        # ----------------------------------------------------------------------

        "explanations": [

            (
                "❌ RESPOSTA INCORRETA\n\n"

                "Não existem evidências suficientes para afirmar que o computador "
                "está definitivamente infectado.\n\n"

                "Os eventos indicam uma possível atividade suspeita, mas ainda "
                "é necessária uma investigação para determinar o que realmente "
                "aconteceu."
            ),

            (
                "❌ RESPOSTA INCORRETA\n\n"

                "Os registros mostram atividade no ambiente, incluindo um login "
                "bem-sucedido, acesso de localização incomum e download de arquivos.\n\n"

                "Portanto, não existe base suficiente para afirmar que o servidor "
                "está necessariamente desligado."
            ),

            (
                "✅ RESPOSTA CORRETA\n\n"

                "As falhas de login, o acesso de uma localização incomum e o "
                "download de arquivos formam um conjunto de indicadores que "
                "merece investigação pelo SOC.\n\n"

                "A conclusão adequada é identificar o comportamento como "
                "suspeito sem afirmar prematuramente que ocorreu uma invasão "
                "ou uma infecção."
            ),

            (
                "❌ RESPOSTA INCORRETA\n\n"

                "As falhas de login podem realmente acontecer porque um usuário "
                "esqueceu a senha.\n\n"

                "Porém, essa explicação é insuficiente para explicar os eventos "
                "seguintes, como o acesso de uma localização incomum e o "
                "download de vários arquivos."
            )
        ],

        # ----------------------------------------------------------------------
        # DICA
        # ----------------------------------------------------------------------

        "tip": (
            "💡 DICA SOC\n\n"

            "Em segurança, investigue os indícios antes de tirar conclusões "
            "definitivas.\n\n"

            "Observe o conjunto de eventos e procure comportamentos anormais "
            "antes de determinar a causa."
        )
    }
]


# ==============================================================================
# --- CLASSE PRINCIPAL ---
# ==============================================================================

class CyberQuizApp:

    def __init__(self, root):

        self.root = root

        # ----------------------------------------------------------------------
        # CONFIGURAÇÃO DA JANELA
        # ----------------------------------------------------------------------

        self.root.title(
            "CyberShield: Ethical Hacker Quiz"
        )

        self.root.geometry(
            "660x560"
        )

        self.root.resizable(
            False,
            False
        )

        # ----------------------------------------------------------------------
        # VARIÁVEIS
        # ----------------------------------------------------------------------

        self.current_q = 0

        self.lives = 3

        self.score = 0

        # ----------------------------------------------------------------------
        # INTERFACE
        # ----------------------------------------------------------------------

        self.setup_ui()

        self.load_question()


    # ==========================================================================
    # --- INTERFACE PRINCIPAL ---
    # ==========================================================================

    def setup_ui(self):

        # ----------------------------------------------------------------------
        # CANVAS
        # ----------------------------------------------------------------------

        self.bg_canvas = tk.Canvas(

            self.root,

            width=660,

            height=560,

            highlightthickness=0
        )

        self.bg_canvas.pack(

            fill="both",

            expand=True
        )

        self.draw_cyber_background()


        # ----------------------------------------------------------------------
        # STATUS
        # ----------------------------------------------------------------------

        self.status_frame = tk.Frame(

            self.bg_canvas,

            bg=COLOR_BG_TOP
        )

        self.bg_canvas.create_window(

            330,

            35,

            window=self.status_frame,

            width=620
        )


        # ----------------------------------------------------------------------
        # FIREWALL
        # ----------------------------------------------------------------------

        self.lbl_firewall = tk.Label(

            self.status_frame,

            text=f"🛡️ FIREWALL: {'█ ' * self.lives}",

            font=("Consolas", 13, "bold"),

            fg=COLOR_HEALTH,

            bg=COLOR_BG_TOP
        )

        self.lbl_firewall.pack(

            side="left"
        )


        # ----------------------------------------------------------------------
        # SCORE
        # ----------------------------------------------------------------------

        self.lbl_score = tk.Label(

            self.status_frame,

            text=f"SCORE: {self.score}",

            font=("Consolas", 13, "bold"),

            fg=COLOR_CYAN_GLOW,

            bg=COLOR_BG_TOP
        )

        self.lbl_score.pack(

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

            330,

            290,

            window=self.card_frame,

            width=620,

            height=430
        )


        # ----------------------------------------------------------------------
        # CATEGORIA
        # ----------------------------------------------------------------------

        self.lbl_category = tk.Label(

            self.card_frame,

            text="",

            font=("Segoe UI", 10, "bold"),

            fg=COLOR_CYAN_GLOW,

            bg=COLOR_CARD_BG
        )

        self.lbl_category.pack(

            anchor="w",

            padx=20,

            pady=(15, 5)
        )


        # ----------------------------------------------------------------------
        # PERGUNTA
        # ----------------------------------------------------------------------

        self.lbl_question = tk.Label(

            self.card_frame,

            text="",

            font=("Segoe UI", 10, "bold"),

            fg=COLOR_TEXT_MAIN,

            bg=COLOR_CARD_BG,

            wraplength=570,

            justify="left"
        )

        self.lbl_question.pack(

            anchor="w",

            padx=20,

            pady=10
        )


        # ----------------------------------------------------------------------
        # FRAME DOS BOTÕES
        # ----------------------------------------------------------------------

        self.btn_frame = tk.Frame(

            self.card_frame,

            bg=COLOR_CARD_BG
        )

        self.btn_frame.pack(

            fill="both",

            expand=True,

            padx=20,

            pady=10
        )


        self.buttons = []


        # ----------------------------------------------------------------------
        # CRIAR 4 BOTÕES
        # ----------------------------------------------------------------------

        for i in range(4):

            btn = tk.Button(

                self.btn_frame,

                text="",

                font=("Segoe UI", 10, "bold"),

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
                self.check_answer(idx)
            )

            btn.pack(

                fill="x",

                pady=5,

                ipady=3
            )


            # Hover

            btn.bind(

                "<Enter>",

                lambda event, button=btn:
                self.on_hover_enter(button)
            )


            btn.bind(

                "<Leave>",

                lambda event, button=btn:
                self.on_hover_leave(button)
            )


            self.buttons.append(btn)


    # ==========================================================================
    # --- HOVER ---
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
    # --- FUNDO CYBER ---
    # ==========================================================================

    def draw_cyber_background(self):

        width = 660

        height = 560


        # ----------------------------------------------------------------------
        # DEGRADÊ
        # ----------------------------------------------------------------------

        r1, g1, b1 = self.hex_to_rgb(

            COLOR_BG_TOP
        )

        r2, g2, b2 = self.hex_to_rgb(

            COLOR_BG_BOTTOM
        )


        for y in range(height):

            r = int(

                r1 +
                (r2 - r1) *
                (y / height)
            )

            g = int(

                g1 +
                (g2 - g1) *
                (y / height)
            )

            b = int(

                b1 +
                (b2 - b1) *
                (y / height)
            )


            color = (

                f"#{r:02x}"
                f"{g:02x}"
                f"{b:02x}"
            )


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


        # Circuito superior

        self.bg_canvas.create_line(

            30,
            25,
            180,
            25,
            230,
            50,
            430,
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

            427,
            47,
            433,
            53,

            fill=glow_dot,

            outline=""
        )


        # Circuito inferior

        self.bg_canvas.create_line(

            50,
            530,
            200,
            530,
            250,
            510,
            500,
            510,
            550,
            535,

            fill=line_color,

            width=1.5
        )


        self.bg_canvas.create_oval(

            247,
            507,
            253,
            513,

            fill=glow_dot,

            outline=""
        )


        self.bg_canvas.create_oval(

            497,
            507,
            503,
            513,

            fill=glow_dot,

            outline=""
        )


    # ==========================================================================
    # --- HEX → RGB ---
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
    # --- CARREGAR QUESTÃO ---
    # ==========================================================================

    def load_question(self):

        if self.current_q < len(QUESTIONS):

            q_data = QUESTIONS[

                self.current_q
            ]


            # Categoria

            self.lbl_category.config(

                text=q_data["category"]
            )


            # Pergunta

            self.lbl_question.config(

                text=q_data["question"]
            )


            # Alternativas

            for i, option in enumerate(

                q_data["options"]
            ):

                self.buttons[i].config(

                    text=f"[ {chr(65 + i)} ]   {option}",

                    bg=COLOR_BTN_BG,

                    fg=COLOR_TEXT_MUTED,

                    state="normal"
                )


        else:

            # ------------------------------------------------------------------
            # FASE 9 TERMINOU
            # ------------------------------------------------------------------

            self.show_boss_transition()


    # ==========================================================================
    # --- VERIFICAR RESPOSTA ---
    # ==========================================================================

    def check_answer(self, selected_idx):

        # ----------------------------------------------------------------------
        # DESATIVAR BOTÕES
        # ----------------------------------------------------------------------

        for btn in self.buttons:

            btn.config(

                state="disabled"
            )


        q_data = QUESTIONS[

            self.current_q
        ]


        correct_idx = q_data["answer"]


        selected_btn = self.buttons[

            selected_idx
        ]


        # ==========================================================================
        # --- CORRETA ---
        # ==========================================================================

        if selected_idx == correct_idx:

            selected_btn.config(

                bg=COLOR_CORRECT,

                fg="#000000"
            )


            self.root.update()


            self.score += 100


            self.lbl_score.config(

                text=f"SCORE: {self.score}"
            )


            messagebox.showinfo(

                "Resposta Correta! 🎯",

                q_data["explanations"][

                    selected_idx
                ]

                + "\n\n"

                + q_data["tip"]

                + "\n\n"

                + "🏆 +100 PONTOS"
            )


        # ==========================================================================
        # --- INCORRETA ---
        # ==========================================================================

        else:

            selected_btn.config(

                bg=COLOR_INCORRECT,

                fg="#FFFFFF"
            )


            self.root.update()


            self.lives -= 1


            self.lbl_firewall.config(

                text=f"🛡️ FIREWALL: {'█ ' * self.lives}"
            )


            messagebox.showerror(

                "Resposta Incorreta! ⚠️",

                q_data["explanations"][

                    selected_idx
                ]

                + "\n\n"

                + q_data["tip"]
            )


            # ------------------------------------------------------------------
            # GAME OVER
            # ------------------------------------------------------------------

            if self.lives == 0:

                messagebox.showerror(

                    "GAME OVER 💀",

                    "O firewall caiu!\n\n"

                    "Você não conseguiu identificar "
                    "corretamente o comportamento suspeito.\n\n"

                    "Revise os conceitos de SOC "
                    "e tente novamente."
                )


                self.root.destroy()

                return


        # ----------------------------------------------------------------------
        # PRÓXIMA QUESTÃO
        # ----------------------------------------------------------------------

        self.current_q += 1


        self.load_question()


    # ==========================================================================
    # --- TELA DE TRANSIÇÃO PARA O BOSS ---
    # ==========================================================================

    def show_boss_transition(self):

        # ----------------------------------------------------------------------
        # ESCONDER A INTERFACE DA FASE 9
        # ----------------------------------------------------------------------

        for widget in self.root.winfo_children():

            widget.destroy()


        # ----------------------------------------------------------------------
        # NOVA TELA
        # ----------------------------------------------------------------------

        self.boss_canvas = tk.Canvas(

            self.root,

            width=660,

            height=560,

            bg=COLOR_BOSS_BG,

            highlightthickness=0
        )

        self.boss_canvas.pack(

            fill="both",

            expand=True
        )


        # ----------------------------------------------------------------------
        # FUNDO VERMELHO ESCURO
        # ----------------------------------------------------------------------

        for y in range(560):

            intensity = int(

                5 +
                25 *
                (y / 560)
            )


            color = (

                f"#{intensity:02x}"
                "0000"
            )


            self.boss_canvas.create_line(

                0,

                y,

                660,

                y,

                fill=color
            )


        # ----------------------------------------------------------------------
        # LINHAS DE ALERTA
        # ----------------------------------------------------------------------

        for y in range(

            80,

            520,

            45
        ):

            self.boss_canvas.create_line(

                0,

                y,

                660,

                y,

                fill="#240006",

                width=1
            )


        # ----------------------------------------------------------------------
        # TÍTULO
        # ----------------------------------------------------------------------

        self.boss_title = self.boss_canvas.create_text(

            330,

            60,

            text="⚠  ALERTA CRÍTICO  ⚠",

            font=("Consolas", 25, "bold"),

            fill=COLOR_BOSS_RED
        )


        # ----------------------------------------------------------------------
        # STATUS
        # ----------------------------------------------------------------------

        self.boss_canvas.create_text(

            330,

            105,

            text="SECURITY BREACH DETECTED",

            font=("Consolas", 16, "bold"),

            fill=COLOR_BOSS_TEXT
        )


        # ----------------------------------------------------------------------
        # LINHA
        # ----------------------------------------------------------------------

        self.boss_canvas.create_line(

            70,

            130,

            590,

            130,

            fill=COLOR_BOSS_RED_DARK,

            width=2
        )


        # ----------------------------------------------------------------------
        # NÍVEL DE AMEAÇA
        # ----------------------------------------------------------------------

        self.boss_canvas.create_text(

            330,

            170,

            text="NÍVEL DE AMEAÇA",

            font=("Consolas", 12, "bold"),

            fill=COLOR_BOSS_MUTED
        )


        self.boss_canvas.create_text(

            330,

            205,

            text="EXTREMO",

            font=("Consolas", 27, "bold"),

            fill=COLOR_BOSS_RED
        )


        # ----------------------------------------------------------------------
        # BARRA DE AMEAÇA
        # ----------------------------------------------------------------------

        self.boss_canvas.create_rectangle(

            80,

            235,

            580,

            255,

            outline=COLOR_BOSS_RED_DARK,

            width=2
        )


        self.boss_canvas.create_rectangle(

            84,

            239,

            576,

            251,

            fill=COLOR_BOSS_RED,

            outline=""
        )


        # ----------------------------------------------------------------------
        # STATUS DO SISTEMA
        # ----------------------------------------------------------------------

        self.boss_canvas.create_text(

            330,

            290,

            text=(
                "🔴 SISTEMA: SOB AMEAÇA\n"
                "🔴 FIREWALL: SOB PRESSÃO\n"
                "🔴 INCIDENTE: NÃO CONTIDO"
            ),

            font=("Consolas", 12, "bold"),

            fill=COLOR_BOSS_MUTED,

            justify="center"
        )


        # ----------------------------------------------------------------------
        # MENSAGEM PRINCIPAL
        # ----------------------------------------------------------------------

        self.boss_canvas.create_text(

            330,

            375,

            text=(
                "VOCÊ CHEGOU AO PONTO CRÍTICO.\n\n"
                "A próxima operação será diferente.\n"
                "Cada decisão poderá determinar o destino\n"
                "de todo o sistema."
            ),

            font=("Segoe UI", 11, "bold"),

            fill=COLOR_BOSS_TEXT,

            justify="center"
        )


        # ----------------------------------------------------------------------
        # AVISO BOSS
        # ----------------------------------------------------------------------

        self.boss_canvas.create_text(

            330,

            455,

            text="⚠  FASE 10 — BOSS INCOMING  ⚠",

            font=("Consolas", 18, "bold"),

            fill=COLOR_BOSS_RED
        )


        # ----------------------------------------------------------------------
        # SCORE
        # ----------------------------------------------------------------------

        self.boss_canvas.create_text(

            330,

            485,

            text=f"SCORE ATUAL: {self.score}",

            font=("Consolas", 11, "bold"),

            fill=COLOR_BOSS_MUTED
        )


        # ----------------------------------------------------------------------
        # BOTÃO
        # ----------------------------------------------------------------------

        self.boss_button = tk.Button(

            self.root,

            text="⚠  ENTRAR NO BOSS  ⚠",

            font=("Consolas", 12, "bold"),

            bg=COLOR_BOSS_RED_DARK,

            fg=COLOR_BOSS_TEXT,

            activebackground=COLOR_BOSS_RED,

            activeforeground="#FFFFFF",

            relief="flat",

            cursor="hand2",

            bd=2,

            highlightbackground=COLOR_BOSS_RED,

            highlightcolor=COLOR_BOSS_RED,

            command=self.enter_boss
        )


        self.boss_button.place(

            x=220,

            y=510,

            width=220,

            height=38
        )


        # ----------------------------------------------------------------------
        # EFEITO PISCANTE DO ALERTA
        # ----------------------------------------------------------------------

        self.boss_flash_state = False

        self.animate_boss_alert()


    # ==========================================================================
    # --- ANIMAÇÃO DO ALERTA ---
    # ==========================================================================

    def animate_boss_alert(self):

        if not self.root.winfo_exists():

            return


        if self.boss_flash_state:

            self.boss_canvas.itemconfig(

                self.boss_title,

                fill="#660010"
            )

        else:

            self.boss_canvas.itemconfig(

                self.boss_title,

                fill=COLOR_BOSS_RED
            )


        self.boss_flash_state = not self.boss_flash_state


        self.root.after(

            500,

            self.animate_boss_alert
        )


    # ==========================================================================
    # --- ENTRAR NO BOSS ---
    # ==========================================================================

    def enter_boss(self):

        messagebox.showwarning(

            "🔴 FASE 10 — BOSS",

            "CONEXÃO ESTABELECIDA.\n\n"

            "O próximo desafio será iniciado.\n\n"

            "Prepare-se para tomar decisões críticas."
        )


        # ----------------------------------------------------------------------
        # Aqui você poderá chamar a Fase 10.
        #
        # Por enquanto, fechamos a Fase 9.
        # ----------------------------------------------------------------------

        self.root.destroy()


# ==============================================================================
# --- EXECUÇÃO ---
# ==============================================================================

if __name__ == "__main__":

    root = tk.Tk()

    app = CyberQuizApp(root)

    root.mainloop()
