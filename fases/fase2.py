import time
import string
import random
import itertools
import tkinter as tk
from tkinter import messagebox


# ==============================================================================
# --- PADRÃO DE DESIGN
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
# --- DADOS DAS PERGUNTAS DA FASE 2
# ==============================================================================

QUIZ_QUESTIONS = [

    {
        "category": "🟢 FASE 2 (NÍVEL 1) — MÚLTIPLOS FATORES (MFA)",

        "question":
            "Qual das opções abaixo oferece a melhor redução de risco "
            "no acesso a uma conta?",

        "options": [
            "A) Trocar a senha toda semana por uma frase curta",
            "B) Usar a mesma senha forte em todos os serviços bancários",
            "C) Usar uma senha forte e exclusiva combinada com MFA "
            "(Autenticação de Múltiplos Fatores)",
            "D) Salvar a senha no bloco de notas do computador"
        ],

        "answer": 2,

        "explanations": [
            "❌ INCORRETO: Senhas curtas continuam vulneráveis a força bruta, "
            "independente da frequência de troca.",

            "❌ INCORRETO: Reutilizar a mesma senha em múltiplos serviços "
            "cria o risco de vazamento em cascata.",

            "✅ CORRETO! A combinação de uma senha exclusiva com MFA cria "
            "duas camadas independentes de proteção.",

            "❌ INCORRETO: Arquivos de texto sem criptografia podem ser "
            "facilmente capturados por malwares locais."
        ]
    },

    {
        "category": "🟢 FASE 2 (NÍVEL 2) — GERENCIADORES DE SENHAS",

        "question":
            "Qual é a principal vantagem de utilizar um Gerenciador "
            "de Senhas homologado?",

        "options": [
            "A) Permite memorizar dezenas de senhas complexas sem anotações",

            "B) Gera e armazena senhas longas, aleatórias e únicas para "
            "cada serviço sob um cofre criptografado",

            "C) Elimina a necessidade de usar senhas ou códigos de verificação",

            "D) Impede que computadores contraiam vírus ao navegar na internet"
        ],

        "answer": 1,

        "explanations": [
            "❌ INCORRETO: Você não precisa memorizá-las; o cofre faz isso por você.",

            "✅ CORRETO! O gerenciador elimina o reuso de senhas e armazena "
            "tudo sob uma única senha-mestre forte.",

            "❌ INCORRETO: A senha-mestre e o MFA ainda são essenciais "
            "para proteger o cofre.",

            "❌ INCORRETO: O gerenciador protege credenciais, não a execução "
            "de arquivos maliciosos no sistema."
        ]
    },

    {
        "category": "🟢 FASE 2 (NÍVEL 3) — ENGENHARIA E CRED STUFFING",

        "question":
            "O que é um ataque de 'Credential Stuffing'?",

        "options": [
            "A) Tentativa de adivinhar o PIN de 4 dígitos do celular por força bruta",

            "B) Automatização que testa pares de login/senha vazados de um "
            "site em vários outros serviços",

            "C) Criptografia maliciosa dos arquivos do computador para exigir resgate",

            "D) Redirecionamento da navegação para um roteador wi-fi falso"
        ],

        "answer": 1,

        "explanations": [
            "❌ INCORRETO: Esse é um ataque direto de PIN ou força bruta simples.",

            "✅ CORRETO! Atacantes usam vazamentos antigos para invadir contas "
            "de pessoas que reutilizam a mesma senha.",

            "❌ INCORRETO: Isso descreve a atuação de um Ransomware.",

            "❌ INCORRETO: Trata-se de um ataque Man-in-the-Middle ou Rogue AP."
        ]
    }
]


# ==============================================================================
# --- APLICAÇÃO DA FASE 2
# ==============================================================================

