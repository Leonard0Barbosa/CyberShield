import tkinter as tk
from tkinter import messagebox


# ==============================================================================
# CYBERSHIELD — FASE 8
# DESENVOLVIMENTO SEGURO
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
# PERGUNTA
# ==============================================================================

QUESTION = {
    "category": "🛠️ FASE 8 — DESENVOLVIMENTO SEGURO",

    "question": (
        "Durante o desenvolvimento de um sistema, "
        "foi identificada uma falha relacionada aos dados "
        "enviados pelos usuários.\n\n"
        "Qual medida é mais adequada para reduzir esse risco?"
    ),

    "options": [
        "Aumentar a velocidade do servidor",
        "Desativar o firewall",
        "Validar e tratar adequadamente as entradas",
        "Armazenar todos os dados em texto puro"
    ],

    "answer": 2
}


# ==============================================================================
# EXPLICAÇÕES
# ==============================================================================

EXPLANATIONS = {

    0: (
        "❌ Aumentar a velocidade do servidor\n\n"
        "Desempenho não corrige falhas de validação. "
        "Um servidor mais rápido continuará vulnerável "
        "se aceitar entradas maliciosas."
    ),

    1: (
        "❌ Desativar o firewall\n\n"
        "Desativar o firewall reduziria ainda mais a segurança "
        "e não corrige o problema relacionado à validação."
    ),

    2: (
        "✅ Validar e tratar adequadamente as entradas\n\n"
        "A validação e o tratamento adequado das entradas "
        "ajudam a impedir que dados maliciosos sejam aceitos "
        "pelo sistema."
    ),

    3: (
        "❌ Armazenar todos os dados em texto puro\n\n"
        "Isso aumenta o risco de exposição e vazamento "
        "de informações."
    )
}


# ==============================================================================
# CLASSE DA FASE 8
# ==============================================================================

class Fase8:

    def __init__(self, root, proxima_fase=None):

        self.root = root
        self.proxima_fase = proxima_fase

        self.lives = 3
        self.score = 0

        # Configuração da janela
        self.root.title("CyberShield — Fase 8")
        self.root.geometry("660x560")
        self.root.resizable(False, False)

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
        # BARRA SUPERIOR
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

        self.lbl_firewall.pack(side="left")


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

        self.lbl_score.pack(side="right")


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
            font=("Segoe UI", 12),
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
        # BOTÕES
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
                pady=6,
                ipady=4
            )


            btn.bind(
                "<Enter>",
                lambda event, b=btn:
                self.on_hover_enter(b)
            )

            btn.bind(
                "<Leave>",
                lambda event, b=btn:
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
    # FUNDO CYBER
    # ==========================================================================

    def draw_cyber_background(self):

        width = 660
        height = 560

        r1, g1, b1 = self.hex_to_rgb(COLOR_BG_TOP)
        r2, g2, b2 = self.hex_to_rgb(COLOR_BG_BOTTOM)

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
        # CIRCUITO SUPERIOR
        # ----------------------------------------------------------------------

        line_color = "#0B3254"

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
            fill=COLOR_CYAN_GLOW,
            outline=""
        )

        self.bg_canvas.create_oval(
            427,
            47,
            433,
            53,
            fill=COLOR_CYAN_GLOW,
            outline=""
        )


        # ----------------------------------------------------------------------
        # CIRCUITO INFERIOR
        # ----------------------------------------------------------------------

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
            fill=COLOR_CYAN_GLOW,
            outline=""
        )

        self.bg_canvas.create_oval(
            497,
            507,
            503,
            513,
            fill=COLOR_CYAN_GLOW,
            outline=""
        )


    # ==========================================================================
    # HEX PARA RGB
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

        self.lbl_category.config(
            text=QUESTION["category"]
        )

        self.lbl_question.config(
            text=QUESTION["question"]
        )

        for i, option in enumerate(QUESTION["options"]):

            self.buttons[i].config(
                text=f"[ {chr(65 + i)} ]   {option}",
                bg=COLOR_BTN_BG,
                fg=COLOR_TEXT_MUTED,
                state="normal"
            )


    # ==========================================================================
    # VERIFICAR RESPOSTA
    # ==========================================================================

    def check_answer(self, selected_idx):

        for btn in self.buttons:
            btn.config(state="disabled")


        correct_idx = QUESTION["answer"]

        selected_btn = self.buttons[selected_idx]


        # ======================================================================
        # CORRETA
        # ======================================================================

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
                EXPLANATIONS[selected_idx]
                + "\n\n+100 PTS"
            )


            # --------------------------------------------------------------
            # SE ESTIVER SENDO EXECUTADA PELO MAIN
            # --------------------------------------------------------------

            if self.proxima_fase is not None:

                self.proxima_fase()

            # --------------------------------------------------------------
            # SE ESTIVER SENDO EXECUTADA SOZINHA
            # --------------------------------------------------------------

            else:

                messagebox.showinfo(
                    "Fase 8 concluída!",
                    "🛡️ Desenvolvimento seguro concluído!\n\n"
                    "Você protegeu o sistema."
                )

                self.root.destroy()

            return


        # ======================================================================
        # INCORRETA
        # ======================================================================

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
            EXPLANATIONS[selected_idx]
        )


        # ======================================================================
        # GAME OVER
        # ======================================================================

        if self.lives <= 0:

            messagebox.showerror(
                "GAME OVER",
                "🚨 O firewall caiu!\n\n"
                "O sistema foi comprometido.\n\n"
                "Tente novamente."
            )

            self.root.destroy()

            return


        # ======================================================================
        # CONTINUA
        # ======================================================================

        for btn in self.buttons:

            btn.config(
                state="normal",
                bg=COLOR_BTN_BG,
                fg=COLOR_TEXT_MUTED
            )


# ==============================================================================
# FUNÇÃO USADA PELO MAIN
# ==============================================================================

def executar(root, proxima_fase):

    Fase8(
        root,
        proxima_fase
    )


# ==============================================================================
# TESTE DIRETO DA FASE 8
# ==============================================================================

if __name__ == "__main__":

    root = tk.Tk()

    app = Fase8(root)

    root.mainloop()
