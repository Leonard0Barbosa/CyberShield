# ==============================================================================
# FASE 6 — CRIPTOGRAFIA
# CyberShield: Academia do Hacker Ético
# ==============================================================================

import hashlib
import tkinter as tk
from tkinter import messagebox


# ==============================================================================
# CORES — CYBER NETWORK
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
# BANCO DE PERGUNTAS — FASE 6
# ==============================================================================

QUIZ_FASE_6 = [

    {
        "category": "🔐 INTEGRIDADE DE DADOS",

        "question":
            "Qual técnica gera um resumo criptográfico de tamanho fixo "
            "para verificar a integridade de um arquivo?",

        "options": [
            "A) DNS",
            "B) Hash",
            "C) DHCP",
            "D) MFA"
        ],

        "answer": 1,

        "explanations": [
            "❌ INCORRETO: DNS é o protocolo que traduz nomes de domínio em endereços IP.",

            "✅ CORRETO! O Hash é uma função unidirecional. "
            "Se o arquivo mudar apenas 1 bit, o Hash resultante muda completamente "
            "(Efeito Avalanche).",

            "❌ INCORRETO: DHCP atribui endereços IP dinamicamente para dispositivos da rede.",

            "❌ INCORRETO: MFA (Autenticação de Múltiplos Fatores) "
            "é usado para proteger o acesso a contas."
        ],

        "tip":
            "💡 Dica: Para checar se um arquivo baixado da internet foi alterado "
            "ou corrompido, compare o seu código Hash!"
    },


    {
        "category": "🔏 AUTENTICIDADE E NÃO-REPÚDIO",

        "question":
            "O que garante tanto a AUTENTICIDADE do remetente "
            "quanto a INTEGRIDADE da mensagem?",

        "options": [
            "A) Compressão de dados (.zip)",
            "B) Codificação Base64",
            "C) Assinatura Digital",
            "D) Configuração DHCP"
        ],

        "answer": 2,

        "explanations": [
            "❌ INCORRETO: A compressão apenas reduz o tamanho de arquivos.",

            "❌ INCORRETO: Base64 apenas converte dados binários em texto; "
            "não oferece segurança nem sigilo.",

            "✅ CORRETO! A Assinatura Digital utiliza criptografia assimétrica "
            "vinculando a identidade do autor ao conteúdo, garantindo o não-repúdio.",

            "❌ INCORRETO: DHCP é um serviço de atribuição de IP de rede."
        ],

        "tip":
            "💡 Dica: Assinatura Digital = Identidade do Autor + "
            "Validação contra alterações de conteúdo!"
    },


    {
        "category": "🔑 CRIPTOGRAFIA SIMÉTRICA VS ASSIMÉTRICA",

        "question":
            "Na Criptografia Assimétrica, qual chave é utilizada "
            "para CRIPTOGRAFAR um dado enviado com segurança "
            "para um destinatário específico?",

        "options": [
            "A) A Chave Privada do remetente",
            "B) A Chave Pública do destinatário",
            "C) A Chave Privada do destinatário",
            "D) A mesma Chave Única compartilhada via pendrive"
        ],

        "answer": 1,

        "explanations": [
            "❌ INCORRETO: A chave privada do remetente é usada "
            "para assinar digitalmente, não para encriptar arquivos confidenciais.",

            "✅ CORRETO! Qualquer pessoa pode usar a Chave Pública "
            "do destinatário para cifrar a mensagem, mas SOMENTE a Chave Privada "
            "do destinatário consegue decifrá-la.",

            "❌ INCORRETO: A chave privada do destinatário é secreta "
            "e nunca deve ser compartilhada.",

            "❌ INCORRETO: Usar uma única chave compartilhada "
            "descreve a Criptografia Simétrica."
        ],

        "tip":
            "💡 Dica: Criptografia Assimétrica: "
            "Chave Pública cifra, Chave Privada decifra!"
    },


    {
        "category": "⚠️ VULNERABILIDADES CRIPTOGRÁFICAS",

        "question":
            "O que ocorre durante um fenômeno conhecido como "
            "'Colisão de Hash' (Hash Collision)?",

        "options": [
            "A) O algoritmo de Hash trava ao processar um arquivo muito grande",

            "B) Dois arquivos com conteúdos completamente diferentes "
            "geram exatamente o mesmo Hash",

            "C) A chave privada é exposta publicamente durante a transmissão",

            "D) O Hash do arquivo muda sozinho após o reinício do sistema"
        ],

        "answer": 1,

        "explanations": [
            "❌ INCORRETO: As funções de hash tratam arquivos de qualquer tamanho "
            "sem travar.",

            "✅ CORRETO! Uma colisão ocorre quando dois dados distintos "
            "resultam no mesmo Hash. É por isso que algoritmos antigos como "
            "MD5 e SHA-1 foram descontinuados.",

            "❌ INCORRETO: Colisões afetam algoritmos de hash, "
            "não a exposição de chaves privadas.",

            "❌ INCORRETO: O hash de um arquivo estático é determinístico "
            "e nunca muda espontaneamente."
        ],

        "tip":
            "💡 Dica: Algoritmos modernos como SHA-256 e SHA-3 "
            "são projetados para evitar colisões!"
    }
]