class Phase2App:

    def __init__(self, root, proxima_fase=None):

        self.root = root
        self.proxima_fase = proxima_fase

        self.root.title(
            "CyberShield: Fase 2 — Gestão e Proteção de Senhas"
        )

        # ----------------------------------------------------------------------
        # TAMANHO INICIAL
        # ----------------------------------------------------------------------

        self.root.geometry("700x640")
        self.root.minsize(700, 640)

        # Permite redimensionar normalmente
        self.root.resizable(True, True)

        # ----------------------------------------------------------------------
        # CONTROLE DE TELA CHEIA
        # ----------------------------------------------------------------------

        self.fullscreen = False

        self.root.bind(
            "<F11>",
            self.toggle_fullscreen
        )

        self.root.bind(
            "<Escape>",
            self.exit_fullscreen
        )

        # ----------------------------------------------------------------------
        # VARIÁVEIS
        # ----------------------------------------------------------------------

        self.current_q = 0

        self.generated_mfa_token = ""
        self.mfa_time_left = 30
        self.mfa_timer_job = None

        # ----------------------------------------------------------------------
        # INTERFACE
        # ----------------------------------------------------------------------

        self.setup_ui()

        self.load_step_brute_force()

    # ==========================================================================
    # --- TELA CHEIA
    # ==========================================================================

    def toggle_fullscreen(self, event=None):

        self.fullscreen = not self.fullscreen

        self.root.attributes(
            "-fullscreen",
            self.fullscreen
        )

        self.update_layout()

    def exit_fullscreen(self, event=None):

        if self.fullscreen:

            self.fullscreen = False

            self.root.attributes(
                "-fullscreen",
                False
            )

            self.update_layout()

    # ==========================================================================
    # --- ATUALIZAR LAYOUT
    # ==========================================================================

    def update_layout(self):

        self.root.update_idletasks()

        width = self.root.winfo_width()
        height = self.root.winfo_height()

        if width < 700:
            width = 700

        if height < 640:
            height = 640

        self.bg_canvas.config(
            width=width,
            height=height
        )

        # ----------------------------------------------------------------------
        # HEADER
        # ----------------------------------------------------------------------

        self.bg_canvas.coords(
            self.status_window,
            width // 2,
            35
        )

        self.bg_canvas.itemconfig(
            self.status_window,
            width=width - 40
        )

        # ----------------------------------------------------------------------
        # CARD
        # ----------------------------------------------------------------------

        card_width = min(
            width - 40,
            1200
        )

        card_height = min(
            height - 100,
            800
        )

        self.bg_canvas.coords(
            self.card_window,
            width // 2,
            height // 2 + 25
        )

        self.bg_canvas.itemconfig(
            self.card_window,
            width=card_width,
            height=card_height
        )

        self.draw_cyber_background()

    # ==========================================================================
    # --- INTERFACE PRINCIPAL
    # ==========================================================================

    def setup_ui(self):

        self.bg_canvas = tk.Canvas(
            self.root,
            highlightthickness=0,
            bd=0
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

        self.status_window = self.bg_canvas.create_window(
            350,
            35,
            window=self.status_frame,
            width=660
        )

        # ----------------------------------------------------------------------
        # TÍTULO
        # ----------------------------------------------------------------------

        self.lbl_header = tk.Label(
            self.status_frame,
            text="🔑 FASE 2: GESTÃO & PROTEÇÃO DE SENHAS",
            font=("Consolas", 11, "bold"),
            fg=COLOR_HEALTH,
            bg=COLOR_BG_TOP
        )

        self.lbl_header.pack(
            side="left"
        )

        # ----------------------------------------------------------------------
        # BOTÃO TELA CHEIA
        # ----------------------------------------------------------------------

        self.btn_fullscreen = tk.Button(
            self.status_frame,
            text="⛶ TELA CHEIA",
            font=("Segoe UI", 9, "bold"),
            bg=COLOR_BTN_BG,
            fg=COLOR_TEXT_MUTED,
            activebackground=COLOR_BTN_HOVER,
            activeforeground=COLOR_TEXT_MAIN,
            relief="flat",
            cursor="hand2",
            bd=0,
            command=self.toggle_fullscreen
        )

        self.btn_fullscreen.pack(
            side="right",
            padx=(10, 0)
        )

        self.btn_fullscreen.bind(
            "<Enter>",
            lambda e: self.btn_fullscreen.config(
                bg=COLOR_BTN_HOVER,
                fg=COLOR_TEXT_MAIN
            )
        )

        self.btn_fullscreen.bind(
            "<Leave>",
            lambda e: self.btn_fullscreen.config(
                bg=COLOR_BTN_BG,
                fg=COLOR_TEXT_MUTED
            )
        )

        # ----------------------------------------------------------------------
        # ETAPA
        # ----------------------------------------------------------------------

        self.lbl_mode = tk.Label(
            self.status_frame,
            text="ETAPA 1/4",
            font=("Consolas", 11, "bold"),
            fg=COLOR_CYAN_GLOW,
            bg=COLOR_BG_TOP
        )

        self.lbl_mode.pack(
            side="right",
            padx=10
        )

        # ----------------------------------------------------------------------
        # CARD
        # ----------------------------------------------------------------------

        self.card_frame = tk.Frame(
            self.bg_canvas,
            bg=COLOR_CARD_BG,
            highlightbackground=COLOR_CARD_BORDER,
            highlightthickness=2,
            bd=0
        )

        self.card_window = self.bg_canvas.create_window(
            350,
            330,
            window=self.card_frame,
            width=660,
            height=520
        )

        # ----------------------------------------------------------------------
        # ATUALIZAÇÃO AUTOMÁTICA AO REDIMENSIONAR
        # ----------------------------------------------------------------------

        self.root.bind(
            "<Configure>",
            self.on_window_resize
        )

    # ==========================================================================
    # --- REDIMENSIONAMENTO
    # ==========================================================================

    def on_window_resize(self, event=None):

        if not self.root.winfo_exists():
            return

        self.root.after_idle(
            self.update_layout
        )

    # ==========================================================================
    # --- FUNDO
    # ==========================================================================

    def draw_cyber_background(self):

        self.bg_canvas.delete(
            "background"
        )

        width = max(
            self.root.winfo_width(),
            700
        )

        height = max(
            self.root.winfo_height(),
            640
        )

        r1, g1, b1 = self.hex_to_rgb(
            COLOR_BG_TOP
        )

        r2, g2, b2 = self.hex_to_rgb(
            COLOR_BG_BOTTOM
        )

        # ----------------------------------------------------------------------
        # DEGRADÊ
        # ----------------------------------------------------------------------

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
                fill=color,
                tags="background"
            )

        # ----------------------------------------------------------------------
        # CIRCUITOS
        # ----------------------------------------------------------------------

        line_color = "#0B3254"
        glow_dot = COLOR_CYAN_GLOW

        # Superior esquerdo

        self.bg_canvas.create_line(
            30,
            25,
            180,
            25,
            230,
            50,
            min(width - 30, 480),
            50,
            fill=line_color,
            width=1.5,
            tags="background"
        )

        self.bg_canvas.create_oval(
            177,
            22,
            183,
            28,
            fill=glow_dot,
            outline="",
            tags="background"
        )

        # Inferior

        y_bottom = height - 30

        self.bg_canvas.create_line(
            50,
            y_bottom,
            200,
            y_bottom,
            250,
            y_bottom - 20,
            max(550, width - 150),
            y_bottom - 20,
            fill=line_color,
            width=1.5,
            tags="background"
        )

        self.bg_canvas.create_oval(
            247,
            y_bottom - 23,
            253,
            y_bottom - 17,
            fill=glow_dot,
            outline="",
            tags="background"
        )

        self.bg_canvas.tag_lower(
            "background"
        )

    @staticmethod
    def hex_to_rgb(hex_str):

        hex_str = hex_str.lstrip("#")

        return tuple(
            int(hex_str[i:i + 2], 16)
            for i in (0, 2, 4)
        )

    # ==========================================================================
    # --- LIMPAR CARD
    # ==========================================================================

    def clear_card(self):

        if self.mfa_timer_job:

            try:

                self.root.after_cancel(
                    self.mfa_timer_job
                )

            except Exception:
                pass

            self.mfa_timer_job = None

        for widget in self.card_frame.winfo_children():

            widget.destroy()

    # ==========================================================================
    # --- BOTÃO PADRÃO
    # ==========================================================================

    def create_custom_button(
        self,
        parent,
        text,
        command
    ):

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
            lambda e, b=btn:
            self.on_hover_enter(b)
        )

        btn.bind(
            "<Leave>",
            lambda e, b=btn:
            self.on_hover_leave(b)
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
    # --- ETAPA 1: FORÇA BRUTA
    # ==========================================================================

    def load_step_brute_force(self):

        self.clear_card()

        self.lbl_mode.config(
            text="ETAPA 1/4 — FORÇA BRUTA"
        )

        lbl_title = tk.Label(
            self.card_frame,
            text="⚡ SIMULADOR DE ATAQUE DE FORÇA BRUTA",
            font=("Segoe UI", 10, "bold"),
            fg=COLOR_CYAN_GLOW,
            bg=COLOR_CARD_BG
        )

        lbl_title.pack(
            anchor="w",
            padx=20,
            pady=(15, 5)
        )

        lbl_desc = tk.Label(
            self.card_frame,
            text=(
                "Digite uma senha curta (até 4 letras minúsculas) "
                "para observar a velocidade com que um script "
                "automatizado consegue quebrá-la:"
            ),
            font=("Segoe UI", 9),
            fg=COLOR_TEXT_MAIN,
            bg=COLOR_CARD_BG,
            wraplength=1000,
            justify="left"
        )

        lbl_desc.pack(
            anchor="w",
            padx=20,
            pady=5
        )

        self.entry_pass = tk.Entry(
            self.card_frame,
            font=("Consolas", 11, "bold"),
            bg=COLOR_BG_TOP,
            fg=COLOR_CYAN_GLOW,
            insertbackground=COLOR_TEXT_MAIN,
            bd=1,
            relief="solid",
            justify="center"
        )

        self.entry_pass.insert(
            0,
            "gato"
        )

        self.entry_pass.pack(
            fill="x",
            padx=20,
            pady=5
        )

        btn_run = self.create_custom_button(
            self.card_frame,
            "▶️ Executar Ataque de Teste",
            self.run_brute_force
        )

        btn_run.pack(
            fill="x",
            padx=20,
            pady=8
        )

        self.txt_console = tk.Text(
            self.card_frame,
            height=9,
            font=("Consolas", 9),
            bg=COLOR_BG_TOP,
            fg=COLOR_TEXT_MUTED,
            bd=1,
            relief="solid",
            state="disabled"
        )

        self.txt_console.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=5
        )

        self.btn_next1 = self.create_custom_button(
            self.card_frame,
            "Avançar para Criador de Senha Forte ➔",
            self.load_step_password_checker
        )

        self.btn_next1.pack(
            fill="x",
            padx=20,
            pady=(5, 15)
        )

        self.btn_next1.config(
            state="disabled"
        )

    # ==========================================================================
    # --- FORÇA BRUTA
    # ==========================================================================

    def run_brute_force(self):

        senha = self.entry_pass.get().strip().lower()

        if (
            not senha
            or len(senha) > 4
            or not senha.isalpha()
        ):

            messagebox.showwarning(
                "Aviso",
                "Por favor, informe uma palavra contendo "
                "de 1 a 4 letras minúsculas.",
                parent=self.root
            )

            return

        caracteres = string.ascii_lowercase

        inicio = time.time()

        tentativas = 0
        descoberta = None

        for comp in range(
            1,
            len(senha) + 1
        ):

            for comb in itertools.product(
                caracteres,
                repeat=comp
            ):

                tentativas += 1

                palpite = "".join(comb)

                if palpite == senha:

                    descoberta = palpite

                    break

            if descoberta:
                break

        tempo_gasto = time.time() - inicio

        log = (
            "[!] Iniciando varredura por força bruta "
            "na wordlist automatizada...\n"
        )

        log += (
            f"[❌] SENHA DESCRIPTOGRAFADA: "
            f"'{descoberta}'\n"
        )

        log += (
            f"[*] Total de combinações testadas: "
            f"{tentativas:,}\n"
        )

        log += (
            f"[*] Tempo total de processamento: "
            f"{tempo_gasto:.4f} segundos\n\n"
        )

        log += (
            "⚠️ CONCLUSÃO TÉCNICA: Senhas curtas de padrão "
            "simples fornecem zero proteção contra ferramentas "
            "cibernéticas de varredura."
        )

        self.txt_console.config(
            state="normal"
        )

        self.txt_console.delete(
            "1.0",
            tk.END
        )

        self.txt_console.insert(
            tk.END,
            log
        )

        self.txt_console.config(
            state="disabled"
        )

        self.btn_next1.config(
            state="normal"
        )

    # ==========================================================================
    # --- ETAPA 2: SENHA FORTE
    # ==========================================================================

    def load_step_password_checker(self):

        self.clear_card()

        self.lbl_mode.config(
            text="ETAPA 2/4 — CRIAÇÃO SEGURA"
        )

        lbl_title = tk.Label(
            self.card_frame,
            text="🛡️ AVALIADOR DE COMPLEXIDADE DE SENHA",
            font=("Segoe UI", 10, "bold"),
            fg=COLOR_CYAN_GLOW,
            bg=COLOR_CARD_BG
        )

        lbl_title.pack(
            anchor="w",
            padx=20,
            pady=(15, 5)
        )

        lbl_desc = tk.Label(
            self.card_frame,
            text=(
                "Crie uma senha que atenda a todos os requisitos "
                "de segurança abaixo (mínimo 8 caracteres, "
                "maiúscula, minúscula, número e símbolo):"
            ),
            font=("Segoe UI", 9),
            fg=COLOR_TEXT_MAIN,
            bg=COLOR_CARD_BG,
            wraplength=1000,
            justify="left"
        )

        lbl_desc.pack(
            anchor="w",
            padx=20,
            pady=5
        )

        self.entry_strong_pass = tk.Entry(
            self.card_frame,
            font=("Consolas", 11, "bold"),
            bg=COLOR_BG_TOP,
            fg=COLOR_TEXT_MAIN,
            insertbackground=COLOR_TEXT_MAIN,
            bd=1,
            relief="solid",
            justify="center"
        )

        self.entry_strong_pass.pack(
            fill="x",
            padx=20,
            pady=5
        )

        self.entry_strong_pass.bind(
            "<KeyRelease>",
            self.evaluate_password_strength
        )

        self.canvas_strength = tk.Canvas(
            self.card_frame,
            height=12,
            bg=COLOR_BG_TOP,
            highlightthickness=1,
            highlightbackground=COLOR_CARD_BORDER
        )

        self.canvas_strength.pack(
            fill="x",
            padx=20,
            pady=5
        )

        self.frame_reqs = tk.Frame(
            self.card_frame,
            bg=COLOR_CARD_BG
        )

        self.frame_reqs.pack(
            fill="x",
            padx=20,
            pady=5
        )

        self.lbl_req_len = tk.Label(
            self.frame_reqs,
            text="❌ Pelo menos 8 caracteres",
            font=("Segoe UI", 9),
            fg=COLOR_INCORRECT,
            bg=COLOR_CARD_BG,
            anchor="w"
        )

        self.lbl_req_len.pack(fill="x")

        self.lbl_req_upper = tk.Label(
            self.frame_reqs,
            text="❌ Pelo menos 1 letra maiúscula (A-Z)",
            font=("Segoe UI", 9),
            fg=COLOR_INCORRECT,
            bg=COLOR_CARD_BG,
            anchor="w"
        )

        self.lbl_req_upper.pack(fill="x")

        self.lbl_req_lower = tk.Label(
            self.frame_reqs,
            text="❌ Pelo menos 1 letra minúscula (a-z)",
            font=("Segoe UI", 9),
            fg=COLOR_INCORRECT,
            bg=COLOR_CARD_BG,
            anchor="w"
        )

        self.lbl_req_lower.pack(fill="x")

        self.lbl_req_digit = tk.Label(
            self.frame_reqs,
            text="❌ Pelo menos 1 número (0-9)",
            font=("Segoe UI", 9),
            fg=COLOR_INCORRECT,
            bg=COLOR_CARD_BG,
            anchor="w"
        )

        self.lbl_req_digit.pack(fill="x")

        self.lbl_req_symbol = tk.Label(
            self.frame_reqs,
            text="❌ Pelo menos 1 símbolo (!@#$%^&*)",
            font=("Segoe UI", 9),
            fg=COLOR_INCORRECT,
            bg=COLOR_CARD_BG,
            anchor="w"
        )

        self.lbl_req_symbol.pack(fill="x")

        btn_generate = self.create_custom_button(
            self.card_frame,
            "🎲 Gerar Senha Segura Automática",
            self.generate_strong_password
        )

        btn_generate.pack(
            fill="x",
            padx=20,
            pady=8
        )

        self.btn_next2 = self.create_custom_button(
            self.card_frame,
            "Avançar para Simulação de Login 2FA ➔",
            self.load_step_mfa_login
        )

        self.btn_next2.pack(
            fill="x",
            padx=20,
            pady=(5, 15)
        )

        self.btn_next2.config(
            state="disabled"
        )

    # ==========================================================================
    # --- AVALIAR SENHA
    # ==========================================================================

    def evaluate_password_strength(self, event=None):

        pwd = self.entry_strong_pass.get()

        has_len = len(pwd) >= 8
        has_upper = any(c.isupper() for c in pwd)
        has_lower = any(c.islower() for c in pwd)
        has_digit = any(c.isdigit() for c in pwd)

        has_symbol = any(
            c in "!@#$%^&*()_+-=[]{}|;:,.<>?"
            for c in pwd
        )

        self.lbl_req_len.config(
            text=f"{'✅' if has_len else '❌'} "
                 "Pelo menos 8 caracteres",
            fg=COLOR_CORRECT if has_len else COLOR_INCORRECT
        )

        self.lbl_req_upper.config(
            text=f"{'✅' if has_upper else '❌'} "
                 "Pelo menos 1 letra maiúscula (A-Z)",
            fg=COLOR_CORRECT if has_upper else COLOR_INCORRECT
        )

        self.lbl_req_lower.config(
            text=f"{'✅' if has_lower else '❌'} "
                 "Pelo menos 1 letra minúscula (a-z)",
            fg=COLOR_CORRECT if has_lower else COLOR_INCORRECT
        )

        self.lbl_req_digit.config(
            text=f"{'✅' if has_digit else '❌'} "
                 "Pelo menos 1 número (0-9)",
            fg=COLOR_CORRECT if has_digit else COLOR_INCORRECT
        )

        self.lbl_req_symbol.config(
            text=f"{'✅' if has_symbol else '❌'} "
                 "Pelo menos 1 símbolo (!@#$%^&*)",
            fg=COLOR_CORRECT if has_symbol else COLOR_INCORRECT
        )

        score = sum([
            has_len,
            has_upper,
            has_lower,
            has_digit,
            has_symbol
        ])

        self.canvas_strength.delete(
            "all"
        )

        w = self.canvas_strength.winfo_width()

        fill_w = (w / 5) * score

        if score <= 2:

            color = COLOR_INCORRECT

        elif score <= 4:

            color = COLOR_WARNING

        else:

            color = COLOR_CORRECT

        self.canvas_strength.create_rectangle(
            0,
            0,
            fill_w,
            15,
            fill=color,
            outline=""
        )

        if score == 5:

            self.btn_next2.config(
                state="normal"
            )

        else:

            self.btn_next2.config(
                state="disabled"
            )

    # ==========================================================================
    # --- GERAR SENHA
    # ==========================================================================

    def generate_strong_password(self):

        chars = (
            string.ascii_letters
            + string.digits
            + "!@#$%^&*"
        )

        password = [
            random.choice(string.ascii_uppercase),
            random.choice(string.ascii_lowercase),
            random.choice(string.digits),
            random.choice("!@#$%^&*")
        ]

        password += [
            random.choice(chars)
            for _ in range(8)
        ]

        random.shuffle(
            password
        )

        res = "".join(
            password
        )

        self.entry_strong_pass.delete(
            0,
            tk.END
        )

        self.entry_strong_pass.insert(
            0,
            res
        )

        self.evaluate_password_strength()

    # ==========================================================================
    # --- ETAPA 3: LOGIN MFA
    # ==========================================================================

    def load_step_mfa_login(self):

        self.clear_card()

        self.lbl_mode.config(
            text="ETAPA 3/4 — LOGIN & MFA"
        )

        lbl_title = tk.Label(
            self.card_frame,
            text="🔐 AMBIENTE DE LOGIN SEGURO (MFA / 2FA)",
            font=("Segoe UI", 10, "bold"),
            fg=COLOR_CYAN_GLOW,
            bg=COLOR_CARD_BG
        )

        lbl_title.pack(
            anchor="w",
            padx=20,
            pady=(15, 5)
        )

        lbl_desc = tk.Label(
            self.card_frame,
            text=(
                "Mesmo com a senha correta, o acesso exige um "
                "código token temporário (MFA). Insira as "
                "credenciais e clique em 'Gerar Token':"
            ),
            font=("Segoe UI", 9),
            fg=COLOR_TEXT_MAIN,
            bg=COLOR_CARD_BG,
            wraplength=1000,
            justify="left"
        )

        lbl_desc.pack(
            anchor="w",
            padx=20,
            pady=5
        )

        frame_form = tk.Frame(
            self.card_frame,
            bg=COLOR_CARD_BG
        )

        frame_form.pack(
            fill="x",
            padx=20,
            pady=5
        )

        tk.Label(
            frame_form,
            text="Usuário:",
            font=("Segoe UI", 9, "bold"),
            fg=COLOR_TEXT_MUTED,
            bg=COLOR_CARD_BG
        ).grid(
            row=0,
            column=0,
            sticky="w",
            pady=2
        )

        self.entry_login_user = tk.Entry(
            frame_form,
            font=("Segoe UI", 10),
            bg=COLOR_BG_TOP,
            fg=COLOR_TEXT_MAIN,
            insertbackground=COLOR_TEXT_MAIN,
            bd=1,
            relief="solid"
        )

        self.entry_login_user.insert(
            0,
            "admin@cybershield.org"
        )

        self.entry_login_user.grid(
            row=0,
            column=1,
            sticky="ew",
            padx=10,
            pady=2
        )

        tk.Label(
            frame_form,
            text="Senha:",
            font=("Segoe UI", 9, "bold"),
            fg=COLOR_TEXT_MUTED,
            bg=COLOR_CARD_BG
        ).grid(
            row=1,
            column=0,
            sticky="w",
            pady=2
        )

        self.entry_login_pass = tk.Entry(
            frame_form,
            font=("Segoe UI", 10),
            show="•",
            bg=COLOR_BG_TOP,
            fg=COLOR_TEXT_MAIN,
            insertbackground=COLOR_TEXT_MAIN,
            bd=1,
            relief="solid"
        )

        self.entry_login_pass.insert(
            0,
            "SenhaSegura123!"
        )

        self.entry_login_pass.grid(
            row=1,
            column=1,
            sticky="ew",
            padx=10,
            pady=2
        )

        frame_form.grid_columnconfigure(
            1,
            weight=1
        )

        # ----------------------------------------------------------------------
        # TOKEN
        # ----------------------------------------------------------------------

        self.frame_token_box = tk.Frame(
            self.card_frame,
            bg=COLOR_BG_TOP,
            highlightbackground=COLOR_CARD_BORDER,
            highlightthickness=1
        )

        self.frame_token_box.pack(
            fill="x",
            padx=20,
            pady=10,
            ipady=5
        )

        self.lbl_mfa_display = tk.Label(
            self.frame_token_box,
            text="📲 GERADOR MFA: [ Clique para solicitar ]",
            font=("Consolas", 10, "bold"),
            fg=COLOR_WARNING,
            bg=COLOR_BG_TOP
        )

        self.lbl_mfa_display.pack()

        btn_get_mfa = self.create_custom_button(
            self.card_frame,
            "📱 Solicitar Código Token (SMS / App Authenticator)",
            self.request_mfa_token
        )

        btn_get_mfa.pack(
            fill="x",
            padx=20,
            pady=2
        )

        frame_mfa_input = tk.Frame(
            self.card_frame,
            bg=COLOR_CARD_BG
        )

        frame_mfa_input.pack(
            fill="x",
            padx=20,
            pady=8
        )

        tk.Label(
            frame_mfa_input,
            text="Digite o Token MFA:",
            font=("Segoe UI", 9, "bold"),
            fg=COLOR_TEXT_MAIN,
            bg=COLOR_CARD_BG
        ).pack(
            side="left"
        )

        self.entry_token_user = tk.Entry(
            frame_mfa_input,
            font=("Consolas", 12, "bold"),
            bg=COLOR_BG_TOP,
            fg=COLOR_CYAN_GLOW,
            insertbackground=COLOR_TEXT_MAIN,
            bd=1,
            relief="solid",
            width=10,
            justify="center"
        )

        self.entry_token_user.pack(
            side="left",
            padx=10
        )

        btn_login = self.create_custom_button(
            self.card_frame,
            "🚀 Autenticar Acesso no Sistema",
            self.verify_full_login
        )

        btn_login.pack(
            fill="x",
            padx=20,
            pady=5
        )

    # ==========================================================================
    # --- SOLICITAR TOKEN MFA
    # ==========================================================================

    def request_mfa_token(self):

        self.generated_mfa_token = str(
            random.randint(
                100000,
                999999
            )
        )

        self.mfa_time_left = 30

        self.update_mfa_timer()

    # ==========================================================================
    # --- TIMER MFA
    # ==========================================================================

    def update_mfa_timer(self):

        if self.mfa_time_left > 0:

            self.lbl_mfa_display.config(
                text=(
                    f"📲 TOKEN MFA: "
                    f"{self.generated_mfa_token} "
                    f"(Expira em {self.mfa_time_left}s)"
                ),
                fg=COLOR_HEALTH
            )

            self.mfa_time_left -= 1

            self.mfa_timer_job = self.root.after(
                1000,
                self.update_mfa_timer
            )

        else:

            self.generated_mfa_token = ""

            self.lbl_mfa_display.config(
                text="📲 TOKEN EXPIRADO! Solicite um novo código.",
                fg=COLOR_INCORRECT
            )

            self.mfa_timer_job = None

    # ==========================================================================
    # --- LOGIN MFA
    # ==========================================================================

    def verify_full_login(self):

        u = self.entry_login_user.get().strip()

        p = self.entry_login_pass.get().strip()

        tok = self.entry_token_user.get().strip()

        if not u or not p:

            messagebox.showwarning(
                "Erro de Validação",
                "Preencha o usuário e a senha!",
                parent=self.root
            )

            return

        if not self.generated_mfa_token:

            messagebox.showerror(
                "Acesso Negado",
                "Solicite um Token MFA válido antes de tentar o acesso.",
                parent=self.root
            )

            return

        if tok == self.generated_mfa_token:

            messagebox.showinfo(
                "Autenticação Concluída! 🔐",
                "Login bem-sucedido!\n\n"
                "A combinação da senha exclusiva com a validação "
                "em dois fatores (MFA) impediu o acesso não autorizado.",
                parent=self.root
            )

            self.load_quiz_mode()

        else:

            messagebox.showerror(
                "Falha no Login ❌",
                "Código MFA incorreto ou expirado! "
                "Verifique e tente novamente.",
                parent=self.root
            )

    # ==========================================================================
    # --- ETAPA 4: QUIZ
    # ==========================================================================

    def load_quiz_mode(self):

        self.clear_card()

        self.lbl_mode.config(
            text=(
                f"ETAPA 4/4 — QUIZ "
                f"({self.current_q + 1}/{len(QUIZ_QUESTIONS)})"
            )
        )

        q_data = QUIZ_QUESTIONS[
            self.current_q
        ]

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
            font=("Segoe UI", 11),
            fg=COLOR_TEXT_MAIN,
            bg=COLOR_CARD_BG,
            wraplength=1000,
            justify="left"
        )

        lbl_q.pack(
            anchor="w",
            padx=20,
            pady=10
        )

        self.quiz_buttons = []

        for i, opt in enumerate(
            q_data["options"]
        ):

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
                command=lambda idx=i:
                self.check_quiz_answer(idx)
            )

            btn.pack(
                fill="x",
                padx=20,
                pady=5,
                ipady=4
            )

            btn.bind(
                "<Enter>",
                lambda e, b=btn:
                self.on_hover_enter(b)
            )

            btn.bind(
                "<Leave>",
                lambda e, b=btn:
                self.on_hover_leave(b)
            )

            self.quiz_buttons.append(
                btn
            )

    # ==========================================================================
    # --- VERIFICAR QUIZ
    # ==========================================================================

    def check_quiz_answer(
        self,
        selected_idx
    ):

        for btn in self.quiz_buttons:

            btn.config(
                state="disabled"
            )

        q_data = QUIZ_QUESTIONS[
            self.current_q
        ]

        correct_idx = q_data["answer"]

        selected_btn = self.quiz_buttons[
            selected_idx
        ]

        if selected_idx == correct_idx:

            selected_btn.config(
                bg=COLOR_CORRECT,
                fg="#000000"
            )

            self.root.update()

            messagebox.showinfo(
                "Resposta Correta! 🎯",
                q_data["explanations"][selected_idx],
                parent=self.root
            )

            self.current_q += 1

            if self.current_q < len(QUIZ_QUESTIONS):

                self.load_quiz_mode()

            else:

                messagebox.showinfo(
                    "Fase 2 Concluída com Sucesso! 🏆",
                    "Parabéns! Você completou o Laboratório de Senhas, "
                    "praticou criação segura, autenticação MFA e "
                    "dominou a teoria!",
                    parent=self.root
                )

                self.finalizar_fase()

        else:

            selected_btn.config(
                bg=COLOR_INCORRECT,
                fg="#FFFFFF"
            )

            self.quiz_buttons[
                correct_idx
            ].config(
                bg=COLOR_CORRECT,
                fg="#000000"
            )

            self.root.update()

            messagebox.showerror(
                "Resposta Incorreta! ⚠️",
                q_data["explanations"][selected_idx],
                parent=self.root
            )

            self.load_quiz_mode()

    # ==========================================================================
    # --- FINALIZAÇÃO
    # ==========================================================================

    def finalizar_fase(self):

        if self.mfa_timer_job:

            try:

                self.root.after_cancel(
                    self.mfa_timer_job
                )

            except Exception:
                pass

            self.mfa_timer_job = None

        # ----------------------------------------------------------------------
        # NÃO destruir a janela.
        # O main.py controla a troca de fases.
        # ----------------------------------------------------------------------

        if self.proxima_fase:

            self.root.after(
                100,
                self.proxima_fase
            )


# ==============================================================================
# --- FUNÇÃO USADA PELO MAIN.PY
# ==============================================================================

def executar(
    root,
    proxima_fase=None
):

    return Phase2App(
        root,
        proxima_fase
    )


# ==============================================================================
# --- TESTE INDIVIDUAL
# ==============================================================================

if __name__ == "__main__":

    root = tk.Tk()

    executar(
        root
    )

    root.mainloop()