import tkinter as tk
from tkinter import messagebox


# ==============================================================================
# CYBERSHIELD: FASE 9 — SOC
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
# CORES DA TELA BOSS
# ==============================================================================

COLOR_BOSS_BG = "#050000"
COLOR_BOSS_RED = "#FF1744"
COLOR_BOSS_RED_DARK = "#8B0000"
COLOR_BOSS_TEXT = "#FFFFFF"
COLOR_BOSS_MUTED = "#FF8A9B"


# ==============================================================================
# BANCO DE PERGUNTAS
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

        "options": [
            "O computador está definitivamente infectado",
            "O servidor está necessariamente desligado",
            "Existe um comportamento suspeito que merece investigação",
            "O usuário esqueceu a senha"
        ],

        "answer": 2,

        "explanations": [

            (
                "❌ RESPOSTA INCORRETA\n\n"
                "Não existem evidências suficientes para afirmar que o computador "
                "está definitivamente infectado.\n\n"
                "Os eventos indicam uma possível atividade suspeita, mas ainda "
                "é necessária uma investigação para determinar o que realmente aconteceu."
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
                "suspeito sem afirmar prematuramente que ocorreu uma invasão ou uma infecção."
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
# CLASSE PRINCIPAL — FASE 9
# ==============================================================================

class CyberQuizApp:

    def __init__(self, root, proxima_fase):

        self.root = root
        self.proxima_fase = proxima_fase

        self.root.title("CyberShield: Fase 9 — SOC")

        self.root.geometry("660x560")

        self.root.minsize(
            660,
            560
        )

        self.root.resizable(
            True,
            True
        )


        # ==========================================================================
        # TELA CHEIA
        # ==========================================================================

        self.fullscreen = False

        self.root.bind(
            "<F11>",
            self.toggle_fullscreen
        )

        self.root.bind(
            "<Escape>",
            self.exit_fullscreen
        )


        self.current_q = 0
        self.lives = 3
        self.score = 0


        # Guarda a referência da animação do alerta Boss

        self.anim_job = None


        # Controle para impedir avanço duplicado

        self.phase_finished = False


        # Evita redesenhar excessivamente

        self.resize_job = None


        self.setup_ui()

        self.load_question()


        # Atualiza o layout quando a janela mudar de tamanho

        self.root.bind(
            "<Configure>",
            self.on_window_resize
        )


    # ==========================================================================
    # TELA CHEIA
    # ==========================================================================

    def toggle_fullscreen(self, event=None):

        self.fullscreen = not self.fullscreen

        self.root.attributes(
            "-fullscreen",
            self.fullscreen
        )

        if self.fullscreen:

            self.btn_fullscreen.config(
                text="🗗 SAIR DA TELA CHEIA"
            )

        else:

            self.btn_fullscreen.config(
                text="⛶ TELA CHEIA"
            )

        self.root.update_idletasks()

        self.update_layout()

        return "break"


    def exit_fullscreen(self, event=None):

        if self.fullscreen:

            self.fullscreen = False

            self.root.attributes(
                "-fullscreen",
                False
            )

            self.btn_fullscreen.config(
                text="⛶ TELA CHEIA"
            )

            self.root.update_idletasks()

            self.update_layout()

        return "break"


    # ==========================================================================
    # REDIMENSIONAMENTO
    # ==========================================================================

    def on_window_resize(self, event=None):

        if event is not None:

            if event.widget != self.root:
                return


        if self.resize_job:

            try:

                self.root.after_cancel(
                    self.resize_job
                )

            except Exception:

                pass


        self.resize_job = self.root.after(
            50,
            self.update_layout
        )


    # ==========================================================================
    # ATUALIZAR LAYOUT
    # ==========================================================================

    def update_layout(self):

        self.resize_job = None

        width = self.root.winfo_width()
        height = self.root.winfo_height()


        if width < 1 or height < 1:
            return


        # ==========================================================================
        # TELA NORMAL / QUIZ
        # ==========================================================================

        if not self.phase_finished:

            self.draw_cyber_background(
                width,
                height
            )


            # ----------------------------------------------------------------------
            # HEADER
            # ----------------------------------------------------------------------

            header_width = max(
                500,
                int(width * 0.94)
            )

            self.bg_canvas.coords(
                self.header_window,
                width / 2,
                max(
                    35,
                    height * 0.055
                )
            )

            self.bg_canvas.itemconfig(
                self.header_window,
                width=header_width
            )


            # ----------------------------------------------------------------------
            # CARD
            # ----------------------------------------------------------------------

            card_width = min(
                int(width * 0.92),
                1200
            )

            card_height = min(
                int(height * 0.78),
                720
            )


            card_width = max(
                card_width,
                620
            )

            card_height = max(
                card_height,
                430
            )


            card_width = min(
                card_width,
                width - 30
            )

            card_height = min(
                card_height,
                height - 100
            )


            card_y = height * 0.54


            self.bg_canvas.coords(
                self.card_window,
                width / 2,
                card_y
            )

            self.bg_canvas.itemconfig(
                self.card_window,
                width=card_width,
                height=card_height
            )


            # ----------------------------------------------------------------------
            # TEXTO DA PERGUNTA
            # ----------------------------------------------------------------------

            question_wrap = max(
                500,
                card_width - 60
            )

            self.lbl_question.config(
                wraplength=question_wrap
            )


            # ----------------------------------------------------------------------
            # BOTÕES
            # ----------------------------------------------------------------------

            self.btn_frame.pack_configure(
                padx=max(
                    20,
                    int(card_width * 0.03)
                )
            )


        # ==========================================================================
        # TELA BOSS
        # ==========================================================================

        else:

            if hasattr(
                self,
                "boss_canvas"
            ):

                self.draw_boss_background(
                    width,
                    height
                )

                self.update_boss_layout(
                    width,
                    height
                )


    # ==========================================================================
    # INTERFACE
    # ==========================================================================

    def setup_ui(self):

        self.bg_canvas = tk.Canvas(
            self.root,
            highlightthickness=0,
            bd=0
        )

        self.bg_canvas.pack(
            fill="both",
            expand=True
        )


        # ==========================================================================
        # HEADER
        # ==========================================================================

        self.status_frame = tk.Frame(
            self.bg_canvas,
            bg=COLOR_BG_TOP
        )


        self.header_window = self.bg_canvas.create_window(
            330,
            35,
            window=self.status_frame,
            width=620
        )


        # ----------------------------------------------------------------------
        # NOME DA FASE
        # ----------------------------------------------------------------------

        self.lbl_phase = tk.Label(
            self.status_frame,
            text="🔴 FASE 9 — SOC",
            font=("Consolas", 12, "bold"),
            fg=COLOR_HEALTH,
            bg=COLOR_BG_TOP
        )

        self.lbl_phase.pack(
            side="left"
        )


        # ==========================================================================
        # BOTÃO TELA CHEIA
        # ==========================================================================

        self.btn_fullscreen = tk.Button(
            self.status_frame,
            text="⛶ TELA CHEIA",
            font=("Consolas", 9, "bold"),
            bg=COLOR_BTN_BG,
            fg=COLOR_TEXT_MUTED,
            activebackground=COLOR_BTN_HOVER,
            activeforeground=COLOR_TEXT_MAIN,
            relief="flat",
            bd=0,
            cursor="hand2",
            command=self.toggle_fullscreen
        )

        self.btn_fullscreen.pack(
            side="right",
            padx=(10, 0)
        )


        self.btn_fullscreen.bind(
            "<Enter>",
            lambda e:
            self.btn_fullscreen.config(
                bg=COLOR_BTN_HOVER,
                fg=COLOR_TEXT_MAIN
            )
        )


        self.btn_fullscreen.bind(
            "<Leave>",
            lambda e:
            self.btn_fullscreen.config(
                bg=COLOR_BTN_BG,
                fg=COLOR_TEXT_MUTED
            )
        )


        # ==========================================================================
        # FIREWALL
        # ==========================================================================

        self.lbl_firewall = tk.Label(
            self.status_frame,
            text=f"🛡️ FIREWALL: {'█ ' * self.lives}",
            font=("Consolas", 12, "bold"),
            fg=COLOR_HEALTH,
            bg=COLOR_BG_TOP
        )

        self.lbl_firewall.pack(
            side="right"
        )


        # ==========================================================================
        # SCORE
        # ==========================================================================

        self.lbl_score = tk.Label(
            self.status_frame,
            text=f"SCORE: {self.score}",
            font=("Consolas", 12, "bold"),
            fg=COLOR_CYAN_GLOW,
            bg=COLOR_BG_TOP
        )

        self.lbl_score.pack(
            side="right",
            padx=20
        )


        # ==========================================================================
        # CARD PRINCIPAL
        # ==========================================================================

        self.card_frame = tk.Frame(
            self.bg_canvas,
            bg=COLOR_CARD_BG,
            highlightbackground=COLOR_CARD_BORDER,
            highlightthickness=2,
            bd=0
        )


        self.card_window = self.bg_canvas.create_window(
            330,
            290,
            window=self.card_frame,
            width=620,
            height=430
        )


        # ==========================================================================
        # CATEGORIA
        # ==========================================================================

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


        # ==========================================================================
        # PERGUNTA
        # ==========================================================================

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


        # ==========================================================================
        # ÁREA DOS BOTÕES
        # ==========================================================================

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


            self.buttons.append(btn)


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
    # FUNDO CYBER RESPONSIVO
    # ==========================================================================

    def draw_cyber_background(
        self,
        width=None,
        height=None
    ):

        if width is None:

            width = max(
                self.root.winfo_width(),
                660
            )


        if height is None:

            height = max(
                self.root.winfo_height(),
                560
            )


        self.bg_canvas.delete(
            "background"
        )


        # ----------------------------------------------------------------------
        # GRADIENTE
        # ----------------------------------------------------------------------

        r1, g1, b1 = self.hex_to_rgb(
            COLOR_BG_TOP
        )

        r2, g2, b2 = self.hex_to_rgb(
            COLOR_BG_BOTTOM
        )


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


            color = (
                f"#{r:02x}{g:02x}{b:02x}"
            )


            self.bg_canvas.create_line(
                0,
                y,
                width,
                y,
                fill=color,
                tags="background"
            )


        # ----------------------------------------------------------------------
        # CIRCUITOS RESPONSIVOS
        # ----------------------------------------------------------------------

        line_color = "#0B3254"
        glow_dot = COLOR_CYAN_GLOW


        # Circuito superior

        x1 = int(width * 0.04)
        x2 = int(width * 0.27)
        x3 = int(width * 0.35)
        x4 = int(width * 0.65)

        y1 = int(height * 0.045)
        y2 = int(height * 0.09)


        self.bg_canvas.create_line(
            x1,
            y1,
            x2,
            y1,
            x3,
            y2,
            x4,
            y2,
            fill=line_color,
            width=2,
            tags="background"
        )


        self.bg_canvas.create_oval(
            x2 - 3,
            y1 - 3,
            x2 + 3,
            y1 + 3,
            fill=glow_dot,
            outline="",
            tags="background"
        )


        self.bg_canvas.create_oval(
            x4 - 3,
            y2 - 3,
            x4 + 3,
            y2 + 3,
            fill=glow_dot,
            outline="",
            tags="background"
        )


        # ----------------------------------------------------------------------
        # CIRCUITO INFERIOR
        # ----------------------------------------------------------------------

        y3 = int(height * 0.94)
        y4 = int(height * 0.91)

        x5 = int(width * 0.06)
        x6 = int(width * 0.25)
        x7 = int(width * 0.32)
        x8 = int(width * 0.72)


        self.bg_canvas.create_line(
            x5,
            y3,
            x6,
            y3,
            x7,
            y4,
            x8,
            y4,
            fill=line_color,
            width=2,
            tags="background"
        )


        self.bg_canvas.create_oval(
            x7 - 3,
            y4 - 3,
            x7 + 3,
            y4 + 3,
            fill=glow_dot,
            outline="",
            tags="background"
        )


        self.bg_canvas.create_oval(
            x8 - 3,
            y4 - 3,
            x8 + 3,
            y4 + 3,
            fill=glow_dot,
            outline="",
            tags="background"
        )


        self.bg_canvas.tag_lower(
            "background"
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
    # CARREGAR PERGUNTA
    # ==========================================================================

    def load_question(self):

        if self.current_q < len(QUESTIONS):

            q_data = QUESTIONS[
                self.current_q
            ]


            self.lbl_category.config(
                text=q_data["category"]
            )


            self.lbl_question.config(
                text=q_data["question"]
            )


            num_options = len(
                q_data["options"]
            )


            for i in range(4):

                if i < num_options:

                    self.buttons[i].config(
                        text=(
                            f"[ {chr(65 + i)} ]   "
                            f"{q_data['options'][i]}"
                        ),
                        bg=COLOR_BTN_BG,
                        fg=COLOR_TEXT_MUTED,
                        state="normal",
                        cursor="hand2"
                    )


                    self.buttons[i].pack(
                        fill="x",
                        pady=5,
                        ipady=3
                    )

                else:

                    self.buttons[i].pack_forget()


        else:

            self.show_boss_transition()


    # ==========================================================================
    # VERIFICAR RESPOSTA
    # ==========================================================================

    def check_answer(
        self,
        selected_idx
    ):

        if self.phase_finished:
            return


        for btn in self.buttons:

            btn.config(
                state="disabled",
                cursor="arrow"
            )


        q_data = QUESTIONS[
            self.current_q
        ]


        correct_idx = q_data[
            "answer"
        ]


        selected_btn = self.buttons[
            selected_idx
        ]


        # ==========================================================================
        # RESPOSTA CORRETA
        # ==========================================================================

        if selected_idx == correct_idx:

            selected_btn.config(
                bg=COLOR_CORRECT,
                fg="#000000"
            )


            self.score += 100


            self.lbl_score.config(
                text=f"SCORE: {self.score}"
            )


            self.root.update_idletasks()


            messagebox.showinfo(
                "Resposta Correta! 🎯",

                f"{q_data['explanations'][selected_idx]}\n\n"
                f"{q_data['tip']}\n\n"
                f"🏆 +100 PONTOS",

                parent=self.root
            )


            self.current_q += 1

            self.load_question()

            return


        # ==========================================================================
        # RESPOSTA INCORRETA
        # ==========================================================================

        selected_btn.config(
            bg=COLOR_INCORRECT,
            fg="#FFFFFF"
        )


        self.lives -= 1


        self.lbl_firewall.config(
            text=f"🛡️ FIREWALL: {'█ ' * self.lives}"
        )


        self.root.update_idletasks()


        messagebox.showerror(
            "Resposta Incorreta! ⚠️",

            f"{q_data['explanations'][selected_idx]}\n\n"
            f"{q_data['tip']}",

            parent=self.root
        )


        # ==========================================================================
        # GAME OVER
        # ==========================================================================

        if self.lives <= 0:

            self.buttons[
                correct_idx
            ].config(
                bg=COLOR_CORRECT,
                fg="#000000"
            )


            self.root.update_idletasks()


            messagebox.showerror(
                "GAME OVER 💀",

                "O firewall caiu!\n\n"
                "Você não conseguiu identificar corretamente "
                "o comportamento suspeito.\n\n"
                "A fase será reiniciada.",

                parent=self.root
            )


            self.current_q = 0

            self.lives = 3

            self.score = 0


            self.lbl_firewall.config(
                text=f"🛡️ FIREWALL: {'█ ' * self.lives}"
            )


            self.lbl_score.config(
                text=f"SCORE: {self.score}"
            )


            self.load_question()

            return


        # ==========================================================================
        # PRÓXIMA QUESTÃO
        # ==========================================================================

        self.current_q += 1

        self.load_question()


    # ==========================================================================
    # TRANSIÇÃO PARA A FASE 10
    # ==========================================================================

    def show_boss_transition(self):

        self.phase_finished = True


        # ----------------------------------------------------------------------
        # REMOVE SOMENTE OS ELEMENTOS VISUAIS DO QUIZ
        # ----------------------------------------------------------------------

        self.bg_canvas.pack_forget()


        # ----------------------------------------------------------------------
        # CANVAS DO BOSS
        # ----------------------------------------------------------------------

        self.boss_canvas = tk.Canvas(
            self.root,
            bg=COLOR_BOSS_BG,
            highlightthickness=0
        )

        self.boss_canvas.pack(
            fill="both",
            expand=True
        )


        # ----------------------------------------------------------------------
        # ELEMENTOS DO BOSS
        # ----------------------------------------------------------------------

        self.boss_title = self.boss_canvas.create_text(
            330,
            60,
            text="⚠  ALERTA CRÍTICO  ⚠",
            font=("Consolas", 25, "bold"),
            fill=COLOR_BOSS_RED
        )


        self.boss_subtitle = self.boss_canvas.create_text(
            330,
            105,
            text="SECURITY BREACH DETECTED",
            font=("Consolas", 16, "bold"),
            fill=COLOR_BOSS_TEXT
        )


        self.boss_line = self.boss_canvas.create_line(
            70,
            130,
            590,
            130,
            fill=COLOR_BOSS_RED_DARK,
            width=2
        )


        self.boss_threat_label = self.boss_canvas.create_text(
            330,
            170,
            text="NÍVEL DE AMEAÇA",
            font=("Consolas", 12, "bold"),
            fill=COLOR_BOSS_MUTED
        )


        self.boss_threat = self.boss_canvas.create_text(
            330,
            205,
            text="EXTREMO",
            font=("Consolas", 27, "bold"),
            fill=COLOR_BOSS_RED
        )


        self.boss_bar_outline = self.boss_canvas.create_rectangle(
            80,
            235,
            580,
            255,
            outline=COLOR_BOSS_RED_DARK,
            width=2
        )


        self.boss_bar = self.boss_canvas.create_rectangle(
            84,
            239,
            576,
            251,
            fill=COLOR_BOSS_RED,
            outline=""
        )


        self.boss_status = self.boss_canvas.create_text(
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


        self.boss_transition_text = self.boss_canvas.create_text(
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


        self.boss_phase10 = self.boss_canvas.create_text(
            330,
            455,
            text="⚠  FASE 10 — BOSS INCOMING  ⚠",
            font=("Consolas", 18, "bold"),
            fill=COLOR_BOSS_RED
        )


        self.boss_score = self.boss_canvas.create_text(
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
            command=self.enter_boss
        )


        self.boss_button.place(
            x=220,
            y=510,
            width=220,
            height=38
        )


        # ----------------------------------------------------------------------
        # ANIMAÇÃO
        # ----------------------------------------------------------------------

        self.boss_flash_state = False

        self.animate_boss_alert()


        self.root.update_idletasks()

        self.update_layout()


    # ==========================================================================
    # FUNDO DA TELA BOSS
    # ==========================================================================

    def draw_boss_background(
        self,
        width,
        height
    ):

        self.boss_canvas.delete(
            "boss_background"
        )


        # ----------------------------------------------------------------------
        # FUNDO VERMELHO
        # ----------------------------------------------------------------------

        for y in range(height):

            intensity = int(
                5 + 25 * (y / max(height, 1))
            )


            self.boss_canvas.create_line(
                0,
                y,
                width,
                y,
                fill=f"#{intensity:02x}0000",
                tags="boss_background"
            )


        # ----------------------------------------------------------------------
        # LINHAS HORIZONTAIS
        # ----------------------------------------------------------------------

        step = max(
            30,
            int(height * 0.08)
        )


        for y in range(
            int(height * 0.14),
            int(height * 0.94),
            step
        ):

            self.boss_canvas.create_line(
                0,
                y,
                width,
                y,
                fill="#240006",
                width=1,
                tags="boss_background"
            )


        self.boss_canvas.tag_lower(
            "boss_background"
        )


    # ==========================================================================
    # ATUALIZAR TELA BOSS
    # ==========================================================================

    def update_boss_layout(
        self,
        width,
        height
    ):

        center_x = width / 2


        self.boss_canvas.coords(
            self.boss_title,
            center_x,
            height * 0.105
        )


        self.boss_canvas.coords(
            self.boss_subtitle,
            center_x,
            height * 0.18
        )


        self.boss_canvas.coords(
            self.boss_line,
            width * 0.10,
            height * 0.23,
            width * 0.90,
            height * 0.23
        )


        self.boss_canvas.coords(
            self.boss_threat_label,
            center_x,
            height * 0.30
        )


        self.boss_canvas.coords(
            self.boss_threat,
            center_x,
            height * 0.36
        )


        # ----------------------------------------------------------------------
        # BARRA
        # ----------------------------------------------------------------------

        bar_left = width * 0.12
        bar_right = width * 0.88

        bar_y1 = height * 0.42
        bar_y2 = height * 0.455


        self.boss_canvas.coords(
            self.boss_bar_outline,
            bar_left,
            bar_y1,
            bar_right,
            bar_y2
        )


        self.boss_canvas.coords(
            self.boss_bar,
            bar_left + 4,
            bar_y1 + 4,
            bar_right - 4,
            bar_y2 - 4
        )


        self.boss_canvas.coords(
            self.boss_status,
            center_x,
            height * 0.52
        )


        self.boss_canvas.coords(
            self.boss_transition_text,
            center_x,
            height * 0.66
        )


        self.boss_canvas.coords(
            self.boss_phase10,
            center_x,
            height * 0.81
        )


        self.boss_canvas.coords(
            self.boss_score,
            center_x,
            height * 0.865
        )


        # ----------------------------------------------------------------------
        # BOTÃO DO BOSS
        # ----------------------------------------------------------------------

        button_width = min(
            300,
            int(width * 0.32)
        )

        button_height = 42


        self.boss_button.place(
            x=(width - button_width) / 2,
            y=height * 0.91,
            width=button_width,
            height=button_height
        )


    # ==========================================================================
    # ANIMAÇÃO DO ALERTA
    # ==========================================================================

    def animate_boss_alert(self):

        if not self.phase_finished:
            return


        try:

            if not self.root.winfo_exists():

                return

        except tk.TclError:

            return


        new_color = (
            "#660010"
            if self.boss_flash_state
            else COLOR_BOSS_RED
        )


        self.boss_canvas.itemconfig(
            self.boss_title,
            fill=new_color
        )


        self.boss_flash_state = not self.boss_flash_state


        self.anim_job = self.root.after(
            500,
            self.animate_boss_alert
        )


    # ==========================================================================
    # ENTRAR NA FASE 10
    # ==========================================================================

    def enter_boss(self):

        # ----------------------------------------------------------------------
        # CANCELA A ANIMAÇÃO
        # ----------------------------------------------------------------------

        if self.anim_job is not None:

            try:

                self.root.after_cancel(
                    self.anim_job
                )

            except tk.TclError:

                pass


            self.anim_job = None


        # ----------------------------------------------------------------------
        # MENSAGEM
        # ----------------------------------------------------------------------

        messagebox.showwarning(
            "🔴 FASE 10 — BOSS",

            "CONEXÃO ESTABELECIDA.\n\n"
            "O próximo desafio será iniciado.\n\n"
            "Prepare-se para tomar decisões críticas.",

            parent=self.root
        )


        # ----------------------------------------------------------------------
        # NÃO DESTRÓI A JANELA
        #
        # O MAIN CONTROLA A PRÓXIMA FASE.
        # ----------------------------------------------------------------------

        self.proxima_fase()


# ==============================================================================
# FUNÇÃO EXECUTAR
# ==============================================================================

def executar(
    root,
    proxima_fase
):

    return CyberQuizApp(
        root,
        proxima_fase
    )


# ==============================================================================
# TESTE INDIVIDUAL
# ==============================================================================

if __name__ == "__main__":

    root = tk.Tk()

    executar(
        root,
        None
    )

    root.mainloop()