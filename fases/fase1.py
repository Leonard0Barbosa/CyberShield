import tkinter as tk
from tkinter import messagebox


# ==============================================================================
# CORES
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
# QUESTÕES DA FASE 1
# ==============================================================================

QUESTIONS = [
    {
        "category": "🛡️ PRINCÍPIOS DE SEGURANÇA",

        "question": (
            "Um arquivo importante foi alterado sem autorização. "
            "Qual princípio da segurança foi afetado?"
        ),

        "options": [
            "Disponibilidade",
            "Confidencialidade",
            "Integridade",
            "Autenticação"
        ],

        "answer": 2,

        "explanations": [
            (
                "❌ INCORRETO!\n\n"
                "A disponibilidade garante que o sistema esteja acessível. "
                "O arquivo continuou lá, porém alterado.\n\n"
                "💡 Dica: Falou em sistema fora do ar? "
                "Pense em Disponibilidade."
            ),

            (
                "❌ INCORRETO!\n\n"
                "A confidencialidade protege contra acesso não autorizado "
                "(vazamento). O foco aqui foi a alteração.\n\n"
                "💡 Dica: Apenas leu dados sem permissão? "
                "Pense em Confidencialidade."
            ),

            (
                "✅ CORRETO!\n\n"
                "A integridade garante que os dados permaneçam exatos, "
                "completos e sem alterações indevidas."
            ),

            (
                "❌ INCORRETO!\n\n"
                "A autenticação verifica a identidade de quem acessa, "
                "mas não o conteúdo do arquivo.\n\n"
                "💡 Dica: Confirmar quem é o usuário? "
                "Pense em Autenticação."
            )
        ]
    }
]


# ==============================================================================
# APLICAÇÃO DA FASE 1
# ==============================================================================

