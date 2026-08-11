import tkinter as tk
from tkinter import messagebox

# ==============================================================================
# --- PADRÃO DE DESIGN (CYBER NETWORK - AZUL SUAVE & CIANO NEON) ---
# ==============================================================================
COLOR_BG_TOP = "#030D22"       # Azul ultra escuro (Topo)
COLOR_BG_BOTTOM = "#0A2542"    # Azul marinho profundo (Base)
COLOR_CARD_BG = "#0D1F38"      # Fundo translúcido do painel
COLOR_CARD_BORDER = "#144574"  # Borda suave do card
COLOR_CYAN_GLOW = "#00F0FF"    # Ciano elétrico (Destaques e Ícones)
COLOR_BTN_BG = "#0F3356"       # Azul suave para botões
COLOR_BTN_HOVER = "#0077B6"    # Azul de navegação ao passar o mouse
COLOR_TEXT_MAIN = "#FFFFFF"    # Texto branco principal
COLOR_TEXT_MUTED = "#8ECAE6"   # Texto secundário suave
COLOR_HEALTH = "#00F5D4"       # Verde/Ciano Neon da barra de vida

# --- CORES DE FEEDBACK (ACERTO / ERRO) ---
COLOR_CORRECT = "#00E676"      # Verde vibrante para acerto
COLOR_INCORRECT = "#FF3366"    # Vermelho/Rosa Neon para erro

# ==============================================================================
# --- DADOS DO QUIZ (FASE 4: INTERNET E LINKS) ---
# ==============================================================================
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
            "O HTTPS apenas criptografa o tráfego. Golpistas também obtêm certificados SSL gratuitos para sites falsos.\n\n💡 Dica: HTTPS garante conexão cifrada, não a honestidade do dono do site.",
            "Lentidão é um problema de desempenho ou de conexão, não um indicador direto de fraude.",
            "Perfeito! Golpistas registram nomes parecidos (ex: banc0-oficial.com) para enganar o usuário.\n\n💡 Dica: Sempre confira com atenção a barra de endereços do navegador.",
            "Design e quantidade de mídias dependem da interface do site, não definindo sua legitimidade."
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
            "Incorreto. Sites maliciosos também utilizam HTTPS para parecerem legítimos.",
            "Correto! Apenas impede que terceiros interceptem o tráfego no meio do caminho (Man-in-the-Middle), mas você ainda pode estar enviando dados criptografados para um criminoso.",
            "Incorreto. Qualquer pessoa física ou jurídica pode emitir um certificado SSL para qualquer domínio registrado.",
            "Incorreto. A política de privacidade e a idoneidade da empresa definem isso, não o protocolo HTTPS."
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
            "DDoS busca tirar serviços do ar por sobrecarga, não criar links falsos de captura de credenciais.",
            "Exato! O atacante cria domínios parecidos com serviços reais usando palavras de suporte/segurança para induzir o clique.\n\n💡 Dica: Passe sempre o ponteiro sobre o link para checar a URL de destino real.",
            "SQL Injection é uma vulnerabilidade em bancos de dados, não uma técnica de camuflagem de URLs.",
            "Força bruta é a tentativa massiva de adivinhar senhas por tentativa e erro."
        ]
    }
]

class CyberQuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("CyberShield: Ethical Hacker Quiz - Fase 4")
        self.root.geometry("660x580")
        self.root.resizable(False, False)

        self.current_q = 0
        self.lives = 3
        self.score = 0

        self.setup_ui()
        self.load_question()

    def setup_ui(self):
        # --- CANVAS DE FUNDO (DEGRADÊ E LINHAS DE CIRCUITO) ---
        self.bg_canvas = tk.Canvas(self.root, width=660, height=580, highlightthickness=0)
        self.bg_canvas.pack(fill="both", expand=True)
        self.draw_cyber_background()

        # --- HEADER / BARRA DE STATUS ---
        self.status_frame = tk.Frame(self.bg_canvas, bg=COLOR_BG_TOP)
        self.bg_canvas.create_window(330, 35, window=self.status_frame, width=620)

        self.lbl_firewall = tk.Label(
            self.status_frame, 
            text=f"🛡️ FIREWALL: {'█ ' * self.lives}", 
            font=("Consolas", 13, "bold"), 
            fg=COLOR_HEALTH, 
            bg=COLOR_BG_TOP
        )
        self.lbl_firewall.pack(side="left")

        self.lbl_score = tk.Label(
            self.status_frame, 
            text=f"SCORE: {self.score}", 
            font=("Consolas", 13, "bold"), 
            fg=COLOR_CYAN_GLOW, 
            bg=COLOR_BG_TOP
        )
        self.lbl_score.pack(side="right")

        # --- CARD PRINCIPAL (PAINEL DA PERGUNTA) ---
        self.card_frame = tk.Frame(
            self.bg_canvas, 
            bg=COLOR_CARD_BG, 
            highlightbackground=COLOR_CARD_BORDER, 
            highlightthickness=2,
            bd=0
        )
        self.bg_canvas.create_window(330, 300, window=self.card_frame, width=620, height=450)

        self.lbl_category = tk.Label(
            self.card_frame, 
            text="", 
            font=("Segoe UI", 10, "bold"), 
            fg=COLOR_CYAN_GLOW, 
            bg=COLOR_CARD_BG
        )
        self.lbl_category.pack(anchor="w", padx=20, pady=(15, 5))

        self.lbl_question = tk.Label(
            self.card_frame, 
            text="", 
            font=("Segoe UI", 12), 
            fg=COLOR_TEXT_MAIN, 
            bg=COLOR_CARD_BG, 
            wraplength=570, 
            justify="left"
        )
        self.lbl_question.pack(anchor="w", padx=20, pady=10)

        # --- CONTAINER DE BOTÕES ---
        self.btn_frame = tk.Frame(self.card_frame, bg=COLOR_CARD_BG)
        self.btn_frame.pack(fill="both", expand=True, padx=20, pady=10)

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
            btn.pack(fill="x", pady=6, ipady=4)
            
            # Efeito Hover
            btn.bind("<Enter>", lambda e, b=btn: self.on_hover_enter(b))
            btn.bind("<Leave>", lambda e, b=btn: self.on_hover_leave(b))
            
            self.buttons.append(btn)

    def on_hover_enter(self, btn):
        if btn["state"] == "normal":
            btn.config(bg=COLOR_BTN_HOVER, fg=COLOR_TEXT_MAIN)

    def on_hover_leave(self, btn):
        if btn["state"] == "normal":
            btn.config(bg=COLOR_BTN_BG, fg=COLOR_TEXT_MUTED)

    def draw_cyber_background(self):
        """ Desenha o fundo degradê e as linhas tecnológicas de circuito """
        width, height = 660, 580
        
        # 1. Degradê
        r1, g1, b1 = self.hex_to_rgb(COLOR_BG_TOP)
        r2, g2, b2 = self.hex_to_rgb(COLOR_BG_BOTTOM)
        
        for y in range(height):
            r = int(r1 + (r2 - r1) * (y / height))
            g = int(g1 + (g2 - g1) * (y / height))
            b = int(b1 + (b2 - b1) * (y / height))
            color = f"#{r:02x}{g:02x}{b:02x}"
            self.bg_canvas.create_line(0, y, width, y, fill=color)

        # 2. Linhas de Circuito Cyber
        line_color = "#0B3254"
        glow_dot = COLOR_CYAN_GLOW

        # Circuito Superior
        self.bg_canvas.create_line(30, 25, 180, 25, 230, 50, 430, 50, fill=line_color, width=1.5)
        self.bg_canvas.create_oval(177, 22, 183, 28, fill=glow_dot, outline="")
        self.bg_canvas.create_oval(427, 47, 433, 53, fill=glow_dot, outline="")

        # Circuito Inferior
        self.bg_canvas.create_line(50, 550, 200, 550, 250, 530, 500, 530, 550, 555, fill=line_color, width=1.5)
        self.bg_canvas.create_oval(247, 527, 253, 533, fill=glow_dot, outline="")
        self.bg_canvas.create_oval(497, 527, 503, 533, fill=glow_dot, outline="")

    @staticmethod
    def hex_to_rgb(hex_str):
        hex_str = hex_str.lstrip('#')
        return tuple(int(hex_str[i:i+2], 16) for i in (0, 2, 4))

    def load_question(self):
        if self.current_q < len(QUESTIONS):
            q_data = QUESTIONS[self.current_q]
            self.lbl_category.config(text=q_data["category"])
            self.lbl_question.config(text=q_data["question"])
            
            for i, opt in enumerate(q_data["options"]):
                self.buttons[i].config(
                    text=f"[ {chr(65+i)} ]   {opt}",
                    bg=COLOR_BTN_BG,
                    fg=COLOR_TEXT_MUTED,
                    state="normal"
                )
        else:
            messagebox.showinfo("Vitória!", f"Você dominou a Fase 4 e protegeu a rede!\nPontuação final: {self.score}")
            self.root.destroy()

    def check_answer(self, selected_idx):
        for btn in self.buttons:
            btn.config(state="disabled")

        q_data = QUESTIONS[self.current_q]
        correct_idx = q_data["answer"]
        explanation = q_data["explanations"][selected_idx]
        selected_btn = self.buttons[selected_idx]

        if selected_idx == correct_idx:
            selected_btn.config(bg=COLOR_CORRECT, fg="#000000")
            self.root.update()
            
            self.score += 100
            self.lbl_score.config(text=f"SCORE: {self.score}")
            
            messagebox.showinfo("Resposta Correta! ✅", f"Parabéns! Você acertou!\n\n{explanation}")
        else:
            selected_btn.config(bg=COLOR_INCORRECT, fg="#FFFFFF")
            self.buttons[correct_idx].config(bg=COLOR_CORRECT, fg="#000000")
            self.root.update()
            
            self.lives -= 1
            self.lbl_firewall.config(text=f"🛡️ FIREWALL: {'█ ' * self.lives}")
            
            messagebox.showwarning("Resposta Incorreta! ❌", f"{explanation}")
            
            if self.lives == 0:
                messagebox.showerror("Game Over", "O firewall caiu! O sistema foi comprometido. Tente novamente.")
                self.root.destroy()
                return

        self.current_q += 1
        self.load_question()

if __name__ == "__main__":
    root = tk.Tk()
    app = CyberQuizApp(root)
    root.mainloop()