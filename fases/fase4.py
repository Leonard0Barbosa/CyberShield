import tkinter as tk
from tkinter import messagebox
import re

# ==============================================================================
# --- PADRÃO DE DESIGN (CYBER NETWORK - AZUL SUAVE & CIANO NEON) ---
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
COLOR_WARNING = "#FFD166"


# ==============================================================================
# --- BANCO DE PERGUNTAS DA FASE 4 ---
# ==============================================================================

QUIZ_FASE_4 = [
    {
        "category": "🌐 NAVEGAÇÃO SEGURA & PROTOCOLOS",
        "question": "Qual sinal indica a maior probabilidade de um site ser uma tentativa de golpe ou Phishing?",
        "options": [
            "A) O site utiliza o protocolo HTTPS com o ícone de cadeado",
            "B) O site carrega as imagens de forma lenta e desconfigurada",
            "C) O domínio na barra de endereços possui grafia ligeiramente alterada em relação ao site oficial",
            "D) O site contém muitos elementos multimídia e animações em vídeo"
        ],
        "answer": 2,
        "explanations": [
            "❌ INCORRETO: O HTTPS apenas criptografa o tráfego de dados; criminosos também obtêm certificados SSL para sites falsos.",
            "❌ INCORRETO: Lentidão é um problema de desempenho de servidor ou conexão, não um indicador direto de fraude.",
            "✅ CORRETO! Golpistas usam domínios parecidos (ex: banc0-oficial.com) para enganar o usuário desatento.",
            "❌ INCORRETO: A quantidade de elementos visuais é uma escolha de design, sem relação direta com a idoneidade do site."
        ],
        "tip": "💡 Dica: Sempre confira com atenção cada caractere da barra de endereços (URL)!"
    },

    {
        "category": "🔒 CRIPTOGRAFIA WEB & CERTIFICADOS",
        "question": "Um site exibe o ícone de 'Cadeado/HTTPS' na barra de endereços. O que esse certificado SSL/TLS garante exatamente?",
        "options": [
            "A) Garante que o site é 100% confiável, auditado e livre de malwares",
            "B) Garante apenas que a comunicação entre o navegador e o servidor está criptografada",
            "C) Garante que o site pertence obrigatoriamente a uma instituição bancária ou governamental",
            "D) Garante que os dados do usuário jamais serão vendidos ou compartilhados com terceiros"
        ],
        "answer": 1,
        "explanations": [
            "❌ INCORRETO: Sites maliciosos podem facilmente obter certificados SSL/TLS gratuitos.",
            "✅ CORRETO! O HTTPS impede a interceptação do tráfego no caminho (Man-in-the-Middle), mas você ainda pode estar enviando dados criptografados para um criminoso.",
            "❌ INCORRETO: Qualquer pessoa física ou jurídica pode registrar um domínio e obter um certificado SSL.",
            "❌ INCORRETO: O HTTPS protege os dados em trânsito, não a conduta ética da empresa que controla o site."
        ],
        "tip": "💡 Dica: HTTPS significa canal seguro, não garantia de um destinatário honesto!"
    },

    {
        "category": "🎣 ENGENHARIA SOCIAL & TYPOSQUATTING",
        "question": "Ao passar o ponteiro do mouse sobre um link em um e-mail, o rodapé mostra: 'https://suporte-security-update.com/login'. Como essa técnica de camuflagem é classificada?",
        "options": [
            "A) Ataque por Negação de Serviço Distribuído (DDoS)",
            "B) Engenharia Social por Typosquatting / Domínio Falso",
            "C) Injeção de código SQL em Banco de Dados (SQLi)",
            "D) Ataque de Força Bruta por Dicionário (Brute Force)"
        ],
        "answer": 1,
        "explanations": [
            "❌ INCORRETO: DDoS busca indisponibilizar sistemas por sobrecarga de acessos.",
            "✅ CORRETO! O atacante cria domínios parecidos com serviços reais usando palavras convincentes (suporte, atualização) para induzir o clique.",
            "❌ INCORRETO: SQL Injection explora falhas em bancos de dados, não camuflagem de URLs em e-mails.",
            "❌ INCORRETO: Força bruta consiste na tentativa massiva de adivinhar senhas."
        ],
        "tip": "💡 Dica: Sempre passe o mouse sobre o link (sem clicar) para inspecionar o destino real na barra de status!"
    },

    {
        "category": "🔗 ENCURTADORES DE LINK & REDIRECIONAMENTOS",
        "question": "Qual é o principal risco de segurança associado ao uso de encurtadores de URL (como bit.ly ou tinyurl) em mensagens não solicitadas?",
        "options": [
            "A) Eles infectam o sistema operacional instantaneamente no momento em que são exibidos na tela",
            "B) Eles ocultam o destino real do link, impedindo a verificação prévia do domínio final",
            "C) Eles desativam os antivírus e firewalls locais durante a navegação",
            "D) Eles alteram a senha das contas que estiverem abertas no navegador"
        ],
        "answer": 1,
        "explanations": [
            "❌ INCORRETO: A visualização de texto contendo uma URL encurtada não executa código no sistema.",
            "✅ CORRETO! Os encurtadores mascaram a URL final, impedindo que o usuário identifique que está sendo direcionado para um site malicioso sem usar um expansor de links.",
            "❌ INCORRETO: Encurtadores de URL não possuem privilégios para alterar configurações de segurança do sistema.",
            "❌ INCORRETO: Um redirecionamento de link não altera senhas de sessões ativas de forma automática."
        ],
        "tip": "💡 Dica: Utilize ferramentas de expansão de URL ('CheckShortURL') antes de clicar em links encurtados suspeitos!"
    },

    {
        "category": "🛑 ATAQUES PUNYCODE & HOMÓGRAFOS",
        "question": "O que é um 'Ataque Homográfico de IDN' (Internationalized Domain Name)?",
        "options": [
            "A) A criação de vírus que atacam especificamente servidores de nomes de domínio (DNS)",
            "B) O uso de caracteres de outros alfabetos (ex: cirílico) idênticos ao alfabeto latino para criar URLs falsas visualmente perfeitas",
            "C) A interceptação do tráfego Wi-Fi por meio de antenas direcionais falsas",
            "D) A alteração do arquivo 'hosts' do sistema para redirecionar IPs de bancos"
        ],
        "answer": 1,
        "explanations": [
            "❌ INCORRETO: Isso refere-se a ataques de envenenamento de cache DNS ou invasão de servidores.",
            "✅ CORRETO! Caracteres como o 'а' cirílico parecem idênticos ao 'a' latino, permitindo criar um site falso como 'аpple.com' que o olho humano não consegue distinguir.",
            "❌ INCORRETO: Isso refere-se a ataques de Evil Twin ou Wi-Fi Rogue.",
            "❌ INCORRETO: A alteração do arquivo hosts é um ataque local (Pharming), diferente do ataque homográfico no registro do domínio."
        ],
        "tip": "💡 Dica: Navegadores modernos convertem domínios com caracteres especiais para o formato 'xn--' (Punycode) para alertar o usuário."
    }
]


