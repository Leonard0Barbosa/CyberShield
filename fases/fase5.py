import tkinter as tk
from tkinter import messagebox
<<<<<<< HEAD
import html

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
COLOR_HEALTH = "#00F5D4"       # Verde/Ciano Neon
COLOR_CORRECT = "#00E676"      # Verde vibrante para acerto
COLOR_INCORRECT = "#FF3366"    # Vermelho/Rosa Neon para erro
COLOR_WARNING = "#FFD166"      # Amarelo/Laranja para alertas

# ==============================================================================
# --- BANCO DE PERGUNTAS DA FASE 5: SEGURANÇA WEB & APLICAÇÕES ---
# ==============================================================================
QUIZ_FASE_5 = [
    {
        "category": "🌐 OWASP TOP 10 — CROSS-SITE SCRIPTING (XSS)",
        "question": "Qual é a principal causa de uma vulnerabilidade de Stored XSS e a melhor forma de mitigá-la na aplicação?",
        "options": [
            "A) Falta de firewall no servidor; mitiga-se bloqueando conexões UDP",
            "B) Renderização de scripts fornecidos por usuários sem sanitização; mitiga-se com Context-Aware Output Encoding",
            "C) Uso de senhas fracas no banco de dados; mitiga-se alterando para senhas de 16 caracteres",
            "D) Transmissão de dados sem HTTPS; mitiga-se comprando um certificado SSL"
        ],
        "answer": 1,
        "explanations": [
            "❌ INCORRETO: XSS é uma vulnerabilidade na camada de aplicação web, não de protocolos de transporte como UDP.",
            "✅ CORRETO! O XSS ocorre quando entradas do usuário são tratadas como código pelo navegador. O Encoding correto desativa a execução de tags como <script>.",
            "❌ INCORRETO: Força de senhas não impede que scripts maliciosos sejam injetados em páginas HTML.",
            "❌ INCORRETO: O HTTPS criptografa o tráfego, mas não previne que a aplicação renderize código malicioso injetado."
        ],
        "tip": "💡 Dica: Nunca confie em entradas de usuários. Trate todo texto exibido no HTML como dado puro usando encoding!"
=======


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
>>>>>>> 925aafaf53a0aea102ea91d0d7cfc7478c0e7b39
    },
    {
        "category": "🔒 MITIGAÇÃO DE CSRF & SEGURANÇA DE COOKIES",
        "question": "Como o mecanismo de Anti-CSRF Token previne ataques de Cross-Site Request Forgery em formulários web?",
        "options": [
            "A) Criptografando o banco de dados para impedir a leitura de registros de usuários",
            "B) Exigindo um valor secreto e imprevisível gerado pela sessão do usuário que sites terceiros não conseguem ler ou adivinhar",
            "C) Bloqueando qualquer requisição que venha de um endereço IP externo",
            "D) Forçando o usuário a resolver um CAPTCHA a cada clique dentro da aplicação"
        ],
<<<<<<< HEAD
        "answer": 1,
        "explanations": [
            "❌ INCORRETO: O CSRF não explora o banco de dados diretamente, mas sim a confiança que a aplicação tem no navegador do usuário.",
            "✅ CORRETO! O token Anti-CSRF valida se a requisição partiu legitimamente da própria aplicação, já que sites maliciosos não conseguem ler o token devido à Same-Origin Policy (SOP).",
            "❌ INCORRETO: Bloquear IPs inviabilizaria o acesso remoto dos usuários à aplicação.",
            "❌ INCORRETO: CAPTCHAs funcionam contra bots, mas tornariam a usabilidade inviável se usados para cada ação."
        ],
        "tip": "💡 Dica: O atributo SameSite=Strict/Lax em cookies também é uma excelente defesa complementar contra CSRF!"
    },
    {
        "category": "🛡️ CABEÇALHOS DE SEGURANÇA (SECURITY HEADERS)",
        "question": "Qual é a função do cabeçalho Content-Security-Policy (CSP) nas respostas HTTP de uma aplicação web?",
        "options": [
            "A) Comprimir imagens para acelerar o carregamento da página",
            "B) Restringir quais origens e tipos de recursos (scripts, estilos, conexões) o navegador tem permissão de carregar",
            "C) Redirecionar automaticamente todas as requisições para o protocolo HTTP simples",
            "D) Ocultar a versão do servidor Apache ou Nginx nas respostas da API"
        ],
        "answer": 1,
        "explanations": [
            "❌ INCORRETO: Compressão de assets é tratada por cabeçalhos como Content-Encoding: gzip.",
            "✅ CORRETO! O CSP atua como uma 'whitelist' no navegador, impedindo a execução de scripts inline não autorizados e reduzindo drasticamente o impacto de vulnerabilidades XSS.",
            "❌ INCORRETO: O recomendado é forçar HTTPS através do cabeçalho HSTS, nunca regressar para HTTP.",
            "❌ INCORRETO: Esconder a versão do servidor é feito removendo o cabeçalho 'Server', não via CSP."
        ],
        "tip": "💡 Dica: Um CSP forte pode bloquear scripts maliciosos injetados mesmo se a aplicação tiver falhas de sanitização XSS."
    },
    {
        "category": "🔐 PROTOCOLOS SEGUROS & HTTPS",
        "question": "Por que o uso do protocolo HTTPS (HTTP sobre TLS/SSL) é indispensável para a segurança de aplicações web modernas?",
        "options": [
            "A) Porque ele impede automaticamente qualquer ataque de SQL Injection ou XSS no servidor",
            "B) Porque ele garante Confidencialidade (criptografia do tráfego) e Autenticidade (certificado do servidor), prevenindo Man-in-the-Middle (MitM)",
            "C) Porque ele torna a aplicação imune a ataques de negação de serviço (DDoS)",
            "D) Porque ele dispensa a necessidade de autenticação por usuário e senha"
        ],
        "answer": 1,
        "explanations": [
            "❌ INCORRETO: O HTTPS protege os dados em trânsito, mas não corrige falhas de programação no backend.",
            "✅ CORRETO! Sem HTTPS, dados sensíveis (senhas, cookies de sessão) trafegam em texto puro pela rede e podem ser interceptados por qualquer um no caminho.",
            "❌ INCORRETO: O HTTPS não bloqueia ataques volumétricos de negação de serviço (DDoS).",
            "❌ INCORRETO: A autenticação do usuário continua sendo necessária para controlar o acesso individual."
        ],
        "tip": "💡 Dica: Sempre utilize a flag 'Secure' em cookies para garantir que só sejam transmitidos via HTTPS!"
=======
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
>>>>>>> 925aafaf53a0aea102ea91d0d7cfc7478c0e7b39
    }
]


