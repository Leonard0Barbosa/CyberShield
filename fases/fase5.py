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
# --- BANCO DE DADOS DAS QUESTÕES (FASE 4 - INTERNET, LINKS & PHISHING) ---
# ==============================================================================
QUESTIONS = [
    {
        "category": "🌐 NAVEGAÇÃO SEGURA & PROTOCOLOS",
        "question": "Qual sinal indica a maior probabilidade de um site ser uma tentativa de golpe ou Phishing?",
        "options": [
            "O site utiliza o protocolo HTTPS com o ícone de cadeado",
            "O site carrega as imagens de forma lenta e desconfigurada",
            "O domínio na barra de endereços possui grafia alterada (ex: banc0.com)",
            "O site contém muitos elementos multimídia e animações em vídeo"
        ],
        "answer": 2
    },
    {
        "category": "🔒 CRIPTOGRAFIA WEB & CERTIFICADOS",
        "question": "Um site exibe o ícone de 'Cadeado/HTTPS' na barra de endereços. O que esse certificado SSL/TLS garante exatamente?",
        "options": [
            "Garante que o site é 100% confiável e livre de malwares",
            "Garante apenas que a comunicação entre navegador e servidor está criptografada",
            "Garante que o site pertence obrigatoriamente a uma instituição bancária",
            "Garante que os dados do usuário jamais serão compartilhados com terceiros"
        ],
        "answer": 1
    },
    {
        "category": "🎣 ENGENHARIA SOCIAL & TYPOSQUATTING",
        "question": "Ao passar o mouse sobre um link, o destino exibe: 'suporte-security-update.com/login'. Como essa técnica é classificada?",
        "options": [
            "Ataque por Negação de Serviço Distribuído (DDoS)",
            "Engenharia Social por Typosquatting / Domínio Falso",
            "Injeção de código SQL em Banco de Dados (SQLi)",
            "Ataque de Força Bruta por Dicionário (Brute Force)"
        ],
        "answer": 1
    },
    {
        "category": "🔗 ENCURTADORES DE LINK & REDIRECIONAMENTOS",
        "question": "Qual é o principal risco de segurança associado ao uso de encurtadores de URL (como bit.ly) em e-mails suspeitos?",
        "options": [
            "Eles infectam o sistema operacional instantaneamente ao serem exibidos na tela",
            "Eles ocultam o destino real do link, impedindo a verificação prévia do domínio final",
            "Eles desativam o antivírus e firewall locais durante a navegação",
            "Eles alteram as senhas salvas automaticamente no navegador"
        ],
        "answer": 1
    },
    {
        "category": "🛑 ATAQUES HOMÓGRAFOS & PUNYCODE",
        "question": "O que caracteriza um Ataque Homográfico de IDN (Internationalized Domain Name)?",
        "options": [
            "A invasão direta de servidores de nomes de domínio (DNS)",
            "Uso de caracteres de outros alfabetos (ex: cirílico) idênticos aos latinos para criar URLs falsas",
            "A interceptação de tráfego de redes Wi-Fi públicas sem senha",
            "A alteração do arquivo 'hosts' local para redirecionar o navegador"
        ],
        "answer": 1
    },
    {
        "category": "🛡️ DEFESA & PREVENÇÃO",
        "question": "Qual é a conduta mais recomendada antes de inserir credenciais em uma página de login recebida por e-mail?",
        "options": [
            "Verificar se o site possui um design moderno e logotipos em alta resolução",
            "Digitar qualquer senha falsa primeiro para testar se o sistema valida",
            "Inspecionar manualmente o domínio na barra de endereços ou acessar digitando a URL oficial diretamente",
            "Confiar caso a mensagem possua um selo visual de 'Antivírus Verificado'"
        ],
        "answer": 2
    }
]

# ==============================================================================
# --- CLASSE PRINCIPAL DO APLICATIVO ---
# ==============================================================================
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
        # --- CANVAS DE FUNDO ---
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
        
        for y in range(height):
            r = int(r1 + (r2 - r1) * (y / height))
            g = int(g1 + (g2 - g1) * (y / height))
            b = int(b1 + (b2 - b1) * (y / height))
            color = f"#{r:02x}{g:02x}{b:02x}"
            self.bg_canvas.create_line(0, y, width, y, fill=color)

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
        if str(btn["state"]) == "normal":
            btn.config(bg=COLOR_BTN_HOVER, fg=COLOR_TEXT_MAIN)

    def on_hover_leave(self, btn):
        if str(btn["state"]) == "normal":
            btn.config(bg=COLOR_BTN_BG, fg=COLOR_TEXT_MUTED)

    def load_question(self):
        if self.current_q < len(QUESTIONS):
            q_data = QUESTIONS[self.current_q]
            self.lbl_category.config(text=f"CATEGORIA: {q_data['category']}")
            self.lbl_question.config(text=f"PERGUNTA {self.current_q + 1}/{len(QUESTIONS)}:\n{q_data['question']}")

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
        q_data = QUESTIONS[self.current_q]
        correct_idx = q_data["answer"]

        for btn in self.buttons:
            btn.config(state="disabled")

        if selected_idx == correct_idx:
            self.score += 100
            self.lbl_score.config(text=f"SCORE: {self.score}")
            self.buttons[selected_idx].config(bg=COLOR_CORRECT, fg="#000000")
            self.current_q += 1
            self.root.after(1200, self.load_question)
        else:
            self.lives -= 1
            self.lbl_firewall.config(text=f"🛡️ FIREWALL: {'█ ' * self.lives}") 
            self.buttons[selected_idx].config(bg=COLOR_INCORRECT, fg=COLOR_TEXT_MAIN)
            self.buttons[correct_idx].config(bg=COLOR_CORRECT, fg="#000000")

            # POP-UP DE ERRO DO WINDOWS NATIVO
            messagebox.showerror(
                "System Error - Security Violation",
                f"system32\\drivers\\firewall.sys\n\n"
                f"ERROR Code: 0x80070005 (Access Denied)\n"
                f"Resposta incorreta! Uma brecha foi explorada.\n\n"
                f"Escudos do Firewall restantes: {self.lives}"
            )

            if self.lives == 0:
                self.game_over()
            else:
                self.current_q += 1
                self.load_question()

    def game_over(self):
        messagebox.showerror(
            "CRITICAL SYSTEM ERROR", 
            "Windows - System Error\n\n"
            "O firewall foi completamente destruído e o sistema travou!\n"
            "A aplicação será encerrada."
        )
        self.root.destroy()


# ==============================================================================
# --- INICIALIZAÇÃO DA APLICAÇÃO ---
# ==============================================================================
if __name__ == "__main__":
    root = tk.Tk()
    
    window_width = 680
    window_height = 600
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    position_right = int(screen_width / 2 - window_width / 2)
    position_top = int(screen_height / 2 - window_height / 2)
    
    root.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")
    
    app = CyberQuizApp(root)
    root.mainloop()