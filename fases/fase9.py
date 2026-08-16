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
        self.root.resizable(False, False)

        self.current_q = 0
        self.lives = 3
        self.score = 0

        # Guarda a referência da animação do alerta Boss
        self.anim_job = None

        # Controle para impedir avanço duplicado
        self.phase_finished = False

        self.setup_ui()
        self.load_question()


    # ==========================================================================
    # INTERFACE
    # ==========================================================================

    def setup_ui(self):

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
        # STATUS BAR
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


        # Firewall

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


        # Score

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
        # CARD PRINCIPAL
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


        # Categoria

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


        # Pergunta

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


        # Área dos botões

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
                command=lambda idx=i: self.check_answer(idx)
            )

            btn.pack(
                fill="x",
                pady=5,
                ipady=3
            )


            btn.bind(
                "<Enter>",
                lambda e, b=btn: self.on_hover_enter(b)
            )

            btn.bind(
                "<Leave>",
                lambda e, b=btn: self.on_hover_leave(b)
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
    # FUNDO CYBER
    # ==========================================================================

    def draw_cyber_background(self):

        width = 660
        height = 560

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

            self.bg_canvas.create_line(
                0,
                y,
                width,
                y,
                fill=f"#{r:02x}{g:02x}{b:02x}"
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
    # HEX → RGB
    # ==========================================================================

    @staticmethod
    def hex_to_rgb(hex_str):

        hex_str = hex_str.lstrip("#")

        return tuple(
            int(hex_str[i:i + 2], 16)
            for i in (0, 2, 4)
        )


    # ==========================================================================
    # CARREGAR PERGUNTA
    # ==========================================================================

    def load_question(self):

        if self.current_q < len(QUESTIONS):

            q_data = QUESTIONS[self.current_q]

            self.lbl_category.config(
                text=q_data["category"]
            )

            self.lbl_question.config(
                text=q_data["question"]
            )


            # ------------------------------------------------------------------
            # GERENCIA DINAMICAMENTE A QUANTIDADE DE OPÇÕES
            # ------------------------------------------------------------------

            num_options = len(
                q_data["options"]
            )


            for i in range(4):

                if i < num_options:

                    self.buttons[i].config(
                        text=f"[ {chr(65 + i)} ]   {q_data['options'][i]}",
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

    def check_answer(self, selected_idx):

        if self.phase_finished:
            return


        # Desativa os botões enquanto a resposta é analisada

        for btn in self.buttons:

            btn.config(
                state="disabled",
                cursor="arrow"
            )


        q_data = QUESTIONS[self.current_q]

        correct_idx = q_data["answer"]

        selected_btn = self.buttons[selected_idx]


        # ----------------------------------------------------------------------
        # RESPOSTA CORRETA
        # ----------------------------------------------------------------------

        if selected_idx == correct_idx:

            selected_btn.config(
                bg=COLOR_CORRECT,
                fg="#000000"
            )

            self.score += 100

            self.lbl_score.config(
                text=f"SCORE: {self.score}"
            )


            # Garante que o botão fique verde antes da mensagem

            self.root.update_idletasks()


            messagebox.showinfo(
                "Resposta Correta! 🎯",

                f"{q_data['explanations'][selected_idx]}\n\n"
                f"{q_data['tip']}\n\n"
                f"🏆 +100 PONTOS"
            )


            self.current_q += 1

            self.load_question()

            return


        # ----------------------------------------------------------------------
        # RESPOSTA INCORRETA
        # ----------------------------------------------------------------------

        selected_btn.config(
            bg=COLOR_INCORRECT,
            fg="#FFFFFF"
        )


        self.lives -= 1


        self.lbl_firewall.config(
            text=f"🛡️ FIREWALL: {'█ ' * self.lives}"
        )


        # Garante que o botão fique vermelho antes da mensagem

        self.root.update_idletasks()


        messagebox.showerror(
            "Resposta Incorreta! ⚠️",

            f"{q_data['explanations'][selected_idx]}\n\n"
            f"{q_data['tip']}"
        )


        # ----------------------------------------------------------------------
        # GAME OVER
        # ----------------------------------------------------------------------

        if self.lives <= 0:

            # Mostra a resposta correta

            self.buttons[correct_idx].config(
                bg=COLOR_CORRECT,
                fg="#000000"
            )

            self.root.update_idletasks()


            messagebox.showerror(
                "GAME OVER 💀",

                "O firewall caiu!\n\n"
                "Você não conseguiu identificar corretamente "
                "o comportamento suspeito.\n\n"
                "A fase será reiniciada."
            )


            # --------------------------------------------------------------
            # Reinicia a fase sem destruir a janela
            # --------------------------------------------------------------

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


        # ----------------------------------------------------------------------
        # CASO TENHA PERDIDO UMA VIDA, CARREGA A PRÓXIMA QUESTÃO
        # ----------------------------------------------------------------------

        self.current_q += 1

        self.load_question()


    # ==========================================================================
    # TRANSIÇÃO PARA A FASE 10
    # ==========================================================================

    def show_boss_transition(self):

        self.phase_finished = True


        # ----------------------------------------------------------------------
        # LIMPA A INTERFACE ATUAL
        # ----------------------------------------------------------------------

        for widget in self.root.winfo_children():

            widget.destroy()


        # ----------------------------------------------------------------------
        # CANVAS DO BOSS
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
        # FUNDO VERMELHO
        # ----------------------------------------------------------------------

        for y in range(560):

            intensity = int(
                5 + 25 * (y / 560)
            )

            self.boss_canvas.create_line(
                0,
                y,
                660,
                y,
                fill=f"#{intensity:02x}0000"
            )


        # Linhas horizontais

        for y in range(80, 520, 45):

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
        # SUBTÍTULO
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
        # STATUS
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
        # TEXTO DE TRANSIÇÃO
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
        # FASE 10
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


    # ==========================================================================
    # ANIMAÇÃO DO ALERTA
    # ==========================================================================

    def animate_boss_alert(self):

        # Não continua se a fase já estiver sendo encerrada

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
        # MENSAGEM DE TRANSIÇÃO
        # ----------------------------------------------------------------------

        messagebox.showwarning(
            "🔴 FASE 10 — BOSS",

            "CONEXÃO ESTABELECIDA.\n\n"
            "O próximo desafio será iniciado.\n\n"
            "Prepare-se para tomar decisões críticas."
        )


        # ----------------------------------------------------------------------
        # NÃO DESTRÓI A JANELA
        #
        # O MAIN controla a próxima fase.
        # ----------------------------------------------------------------------

        self.proxima_fase()


# ==============================================================================
# FUNÇÃO EXECUTAR
# ==============================================================================

def executar(root, proxima_fase):

    CyberQuizApp(
        root,
        proxima_fase
    )