<<<<<<< HEAD
class Phase5App:
    def __init__(self, root):
        self.root = root
        self.root.title("CyberShield: Fase 5 — Segurança Web & Aplicações")
        self.root.geometry("700x640")
        self.root.resizable(False, False)

        self.current_q = 0

        # Atributos para o Simulador CSRF
        self.csrf_token_enabled = None
        self.csrf_samesite_enabled = None
=======
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
>>>>>>> 925aafaf53a0aea102ea91d0d7cfc7478c0e7b39

        self.setup_ui()
        self.load_step_xss_lab()

    # ========================================================
    # INTERFACE
    # ========================================================
    def setup_ui(self):
<<<<<<< HEAD
        # --- CANVAS DE FUNDO ---
        self.bg_canvas = tk.Canvas(self.root, width=700, height=640, highlightthickness=0)
        self.bg_canvas.pack(fill="both", expand=True)
        self.draw_cyber_background()

        # --- HEADER DE STATUS ---
        self.status_frame = tk.Frame(self.bg_canvas, bg=COLOR_BG_TOP)
        self.bg_canvas.create_window(350, 35, window=self.status_frame, width=660)

        self.lbl_header = tk.Label(
            self.status_frame, 
            text="🛡️ FASE 5: SEGURANÇA WEB & APLICAÇÕES", 
            font=("Consolas", 11, "bold"), 
            fg=COLOR_HEALTH, 
            bg=COLOR_BG_TOP
        )
        self.lbl_header.pack(side="left")

        self.lbl_mode = tk.Label(
            self.status_frame, 
            text="ETAPA 1/3", 
            font=("Consolas", 11, "bold"), 
            fg=COLOR_CYAN_GLOW, 
            bg=COLOR_BG_TOP
        )
        self.lbl_mode.pack(side="right")

        # --- CARD PRINCIPAL ---
=======

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
>>>>>>> 925aafaf53a0aea102ea91d0d7cfc7478c0e7b39
        self.card_frame = tk.Frame(
            self.bg_canvas,
            bg=COLOR_CARD_BG,
            highlightbackground=COLOR_CARD_BORDER,
            highlightthickness=2,
            bd=0
        )
