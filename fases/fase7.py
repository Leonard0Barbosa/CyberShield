import tkinter as tk
from tkinter import messagebox

# --- CONFIGURAÇÃO DE CORES (TEMA HACKER ÉTICO) ---
COLOR_BG = "#0B132B"         # Fundo azul bem escuro
COLOR_CARD = "#1C2541"       # Fundo da caixa da pergunta
COLOR_BTN = "#00B4D8"        # Botões (Azul Neon)
COLOR_TEXT = "#FFFFFF"       # Texto branco
COLOR_HEALTH = "#06D6A0"     # Barra de vida (Verde/Ciano)

# --- DADOS DO QUIZ (Questões da Fase 7) ---
QUESTIONS = [
    {
        "category": "A) FALHA DE AUTENTICAÇÃO ❌",
        "question": "O que a autenticação verifica em um sistema?",
        "options": [
            "O que o usuário pode fazer",
            "Quem é o usuário",
            "A criptografia dos dados",
            "A disponibilidade do sistema"
        ],
        "answer": 1
    },
    {
        "category": "B) FALHA DE CRIPTOGRAFIA ❌",
        "question": "Qual é o principal objetivo da criptografia em um banco de dados?",
        "options": [
            "Controlar quem pode acessar os dados",
            "Garantir que o sistema continue funcionando",
            "Proteger os dados, mas sem controlar quem pode acessá-los",
            "Verificar a identidade do usuário"
        ],
        "answer": 2
    },
    {
        "category": "C) FALHA DE AUTORIZAÇÃO / CONTROLE DE ACESSO ✅",
        "question": "O que acontece em uma falha de autorização/controle de acesso?",
        "options": [
            "O usuário foi autenticado, porém recebeu permissões que não deveria possuir",
            "O usuário não conseguiu fazer login no sistema",
            "O banco de dados foi apagado por falta de disponibilidade",
            "A senha do usuário era fraca e foi descoberta"
        ],
        "answer": 0
    },
    {
        "category": "D) FALHA DE DISPONIBILIDADE ❌",
        "question": "Em um cenário de falha de disponibilidade, qual é a situação do sistema?",
        "options": [
            "O sistema continua funcionando normalmente",
            "O problema está exclusivamente nas permissões de acesso",
            "O usuário recebe permissões incorretas",
            "O sistema deixa de funcionar ou fica inacessível"
        ],
        "answer": 3
    }
]

class CyberQuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("CyberShield: Fase 7 — Banco de Dados")
        self.root.geometry("650x550")
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
            font=("Helvetica", 12), 
            fg=COLOR_TEXT, 
            bg=COLOR_CARD, 
            wraplength=550, 
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
                font=("Helvetica", 10), 
                bg=COLOR_BTN, 
                fg="#000000", 
                activebackground="#48CAE4",
                relief="flat",
                cursor="hand2",
                command=lambda idx=i: self.check_answer(idx)
            )
            btn.pack(fill="x", pady=4)
            self.buttons.append(btn)

    def load_question(self):
        if self.current_q < len(QUESTIONS):
            q_data = QUESTIONS[self.current_q]
            self.lbl_category.config(text=q_data["category"])
            self.lbl_question.config(text=q_data["question"])
            
            for i, opt in enumerate(q_data["options"]):
                self.buttons[i].config(text=f"[ {chr(65+i)} ]  {opt}")
        else:
            messagebox.showinfo("Vitória!", f"Parabéns! Você concluiu a Fase 7 com sucesso!\nPontuação final: {self.score}\n\n💡 Dica lembrada: Autenticação responde 'quem é você?'. Autorização responde 'o que você pode fazer?'.")
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
                messagebox.showerror("Game Over", "O sistema foi comprometido! Tente novamente.")
                self.root.destroy()
                return

        self.current_q += 1
        self.load_question()

if __name__ == "__main__":
    root = tk.Tk()
    app = CyberQuizApp(root)
    root.mainloop()