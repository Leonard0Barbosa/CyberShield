import tkinter as tk
from tkinter import messagebox


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
# --- BANCO DE PERGUNTAS DA FASE 7 ---
# ==============================================================================

QUIZ_FASE_7 = [

    {
        "category": "🗄️ SEGURANÇA EM BANCO DE DADOS",

        "question":
            "Qual é a técnica primária e mais eficaz para mitigar vulnerabilidades "
            "de SQL Injection (SQLi) em aplicações web?",

        "options": [
            "A) Ocultar a estrutura da tabela utilizando nomes codificados",
            "B) Utilizar Prepared Statements (Consultas Parametrizadas)",
            "C) Bloquear completamente o uso do caractere ponto e vírgula (;)",
            "D) Criptografar o banco de dados inteiro com AES-256"
        ],

        "answer": 1,

        "explanations": [
            "❌ INCORRETO: Mudar nomes de tabelas é 'segurança por obscuridade' e não previne injeção.",

            "✅ CORRETO! Prepared Statements separam o código SQL dos dados fornecidos "
            "pelo usuário, impedindo que entradas maliciosas alterem a lógica da query.",

            "❌ INCORRETO: Apenas filtrar um caractere específico (blacklist) é facilmente burlado por atacantes.",

            "❌ INCORRETO: Criptografar os dados gravados não previne que a aplicação "
            "execute queries maliciosas no banco."
        ],

        "tip":
            "💡 Dica: Nunca concatene entradas do usuário diretamente no texto do comando SQL!"
    },

    {
        "category": "🔑 GESTÃO DE CREDENCIAIS & HASHING",

        "question":
            "Como as senhas dos usuários devem ser armazenadas de forma segura "
            "em uma tabela do banco de dados?",

        "options": [
            "A) Em texto puro para facilitar a recuperação de senha",

            "B) Criptografadas com chave simétrica salva no próprio código da aplicação",

            "C) Aplicando funções de Hash criptográfico fortes "
            "(ex: bcrypt, Argon2) com Salt único",

            "D) Utilizando codificação Base64 para ocultar os caracteres"
        ],

        "answer": 2,

        "explanations": [
            "❌ INCORRETO: Armazenar senhas em texto puro é uma falha grave "
            "que expõe os dados em caso de vazamento.",

            "❌ INCORRETO: Chaves simétricas podem ser extraídas da aplicação "
            "se o código for comprometido.",

            "✅ CORRETO! Hashes unidirecionais lentos com Salt impedem a reversão "
            "e dificultam ataques de Rainbow Tables.",

            "❌ INCORRETO: Base64 é apenas um formato de codificação, "
            "não de criptografia ou segurança. Pode ser facilmente decodificado."
        ],

        "tip":
            "💡 Dica: Senhas nunca devem ser reversíveis! Utilize algoritmos de hashing com Salt."
    },

    {
        "category": "🛡️ MODELOS DE CONTROLE DE ACESSO",

        "question":
            "O que caracteriza o modelo ABAC (Attribute-Based Access Control) "
            "em comparação ao modelo RBAC?",

        "options": [
            "A) O acesso é concedido baseado exclusivamente no cargo (Role) do usuário",

            "B) As permissões consideram atributos do sujeito, do recurso, "
            "da ação e do contexto (ex: horário, IP)",

            "C) Cada proprietário de arquivo decide individualmente quem pode acessá-lo",

            "D) O acesso é determinado de forma estática pelo sistema operacional "
            "sem regras dinâmicas"
        ],

        "answer": 1,

        "explanations": [
            "❌ INCORRETO: Isso descreve o modelo RBAC (Role-Based Access Control).",

            "✅ CORRETO! O ABAC avalia políticas dinâmicas utilizando múltiplos "
            "atributos contextuais e do recurso.",

            "❌ INCORRETO: Isso descreve o modelo DAC (Discretionary Access Control).",

            "❌ INCORRETO: O ABAC é um modelo altamente dinâmico e granular, "
            "não estático."
        ],

        "tip":
            "💡 Dica: ABAC permite regras como: 'Apenas acessar se for horário "
            "comercial E o IP for da VPN interna'."
    },

    {
        "category": "📜 PRINCÍPIO DO MENOR PRIVILÉGIO (POLEP)",

        "question":
            "Ao configurar a conta de conexão do banco de dados que a aplicação "
            "web utiliza, qual é a boa prática recomendada?",

        "options": [
            "A) Utilizar o usuário 'root' ou 'sa' para garantir que nenhuma query "
            "falhe por falta de acesso",

            "B) Conceder apenas as permissões estritamente necessárias "
            "(ex: SELECT, INSERT) nas tabelas específicas que a aplicação usa",

            "C) Liberar permissão de DROP e ALTER TABLE para facilitar atualizações "
            "automáticas do sistema",

            "D) Desativar o sistema de privilégios do banco de dados "
            "para melhorar a performance de leitura"
        ],

        "answer": 1,

        "explanations": [
            "❌ INCORRETO: Conectar como superusuário amplifica drasticamente "
            "o dano de qualquer vulnerabilidade como SQLi.",

            "✅ CORRETO! O Princípio do Menor Privilégio garante que, se a aplicação "
            "for invadida, o atacante não poderá apagar o banco ou alterar esquemas.",

            "❌ INCORRETO: Permissões de DDL (DROP, ALTER) não devem ser concedidas "
            "à conta de execução diária da aplicação.",

            "❌ INCORRETO: Desativar controles de acesso expõe o banco a comprometimento total."
        ],

        "tip":
            "💡 Dica: Se a aplicação só lê notícias, a conta do banco precisa apenas do privilégio SELECT!"
    }
]


