import tkinter as tk
from tkinter import messagebox

# --- CONFIGURAÇÃO DE CORES (TEMA HACKER ÉTICO) ---
COLOR_BG = "#0B132B"         # Fundo azul bem escuro
COLOR_CARD = "#1C2541"       # Fundo da caixa da pergunta
COLOR_BTN = "#00B4D8"        # Botões (Azul Neon)
COLOR_TEXT = "#FFFFFF"       # Texto branco
COLOR_HEALTH = "#06D6A0"     # Barra de vida (Verde/Ciano)

# --- DADOS DO QUIZ (FASE 4: INTERNET E LINKS) ---
QUESTIONS = [
    {
        "category": "🌐 INTERNET E LINKS (Fase 4 - Nível 1)",
        "question": "Qual sinal indica a maior probabilidade de um site ser uma tentativa de golpe?",
        "options": [
            "Site usando protocolo HTTPS com cadeado",
            "Site carregando imagens lentamente",
            "Domínio ligeiramente diferente do site oficial da empresa",
            "Site contendo muitas imagens e animações"
        ],
        "answer": 2,
        "explanations": [
            "A) O HTTPS apenas criptografa o tráfego. Golpistas também obtêm certificados SSL gratuitos para sites falsos.\n\n💡 Dica: HTTPS garante conexão cifrada, não a honestidade do dono do site.",
            "B) Lentidão é um problema de desempenho ou de conexão, não um indicador direto de fraude.",
            "C) Perfeito! Golpistas registram nomes parecidos (ex: banc0-oficial.com) para enganar o usuário.\n\n💡 Dica: Sempre confira com atenção a barra de endereços do navegador.",
            "D) Design e quantidade de mídias dependem da interface do site, não definindo sua legitimidade."
        ]
    },
    {
        "category": "🌐 INTERNET E LINKS (Fase 4 - Nível 2)",
        "question": "Um site exibe o ícone de 'Cadeado Verde/HTTPS' na barra de endereços. O que isso garante exatamente?",
        "options": [
            "Garante que o site é 100% confiável e livre de vírus",
            "Garante apenas que a comunicação entre o seu navegador e o site está criptografada",
            "Garante que o site pertence a um banco ou instituição governamental",
            "Garante que seus dados não poderão ser vendidos a terceiros"
        ],
        "answer": 1,
        "explanations": [
            "A) Incorreto. Sites maliciosos também utilizam HTTPS para parecerem legítimos.",
            "B) Correto! Apenas impede que terceiros interceptem o tráfego no meio do caminho (Man-in-the-Middle), mas você ainda pode estar enviando dados criptografados para um criminoso.",
            "C) Incorreto. Qualquer pessoa física ou jurídica pode emitir um certificado SSL para qualquer domínio registrado.",
            "D) Incorreto. A política de privacidade e a idoneidade da empresa definem isso, não o protocolo HTTPS."
        ]
    },
    {
        "category": "🌐 INTERNET E LINKS (Fase 4 - Nível 3)",
        "question": "Ao passar o ponteiro do mouse sobre um link em um e-mail, o rodapé mostra: 'https://suporte-security-update.com/login'. Como essa técnica é classificada?",
        "options": [
            "Ataque por negação de serviço (DDoS)",
            "Engenharia social por Typosquatting / Domínio Falso",
            "Injeção de código via SQL (SQL Injection)",
            "Ataque de força bruta (Brute Force)"
        ],
        "answer": 1,
        "explanations": [
            "A) DDoS busca tirar serviços do ar por sobrecarga, não criar links falsos de captura de credenciais.",
            "B) Exato! O atacante cria domínios parecidos com serviços reais usando palavras de suporte/segurança para induzir o clique.\n\n💡 Dica: Passe sempre o ponteiro sobre o link para checar a URL de destino real.",
            "C) SQL Injection é uma vulnerabilidade em bancos de dados, não uma técnica de camuflagem de URLs.",
            "D) Força bruta é a tentativa massiva de adivinhar senhas por tentativa e erro."
        ]
    }
]

class CyberQuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("CyberShield: Ethical Hacker Quiz - Fase 4")
        self.root.geometry("660x580")
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
            wraplength=580, 
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
            messagebox.showinfo("Vitória!", f"Você dominou a Fase 4 e protegeu a rede!\nPontuação final: {self.score}")
            self.root.destroy()

    def check_answer(self, selected_idx):
        q_data = QUESTIONS[self.current_q]
        correct_idx = q_data["answer"]
        feedback = q_data["explanations"][selected_idx]

        if selected_idx == correct_idx:
            self.score += 100
            self.lbl_score.config(text=f"SCORE: {self.score}")
            messagebox.showinfo("Resposta Correta! ✅", f"{feedback}")
        else:
            self.lives -= 1
            self.lbl_firewall.config(text=f"🛡️ FIREWALL: {'█ ' * self.lives}")
            messagebox.showwarning("Resposta Incorreta! ❌", f"{feedback}")
            
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