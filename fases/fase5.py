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
COLOR_HEALTH = "#00F5D4"       # Verde/Ciano Neon (Barra de Vida)
COLOR_CORRECT = "#00E676"      # Verde vibrante para acerto
COLOR_INCORRECT = "#FF3366"    # Vermelho/Rosa Neon para erro

# ==============================================================================
# --- DADOS DO QUIZ INTEGRADOS (6 PERGUNTAS) ---
# ==============================================================================
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
        self.root.geometry("680x600")
        self.root.resizable(False, False)

        self.current_q = 0
        self.lives = 3
        self.score = 0

        self.setup_ui()
        self.load_question()

    def setup_ui(self):
        # --- CANVAS DE FUNDO (DEGRADÊ + DETALHES DE CIRCUITO) ---
        self.bg_canvas = tk.Canvas(self.root, width=680, height=600, highlightthickness=0)
        self.bg_canvas.pack(fill="both", expand=True)
        self.draw_cyber_background()

        # --- HEADER DE STATUS ---
        self.status_frame = tk.Frame(self.bg_canvas, bg=COLOR_BG_TOP)
        self.bg_canvas.create_window(340, 35, window=self.status_frame, width=640)

        self.lbl_firewall = tk.Label(
            self.status_frame, 
            text=f"🛡️ FIREWALL: {'█ ' * self.lives}", 
            font=("Consolas", 12, "bold"), 
            fg=COLOR_HEALTH, 
            bg=COLOR_BG_TOP
        )
        self.lbl_firewall.pack(side="left")

        self.lbl_score = tk.Label(
            self.status_frame, 
            text=f"SCORE: {self.score}", 
            font=("Consolas", 12, "bold"), 
            fg=COLOR_CYAN_GLOW, 
            bg=COLOR_BG_TOP
        )
        self.lbl_score.pack(side="right")

        # --- CARD PRINCIPAL DE CONTEÚDO ---
        self.card_frame = tk.Frame(
            self.bg_canvas, 
            bg=COLOR_CARD_BG, 
            highlightbackground=COLOR_CARD_BORDER, 
            highlightthickness=2,
            bd=0
        )
        self.bg_canvas.create_window(340, 310, window=self.card_frame, width=640, height=470)

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
            font=("Segoe UI", 11), 
            fg=COLOR_TEXT_MAIN, 
            bg=COLOR_CARD_BG, 
            wraplength=580, 
            justify="left"
        )
        self.lbl_question.pack(anchor="w", padx=20, pady=10)

        # --- CONTAINER DOS BOTÕES ---
        self.btn_frame = tk.Frame(self.card_frame, bg=COLOR_CARD_BG)
        self.btn_frame.pack(fill="both", expand=True, padx=20, pady=(5, 15))

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
            btn.pack(fill="x", pady=5, ipady=4)
            btn.bind("<Enter>", lambda e, b=btn: self.on_hover_enter(b))
            btn.bind("<Leave>", lambda e, b=btn: self.on_hover_leave(b))
            self.buttons.append(btn)

    def draw_cyber_background(self):
        width, height = 680, 600
        r1, g1, b1 = self.hex_to_rgb(COLOR_BG_TOP)
        r2, g2, b2 = self.hex_to_rgb(COLOR_BG_BOTTOM)
        
        # Gradiente suave
        for y in range(height):
            r = int(r1 + (r2 - r1) * (y / height))
            g = int(g1 + (g2 - g1) * (y / height))
            b = int(b1 + (b2 - b1) * (y / height))
            color = f"#{r:02x}{g:02x}{b:02x}"
            self.bg_canvas.create_line(0, y, width, y, fill=color)

        # Linhas de circuito cibernético
        line_color = "#0B3254"
        glow_dot = COLOR_CYAN_GLOW

        self.bg_canvas.create_line(30, 25, 180, 25, 230, 50, 450, 50, fill=line_color, width=1.5)
        self.bg_canvas.create_oval(177, 22, 183, 28, fill=glow_dot, outline="")
        self.bg_canvas.create_oval(447, 47, 453, 53, fill=glow_dot, outline="")

        self.bg_canvas.create_line(50, 570, 200, 570, 250, 550, 520, 550, fill=line_color, width=1.5)
        self.bg_canvas.create_oval(247, 547, 253, 553, fill=glow_dot, outline="")

    @staticmethod
    def hex_to_rgb(hex_str):
        hex_str = hex_str.lstrip('#')
        return tuple(int(hex_str[i:i+2], 16) for i in (0, 2, 4))

    def on_hover_enter(self, btn):
        if btn["state"] == "normal":
            btn.config(bg=COLOR_BTN_HOVER, fg=COLOR_TEXT_MAIN)

    def on_hover_leave(self, btn):
        if btn["state"] == "normal":
            btn.config(bg=COLOR_BTN_BG, fg=COLOR_TEXT_MUTED)

    def load_question(self):
        if self.current_q < len(QUESTIONS):
            q_data = QUESTIONS[self.current_q]
            self.lbl_category.config(text=q_data["category"])
            self.lbl_question.config(text=q_data["question"])
            
            for i, opt in enumerate(q_data["options"]):
                self.buttons[i].config(
                    text=f"[ {chr(65+i)} ]  {opt}",
                    bg=COLOR_BTN_BG,
                    fg=COLOR_TEXT_MUTED,
                    state="normal"
                )
        else:
            messagebox.showinfo("Vitória! 🏆", f"Você protegeu a rede com sucesso!\n\nPontuação Final: {self.score}")
            self.root.destroy()

    def check_answer(self, selected_idx):
        correct_idx = QUESTIONS[self.current_q]["answer"]
        
        for btn in self.buttons:
            btn.config(state="disabled")

        if selected_idx == correct_idx:
            self.score += 100
            self.lbl_score.config(text=f"SCORE: {self.score}")
            self.buttons[selected_idx].config(bg=COLOR_CORRECT, fg="#000000")
        else:
            self.lives -= 1
            self.lbl_firewall.config(text=f"🛡️ FIREWALL: {'█ ' * self.lives}")
            self.buttons[selected_idx].config(bg=COLOR_INCORRECT, fg=COLOR_TEXT_MAIN)
            self.buttons[correct_idx].config(bg=COLOR_CORRECT, fg="#000000")

            if self.lives == 0:
                self.root.after(1000, self.game_over)
                return

        self.current_q += 1
        self.root.after(1200, self.load_question)

    def game_over(self):
        messagebox.showerror("Game Over ⚠️", "O firewall caiu e o sistema foi comprometido!\n\nTente novamente.")
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    
    # Centralização da janela na tela
    window_width = 680
    window_height = 600
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    position_right = int(screen_width/2 - window_width/2)
    position_top = int(screen_height/2 - window_height/2)
    root.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")
    
    app = CyberQuizApp(root)
    root.mainloop()