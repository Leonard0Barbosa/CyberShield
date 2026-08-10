import tkinter as tk
from tkinter import messagebox

# --- CONFIGURAÇÃO DE CORES (TEMA HACKER ÉTICO) ---
COLOR_BG = "#0B132B"         # Fundo azul bem escuro
COLOR_CARD = "#1C2541"       # Fundo da caixa da pergunta
COLOR_BTN = "#00B4D8"        # Botões (Azul Neon)
COLOR_TEXT = "#FFFFFF"       # Texto branco
COLOR_HEALTH = "#06D6A0"     # Barra de vida (Verde/Ciano)

# --- DADOS DO QUIZ ---
QUESTIONS = [
    {
        "category": "🔒 SENHAS SEGURAS",
        "question": "Qual das alternativas abaixo representa uma senha forte?",
        "options": ["12345678", "admin2026", "K#9vP!x2$Lq", "senhasecreta"],
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
    }
]

class CyberQuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("CyberShield: Ethical Hacker Quiz")
        self.root.geometry("600x500")
        self.root.configure(bg=COLOR_BG)

        self.current_q = 0
        self.lives = 3
        self.score = 0

        self.setup_ui()
        self.load_question()

    def setup_ui(self):
        # Header / Status Bar
        self.status_frame = tk.Frame(self.root, bg=COLOR_BG)
        self.status_frame.pack(fill="x", padx=20, pady=15)

        self.lbl_firewall = tk.Label(
            self.status_frame, 
            text=f"🛡️ FIREWALL: {'█ ' * self.lives}", 
            font=("Consolas", 14, "bold"), 
            fg=COLOR_HEALTH, 
            bg=COLOR_BG
        )
        self.lbl_firewall.pack(side="left")

        self.lbl_score = tk.Label(
            self.status_frame, 
            text=f"SCORE: {self.score}", 
            font=("Consolas", 14, "bold"), 
            fg=COLOR_TEXT, 
            bg=COLOR_BG
        )
        self.lbl_score.pack(side="right")

        # Painel da Pergunta
        self.card_frame = tk.Frame(self.root, bg=COLOR_CARD, bd=2, relief="groove")
        self.card_frame.pack(fill="both", expand=True, padx=20, pady=10)

        self.lbl_category = tk.Label(
            self.card_frame, 
            text="", 
            font=("Helvetica", 11, "bold"), 
            fg=COLOR_BTN, 
            bg=COLOR_CARD
        )
        self.lbl_category.pack(anchor="w", padx=15, pady=(15, 5))

        self.lbl_question = tk.Label(
            self.card_frame, 
            text="", 
            font=("Helvetica", 13), 
            fg=COLOR_TEXT, 
            bg=COLOR_CARD, 
            wraplength=500, 
            justify="left"
        )
        self.lbl_question.pack(anchor="w", padx=15, pady=10)

        # Botões de Resposta
        self.btn_frame = tk.Frame(self.card_frame, bg=COLOR_CARD)
        self.btn_frame.pack(fill="x", padx=15, pady=15)

        self.buttons = []
        for i in range(4):
            btn = tk.Button(
                self.btn_frame, 
                text="", 
                font=("Helvetica", 11), 
                bg=COLOR_BTN, 
                fg="#000000", 
                activebackground="#48CAE4",
                relief="flat",
                cursor="hand2",
                command=lambda idx=i: self.check_answer(idx)
            )
            btn.pack(fill="x", pady=5)
            self.buttons.append(btn)

    def load_question(self):
        if self.current_q < len(QUESTIONS):
            q_data = QUESTIONS[self.current_q]
            self.lbl_category.config(text=q_data["category"])
            self.lbl_question.config(text=q_data["question"])
            
            for i, opt in enumerate(q_data["options"]):
                self.buttons[i].config(text=f"[ {chr(65+i)} ]  {opt}")
        else:
            messagebox.showinfo("Vitória!", f"Você protegeu o sistema!\nPontuação final: {self.score}")
            self.root.destroy()

    def check_answer(self, selected_idx):
        correct_idx = QUESTIONS[self.current_q]["answer"]

        if selected_idx == correct_idx:
            self.score += 100
            self.lbl_score.config(text=f"SCORE: {self.score}")
        else:
            self.lives -= 1
            self.lbl_firewall.config(text=f"🛡️ FIREWALL: {'█ ' * self.lives}")
            if self.lives == 0:
                messagebox.showerror("Game Over", "O sistema foi hackeado! Tente novamente.")
                self.root.destroy()
                return

        self.current_q += 1
        self.load_question()

if __name__ == "__main__":
    root = tk.Tk()
    app = CyberQuizApp(root)
    root.mainloop()