<<<<<<< HEAD
        self.bg_canvas.create_window(350, 330, window=self.card_frame, width=660, height=520)
=======

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
>>>>>>> 925aafaf53a0aea102ea91d0d7cfc7478c0e7b39

    # ========================================================
    # FUNDO CYBER
    # ========================================================
    def draw_cyber_background(self):
<<<<<<< HEAD
        width, height = 700, 640
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

        self.bg_canvas.create_line(30, 25, 180, 25, 230, 50, 480, 50, fill=line_color, width=1.5)
        self.bg_canvas.create_oval(177, 22, 183, 28, fill=glow_dot, outline="")
        self.bg_canvas.create_oval(477, 47, 483, 53, fill=glow_dot, outline="")

        self.bg_canvas.create_line(50, 610, 200, 610, 250, 590, 550, 590, fill=line_color, width=1.5)
        self.bg_canvas.create_oval(247, 587, 253, 593, fill=glow_dot, outline="")
=======

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
>>>>>>> 925aafaf53a0aea102ea91d0d7cfc7478c0e7b39

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

<<<<<<< HEAD
    def clear_card(self):
        for widget in self.card_frame.winfo_children():
            widget.destroy()

    def create_custom_button(self, parent, text, command):
        btn = tk.Button(
            parent,
            text=text,
            font=("Segoe UI", 10, "bold"),
            bg=COLOR_BTN_BG,
            fg=COLOR_TEXT_MUTED,
            activebackground=COLOR_BTN_HOVER,
            activeforeground=COLOR_TEXT_MAIN,
            relief="flat",
            cursor="hand2",
            bd=1,
            highlightbackground=COLOR_CARD_BORDER,
            command=command
        )
        btn.bind("<Enter>", lambda e, b=btn: self.on_hover_enter(b))
        btn.bind("<Leave>", lambda e, b=btn: self.on_hover_leave(b))
        return btn

=======
        hex_str = hex_str.lstrip("#")

        return tuple(
            int(hex_str[i:i + 2], 16)
            for i in (0, 2, 4)
        )

    # ========================================================
    # EFEITO DO MOUSE
    # ========================================================
>>>>>>> 925aafaf53a0aea102ea91d0d7cfc7478c0e7b39
    def on_hover_enter(self, btn):

        if btn["state"] == "normal":

            btn.config(
                bg=COLOR_BTN_HOVER,
                fg=COLOR_TEXT_MAIN
            )

    def on_hover_leave(self, btn):

