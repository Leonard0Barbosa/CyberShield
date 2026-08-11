import tkinter as tk
from tkinter import messagebox


# ============================================================
# TKINTER
# ============================================================
TKINTER_DISPONIVEL = True


# ============================================================
# CORES DO PROGRAMA
# ============================================================
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


# ============================================================
# PERGUNTAS DO QUIZ
# ============================================================
QUESTIONS = [
    {
        "category": "🔒 SENHAS SEGURAS",
        "question": "Qual das alternativas abaixo representa uma senha forte?",
        "options": [
            "12345678",
            "admin2026",
            "K#9vP!x2$Lq",
            "senhasecreta"
        ],
        "answer": 2
    },
    {
        "category": "✉️ PHISHING",
        "question": "Você recebe um e-mail urgente do seu banco pedindo para clicar num link. O que fazer?",
        "options": [
            "Clicar imediatamente",
            "Ignorar e verificar o remetente / canal oficial",
            "Encaminhar para todos os amigos",
            "Responder fornecendo sua senha"
        ],
        "answer": 1
    },
    {
        "category": "🔐 AUTENTICAÇÃO",
        "question": "Qual medida aumenta a segurança de uma conta?",
        "options": [
            "Usar a mesma senha em todos os sites",
            "Desativar a autenticação em dois fatores",
            "Ativar autenticação multifator",
            "Compartilhar a senha com amigos"
        ],
        "answer": 2
    },
    {
        "category": "🌐 NAVEGAÇÃO",
        "question": "Ao acessar um site desconhecido, qual atitude é mais segura?",
        "options": [
            "Baixar qualquer arquivo oferecido",
            "Verificar o endereço e a reputação do site",
            "Informar seus dados pessoais imediatamente",
            "Desativar o antivírus"
        ],
        "answer": 1
    },
    {
        "category": "🦠 MALWARE",
        "question": "O que é malware?",
        "options": [
            "Um programa criado para realizar ações maliciosas",
            "Um tipo de senha",
            "Um sistema operacional",
            "Um antivírus"
        ],
        "answer": 0
    },
    {
        "category": "💾 BACKUP",
        "question": "Qual é uma boa prática para proteger arquivos importantes?",
        "options": [
            "Nunca fazer backup",
            "Manter cópias de segurança atualizadas",
            "Salvar tudo apenas em um computador",
            "Compartilhar todos os arquivos publicamente"
        ],
        "answer": 1
    }
]