class CyberQuizApp:

    def __init__(self, root, proxima_fase=None):

        self.root = root
        self.proxima_fase = proxima_fase

        self.root.title("CyberShield: Fase 1")
        self.root.geometry("660x560")
        self.root.resizable(False, False)

        self.current_q = 0
        self.lives = 3
        self.score = 0

        # Evita chamar a próxima fase duas vezes
        self.finalizando = False

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
        # HEADER
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

        self.lbl_phase = tk.Label(
            self.status_frame,
            text="🛡️ FASE 1 — FUNDAMENTOS",
            font=("Consolas", 12, "bold"),
            fg=COLOR_HEALTH,
            bg=COLOR_BG_TOP
        )

        self.lbl_phase.pack(side="left")

        self.lbl_firewall = tk.Label(
            self.status_frame,
            text=f"🛡️ FIREWALL: {'█ ' * self.lives}",
            font=("Consolas", 13, "bold"),
            fg=COLOR_HEALTH,
            bg=COLOR_BG_TOP
        )

        self.lbl_firewall.pack(side="right")

        self.lbl_score = tk.Label(
            self.status_frame,
            text=f"SCORE: {self.score}",
            font=("Consolas", 13, "bold"),
            fg=COLOR_CYAN_GLOW,
            bg=COLOR_BG_TOP
        )

        self.lbl_score.pack(
            side="right",
            padx=20
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
        # PROGRESSO
        # ----------------------------------------------------------------------

        self.lbl_progress = tk.Label(
            self.card_frame,
            text="",
            font=("Consolas", 9, "bold"),
            fg=COLOR_TEXT_MUTED,
            bg=COLOR_CARD_BG
        )

        self.lbl_progress.pack(
            anchor="e",
            padx=20,
            pady=(12, 0)
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
            pady=(4, 5)
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
    # FUNDO
    # ==========================================================================

    def draw_cyber_background(self):

        width = 660
        height = 560

        r1, g1, b1 = self.hex_to_rgb(COLOR_BG_TOP)
        r2, g2, b2 = self.hex_to_rgb(COLOR_BG_BOTTOM)

        # ----------------------------------------------------------------------
        # DEGRADÊ
        # ----------------------------------------------------------------------

        for y in range(height):

            r = int(r1 + (r2 - r1) * (y / height))
            g = int(g1 + (g2 - g1) * (y / height))
            b = int(b1 + (b2 - b1) * (y / height))

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

    @staticmethod
    def hex_to_rgb(hex_str):

        hex_str = hex_str.lstrip("#")

        return tuple(
            int(hex_str[i:i + 2], 16)
            for i in (0, 2, 4)
        )

    # ==========================================================================
    # CARREGAR QUESTÃO
    # ==========================================================================

    def load_question(self):

        # Se acabaram as perguntas
        if self.current_q >= len(QUESTIONS):
            self.finalizar_fase()
            return

        q_data = QUESTIONS[self.current_q]

        self.lbl_progress.config(
            text=f"QUESTÃO {self.current_q + 1}/{len(QUESTIONS)}"
        )

        self.lbl_category.config(
            text=q_data["category"]
        )

        self.lbl_question.config(
            text=q_data["question"]
        )

        for i, option in enumerate(q_data["options"]):

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

        if self.finalizando:
            return

        # Desativa os botões para impedir duplo clique
        for btn in self.buttons:
            btn.config(state="disabled")

        q_data = QUESTIONS[self.current_q]

        correct_idx = q_data["answer"]

        explanation = q_data["explanations"][selected_idx]

        selected_btn = self.buttons[selected_idx]

        # ----------------------------------------------------------------------
        # ACERTO
        # ----------------------------------------------------------------------

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
                "Resposta Correta! ✅",
                f"Parabéns! Você acertou!\n\n{explanation}",
                parent=self.root
            )

        # ----------------------------------------------------------------------
        # ERRO
        # ----------------------------------------------------------------------

        else:

            selected_btn.config(
                bg=COLOR_INCORRECT,
                fg="#FFFFFF"
            )

            # Mostra também a resposta correta
            self.buttons[correct_idx].config(
                bg=COLOR_CORRECT,
                fg="#000000"
            )

            self.root.update()

            self.lives -= 1

            self.lbl_firewall.config(
                text=f"🛡️ FIREWALL: {'█ ' * self.lives}"
            )

            messagebox.showwarning(
                "Resposta Incorreta! ❌",
                explanation,
                parent=self.root
            )

            # ------------------------------------------------------------------
            # GAME OVER
            # ------------------------------------------------------------------

            if self.lives <= 0:

                messagebox.showerror(
                    "Game Over",
                    "O firewall caiu!\n\n"
                    "Você perdeu todas as vidas e não pode avançar.",
                    parent=self.root
                )

                # Aqui a fase pode ser encerrada.
                # O mainloop continua pertencendo ao main.py.
                self.root.destroy()

                return

        # ----------------------------------------------------------------------
        # PRÓXIMA QUESTÃO
        # ----------------------------------------------------------------------

        self.current_q += 1

        self.load_question()

    # ==========================================================================
    # FINALIZAR FASE
    # ==========================================================================

    def finalizar_fase(self):

        # Impede duplicação
        if self.finalizando:
            return

        self.finalizando = True

        messagebox.showinfo(
            "FASE 1 CONCLUÍDA! 🏆",
            "Excelente trabalho!\n\n"
            "Você concluiu os fundamentos de segurança "
            "da informação.\n\n"
            f"Pontuação da Fase 1: {self.score}\n\n"
            "Preparando a próxima fase...",
            parent=self.root
        )

        # ======================================================================
        # IMPORTANTE:
        #
        # NÃO usamos:
        #
        # self.root.destroy()
        #
        # porque quem controla a troca de janelas é o main.py.
        #
        # A próxima fase é chamada depois de 100ms para permitir que
        # a janela termine de processar a mensagem.
        # ======================================================================

        if self.proxima_fase:

            self.root.after(
                100,
                self.proxima_fase
            )

        else:

            # Caso queira executar a Fase 1 sozinha
            messagebox.showinfo(
                "Fim",
                "A Fase 1 foi concluída!",
                parent=self.root
            )


# ==============================================================================
# FUNÇÃO USADA PELO MAIN.PY
# ==============================================================================

def executar(root, proxima_fase=None):

    return CyberQuizApp(
        root,
        proxima_fase
    )


# ==============================================================================
# TESTE INDIVIDUAL
# ==============================================================================

if __name__ == "__main__":

    root = tk.Tk()

    executar(root)

    root.mainloop()