# ==============================================================================
# --- APLICAÇÃO DA FASE 4 ---
# ==============================================================================

class Phase4App:

    def __init__(self, root, proxima_fase=None):

        self.root = root
        self.proxima_fase = proxima_fase

        self.root.title(
            "CyberShield: Fase 4 — Internet, Links & Phishing"
        )

        self.root.geometry("700x640")
        self.root.resizable(False, False)

        self.current_q = 0

        # Controle para evitar chamada duplicada
        self.finalizando = False

        # Atributos do Simulador de Phishing
        self.phish_sender_var = None
        self.phish_link_var = None
        self.phish_urgency_var = None
        self.phish_attachment_var = None

        self.setup_ui()
        self.load_step_url_lab()

    # ==========================================================================
    # INTERFACE
    # ==========================================================================

    def setup_ui(self):

        self.bg_canvas = tk.Canvas(
            self.root,
            width=700,
            height=640,
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
            350,
            35,
            window=self.status_frame,
            width=660
        )

        self.lbl_header = tk.Label(
            self.status_frame,
            text="🛡️ FASE 4: INTERNET, LINKS & PHISHING",
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

        # ----------------------------------------------------------------------
        # CARD PRINCIPAL
        # ----------------------------------------------------------------------

        self.card_frame = tk.Frame(
            self.bg_canvas,
            bg=COLOR_CARD_BG,
            highlightbackground=COLOR_CARD_BORDER,
            highlightthickness=2,
            bd=0
        )

        self.bg_canvas.create_window(
            350,
            330,
            window=self.card_frame,
            width=660,
            height=520
        )

    # ==========================================================================
    # FUNDO
    # ==========================================================================

    def draw_cyber_background(self):

        width, height = 700, 640

        r1, g1, b1 = self.hex_to_rgb(COLOR_BG_TOP)
        r2, g2, b2 = self.hex_to_rgb(COLOR_BG_BOTTOM)

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

        line_color = "#0B3254"
        glow_dot = COLOR_CYAN_GLOW

        self.bg_canvas.create_line(
            30,
            25,
            180,
            25,
            230,
            50,
            480,
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
            477,
            47,
            483,
            53,
            fill=glow_dot,
            outline=""
        )

        self.bg_canvas.create_line(
            50,
            610,
            200,
            610,
            250,
            590,
            550,
            590,
            fill=line_color,
            width=1.5
        )

        self.bg_canvas.create_oval(
            247,
            587,
            253,
            593,
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
    # LIMPAR CARD
    # ==========================================================================

    def clear_card(self):

        for widget in self.card_frame.winfo_children():
            widget.destroy()

    # ==========================================================================
    # BOTÃO PADRÃO
    # ==========================================================================

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

        btn.bind(
            "<Enter>",
            lambda e, b=btn: self.on_hover_enter(b)
        )

        btn.bind(
            "<Leave>",
            lambda e, b=btn: self.on_hover_leave(b)
        )

        return btn

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
    # ETAPA 1 — LABORATÓRIO DE URLS
    # ==========================================================================

    def load_step_url_lab(self):

        self.clear_card()

        self.lbl_mode.config(
            text="ETAPA 1/3 — INSPEÇÃO DE URLS E DOMÍNIOS"
        )

        lbl_title = tk.Label(
            self.card_frame,
            text="🔍 LABORATÓRIO DE ANÁLISE DE URLS & TYPOSQUATTING",
            font=("Segoe UI", 10, "bold"),
            fg=COLOR_CYAN_GLOW,
            bg=COLOR_CARD_BG
        )

        lbl_title.pack(
            anchor="w",
            padx=20,
            pady=(12, 4)
        )

        lbl_desc = tk.Label(
            self.card_frame,
            text=(
                "Insira uma URL para analisar a estrutura do domínio. "
                "Teste com os exemplos fornecidos para identificar truques "
                "de camuflagem de atacantes:"
            ),
            font=("Segoe UI", 9),
            fg=COLOR_TEXT_MAIN,
            bg=COLOR_CARD_BG,
            wraplength=610,
            justify="left"
        )

        lbl_desc.pack(
            anchor="w",
            padx=20,
            pady=2
        )

        frame_input = tk.Frame(
            self.card_frame,
            bg=COLOR_CARD_BG
        )

        frame_input.pack(
            fill="x",
            padx=20,
            pady=5
        )

        tk.Label(
            frame_input,
            text="URL para Análise:",
            font=("Segoe UI", 9, "bold"),
            fg=COLOR_TEXT_MUTED,
            bg=COLOR_CARD_BG
        ).pack(anchor="w")

        self.entry_url_input = tk.Entry(
            frame_input,
            font=("Segoe UI", 10),
            bg=COLOR_BG_TOP,
            fg=COLOR_TEXT_MAIN,
            insertbackground=COLOR_TEXT_MAIN,
            bd=1,
            relief="solid"
        )

        self.entry_url_input.insert(
            0,
            "https://www.banc0-seguro-login.com/atualizacao"
        )

        self.entry_url_input.pack(
            fill="x",
            pady=2
        )

        self.entry_url_input.bind(
            "<KeyRelease>",
            self.update_live_url_analysis
        )

        frame_payloads = tk.Frame(
            frame_input,
            bg=COLOR_CARD_BG
        )

        frame_payloads.pack(
            fill="x",
            pady=2
        )

        btn_p1 = tk.Button(
            frame_payloads,
            text="⚡ Teste 1: Typosquatting",
            font=("Segoe UI", 8, "bold"),
            bg="#1B3B6F",
            fg=COLOR_CYAN_GLOW,
            activebackground=COLOR_BTN_HOVER,
            activeforeground=COLOR_TEXT_MAIN,
            relief="flat",
            cursor="hand2",
            command=lambda: self.set_url_payload(
                "https://www.banc0-seguro-login.com/atualizacao"
            )
        )

        btn_p1.pack(
            side="left",
            padx=(0, 5)
        )

        btn_p2 = tk.Button(
            frame_payloads,
            text="⚡ Teste 2: Subdomínio Falso",
            font=("Segoe UI", 8, "bold"),
            bg="#1B3B6F",
            fg=COLOR_CYAN_GLOW,
            activebackground=COLOR_BTN_HOVER,
            activeforeground=COLOR_TEXT_MAIN,
            relief="flat",
            cursor="hand2",
            command=lambda: self.set_url_payload(
                "https://www.meubanco.com.br.login-atendimento.net/auth"
            )
        )

        btn_p2.pack(
            side="left",
            padx=5
        )

        btn_p3 = tk.Button(
            frame_payloads,
            text="⚡ Teste 3: URL Oficial",
            font=("Segoe UI", 8, "bold"),
            bg="#1B3B6F",
            fg=COLOR_CYAN_GLOW,
            activebackground=COLOR_BTN_HOVER,
            activeforeground=COLOR_TEXT_MAIN,
            relief="flat",
            cursor="hand2",
            command=lambda: self.set_url_payload(
                "https://www.meubanco.com.br/login"
            )
        )

        btn_p3.pack(
            side="left",
            padx=5
        )

        tk.Label(
            self.card_frame,
            text="Decomposição da URL:",
            font=("Segoe UI", 9, "bold"),
            fg=COLOR_TEXT_MUTED,
            bg=COLOR_CARD_BG
        ).pack(
            anchor="w",
            padx=20,
            pady=(4, 1)
        )

        self.lbl_url_protocol = tk.Label(
            self.card_frame,
            text="",
            font=("Consolas", 8, "bold"),
            fg=COLOR_HEALTH,
            bg=COLOR_BG_TOP,
            bd=1,
            relief="solid",
            anchor="w",
            padx=10
        )

        self.lbl_url_protocol.pack(
            fill="x",
            padx=20,
            pady=2
        )

        self.lbl_url_domain = tk.Label(
            self.card_frame,
            text="",
            font=("Consolas", 8, "bold"),
            fg=COLOR_WARNING,
            bg=COLOR_BG_TOP,
            bd=1,
            relief="solid",
            anchor="w",
            padx=10
        )

        self.lbl_url_domain.pack(
            fill="x",
            padx=20,
            pady=2
        )

        self.lbl_url_status = tk.Label(
            self.card_frame,
            text="",
            font=("Segoe UI", 9, "bold"),
            bg=COLOR_CARD_BG,
            wraplength=600,
            justify="left"
        )

        self.lbl_url_status.pack(
            anchor="w",
            padx=20,
            pady=6
        )

        self.update_live_url_analysis()

        btn_next1 = self.create_custom_button(
            self.card_frame,
            "Avançar para o Analisador de E-mail Phishing ➔",
            self.load_step_phishing_lab
        )

        btn_next1.pack(
            fill="x",
            padx=20,
            pady=(6, 12)
        )

    def set_url_payload(self, url):

        self.entry_url_input.delete(
            0,
            tk.END
        )

        self.entry_url_input.insert(
            0,
            url
        )

        self.update_live_url_analysis()

    def update_live_url_analysis(self, event=None):

        url = self.entry_url_input.get().strip()

        protocol_match = re.match(
            r'^(https?://)',
            url,
            re.IGNORECASE
        )

        protocol = (
            protocol_match.group(1)
            if protocol_match
            else "HTTP (Não Seguro / Ausente)"
        )

        clean_url = re.sub(
            r'^(https?://)',
            '',
            url,
            flags=re.IGNORECASE
        )

        domain_part = (
            clean_url.split('/')[0]
            if '/' in clean_url
            else clean_url
        )

        self.lbl_url_protocol.config(
            text=f"PROTOCOLO: {protocol}"
        )

        self.lbl_url_domain.config(
            text=f"DOMÍNIO PRINCIPAL RECONHECIDO: {domain_part}"
        )

        alerts = []

        if "0" in domain_part or "1" in domain_part:

            alerts.append(
                "⚠️ Leet Speak / Substituição de letras por números detectada "
                "(ex: '0' no lugar de 'o')."
            )

        if domain_part.count(".") > 2:

            alerts.append(
                "⚠️ Múltiplos subdomínios encadeados. O domínio real é a "
                "última parte antes do TLD (.net, .com)."
            )

        if "-" in domain_part:

            alerts.append(
                "⚠️ Uso de hífen em nomes de marcas "
                "(técnica comum em Typosquatting)."
            )

        if not url.startswith("https://"):

            alerts.append(
                "❌ Conexão não criptografada (Sem HTTPS)."
            )

        if alerts:

            self.lbl_url_status.config(
                text="AMEAÇA DETECTADA:\n" + "\n".join(alerts),
                fg=COLOR_INCORRECT
            )

        else:

            self.lbl_url_status.config(
                text=(
                    "✅ ESTRUTURA NORMAL: O domínio aparenta seguir "
                    "padrões legítimos de formatação."
                ),
                fg=COLOR_HEALTH
            )

    # ==========================================================================
    # ETAPA 2 — SIMULADOR DE PHISHING
    # ==========================================================================

    def load_step_phishing_lab(self):

        self.clear_card()

        self.lbl_mode.config(
            text="ETAPA 2/3 — ANALISADOR DE PHISHING"
        )

        lbl_title = tk.Label(
            self.card_frame,
            text="🛡️ MINIGAME: MOTOR DE DETECÇÃO DE PHISHING EM E-MAILS",
            font=("Segoe UI", 10, "bold"),
            fg=COLOR_CYAN_GLOW,
            bg=COLOR_CARD_BG
        )

        lbl_title.pack(
            anchor="w",
            padx=20,
            pady=(10, 2)
        )

        lbl_desc = tk.Label(
            self.card_frame,
            text=(
                "Ajuste os parâmetros da mensagem recebida para simular "
                "a análise de um filtro Anti-Phishing de e-mail:"
            ),
            font=("Segoe UI", 9),
            fg=COLOR_TEXT_MAIN,
            bg=COLOR_CARD_BG,
            wraplength=610,
            justify="left"
        )

        lbl_desc.pack(
            anchor="w",
            padx=20,
            pady=2
        )

        grid_frame = tk.Frame(
            self.card_frame,
            bg=COLOR_CARD_BG
        )

        grid_frame.pack(
            fill="x",
            padx=20,
            pady=6
        )

        # Remetente
        tk.Label(
            grid_frame,
            text="Remetente:",
            font=("Segoe UI", 9, "bold"),
            fg=COLOR_TEXT_MUTED,
            bg=COLOR_CARD_BG
        ).grid(
            row=0,
            column=0,
            sticky="w",
            pady=3
        )

        self.phish_sender_var = tk.StringVar(
            value="suporte@seguranca-banco.com"
        )

        opt_sender = tk.OptionMenu(
            grid_frame,
            self.phish_sender_var,
            "suporte@seguranca-banco.com",
            "contato@bancooficial.com.br"
        )

        opt_sender.config(
            bg=COLOR_BTN_BG,
            fg=COLOR_TEXT_MAIN,
            activebackground=COLOR_BTN_HOVER,
            activeforeground=COLOR_TEXT_MAIN,
            highlightthickness=0,
            width=28
        )

        opt_sender.grid(
            row=0,
            column=1,
            sticky="w",
            padx=10,
            pady=3
        )

        # Urgência
        tk.Label(
            grid_frame,
            text="Tom da Mensagem:",
            font=("Segoe UI", 9, "bold"),
            fg=COLOR_TEXT_MUTED,
            bg=COLOR_CARD_BG
        ).grid(
            row=1,
            column=0,
            sticky="w",
            pady=3
        )

        self.phish_urgency_var = tk.StringVar(
            value="Urgente: Conta Bloqueada em 2h!"
        )

        opt_urgency = tk.OptionMenu(
            grid_frame,
            self.phish_urgency_var,
            "Urgente: Conta Bloqueada em 2h!",
            "Informativo: Seu Extrato Mensal"
        )

        opt_urgency.config(
            bg=COLOR_BTN_BG,
            fg=COLOR_TEXT_MAIN,
            activebackground=COLOR_BTN_HOVER,
            activeforeground=COLOR_TEXT_MAIN,
            highlightthickness=0,
            width=28
        )

        opt_urgency.grid(
            row=1,
            column=1,
            sticky="w",
            padx=10,
            pady=3
        )

        # Link
        tk.Label(
            grid_frame,
            text="Link de Destino:",
            font=("Segoe UI", 9, "bold"),
            fg=COLOR_TEXT_MUTED,
            bg=COLOR_CARD_BG
        ).grid(
            row=2,
            column=0,
            sticky="w",
            pady=3
        )

        self.phish_link_var = tk.StringVar(
            value="http://bit.ly/recuperar-senha"
        )

        opt_link = tk.OptionMenu(
            grid_frame,
            self.phish_link_var,
            "http://bit.ly/recuperar-senha",
            "https://bancooficial.com.br/extrato"
        )

        opt_link.config(
            bg=COLOR_BTN_BG,
            fg=COLOR_TEXT_MAIN,
            activebackground=COLOR_BTN_HOVER,
            activeforeground=COLOR_TEXT_MAIN,
            highlightthickness=0,
            width=28
        )

        opt_link.grid(
            row=2,
            column=1,
            sticky="w",
            padx=10,
            pady=3
        )

        # Anexo
        tk.Label(
            grid_frame,
            text="Arquivo Anexo:",
            font=("Segoe UI", 9, "bold"),
            fg=COLOR_TEXT_MUTED,
            bg=COLOR_CARD_BG
        ).grid(
            row=3,
            column=0,
            sticky="w",
            pady=3
        )

        self.phish_attachment_var = tk.StringVar(
            value="Comprovante.pdf.exe"
        )

        opt_attach = tk.OptionMenu(
            grid_frame,
            self.phish_attachment_var,
            "Comprovante.pdf.exe",
            "Sem Anexo / Nenhum"
        )

        opt_attach.config(
            bg=COLOR_BTN_BG,
            fg=COLOR_TEXT_MAIN,
            activebackground=COLOR_BTN_HOVER,
            activeforeground=COLOR_TEXT_MAIN,
            highlightthickness=0,
            width=28
        )

        opt_attach.grid(
            row=3,
            column=1,
            sticky="w",
            padx=10,
            pady=3
        )

        btn_eval = self.create_custom_button(
            self.card_frame,
            "⚙️ Executar Varredura Anti-Phishing",
            self.evaluate_phishing
        )

        btn_eval.pack(
            fill="x",
            padx=20,
            pady=6
        )

        self.lbl_phish_result = tk.Label(
            self.card_frame,
            text="Status: Aguardando Análise de Cabeçalho e Conteúdo",
            font=("Consolas", 9, "bold"),
            fg=COLOR_WARNING,
            bg=COLOR_BG_TOP,
            bd=1,
            relief="solid",
            pady=8
        )

        self.lbl_phish_result.pack(
            fill="x",
            padx=20,
            pady=4
        )

        self.btn_next2 = self.create_custom_button(
            self.card_frame,
            "Ir para o Quiz Conceitual Expandido ➔",
            self.load_quiz_mode
        )

        self.btn_next2.pack(
            fill="x",
            padx=20,
            pady=(8, 12)
        )

        self.btn_next2.config(
            state="disabled"
        )

    def evaluate_phishing(self):

        sender = self.phish_sender_var.get()
        urgency = self.phish_urgency_var.get()
        link = self.phish_link_var.get()
        attach = self.phish_attachment_var.get()

        flags = []

        if "seguranca-banco.com" in sender:
            flags.append(
                "❌ Domínio do remetente não oficial."
            )

        if "Urgente" in urgency:
            flags.append(
                "❌ Gatilho alarmista de urgência/falso senso de pânico."
            )

        if "bit.ly" in link or "http://" in link:
            flags.append(
                "❌ Uso de link encurtado/não seguro (HTTP)."
            )

        if ".exe" in attach:
            flags.append(
                "❌ Anexo com extensão executável dupla perigosa (.pdf.exe)."
            )

        if not flags:

            messagebox.showinfo(
                "E-MAIL LEGÍTIMO VERIFICADO! 🟢",
                "Nenhum indicador de comprometimento (IoC) foi encontrado.\n\n"
                "- Remetente Oficial\n"
                "- Comunicação Normal\n"
                "- Link Seguro com HTTPS\n"
                "- Sem Anexos Suspeitos",
                parent=self.root
            )

            self.lbl_phish_result.config(
                text="✅ DECISÃO: E-MAIL SEGURO / CAIXA DE ENTRADA",
                fg=COLOR_HEALTH
            )

            self.btn_next2.config(
                state="normal"
            )

        else:

            reason_str = "\n".join(flags)

            messagebox.showerror(
                "PHISHING DETECTADO! 🚨",
                "O motor de segurança identificou os seguintes "
                "alertas de ameaça:\n\n" + reason_str,
                parent=self.root
            )

            self.lbl_phish_result.config(
                text=f"❌ DECISÃO: AMEAÇA BLOQUEADA ({len(flags)} ALERTAS)",
                fg=COLOR_INCORRECT
            )

    # ==========================================================================
    # ETAPA 3 — QUIZ
    # ==========================================================================

    def load_quiz_mode(self):

        self.clear_card()

        self.lbl_mode.config(
            text=f"ETAPA 3/3 — QUIZ ({self.current_q + 1}/{len(QUIZ_FASE_4)})"
        )

        q_data = QUIZ_FASE_4[self.current_q]

        lbl_cat = tk.Label(
            self.card_frame,
            text=q_data["category"],
            font=("Segoe UI", 10, "bold"),
            fg=COLOR_CYAN_GLOW,
            bg=COLOR_CARD_BG
        )

        lbl_cat.pack(
            anchor="w",
            padx=20,
            pady=(15, 5)
        )

        lbl_q = tk.Label(
            self.card_frame,
            text=q_data["question"],
            font=("Segoe UI", 10),
            fg=COLOR_TEXT_MAIN,
            bg=COLOR_CARD_BG,
            wraplength=600,
            justify="left"
        )

        lbl_q.pack(
            anchor="w",
            padx=20,
            pady=10
        )

        self.quiz_buttons = []

        for i, opt in enumerate(q_data["options"]):

            btn = self.create_custom_button(
                self.card_frame,
                text=opt,
                command=lambda idx=i: self.check_quiz_answer(idx)
            )

            btn.config(
                anchor="w",
                justify="left",
                padx=15,
                pady=8
            )

            btn.pack(
                fill="x",
                padx=20,
                pady=4
            )

            self.quiz_buttons.append(btn)

    def check_quiz_answer(self, selected_idx):

        q_data = QUIZ_FASE_4[self.current_q]
        correct_idx = q_data["answer"]

        for btn in self.quiz_buttons:
            btn.config(
                state="disabled"
            )

        if selected_idx == correct_idx:

            self.quiz_buttons[selected_idx].config(
                bg=COLOR_CORRECT,
                fg="#000000"
            )

            messagebox.showinfo(
                "RESPOSTA CORRETA! 🎯",
                f"{q_data['explanations'][selected_idx]}\n\n"
                f"{q_data['tip']}",
                parent=self.root
            )

        else:

            self.quiz_buttons[selected_idx].config(
                bg=COLOR_INCORRECT,
                fg="#FFFFFF"
            )

            self.quiz_buttons[correct_idx].config(
                bg=COLOR_CORRECT,
                fg="#000000"
            )

            messagebox.showerror(
                "RESPOSTA INCORRETA! ❌",
                f"{q_data['explanations'][selected_idx]}\n\n"
                f"{q_data['tip']}",
                parent=self.root
            )

        self.current_q += 1

        if self.current_q < len(QUIZ_FASE_4):

            self.root.after(
                800,
                self.load_quiz_mode
            )

        else:

            self.root.after(
                800,
                self.finish_phase
            )

    # ==========================================================================
    # FINALIZAR FASE 4
    # ==========================================================================

    def finish_phase(self):

        if self.finalizando:
            return

        self.finalizando = True

        self.clear_card()

        self.lbl_mode.config(
            text="FASE CONCLUÍDA"
        )

        lbl_end = tk.Label(
            self.card_frame,
            text="🚀 FASE 4 CONCLUÍDA COM SUCESSO!",
            font=("Segoe UI", 12, "bold"),
            fg=COLOR_HEALTH,
            bg=COLOR_CARD_BG
        )

        lbl_end.pack(
            pady=(40, 10)
        )

        lbl_sub = tk.Label(
            self.card_frame,
            text=(
                "Você dominou a inspeção de URLs, identificou ataques "
                "de Typosquatting/Phishing e compreendeu o funcionamento "
                "real do protocolo HTTPS.\n\n"
                "Sistema protegido contra links maliciosos!"
            ),
            font=("Segoe UI", 10),
            fg=COLOR_TEXT_MAIN,
            bg=COLOR_CARD_BG,
            wraplength=550,
            justify="center"
        )

        lbl_sub.pack(
            pady=10
        )

        # ----------------------------------------------------------------------
        # AGORA O CONTROLE VOLTA PARA O MAIN.PY
        # ----------------------------------------------------------------------

        btn_next = self.create_custom_button(
            self.card_frame,
            "Avançar para a Próxima Fase ➜",
            self.avancar_para_proxima_fase
        )

        btn_next.pack(
            pady=30,
            padx=20,
            fill="x"
        )

    # ==========================================================================
    # CHAMAR PRÓXIMA FASE
    # ==========================================================================

    def avancar_para_proxima_fase(self):

        if self.proxima_fase:

            self.proxima_fase()

        else:

            messagebox.showinfo(
                "Fim do módulo",
                "A Fase 4 foi concluída!",
                parent=self.root
            )


# ==============================================================================
# FUNÇÃO COMPATÍVEL COM O MAIN.PY
# ==============================================================================

def executar(root, proxima_fase=None):

    return Phase4App(
        root,
        proxima_fase
    )


# ==============================================================================
# EXECUÇÃO INDIVIDUAL
# ==============================================================================

if __name__ == "__main__":

    root = tk.Tk()

    app = Phase4App(root)

    root.mainloop()