# ============================================================
# APLICAÇÃO DO QUIZ
# ============================================================
class CyberQuizApp:

    def __init__(self, root):
        self.root = root

        self.root.title("CyberShield: Ethical Hacker Quiz")
        self.root.resizable(False, False)

        self.window_width = 680
        self.window_height = 600

        # Centraliza a janela
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        position_x = int(
            (screen_width - self.window_width) / 2
        )

        position_y = int(
            (screen_height - self.window_height) / 2
        )

        self.root.geometry(
            f"{self.window_width}x{self.window_height}"
            f"+{position_x}+{position_y}"
        )

        self.current_q = 0
        self.lives = 3
        self.score = 0

        self.setup_ui()
        self.load_question()

    # ========================================================
    # INTERFACE
    # ========================================================
    def setup_ui(self):

        # Canvas de fundo
        self.bg_canvas = tk.Canvas(
            self.root,
            width=self.window_width,
            height=self.window_height,
            highlightthickness=0,
            bg=COLOR_BG_TOP
        )

        self.bg_canvas.pack(
            fill="both",
            expand=True
        )

        self.draw_cyber_background()

        # ====================================================
        # STATUS
        # ====================================================
        self.status_frame = tk.Frame(
            self.bg_canvas,
            bg=COLOR_BG_TOP
        )

        self.bg_canvas.create_window(
            self.window_width // 2,
            35,
            window=self.status_frame,
            width=640,
            height=50
        )

        self.lbl_firewall = tk.Label(
            self.status_frame,
            text=f"🛡️ FIREWALL: {'█ ' * self.lives}",
            font=("Consolas", 12, "bold"),
            fg=COLOR_HEALTH,
            bg=COLOR_BG_TOP
        )

        self.lbl_firewall.pack(
            side="left"
        )

        self.lbl_score = tk.Label(
            self.status_frame,
            text=f"SCORE: {self.score}",
            font=("Consolas", 12, "bold"),
            fg=COLOR_CYAN_GLOW,
            bg=COLOR_BG_TOP
        )

        self.lbl_score.pack(
            side="right"
        )

        # ====================================================
        # CARD PRINCIPAL
        # ====================================================
        self.card_frame = tk.Frame(
            self.bg_canvas,
            bg=COLOR_CARD_BG,
            highlightbackground=COLOR_CARD_BORDER,
            highlightthickness=2,
            bd=0
        )

        self.bg_canvas.create_window(
            self.window_width // 2,
            310,
            window=self.card_frame,
            width=640,
            height=470
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
            font=("Segoe UI", 11),
            fg=COLOR_TEXT_MAIN,
            bg=COLOR_CARD_BG,
            wraplength=580,
            justify="left"
        )

        self.lbl_question.pack(
            anchor="w",
            padx=20,
            pady=10
        )

        # Botões
        self.btn_frame = tk.Frame(
            self.card_frame,
            bg=COLOR_CARD_BG
        )

        self.btn_frame.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=(5, 15)
        )

        self.buttons = []

        for i in range(4):

            btn = tk.Button(
                self.btn_frame,
                text="",
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
                command=lambda idx=i: self.check_answer(idx)
            )

            btn.pack(
                fill="x",
                pady=5,
                ipady=4
            )

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

    # ========================================================
    # FUNDO CYBER
    # ========================================================
    def draw_cyber_background(self):

        width = self.window_width
        height = self.window_height

        r1, g1, b1 = self.hex_to_rgb(
            COLOR_BG_TOP
        )

        r2, g2, b2 = self.hex_to_rgb(
            COLOR_BG_BOTTOM
        )

        # Gradiente
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

        # Linhas de circuito
        line_color = "#0B3254"
        glow_dot = COLOR_CYAN_GLOW

        self.bg_canvas.create_line(
            30, 25,
            180, 25,
            230, 50,
            450, 50,
            fill=line_color,
            width=2
        )

        self.bg_canvas.create_oval(
            177, 22,
            183, 28,
            fill=glow_dot,
            outline=""
        )

        self.bg_canvas.create_oval(
            447, 47,
            453, 53,
            fill=glow_dot,
            outline=""
        )

        self.bg_canvas.create_line(
            50, 570,
            200, 570,
            250, 550,
            520, 550,
            fill=line_color,
            width=2
        )

        self.bg_canvas.create_oval(
            247, 547,
            253, 553,
            fill=glow_dot,
            outline=""
        )

    # ========================================================
    # CONVERTE HEX PARA RGB
    # ========================================================
    @staticmethod
    def hex_to_rgb(hex_str):

        hex_str = hex_str.lstrip("#")

        return tuple(
            int(hex_str[i:i + 2], 16)
            for i in (0, 2, 4)
        )

    # ========================================================
    # EFEITO DO MOUSE
    # ========================================================
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

    # ========================================================
    # CARREGA PERGUNTA
    # ========================================================
    def load_question(self):

        if self.current_q < len(QUESTIONS):

            q_data = QUESTIONS[self.current_q]

            self.lbl_category.config(
                text=q_data["category"]
            )

            self.lbl_question.config(
                text=q_data["question"]
            )

            for i, option in enumerate(
                q_data["options"]
            ):

                self.buttons[i].config(
                    text=f"[ {chr(65 + i)} ]  {option}",
                    bg=COLOR_BTN_BG,
                    fg=COLOR_TEXT_MUTED,
                    state="normal"
                )

        else:

            messagebox.showinfo(
                "Vitória! 🏆",
                "Você protegeu a rede com sucesso!\n\n"
                f"Pontuação Final: {self.score}"
            )

            self.root.destroy()

    # ========================================================
    # VERIFICA RESPOSTA
    # ========================================================
    def check_answer(self, selected_idx):

        correct_idx = QUESTIONS[
            self.current_q
        ]["answer"]

        # Desativa os botões
        for btn in self.buttons:

            btn.config(
                state="disabled"
            )

        # Resposta correta
        if selected_idx == correct_idx:

            self.score += 100

            self.lbl_score.config(
                text=f"SCORE: {self.score}"
            )

            self.buttons[selected_idx].config(
                bg=COLOR_CORRECT,
                fg="#000000"
            )

        # Resposta errada
        else:

            self.lives -= 1

            self.lbl_firewall.config(
                text=f"🛡️ FIREWALL: {'█ ' * self.lives}"
            )

            self.buttons[selected_idx].config(
                bg=COLOR_INCORRECT,
                fg=COLOR_TEXT_MAIN
            )

            self.buttons[correct_idx].config(
                bg=COLOR_CORRECT,
                fg="#000000"
            )

            # Game Over
            if self.lives == 0:

                self.root.after(
                    500,
                    self.game_over
                )

                return

        self.current_q += 1

        # Próxima pergunta
        self.root.after(
            1200,
            self.load_question
        )

    # ========================================================
    # GAME OVER
    # ========================================================
    def game_over(self):

        messagebox.showerror(
            "Game Over ⚠️",
            "O firewall caiu e o sistema foi comprometido!\n\n"
            f"Pontuação: {self.score}"
        )

        self.root.destroy()


# ============================================================
# INICIA DIRETAMENTE A JANELA
# ============================================================
def main():

    root = tk.Tk()

    CyberQuizApp(root)

    root.mainloop()


# ============================================================
# EXECUÇÃO
# ============================================================
if __name__ == "__main__":
    main()
