import tkinter as tk
from tkinter import messagebox

# --- CONFIGURAÇÃO DE CORES (TEMA HACKER ÉTICO) ---
COLOR_BG = "#0B132B"         # Fundo azul bem escuro
COLOR_CARD = "#1C2541"       # Fundo da caixa da pergunta
COLOR_BTN = "#00B4D8"        # Botões (Azul Neon)
COLOR_TEXT = "#FFFFFF"       # Texto branco
COLOR_HEALTH = "#06D6A0"     # Barra de vida (Verde/Ciano)
COLOR_RIGHT = "#4BB543"      # Feedback de acerto (Verde)
COLOR_WRONG = "#D9534F"      # Feedback de erro (Vermelho)

# --- DADOS DO QUIZ INTEGRADOS (6 PERGUNTAS) ---
QUESTIONS = [
    {
        "category": "🌐 SERVIÇOS DE REDE",
        "question": "Qual serviço é responsável por traduzir nomes de domínio (ex: site.com) para endereços IP?",
        "options": ["DHCP", "Firewall", "DNS", "HTTP"],
        "answer": 2
    },
    {
        "category": "📦 MODELO OSI",
        "question": "Qual é a principal função da Camada de Rede (Camada 3) no modelo OSI?",
        "options": [
            "Transmissão de bits brutos pelo meio físico.",
            "Estabelecimento, manutenção e encerramento de sessões entre aplicações.",
            "Determinação do melhor caminho e roteamento de pacotes.",
            "Formatação, criptografia e compressão de dados."
        ],
        "answer": 2
    },
    {
        "category": "🔢 ENDEREÇAMENTO IP",
        "question": "Quantos bits compõem um endereço IPv4 padrão?",
        "options": ["32 bits", "64 bits", "128 bits", "256 bits"],
        "answer": 0
    },
    {
        "category": "🚀 PROTOCOLOS DE TRANSPORTE",
        "question": "Qual dos seguintes protocolos pertence à camada de Transporte, é orientado à conexão e garante a entrega dos dados?",
        "options": ["UDP", "IP", "TCP", "ICMP"],
        "answer": 2
    },
    {
        "category": "🌐 PROTOCOLOS DE APLICAÇÃO",
        "question": "Qual é a principal diferença entre os protocolos HTTP e HTTPS?",
        "options": [
            "O HTTP é usado apenas para arquivos de áudio, enquanto o HTTPS é para imagens.",
            "O HTTPS utiliza criptografia, tornando a transmissão de dados mais segura.",
            "O HTTPS é uma versão desatualizada e mais lenta do protocolo HTTP.",
            "O HTTP permite acesso a redes privadas, e o HTTPS é exclusivo para a internet pública."
        ],
        "answer": 1
    },
    {
        "category": "🛡️ SEGURANÇA DE REDE",
        "question": "Qual é o principal objetivo de um Firewall em uma rede de computadores?",
        "options": [
            "Fornecer e gerenciar automaticamente os endereços IP dos dispositivos.",
            "Filtrar e controlar o tráfego de rede com base em regras de segurança.",
            "Traduzir nomes de sites (URLs) em endereços IP legíveis.",
            "Ampliar o alcance do sinal de Wi-Fi em grandes empresas."
        ],
        "answer": 1
    }
]

class CyberQuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("CyberShield: Ethical Hacker Quiz")
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
            font=("Helvetica", 12, "bold"), 
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
                self.buttons[i].config(
                    text=f"[ {chr(65+i)} ]  {opt}",
                    bg=COLOR_BTN,
                    fg="#000000",
                    state="normal"
                )
        else:
            messagebox.showinfo("Vitória!", f"Você protegeu o sistema!\nPontuação final: {self.score}")
            self.root.destroy()

    def check_answer(self, selected_idx):
        correct_idx = QUESTIONS[self.current_q]["answer"]
        
        for btn in self.buttons:
            btn.config(state="disabled")

        if selected_idx == correct_idx:
            self.score += 100
            self.lbl_score.config(text=f"SCORE: {self.score}")
            self.buttons[selected_idx].config(bg=COLOR_RIGHT, fg=COLOR_TEXT)
        else:
            self.lives -= 1
            self.lbl_firewall.config(text=f"🛡️ FIREWALL: {'█ ' * self.lives}")
            self.buttons[selected_idx].config(bg=COLOR_WRONG, fg=COLOR_TEXT)
            self.buttons[correct_idx].config(bg=COLOR_RIGHT, fg=COLOR_TEXT)

            if self.lives == 0:
                self.root.after(1000, self.game_over)
                return

        self.current_q += 1
        self.root.after(1000, self.load_question)

    def game_over(self):
        messagebox.showerror("Game Over", "O sistema foi hackeado! Tente novamente.")
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    
    # Centraliza a janela na tela do usuário
    window_width = 650
    window_height = 550
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    position_right = int(screen_width/2 - window_width/2)
    position_top = int(screen_height/2 - window_height/2)
    root.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")
    
    app = CyberQuizApp(root)
    root.mainloop()