# ==============================================================================
# CLASSE PRINCIPAL — FASE 6
# ==============================================================================

class Phase6App:

    def __init__(self, root, proxima_fase):

        self.root = root
        self.proxima_fase = proxima_fase

        # ----------------------------------------------------------------------
        # CONFIGURAÇÃO DA JANELA
        # ----------------------------------------------------------------------

        self.root.title(
            "CyberShield: Fase 6 — Integridade, Hash & Assinatura Digital"
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

        self.simulated_message = (
            "Transferir R$ 10.000,00 para Conta A"
        )

        self.simulated_signature = ""

        self.resize_job = None

        self.finalizando = False

        # ----------------------------------------------------------------------
        # INTERFACE
        # ----------------------------------------------------------------------

        self.setup_ui()

        self.load_step_hash_lab()

        # Atualiza layout quando a janela for redimensionada
        self.root.bind(
            "<Configure>",
            self.on_window_resize
        )

        self.root.update_idletasks()

        self.update_layout()


    # ==========================================================================
    # TELA CHEIA
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
    # REDIMENSIONAMENTO
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


    # ==========================================================================
    # ATUALIZAR LAYOUT
    # ==========================================================================

    def update_layout(self):

        self.resize_job = None

        width = self.root.winfo_width()
        height = self.root.winfo_height()

        if width < 1 or height < 1:
            return

        # ----------------------------------------------------------------------
        # FUNDO
        # ----------------------------------------------------------------------

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
            max(35, height * 0.055)
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
        # WRAPLENGTH DOS ELEMENTOS
        # ----------------------------------------------------------------------

        content_wrap = max(
            450,
            card_width - 60
        )

        if hasattr(self, "lbl_hash_output"):

            self.lbl_hash_output.config(
                wraplength=max(
                    400,
                    card_width - 80
                )
            )

        # Procura labels criados dinamicamente no card
        for widget in self.card_frame.winfo_children():

            if isinstance(widget, tk.Label):

                try:

                    current_wrap = int(
                        widget.cget("wraplength")
                    )

                    if current_wrap > 0:

                        widget.config(
                            wraplength=content_wrap
                        )

                except Exception:
                    pass

        # ----------------------------------------------------------------------
        # ENTRIES
        # ----------------------------------------------------------------------

        if hasattr(self, "entry_hash_input"):

            self.entry_hash_input.pack_configure(
                padx=max(
                    20,
                    int(card_width * 0.03)
                )
            )

        if hasattr(self, "entry_doc_content"):

            self.entry_doc_content.pack_configure(
                padx=max(
                    20,
                    int(card_width * 0.03)
                )
            )


    # ==========================================================================
    # INTERFACE
    # ==========================================================================

    def setup_ui(self):

        # ----------------------------------------------------------------------
        # CANVAS
        # ----------------------------------------------------------------------

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
            text="🛡️ FASE 6: INTEGRIDADE & CRIPTOGRAFIA",
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
    # FUNDO RESPONSIVO
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

        # ----------------------------------------------------------------------
        # REMOVE FUNDO ANTERIOR
        # ----------------------------------------------------------------------

        self.bg_canvas.delete(
            "background"
        )

        # ----------------------------------------------------------------------
        # CORES DO GRADIENTE
        # ----------------------------------------------------------------------

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
                r1 + (r2 - r1) * (y / height)
            )

            g = int(
                g1 + (g2 - g1) * (y / height)
            )

            b = int(
                b1 + (b2 - b1) * (y / height)
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
        # CIRCUITOS RESPONSIVOS
        # ----------------------------------------------------------------------

        line_color = "#0B3254"
        glow_dot = COLOR_CYAN_GLOW

        # ----------------------------------------------------------------------
        # CIRCUITO SUPERIOR
        # ----------------------------------------------------------------------

        x1 = int(width * 0.04)
        x2 = int(width * 0.25)
        x3 = int(width * 0.32)
        x4 = int(width * 0.48)

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
        x8 = int(width * 0.72)

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

        # ----------------------------------------------------------------------
        # MANDA O FUNDO PARA TRÁS
        # ----------------------------------------------------------------------

        self.bg_canvas.tag_lower(
            "background"
        )


    # ==========================================================================
    # HEX → RGB
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
    # LIMPAR CARD
    # ==========================================================================

    def clear_card(self):

        for widget in self.card_frame.winfo_children():

            widget.destroy()

        # Remove referências aos widgets antigos
        for attr in [
            "entry_hash_input",
            "lbl_hash_output",
            "lbl_hash_info",
            "entry_doc_content",
            "lbl_sig_status",
            "btn_next2",
            "quiz_buttons"
        ]:

            if hasattr(self, attr):

                try:
                    delattr(
                        self,
                        attr
                    )

                except Exception:
                    pass


    # ==========================================================================
    # BOTÃO PADRÃO
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


    # ==========================================================================
    # HOVER
    # ==========================================================================

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
    # ETAPA 1 — LABORATÓRIO DE HASH
    # ==========================================================================

    def load_step_hash_lab(self):

        self.clear_card()

        self.lbl_mode.config(
            text="ETAPA 1/3 — GERADOR DE HASH"
        )

        lbl_title = tk.Label(
            self.card_frame,
            text="⚡ LABORATÓRIO DE HASHING (SHA-256 EM TEMPO REAL)",
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
                "Digite qualquer texto na caixa abaixo. "
                "Mude apenas 1 letra ou ponto para observar "
                "o 'Efeito Avalanche': o resumo de tamanho fixo "
                "muda completamente!"
            ),
            font=("Segoe UI", 9),
            fg=COLOR_TEXT_MAIN,
            bg=COLOR_CARD_BG,
            wraplength=600,
            justify="left"
        )

        lbl_desc.pack(
            anchor="w",
            padx=20,
            pady=5
        )

        self.entry_hash_input = tk.Entry(
            self.card_frame,
            font=("Segoe UI", 10),
            bg=COLOR_BG_TOP,
            fg=COLOR_TEXT_MAIN,
            insertbackground=COLOR_TEXT_MAIN,
            bd=1,
            relief="solid"
        )

        self.entry_hash_input.insert(
            0,
            "Relatorio_Financeiro_2026.pdf"
        )

        self.entry_hash_input.pack(
            fill="x",
            padx=20,
            pady=5
        )

        self.entry_hash_input.bind(
            "<KeyRelease>",
            self.update_live_hash
        )

        tk.Label(
            self.card_frame,
            text="Resumo Criptográfico SHA-256 (64 caracteres hex):",
            font=("Segoe UI", 9, "bold"),
            fg=COLOR_TEXT_MUTED,
            bg=COLOR_CARD_BG
        ).pack(
            anchor="w",
            padx=20,
            pady=(10, 2)
        )

        self.lbl_hash_output = tk.Label(
            self.card_frame,
            text="",
            font=("Consolas", 9, "bold"),
            fg=COLOR_HEALTH,
            bg=COLOR_BG_TOP,
            bd=1,
            relief="solid",
            wraplength=580,
            justify="center",
            pady=10
        )

        self.lbl_hash_output.pack(
            fill="x",
            padx=20,
            pady=5
        )

        self.lbl_hash_info = tk.Label(
            self.card_frame,
            text=(
                "💡 Teste: Adicione um ponto no final do texto "
                "acima e compare o resultado Hash obtido!"
            ),
            font=("Segoe UI", 9, "italic"),
            fg=COLOR_WARNING,
            bg=COLOR_CARD_BG,
            wraplength=600,
            justify="left"
        )

        self.lbl_hash_info.pack(
            anchor="w",
            padx=20,
            pady=10
        )

        self.update_live_hash()

        btn_next1 = self.create_custom_button(
            self.card_frame,
            "Avançar para Simulador de Assinatura Digital ➔",
            self.load_step_signature_lab
        )

        btn_next1.pack(
            fill="x",
            padx=20,
            pady=(10, 15)
        )

        self.root.after(
            50,
            self.update_layout
        )


    # ==========================================================================
    # ATUALIZAR HASH
    # ==========================================================================

    def update_live_hash(self, event=None):

        if not hasattr(
            self,
            "entry_hash_input"
        ):
            return

        if not hasattr(
            self,
            "lbl_hash_output"
        ):
            return

        text = self.entry_hash_input.get()

        hash_result = hashlib.sha256(
            text.encode("utf-8")
        ).hexdigest()

        self.lbl_hash_output.config(
            text=hash_result
        )


    # ==========================================================================
    # ETAPA 2 — ASSINATURA DIGITAL
    # ==========================================================================

    def load_step_signature_lab(self):

        self.clear_card()

        self.lbl_mode.config(
            text="ETAPA 2/3 — ASSINATURA DIGITAL"
        )

        lbl_title = tk.Label(
            self.card_frame,
            text="🔏 MINIGAME: AUDITORIA E VERIFICAÇÃO DE ADULTERAÇÃO",
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
                "A Assinatura Digital une o Hash da mensagem "
                "com a Chave Privada do remetente. "
                "Experimente alterar a ordem de pagamento "
                "e tente validar:"
            ),
            font=("Segoe UI", 9),
            fg=COLOR_TEXT_MAIN,
            bg=COLOR_CARD_BG,
            wraplength=600,
            justify="left"
        )

        lbl_desc.pack(
            anchor="w",
            padx=20,
            pady=5
        )

        tk.Label(
            self.card_frame,
            text="Conteúdo do Documento / Ordem Bancária:",
            font=("Segoe UI", 9, "bold"),
            fg=COLOR_TEXT_MUTED,
            bg=COLOR_CARD_BG
        ).pack(
            anchor="w",
            padx=20,
            pady=(5, 2)
        )

        self.entry_doc_content = tk.Entry(
            self.card_frame,
            font=("Segoe UI", 10),
            bg=COLOR_BG_TOP,
            fg=COLOR_TEXT_MAIN,
            insertbackground=COLOR_TEXT_MAIN,
            bd=1,
            relief="solid"
        )

        self.entry_doc_content.insert(
            0,
            self.simulated_message
        )

        self.entry_doc_content.pack(
            fill="x",
            padx=20,
            pady=2
        )

        btn_sign = self.create_custom_button(
            self.card_frame,
            "✍️ Assinar Documento com Chave Privada",
            self.generate_digital_signature
        )

        btn_sign.pack(
            fill="x",
            padx=20,
            pady=6
        )

        self.lbl_sig_status = tk.Label(
            self.card_frame,
            text="Status: Documento NÃO Assinado",
            font=("Consolas", 9, "bold"),
            fg=COLOR_WARNING,
            bg=COLOR_BG_TOP,
            bd=1,
            relief="solid",
            pady=6,
            wraplength=600,
            justify="left"
        )

        self.lbl_sig_status.pack(
            fill="x",
            padx=20,
            pady=4
        )

        btn_verify = self.create_custom_button(
            self.card_frame,
            "🔍 Auditar Assinatura com Chave Pública",
            self.verify_digital_signature
        )

        btn_verify.pack(
            fill="x",
            padx=20,
            pady=6
        )

        self.btn_next2 = self.create_custom_button(
            self.card_frame,
            "Ir para o Quiz Conceitual Expandido ➔",
            self.load_quiz_mode
        )

        self.btn_next2.pack(
            fill="x",
            padx=20,
            pady=(10, 15)
        )

        self.btn_next2.config(
            state="disabled"
        )

        self.root.after(
            50,
            self.update_layout
        )


    # ==========================================================================
    # GERAR ASSINATURA
    # ==========================================================================

    def generate_digital_signature(self):

        text = self.entry_doc_content.get().strip()

        if not text:

            messagebox.showwarning(
                "Aviso",
                "O documento não pode estar vazio!",
                parent=self.root
            )

            return

        self.simulated_message = text

        raw_hash = hashlib.sha256(
            text.encode("utf-8")
        ).hexdigest()

        self.simulated_signature = (
            f"SIG_PRIVKEY_RSA2048[{raw_hash[:16]}]"
        )

        self.lbl_sig_status.config(
            text=(
                f"✅ ASSINADO DIGITALMENTE!\n"
                f"Hash: {raw_hash[:24]}...\n"
                f"Assinatura: {self.simulated_signature}"
            ),
            fg=COLOR_HEALTH
        )

        self.update_layout()


    # ==========================================================================
    # VERIFICAR ASSINATURA
    # ==========================================================================

    def verify_digital_signature(self):

        if not self.simulated_signature:

            messagebox.showerror(
                "Erro de Auditoria",
                "Assine o documento primeiro para gerar "
                "o registro de validação!",
                parent=self.root
            )

            return

        current_text = (
            self.entry_doc_content.get().strip()
        )

        current_hash = hashlib.sha256(
            current_text.encode("utf-8")
        ).hexdigest()

        expected_hash = hashlib.sha256(
            self.simulated_message.encode("utf-8")
        ).hexdigest()

        if current_hash == expected_hash:

            messagebox.showinfo(
                "INTEGRIDADE E AUTENTICIDADE CONFIRMADAS! 🎯",

                "1. INTEGRIDADE: NENHUM bit do texto foi alterado.\n"
                "2. AUTENTICIDADE: A assinatura corresponde "
                "exatamente à Chave Pública do autor.\n\n"
                "Status: VÁLIDO (Garantia de Não-Repúdio).",

                parent=self.root
            )

            self.btn_next2.config(
                state="normal"
            )

        else:

            messagebox.showerror(
                "ALERTA DE SEGURANÇA: DOCUMENTO ADULTERADO! ❌",

                "Falha na Verificação!\n\n"
                "O Hash do conteúdo atual difere do Hash "
                "vinculado à Assinatura Digital.\n"
                "Alguém modificou a mensagem durante a transmissão!",

                parent=self.root
            )


    # ==========================================================================
    # ETAPA 3 — QUIZ
    # ==========================================================================

    def load_quiz_mode(self):

        self.clear_card()

        self.lbl_mode.config(
            text=(
                f"ETAPA 3/3 — QUIZ "
                f"({self.current_q + 1}/{len(QUIZ_FASE_6)})"
            )
        )

        q_data = QUIZ_FASE_6[
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
    # VERIFICAR RESPOSTA
    # ==========================================================================

    def check_quiz_answer(
        self,
        selected_idx
    ):

        for btn in self.quiz_buttons:

            btn.config(
                state="disabled"
            )

        q_data = QUIZ_FASE_6[
            self.current_q
        ]

        correct_idx = q_data["answer"]

        selected_btn = self.quiz_buttons[
            selected_idx
        ]

        # ----------------------------------------------------------------------
        # RESPOSTA CORRETA
        # ----------------------------------------------------------------------

        if selected_idx == correct_idx:

            selected_btn.config(
                bg=COLOR_CORRECT,
                fg="#000000"
            )

            self.root.update()

            messagebox.showinfo(
                "Resposta Correta! 🎯",

                f"{q_data['explanations'][selected_idx]}"
                f"\n\n{q_data['tip']}",

                parent=self.root
            )

            self.current_q += 1

            # ------------------------------------------------------------------
            # PRÓXIMA QUESTÃO
            # ------------------------------------------------------------------

            if self.current_q < len(QUIZ_FASE_6):

                self.load_quiz_mode()

            # ------------------------------------------------------------------
            # FASE 6 TERMINOU
            # ------------------------------------------------------------------

            else:

                self.finalizar_fase()


        # ----------------------------------------------------------------------
        # RESPOSTA INCORRETA
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

                f"{q_data['explanations'][selected_idx]}"
                f"\n\n{q_data['tip']}",

                parent=self.root
            )

            # Tenta novamente a mesma pergunta
            self.load_quiz_mode()


    # ==========================================================================
    # FINALIZAR FASE
    # ==========================================================================

    def finalizar_fase(self):

        if self.finalizando:
            return

        self.finalizando = True

        messagebox.showinfo(
            "Fase 6 Concluída! 🏆",

            "Parabéns!\n\n"
            "Você dominou os conceitos essenciais de:\n\n"
            "• Hashing\n"
            "• Integridade de Dados\n"
            "• Criptografia Assimétrica\n"
            "• Assinatura Digital\n"
            "• Colisões de Hash\n\n"
            "Prepare-se para a próxima fase!",

            parent=self.root
        )

        # ----------------------------------------------------------------------
        # NÃO DESTRÓI A JANELA.
        #
        # O MAIN CONTROLA A PRÓXIMA FASE.
        # ----------------------------------------------------------------------

        if self.proxima_fase:

            self.root.after(
                100,
                self.proxima_fase
            )


# ==============================================================================
# FUNÇÃO EXECUTAR
# ==============================================================================

def executar(
    root,
    proxima_fase=None
):

    return Phase6App(
        root,
        proxima_fase
    )


# ==============================================================================
# TESTE INDIVIDUAL
# ==============================================================================

if __name__ == "__main__":

    root = tk.Tk()

    executar(
        root
    )

    root.mainloop()
    