<<<<<<< HEAD
    # ==========================================================================
    # --- ETAPA 1: LABORATÓRIO DE XSS (CROSS-SITE SCRIPTING) ---
    # ==========================================================================
    def load_step_xss_lab(self):
        self.clear_card()
        self.lbl_mode.config(text="ETAPA 1/3 — LABORATÓRIO DE XSS")

        lbl_title = tk.Label(
            self.card_frame, 
            text="💉 LABORATÓRIO DE INJEÇÃO XSS (SANITIÇÃO DE OUTPUT)", 
            font=("Segoe UI", 10, "bold"), 
            fg=COLOR_CYAN_GLOW, 
            bg=COLOR_CARD_BG
        )
        lbl_title.pack(anchor="w", padx=20, pady=(12, 4))

        lbl_desc = tk.Label(
            self.card_frame, 
            text="Digite um comentário. Experimente usar tags HTML/JavaScript como <script>alert('Hack')</script> para comparar a renderização vulnerável com a segura (encoded):", 
            font=("Segoe UI", 9), 
            fg=COLOR_TEXT_MAIN, 
            bg=COLOR_CARD_BG, 
            wraplength=610, 
            justify="left"
        )
        lbl_desc.pack(anchor="w", padx=20, pady=2)

        # Campo de entrada
        frame_input = tk.Frame(self.card_frame, bg=COLOR_CARD_BG)
        frame_input.pack(fill="x", padx=20, pady=5)

        tk.Label(frame_input, text="Entrada de Comentário:", font=("Segoe UI", 9, "bold"), fg=COLOR_TEXT_MUTED, bg=COLOR_CARD_BG).pack(anchor="w")

        self.entry_xss_input = tk.Entry(
            frame_input, 
            font=("Segoe UI", 10), 
            bg=COLOR_BG_TOP, 
            fg=COLOR_TEXT_MAIN, 
            insertbackground=COLOR_TEXT_MAIN,
            bd=1,
            relief="solid"
        )
        self.entry_xss_input.insert(0, "<script>alert('XSS_COOKIE_ROUBO')</script>")
        self.entry_xss_input.pack(fill="x", pady=2)
        self.entry_xss_input.bind("<KeyRelease>", self.update_live_xss)

        # Botão rápido para inserir Payload de Teste
        btn_quick_payload = tk.Button(
            frame_input,
            text="⚡ Inserir Payload XSS: <script>alert('XSS')</script>",
            font=("Segoe UI", 8, "bold"),
            bg="#1B3B6F",
            fg=COLOR_CYAN_GLOW,
            activebackground=COLOR_BTN_HOVER,
            activeforeground=COLOR_TEXT_MAIN,
            relief="flat",
            cursor="hand2",
            command=self.insert_xss_payload
        )
        btn_quick_payload.pack(anchor="e", pady=2)

        # Saída 1: Renderização Vulnerável
        tk.Label(self.card_frame, text="1. Renderização Vulnerável (Interpretação Direta do Navegador):", font=("Segoe UI", 9, "bold"), fg=COLOR_INCORRECT, bg=COLOR_CARD_BG).pack(anchor="w", padx=20, pady=(4, 1))
        
        self.lbl_vuln_xss = tk.Label(
            self.card_frame, 
            text="", 
            font=("Consolas", 8, "bold"), 
            fg=COLOR_WARNING, 
            bg=COLOR_BG_TOP, 
            bd=1, 
            relief="solid", 
            wraplength=600, 
            justify="center", 
            pady=6
        )
        self.lbl_vuln_xss.pack(fill="x", padx=20, pady=2)

        # Saída 2: Renderização Segura (HTML Entity Encoding)
        tk.Label(self.card_frame, text="2. Renderização Segura (HTML Entity Encoding / Output Sanitizado):", font=("Segoe UI", 9, "bold"), fg=COLOR_CORRECT, bg=COLOR_CARD_BG).pack(anchor="w", padx=20, pady=(4, 1))

        self.lbl_safe_xss = tk.Label(
            self.card_frame, 
            text="", 
            font=("Consolas", 8, "bold"), 
            fg=COLOR_HEALTH, 
            bg=COLOR_BG_TOP, 
            bd=1, 
            relief="solid", 
            wraplength=600, 
            justify="center", 
            pady=6
        )
        self.lbl_safe_xss.pack(fill="x", padx=20, pady=2)

        self.lbl_xss_status = tk.Label(
            self.card_frame, 
            text="", 
            font=("Segoe UI", 9, "bold"), 
            bg=COLOR_CARD_BG
        )
        self.lbl_xss_status.pack(anchor="w", padx=20, pady=4)

        self.update_live_xss()

        btn_next1 = self.create_custom_button(self.card_frame, "Avançar para o Simulador Anti-CSRF ➔", self.load_step_csrf_lab)
        btn_next1.pack(fill="x", padx=20, pady=(6, 12))

    def insert_xss_payload(self):
        self.entry_xss_input.delete(0, tk.END)
        self.entry_xss_input.insert(0, "<script>alert('XSS_COOKIE_ROUBO')</script>")
        self.update_live_xss()

    def update_live_xss(self, event=None):
        user_in = self.entry_xss_input.get()
        
        # Simulação Vulnerável
        vuln_out = f"<div>Comentário exibido: {user_in}</div>"
        self.lbl_vuln_xss.config(text=vuln_out)

        # Simulação Segura (HTML Escape)
        safe_encoded = html.escape(user_in)
        safe_out = f"<div>Comentário exibido: {safe_encoded}</div>"
        self.lbl_safe_xss.config(text=safe_out)

        if "<script>" in user_in.lower() or "javascript:" in user_in.lower() or "onerror=" in user_in.lower() or "onload=" in user_in.lower():
            self.lbl_xss_status.config(
                text="⚠️ ALERTA: Script malicioso detectado! Na versão vulnerável, o código seria executado no navegador do vítima!",
                fg=COLOR_INCORRECT
            )
        else:
            self.lbl_xss_status.config(
                text="✅ Entrada tratada como texto comum. Sem tags ativas de script.",
                fg=COLOR_HEALTH
            )

    # ==========================================================================
    # --- ETAPA 2: SIMULADOR DE PROTEÇÃO ANTI-CSRF ---
    # ==========================================================================
    def load_step_csrf_lab(self):
        self.clear_card()
        self.lbl_mode.config(text="ETAPA 2/3 — PROTEÇÃO CONTRA CSRF")

        lbl_title = tk.Label(
            self.card_frame, 
            text="🕹️ SIMULADOR DE TRANSFERÊNCIA BANCÁRIA (DEFESA CSRF)", 
            font=("Segoe UI", 10, "bold"), 
            fg=COLOR_CYAN_GLOW, 
            bg=COLOR_CARD_BG
        )
        lbl_title.pack(anchor="w", padx=20, pady=(10, 2))

        lbl_desc = tk.Label(
            self.card_frame, 
            text="Um site malicioso tenta forjar uma transferência bancária silenciosa ($1.000) usando sua sessão ativa. Ative os mecanismos de defesa para verificar o bloqueio:", 
            font=("Segoe UI", 9), 
            fg=COLOR_TEXT_MAIN, 
            bg=COLOR_CARD_BG, 
            wraplength=610, 
            justify="left"
        )
        lbl_desc.pack(anchor="w", padx=20, pady=2)

        # Opções de Defesa
        opts_frame = tk.Frame(self.card_frame, bg=COLOR_CARD_BG)
        opts_frame.pack(fill="x", padx=20, pady=8)

        self.csrf_token_enabled = tk.BooleanVar(value=False)
        chk_token = tk.Checkbutton(
            opts_frame,
            text="Habilitar Token Anti-CSRF (Único e Imprevisível por Formulário)",
            variable=self.csrf_token_enabled,
            font=("Segoe UI", 9, "bold"),
            fg=COLOR_TEXT_MAIN,
            bg=COLOR_CARD_BG,
            selectcolor=COLOR_BG_TOP,
            activebackground=COLOR_CARD_BG,
            activeforeground=COLOR_CYAN_GLOW
        )
        chk_token.pack(anchor="w", pady=4)

        self.csrf_samesite_enabled = tk.BooleanVar(value=False)
        chk_samesite = tk.Checkbutton(
            opts_frame,
            text="Habilitar Cookie SameSite=Strict (Impede envio de cookie cross-site)",
            variable=self.csrf_samesite_enabled,
            font=("Segoe UI", 9, "bold"),
            fg=COLOR_TEXT_MAIN,
            bg=COLOR_CARD_BG,
            selectcolor=COLOR_BG_TOP,
            activebackground=COLOR_CARD_BG,
            activeforeground=COLOR_CYAN_GLOW
        )
        chk_samesite.pack(anchor="w", pady=4)

        btn_simulate = self.create_custom_button(self.card_frame, "🚨 Simular Requisição Forjada (Ataque Cross-Site)", self.evaluate_csrf_attack)
        btn_simulate.pack(fill="x", padx=20, pady=8)

        self.lbl_csrf_result = tk.Label(
            self.card_frame, 
            text="Status do Banco: Aguardando Tentativa de Requisição Cross-Site", 
            font=("Consolas", 9, "bold"), 
            fg=COLOR_WARNING, 
            bg=COLOR_BG_TOP, 
            bd=1, 
            relief="solid", 
            pady=8
        )
        self.lbl_csrf_result.pack(fill="x", padx=20, pady=4)

        self.btn_next2 = self.create_custom_button(self.card_frame, "Ir para o Quiz de Segurança Web ➔", self.load_quiz_mode)
        self.btn_next2.pack(fill="x", padx=20, pady=(8, 12))
        self.btn_next2.config(state="disabled")

    def evaluate_csrf_attack(self):
        token_active = self.csrf_token_enabled.get()
        samesite_active = self.csrf_samesite_enabled.get()

        if token_active or samesite_active:
            reasons = []
            if token_active:
                reasons.append("• Token Anti-CSRF ausente/inválido na requisição forjada pelo site malicioso.")
            if samesite_active:
                reasons.append("• Cookie de sessão bloqueado pelo navegador por ser uma requisição Cross-Site (SameSite=Strict).")

            reasons_str = "\n".join(reasons)
            messagebox.showinfo(
                "ATAQUE CSRF BLOQUEADO! 🛡️",
                f"As defesas configuradas impediram a transferência forjada com sucesso!\n\nMotivo(s) do Bloqueio:\n{reasons_str}"
            )
            self.lbl_csrf_result.config(text="✅ DECISÃO: TRANSFERÊNCIA BLOQUEADA (MECANISMO DE DEFESA ATIVO)", fg=COLOR_HEALTH)
            self.btn_next2.config(state="normal")
        else:
            messagebox.showerror(
                "ATAQUE BEM SUCEDIDO! 🚫",
                "TRANSFERÊNCIA DE $1.000 REALIZADA COM SUCESSO!\n\nSem Token Anti-CSRF e sem SameSite no Cookie, o navegador enviou automaticamente seus cookies de sessão autênticos ao responder à requisição do site malicioso."
            )
            self.lbl_csrf_result.config(text="❌ DECISÃO: TRANSFERÊNCIA FORJADA EXECUTADA COM SUCESSO!", fg=COLOR_INCORRECT)

    # ==========================================================================
    # --- ETAPA 3: QUIZ EDUCATIVO DA FASE 5 ---
    # ==========================================================================
    def load_quiz_mode(self):
        self.clear_card()
        self.lbl_mode.config(text=f"ETAPA 3/3 — QUIZ ({self.current_q + 1}/{len(QUIZ_FASE_5)})")

        q_data = QUIZ_FASE_5[self.current_q]

        lbl_cat = tk.Label(
            self.card_frame, 
            text=q_data["category"], 
            font=("Segoe UI", 10, "bold"), 
            fg=COLOR_CYAN_GLOW, 
            bg=COLOR_CARD_BG
        )
        lbl_cat.pack(anchor="w", padx=20, pady=(15, 5))

        lbl_q = tk.Label(
            self.card_frame, 
            text=q_data["question"], 
            font=("Segoe UI", 10), 
            fg=COLOR_TEXT_MAIN, 
            bg=COLOR_CARD_BG, 
            wraplength=600, 
            justify="left"
        )
        lbl_q.pack(anchor="w", padx=20, pady=10)

        self.quiz_buttons = []
        for i, opt in enumerate(q_data["options"]):
            btn = tk.Button(
                self.card_frame,
                text=opt,
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
                command=lambda idx=i: self.check_quiz_answer(idx)
            )
            btn.pack(fill="x", padx=20, pady=5, ipady=4)
            btn.bind("<Enter>", lambda e, b=btn: self.on_hover_enter(b))
            btn.bind("<Leave>", lambda e, b=btn: self.on_hover_leave(b))
            self.quiz_buttons.append(btn)

    def check_quiz_answer(self, selected_idx):
        for btn in self.quiz_buttons:
            btn.config(state="disabled")

        q_data = QUIZ_FASE_5[self.current_q]
        correct_idx = q_data["answer"]
        selected_btn = self.quiz_buttons[selected_idx]

        if selected_idx == correct_idx:
            selected_btn.config(bg=COLOR_CORRECT, fg="#000000")
            self.root.update()
            
            messagebox.showinfo(
                "Resposta Correta! 🎯", 
                f"{q_data['explanations'][selected_idx]}\n\n{q_data['tip']}"
            )
            
            self.current_q += 1
            if self.current_q < len(QUIZ_FASE_5):
                self.load_quiz_mode()
            else:
                messagebox.showinfo(
                    "Fase 5 Concluída com Sucesso! 🏆", 
                    "Parabéns! Você dominou os principais conceitos de Segurança Web: Prevenção contra XSS, Defesas Anti-CSRF, HTTPS e Cabeçalhos de Segurança como CSP!"
                )
                self.root.destroy()
        else:
            selected_btn.config(bg=COLOR_INCORRECT, fg="#FFFFFF")
            self.quiz_buttons[correct_idx].config(bg=COLOR_CORRECT, fg="#000000")
            self.root.update()
            
            messagebox.showerror(
                "Resposta Incorreta! ⚠️", 
                f"{q_data['explanations'][selected_idx]}\n\n{q_data['tip']}"
            )
            self.load_quiz_mode()  # Tenta novamente a mesma questão

if __name__ == "__main__":
    root = tk.Tk()
    
    # Centralização da Janela
    window_width = 700
    window_height = 640
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    position_right = int(screen_width/2 - window_width/2)
    position_top = int(screen_height/2 - window_height/2)
    root.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")

    app = Phase5App(root)
    root.mainloop()
=======
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
>>>>>>> 925aafaf53a0aea102ea91d0d7cfc7478c0e7b39