# ==============================================================================
# --- CLASSE PRINCIPAL DA FASE 7 ---
# ==============================================================================

class Phase7App:

    def __init__(self, root, ao_concluir=None):

        self.root = root
        self.ao_concluir = ao_concluir

        self.root.title(
            "CyberShield: Fase 7 — Banco de Dados & Acessos"
        )

        self.root.geometry("700x640")

        self.root.minsize(
            660,
            560
        )

        self.root.resizable(
            True,
            True
        )

        # ----------------------------------------------------------------------
        # TELA CHEIA
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
        # ESTADO
        # ----------------------------------------------------------------------

        self.current_q = 0

        self.abac_role_var = None
        self.abac_time_var = None
        self.abac_loc_var = None
        self.abac_sens_var = None

        self.resize_job = None

        self.setup_ui()
        self.load_step_sqli_lab()

        self.root.bind(
            "<Configure>",
            self.on_window_resize
        )

        self.root.update_idletasks()
        self.update_layout()


    # ==========================================================================
    # --- TELA CHEIA
    # ==========================================================================

    def toggle_fullscreen(self, event=None):

        self.fullscreen = not self.fullscreen

        self.root.attributes(
            "-fullscreen",
            self.fullscreen
        )

        if self.fullscreen:

            self.btn_fullscreen.config(
                text="🗗 SAIR DA TELA CHEIA"
            )

        else:

            self.btn_fullscreen.config(
                text="⛶ TELA CHEIA"
            )

        self.root.update_idletasks()
        self.update_layout()

        return "break"


    def exit_fullscreen(self, event=None):

        if self.fullscreen:

            self.fullscreen = False

            self.root.attributes(
                "-fullscreen",
                False
            )

            self.btn_fullscreen.config(
                text="⛶ TELA CHEIA"
            )

            self.root.update_idletasks()
            self.update_layout()

        return "break"


    # ==========================================================================
    # --- REDIMENSIONAMENTO
    # ==========================================================================

    def on_window_resize(self, event=None):

        if event is not None:

            if event.widget != self.root:
                return

        if self.resize_job:

            try:
                self.root.after_cancel(
                    self.resize_job
                )
            except Exception:
                pass

        self.resize_job = self.root.after(
            50,
            self.update_layout
        )


    def update_layout(self):

        self.resize_job = None

        width = self.root.winfo_width()
        height = self.root.winfo_height()

        if width < 1 or height < 1:
            return

        self.draw_cyber_background(
            width,
            height
        )

        # ----------------------------------------------------------------------
        # HEADER
        # ----------------------------------------------------------------------

        header_width = max(
            500,
            int(width * 0.94)
        )

        header_width = min(
            header_width,
            width - 30
        )

        self.bg_canvas.coords(
            self.header_window,
            width / 2,
            max(
                35,
                height * 0.055
            )
        )

        self.bg_canvas.itemconfig(
            self.header_window,
            width=header_width
        )

        # ----------------------------------------------------------------------
        # CARD
        # ----------------------------------------------------------------------

        card_width = min(
            int(width * 0.92),
            1200
        )

        card_height = min(
            int(height * 0.80),
            760
        )

        card_width = max(
            card_width,
            620
        )

        card_height = max(
            card_height,
            430
        )

        card_width = min(
            card_width,
            width - 30
        )

        card_height = min(
            card_height,
            height - 100
        )

        card_y = height * 0.54

        self.bg_canvas.coords(
            self.card_window,
            width / 2,
            card_y
        )

        self.bg_canvas.itemconfig(
            self.card_window,
            width=card_width,
            height=card_height
        )

        # ----------------------------------------------------------------------
        # WRAPLENGTH
        # ----------------------------------------------------------------------

        content_wrap = max(
            450,
            card_width - 60
        )

        for widget in self.card_frame.winfo_children():

            if isinstance(
                widget,
                tk.Label
            ):

                try:

                    current_wrap = int(
                        widget.cget(
                            "wraplength"
                        )
                    )

                    if current_wrap > 0:

                        widget.config(
                            wraplength=content_wrap
                        )

                except Exception:
                    pass


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

        # ----------------------------------------------------------------------
        # HEADER
        # ----------------------------------------------------------------------

        self.status_frame = tk.Frame(
            self.bg_canvas,
            bg=COLOR_BG_TOP
        )

        self.header_window = self.bg_canvas.create_window(
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
            text="🛡️ FASE 7: BANCO DE DADOS & ACESSOS",
            font=("Consolas", 11, "bold"),
            fg=COLOR_HEALTH,
            bg=COLOR_BG_TOP
        )

        self.lbl_header.pack(
            side="left"
        )

        # ----------------------------------------------------------------------
        # TELA CHEIA
        # ----------------------------------------------------------------------

        self.btn_fullscreen = tk.Button(
            self.status_frame,
            text="⛶ TELA CHEIA",
            font=("Consolas", 9, "bold"),
            bg=COLOR_BTN_BG,
            fg=COLOR_TEXT_MUTED,
            activebackground=COLOR_BTN_HOVER,
            activeforeground=COLOR_TEXT_MAIN,
            relief="flat",
            bd=0,
            cursor="hand2",
            command=self.toggle_fullscreen
        )

        self.btn_fullscreen.pack(
            side="right",
            padx=(10, 0)
        )

        self.btn_fullscreen.bind(
            "<Enter>",
            lambda e:
            self.btn_fullscreen.config(
                bg=COLOR_BTN_HOVER,
                fg=COLOR_TEXT_MAIN
            )
        )

        self.btn_fullscreen.bind(
            "<Leave>",
            lambda e:
            self.btn_fullscreen.config(
                bg=COLOR_BTN_BG,
                fg=COLOR_TEXT_MUTED
            )
        )

        # ----------------------------------------------------------------------
        # ETAPA
        # ----------------------------------------------------------------------

        self.lbl_mode = tk.Label(
            self.status_frame,
            text="ETAPA 1/3",
            font=("Consolas", 11, "bold"),
            fg=COLOR_CYAN_GLOW,
            bg=COLOR_BG_TOP
        )

        self.lbl_mode.pack(
            side="right",
            padx=20
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


    # ==========================================================================
    # --- FUNDO CYBER RESPONSIVO
    # ==========================================================================

    def draw_cyber_background(
        self,
        width=None,
        height=None
    ):

        if width is None:
            width = max(
                self.root.winfo_width(),
                680
            )

        if height is None:
            height = max(
                self.root.winfo_height(),
                600
            )

        self.bg_canvas.delete(
            "background"
        )

        r1, g1, b1 = self.hex_to_rgb(
            COLOR_BG_TOP
        )

        r2, g2, b2 = self.hex_to_rgb(
            COLOR_BG_BOTTOM
        )

        # ----------------------------------------------------------------------
        # GRADIENTE
        # ----------------------------------------------------------------------

        for y in range(height):

            r = int(
                r1 +
                (r2 - r1) *
                (y / height)
            )

            g = int(
                g1 +
                (g2 - g1) *
                (y / height)
            )

            b = int(
                b1 +
                (b2 - b1) *
                (y / height)
            )

            color = (
                f"#{r:02x}{g:02x}{b:02x}"
            )

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

        x1 = int(width * 0.04)
        x2 = int(width * 0.25)
        x3 = int(width * 0.32)
        x4 = int(width * 0.68)

        y1 = int(height * 0.045)
        y2 = int(height * 0.09)

        self.bg_canvas.create_line(
            x1,
            y1,
            x2,
            y1,
            x3,
            y2,
            x4,
            y2,
            fill=line_color,
            width=2,
            tags="background"
        )

        self.bg_canvas.create_oval(
            x2 - 3,
            y1 - 3,
            x2 + 3,
            y1 + 3,
            fill=glow_dot,
            outline="",
            tags="background"
        )

        self.bg_canvas.create_oval(
            x4 - 3,
            y2 - 3,
            x4 + 3,
            y2 + 3,
            fill=glow_dot,
            outline="",
            tags="background"
        )

        # ----------------------------------------------------------------------
        # CIRCUITO INFERIOR
        # ----------------------------------------------------------------------

        y3 = int(height * 0.94)
        y4 = int(height * 0.91)

        x5 = int(width * 0.06)
        x6 = int(width * 0.25)
        x7 = int(width * 0.32)
        x8 = int(width * 0.78)

        self.bg_canvas.create_line(
            x5,
            y3,
            x6,
            y3,
            x7,
            y4,
            x8,
            y4,
            fill=line_color,
            width=2,
            tags="background"
        )

        self.bg_canvas.create_oval(
            x7 - 3,
            y4 - 3,
            x7 + 3,
            y4 + 3,
            fill=glow_dot,
            outline="",
            tags="background"
        )

        self.bg_canvas.create_oval(
            x8 - 3,
            y4 - 3,
            x8 + 3,
            y4 + 3,
            fill=glow_dot,
            outline="",
            tags="background"
        )

        self.bg_canvas.tag_lower(
            "background"
        )


    # ==========================================================================
    # --- HEX → RGB
    # ==========================================================================

    @staticmethod
    def hex_to_rgb(hex_str):

        hex_str = hex_str.lstrip("#")

        return tuple(
            int(
                hex_str[i:i + 2],
                16
            )
            for i in (0, 2, 4)
        )


    # ==========================================================================
    # --- LIMPAR CARD
    # ==========================================================================

    def clear_card(self):

        for widget in self.card_frame.winfo_children():

            widget.destroy()


    # ==========================================================================
    # --- BOTÕES
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
    # --- ETAPA 1: SQL INJECTION
    # ==========================================================================

    def load_step_sqli_lab(self):

        self.clear_card()

        self.lbl_mode.config(
            text="ETAPA 1/3 — LABORATÓRIO DE INJEÇÃO SQL"
        )

        lbl_title = tk.Label(
            self.card_frame,
            text="💉 LABORATÓRIO DE INJEÇÃO SQL (SQLi) VS PREPARED STATEMENTS",
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
                "Digite um nome de usuário. Experimente usar a payload "
                "maliciosa ' OR '1'='1 para ver como a consulta vulnerável "
                "é alterada, comparada à segura:"
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
            text="Entrada do Usuário:",
            font=("Segoe UI", 9, "bold"),
            fg=COLOR_TEXT_MUTED,
            bg=COLOR_CARD_BG
        ).pack(
            anchor="w"
        )

        self.entry_user_input = tk.Entry(
            frame_input,
            font=("Segoe UI", 10),
            bg=COLOR_BG_TOP,
            fg=COLOR_TEXT_MAIN,
            insertbackground=COLOR_TEXT_MAIN,
            bd=1,
            relief="solid"
        )

        self.entry_user_input.insert(
            0,
            "' OR '1'='1"
        )

        self.entry_user_input.pack(
            fill="x",
            pady=2
        )

        self.entry_user_input.bind(
            "<KeyRelease>",
            self.update_live_sqli
        )

        btn_quick_payload = tk.Button(
            frame_input,
            text="⚡ Inserir Payload SQLi: ' OR '1'='1",
            font=("Segoe UI", 8, "bold"),
            bg="#1B3B6F",
            fg=COLOR_CYAN_GLOW,
            activebackground=COLOR_BTN_HOVER,
            activeforeground=COLOR_TEXT_MAIN,
            relief="flat",
            cursor="hand2",
            command=self.insert_sqli_payload
        )

        btn_quick_payload.pack(
            anchor="e",
            pady=2
        )

        tk.Label(
            self.card_frame,
            text="1. Consulta Vulnerável (Concatenação de Strings):",
            font=("Segoe UI", 9, "bold"),
            fg=COLOR_INCORRECT,
            bg=COLOR_CARD_BG
        ).pack(
            anchor="w",
            padx=20,
            pady=(4, 1)
        )

        self.lbl_vuln_sql = tk.Label(
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

        self.lbl_vuln_sql.pack(
            fill="x",
            padx=20,
            pady=2
        )

        tk.Label(
            self.card_frame,
            text="2. Consulta Segura (Prepared Statement / Parametrizada):",
            font=("Segoe UI", 9, "bold"),
            fg=COLOR_CORRECT,
            bg=COLOR_CARD_BG
        ).pack(
            anchor="w",
            padx=20,
            pady=(4, 1)
        )

        self.lbl_safe_sql = tk.Label(
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

        self.lbl_safe_sql.pack(
            fill="x",
            padx=20,
            pady=2
        )

        self.lbl_sqli_status = tk.Label(
            self.card_frame,
            text="",
            font=("Segoe UI", 9, "bold"),
            bg=COLOR_CARD_BG
        )

        self.lbl_sqli_status.pack(
            anchor="w",
            padx=20,
            pady=4
        )

        self.update_live_sqli()

        btn_next1 = self.create_custom_button(
            self.card_frame,
            "Avançar para o Simulador de Controle de Acesso ABAC ➔",
            self.load_step_abac_lab
        )

        btn_next1.pack(
            fill="x",
            padx=20,
            pady=(6, 12)
        )

        self.root.after(
            50,
            self.update_layout
        )


    def insert_sqli_payload(self):

        self.entry_user_input.delete(
            0,
            tk.END
        )

        self.entry_user_input.insert(
            0,
            "' OR '1'='1"
        )

        self.update_live_sqli()


    def update_live_sqli(self, event=None):

        if not hasattr(
            self,
            "entry_user_input"
        ):
            return

        user_in = self.entry_user_input.get()

        vuln_query = (
            f"SELECT * FROM usuarios WHERE "
            f"username = '{user_in}' AND status = 'ATIVO';"
        )

        self.lbl_vuln_sql.config(
            text=vuln_query
        )

        safe_query = (
            "SELECT * FROM usuarios WHERE "
            "username = ? AND status = 'ATIVO';\n"
            "[Parâmetro 1 = " +
            repr(user_in) +
            "]"
        )

        self.lbl_safe_sql.config(
            text=safe_query
        )

        if (
            "'" in user_in
            or "OR" in user_in.upper()
            or "--" in user_in
            or ";" in user_in
        ):

            self.lbl_sqli_status.config(
                text=(
                    "⚠️ AVISO: A entrada possui caracteres de injeção! "
                    "Na versão vulnerável, a lógica da query foi alterada!"
                ),
                fg=COLOR_INCORRECT
            )

        else:

            self.lbl_sqli_status.config(
                text=(
                    "✅ Entrada padrão de texto tratada como valor literal "
                    "em ambos os cenários."
                ),
                fg=COLOR_HEALTH
            )


    # ==========================================================================
    # --- ETAPA 2: ABAC
    # ==========================================================================

    def load_step_abac_lab(self):

        self.clear_card()

        self.lbl_mode.config(
            text="ETAPA 2/3 — CONTROLE DE ACESSO ABAC"
        )

        lbl_title = tk.Label(
            self.card_frame,
            text="🛡️ MINIGAME: AVALIADOR DE POLÍTICA DINÂMICA (ABAC)",
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
                "Regra da Política: 'Permitir acesso aos dados FINANCEIROS "
                "se Cargo = Gerente, Horário = Comercial E Conectado via VPN "
                "Interna'. Ajuste os atributos e avalie:"
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

        # Cargo

        tk.Label(
            grid_frame,
            text="Cargo (Usuário):",
            font=("Segoe UI", 9, "bold"),
            fg=COLOR_TEXT_MUTED,
            bg=COLOR_CARD_BG
        ).grid(
            row=0,
            column=0,
            sticky="w",
            pady=3
        )

        self.abac_role_var = tk.StringVar(
            value="Analista"
        )

        opt_role = tk.OptionMenu(
            grid_frame,
            self.abac_role_var,
            "Analista",
            "Gerente",
            "Estagiário"
        )

        opt_role.config(
            bg=COLOR_BTN_BG,
            fg=COLOR_TEXT_MAIN,
            activebackground=COLOR_BTN_HOVER,
            activeforeground=COLOR_TEXT_MAIN,
            highlightthickness=0,
            width=16
        )

        opt_role.grid(
            row=0,
            column=1,
            sticky="w",
            padx=10,
            pady=3
        )

        # Horário

        tk.Label(
            grid_frame,
            text="Horário Acesso:",
            font=("Segoe UI", 9, "bold"),
            fg=COLOR_TEXT_MUTED,
            bg=COLOR_CARD_BG
        ).grid(
            row=1,
            column=0,
            sticky="w",
            pady=3
        )

        self.abac_time_var = tk.StringVar(
            value="Comercial (08h-18h)"
        )

        opt_time = tk.OptionMenu(
            grid_frame,
            self.abac_time_var,
            "Comercial (08h-18h)",
            "Madrugada (02h)"
        )

        opt_time.config(
            bg=COLOR_BTN_BG,
            fg=COLOR_TEXT_MAIN,
            activebackground=COLOR_BTN_HOVER,
            activeforeground=COLOR_TEXT_MAIN,
            highlightthickness=0,
            width=16
        )

        opt_time.grid(
            row=1,
            column=1,
            sticky="w",
            padx=10,
            pady=3
        )

        # Local

        tk.Label(
            grid_frame,
            text="Local/Rede:",
            font=("Segoe UI", 9, "bold"),
            fg=COLOR_TEXT_MUTED,
            bg=COLOR_CARD_BG
        ).grid(
            row=2,
            column=0,
            sticky="w",
            pady=3
        )

        self.abac_loc_var = tk.StringVar(
            value="VPN Interna"
        )

        opt_loc = tk.OptionMenu(
            grid_frame,
            self.abac_loc_var,
            "VPN Interna",
            "Wi-Fi Público (Externo)"
        )

        opt_loc.config(
            bg=COLOR_BTN_BG,
            fg=COLOR_TEXT_MAIN,
            activebackground=COLOR_BTN_HOVER,
            activeforeground=COLOR_TEXT_MAIN,
            highlightthickness=0,
            width=16
        )

        opt_loc.grid(
            row=2,
            column=1,
            sticky="w",
            padx=10,
            pady=3
        )

        # Recurso

        tk.Label(
            grid_frame,
            text="Recurso Alvo:",
            font=("Segoe UI", 9, "bold"),
            fg=COLOR_TEXT_MUTED,
            bg=COLOR_CARD_BG
        ).grid(
            row=3,
            column=0,
            sticky="w",
            pady=3
        )

        self.abac_sens_var = tk.StringVar(
            value="Relatório Financeiro"
        )

        opt_sens = tk.OptionMenu(
            grid_frame,
            self.abac_sens_var,
            "Relatório Financeiro",
            "Mural Público"
        )

        opt_sens.config(
            bg=COLOR_BTN_BG,
            fg=COLOR_TEXT_MAIN,
            activebackground=COLOR_BTN_HOVER,
            activeforeground=COLOR_TEXT_MAIN,
            highlightthickness=0,
            width=16
        )

        opt_sens.grid(
            row=3,
            column=1,
            sticky="w",
            padx=10,
            pady=3
        )

        btn_eval = self.create_custom_button(
            self.card_frame,
            "⚙️ Testar Política de Acesso (Motor ABAC)",
            self.evaluate_abac
        )

        btn_eval.pack(
            fill="x",
            padx=20,
            pady=6
        )

        self.lbl_abac_result = tk.Label(
            self.card_frame,
            text="Status: Aguardando Avaliação de Atributos",
            font=("Consolas", 9, "bold"),
            fg=COLOR_WARNING,
            bg=COLOR_BG_TOP,
            bd=1,
            relief="solid",
            pady=8
        )

        self.lbl_abac_result.pack(
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

        self.root.after(
            50,
            self.update_layout
        )


    def evaluate_abac(self):

        role = self.abac_role_var.get()
        time = self.abac_time_var.get()
        loc = self.abac_loc_var.get()
        sens = self.abac_sens_var.get()

        if sens == "Mural Público":

            messagebox.showinfo(
                "ACESSO PERMITIDO! 🔓",
                "Recurso Público: Acesso concedido a todos os usuários "
                "sem restrições contextuais.",
                parent=self.root
            )

            self.lbl_abac_result.config(
                text="✅ DECISÃO: PERMITIR (RECURSO PÚBLICO)",
                fg=COLOR_HEALTH
            )

            self.btn_next2.config(
                state="normal"
            )

        else:

            reasons = []

            if role != "Gerente":
                reasons.append(
                    "❌ Cargo inadequado (Exige 'Gerente')."
                )

            if time != "Comercial (08h-18h)":
                reasons.append(
                    "❌ Fora do horário autorizado (Exige 'Comercial')."
                )

            if loc != "VPN Interna":
                reasons.append(
                    "❌ Local não confiável (Exige 'VPN Interna')."
                )

            if not reasons:

                messagebox.showinfo(
                    "ACESSO CONCEDIDO! 🎯",
                    "Todos os atributos satisfazem a política "
                    "de segurança ABAC!\n\n"
                    "- Cargo: Gerente\n"
                    "- Horário: Comercial\n"
                    "- Origem: VPN Interna",
                    parent=self.root
                )

                self.lbl_abac_result.config(
                    text="✅ DECISÃO: ACESSO REGISTRADO E LIBERADO",
                    fg=COLOR_HEALTH
                )

                self.btn_next2.config(
                    state="normal"
                )

            else:

                reason_str = "\n".join(
                    reasons
                )

                messagebox.showerror(
                    "ACESSO NEGADO! 🚫",
                    "A política ABAC bloqueou a solicitação devido "
                    "aos seguintes atributos:\n\n"
                    f"{reason_str}",
                    parent=self.root
                )

                self.lbl_abac_result.config(
                    text="❌ DECISÃO: ACESSO BLOQUEADO PELO MOTOR ABAC",
                    fg=COLOR_INCORRECT
                )


    # ==========================================================================
    # --- ETAPA 3: QUIZ
    # ==========================================================================

    def load_quiz_mode(self):

        self.clear_card()

        self.lbl_mode.config(
            text=(
                f"ETAPA 3/3 — QUIZ "
                f"({self.current_q + 1}/{len(QUIZ_FASE_7)})"
            )
        )

        q_data = QUIZ_FASE_7[
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

        self.root.after(
            50,
            self.update_layout
        )


    # ==========================================================================
    # --- VERIFICAR RESPOSTA
    # ==========================================================================

    def check_quiz_answer(
        self,
        selected_idx
    ):

        for btn in self.quiz_buttons:

            btn.config(
                state="disabled"
            )

        q_data = QUIZ_FASE_7[
            self.current_q
        ]

        correct_idx = q_data["answer"]

        selected_btn = self.quiz_buttons[
            selected_idx
        ]

        # ----------------------------------------------------------------------
        # CORRETA
        # ----------------------------------------------------------------------

        if selected_idx == correct_idx:

            selected_btn.config(
                bg=COLOR_CORRECT,
                fg="#000000"
            )

            self.root.update()

            messagebox.showinfo(
                "Resposta Correta! 🎯",
                f"{q_data['explanations'][selected_idx]}\n\n"
                f"{q_data['tip']}",
                parent=self.root
            )

            self.current_q += 1

            if self.current_q < len(QUIZ_FASE_7):

                self.load_quiz_mode()

            else:

                messagebox.showinfo(
                    "Fase 7 Concluída com Excelência! 🏆",
                    "Parabéns! Você dominou a proteção contra SQL Injection, "
                    "Hashing de Senhas, Controles ABAC e o Princípio do Menor Privilégio!",
                    parent=self.root
                )

                if self.ao_concluir:

                    self.ao_concluir()

        # ----------------------------------------------------------------------
        # INCORRETA
        # ----------------------------------------------------------------------

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
                f"{q_data['explanations'][selected_idx]}\n\n"
                f"{q_data['tip']}",
                parent=self.root
            )

            self.load_quiz_mode()


# ==============================================================================
# --- FUNÇÃO PADRÃO PARA O MAIN.PY
# ==============================================================================

def executar(
    root,
    ao_concluir=None
):

    return Phase7App(
        root,
        ao_concluir
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