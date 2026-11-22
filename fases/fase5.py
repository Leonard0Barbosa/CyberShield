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
# BANCO DE DADOS DAS QUESTÕES — FASE 5
# ==============================================================================

QUESTIONS = [

    {
        "category": "🌐 NAVEGAÇÃO SEGURA & PROTOCOLOS",

        "question": (
            "Qual sinal indica a maior probabilidade de um site ser "
            "uma tentativa de golpe ou Phishing?"
        ),

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

        "question": (
            "Um site exibe o ícone de 'Cadeado/HTTPS' na barra de endereços. "
            "O que esse certificado SSL/TLS garante exatamente?"
        ),

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

        "question": (
            "Ao passar o mouse sobre um link, o destino exibe: "
            "'suporte-security-update.com/login'. Como essa técnica é classificada?"
        ),

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

        "question": (
            "Qual é o principal risco de segurança associado ao uso "
            "de encurtadores de URL (como bit.ly) em e-mails suspeitos?"
        ),

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

        "question": (
            "O que caracteriza um Ataque Homográfico de IDN "
            "(Internationalized Domain Name)?"
        ),

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

        "question": (
            "Qual é a conduta mais recomendada antes de inserir credenciais "
            "em uma página de login recebida por e-mail?"
        ),

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
# CLASSE PRINCIPAL
# ==============================================================================

class CyberQuizApp:

    def __init__(self, root, proxima_fase=None):

        self.root = root
        self.proxima_fase = proxima_fase

        # ----------------------------------------------------------------------
        # CONFIGURAÇÃO DA JANELA
        # ----------------------------------------------------------------------

        self.root.title(
            "CyberShield: Fase 5 — Ethical Hacker Quiz"
        )

        self.root.geometry(
            "680x600"
        )

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
        # ESTADO DO JOGO
        # ----------------------------------------------------------------------

        self.current_q = 0
        self.lives = 3
        self.score = 0

        self.finalizando = False

        # Evita redesenhar excessivamente
        self.resize_job = None

        # ----------------------------------------------------------------------
        # INTERFACE
        # ----------------------------------------------------------------------

        self.setup_ui()

        self.load_question()

        # Atualiza o layout sempre que a janela mudar de tamanho
        self.root.bind(
            "<Configure>",
            self.on_window_resize
        )


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
    # REDIMENSIONAMENTO DA JANELA
    # ==========================================================================

    def on_window_resize(self, event=None):

        # Ignora eventos que não sejam da janela principal
        if event is not None:

            if event.widget != self.root:
                return

        # Evita vários redesenhos seguidos
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

        if width < 1:
            return

        if height < 1:
            return

        # ----------------------------------------------------------------------
        # FUNDO OCUPA A JANELA INTEIRA
        # ----------------------------------------------------------------------

        self.draw_cyber_background(
            width,
            height
        )

        # ----------------------------------------------------------------------
        # TAMANHO DO HEADER
        # ----------------------------------------------------------------------

        header_width = max(
            500,
            int(width * 0.94)
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
        # TAMANHO DO CARD
        # ----------------------------------------------------------------------

        card_width = min(
            int(width * 0.92),
            1200
        )

        card_height = min(
            int(height * 0.78),
            720
        )

        # Garante tamanho mínimo
        card_width = max(
            card_width,
            620
        )

        card_height = max(
            card_height,
            430
        )

        # Não deixa ultrapassar a tela
        card_width = min(
            card_width,
            width - 30
        )

        card_height = min(
            card_height,
            height - 100
        )

        card_y = (
            height * 0.54
        )

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
        # AJUSTA WRAP DA PERGUNTA
        # ----------------------------------------------------------------------

        question_wrap = max(
            500,
            card_width - 60
        )

        self.lbl_question.config(
            wraplength=question_wrap
        )

        # ----------------------------------------------------------------------
        # AJUSTA O FRAME DOS BOTÕES
        # ----------------------------------------------------------------------

        self.btn_frame.pack_configure(
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
        # CANVAS PRINCIPAL
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
            340,
            35,
            window=self.status_frame,
            width=640
        )

        # ----------------------------------------------------------------------
        # NOME DA FASE
        # ----------------------------------------------------------------------

        self.lbl_phase = tk.Label(
            self.status_frame,
            text="🌐 FASE 5 — NAVEGAÇÃO SEGURA",
            font=("Consolas", 12, "bold"),
            fg=COLOR_HEALTH,
            bg=COLOR_BG_TOP
        )

        self.lbl_phase.pack(
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
        # FIREWALL
        # ----------------------------------------------------------------------

        self.lbl_firewall = tk.Label(
            self.status_frame,
            text=f"🛡️ FIREWALL: {'█ ' * self.lives}",
            font=("Consolas", 12, "bold"),
            fg=COLOR_HEALTH,
            bg=COLOR_BG_TOP
        )

        self.lbl_firewall.pack(
            side="right"
        )

        # ----------------------------------------------------------------------
        # SCORE
        # ----------------------------------------------------------------------

        self.lbl_score = tk.Label(
            self.status_frame,
            text=f"SCORE: {self.score}",
            font=("Consolas", 12, "bold"),
            fg=COLOR_CYAN_GLOW,
            bg=COLOR_BG_TOP
        )

        self.lbl_score.pack(
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
            340,
            310,
            window=self.card_frame,
            width=640,
            height=470
        )

        # ----------------------------------------------------------------------
        # PROGRESSO
        # ----------------------------------------------------------------------

        self.lbl_progress = tk.Label(
            self.card_frame,
            text="",
            font=("Consolas", 9, "bold"),
            fg=COLOR_TEXT_MUTED,
            bg=COLOR_CARD_BG
        )

        self.lbl_progress.pack(
            anchor="e",
            padx=20,
            pady=(12, 0)
        )

        # ----------------------------------------------------------------------
        # CATEGORIA
        # ----------------------------------------------------------------------

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
            pady=(4, 5)
        )

        # ----------------------------------------------------------------------
        # PERGUNTA
        # ----------------------------------------------------------------------

        self.lbl_question = tk.Label(
            self.card_frame,
            text="",
            font=("Segoe UI", 12),
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

        # ----------------------------------------------------------------------
        # FRAME DOS BOTÕES
        # ----------------------------------------------------------------------

        self.btn_frame = tk.Frame(
            self.card_frame,
            bg=COLOR_CARD_BG
        )

        self.btn_frame.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=10
        )

        self.buttons = []

        # ----------------------------------------------------------------------
        # 4 ALTERNATIVAS
        # ----------------------------------------------------------------------

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
                command=lambda idx=i:
                self.check_answer(idx)
            )

            btn.pack(
                fill="x",
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

            self.buttons.append(
                btn
            )


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
        # LIMPA FUNDO ANTIGO
        # ----------------------------------------------------------------------

        self.bg_canvas.delete(
            "background"
        )

        # ----------------------------------------------------------------------
        # DEGRADÊ
        # ----------------------------------------------------------------------

        r1, g1, b1 = self.hex_to_rgb(
            COLOR_BG_TOP
        )

        r2, g2, b2 = self.hex_to_rgb(
            COLOR_BG_BOTTOM
        )

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

        # Circuito superior esquerdo
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

        # Circuito inferior
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
        # FUNDO ATRÁS DOS ELEMENTOS
        # ----------------------------------------------------------------------

        self.bg_canvas.tag_lower(
            "background"
        )


    # ==========================================================================
    # CONVERTER HEX
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
    # CARREGAR QUESTÃO
    # ==========================================================================

    def load_question(self):

        if self.finalizando:
            return

        if self.current_q >= len(QUESTIONS):

            self.finalizar_fase()

            return

        q_data = QUESTIONS[
            self.current_q
        ]

        # ----------------------------------------------------------------------
        # PROGRESSO
        # ----------------------------------------------------------------------

        self.lbl_progress.config(
            text=(
                f"QUESTÃO "
                f"{self.current_q + 1}/"
                f"{len(QUESTIONS)}"
            )
        )

        # ----------------------------------------------------------------------
        # CATEGORIA
        # ----------------------------------------------------------------------

        self.lbl_category.config(
            text=q_data["category"]
        )

        # ----------------------------------------------------------------------
        # PERGUNTA
        # ----------------------------------------------------------------------

        self.lbl_question.config(
            text=q_data["question"]
        )

        # ----------------------------------------------------------------------
        # ALTERNATIVAS
        # ----------------------------------------------------------------------

        for i, option in enumerate(
            q_data["options"]
        ):

            self.buttons[i].config(
                text=(
                    f"[ {chr(65 + i)} ]   "
                    f"{option}"
                ),
                bg=COLOR_BTN_BG,
                fg=COLOR_TEXT_MUTED,
                state="normal"
            )


    # ==========================================================================
    # VERIFICAR RESPOSTA
    # ==========================================================================

    def check_answer(
        self,
        selected_idx
    ):

        if self.finalizando:
            return

        q_data = QUESTIONS[
            self.current_q
        ]

        correct_idx = q_data[
            "answer"
        ]

        # ----------------------------------------------------------------------
        # DESABILITA BOTÕES
        # ----------------------------------------------------------------------

        for btn in self.buttons:

            btn.config(
                state="disabled"
            )

        # ======================================================================
        # ACERTO
        # ======================================================================

        if selected_idx == correct_idx:

            self.buttons[
                selected_idx
            ].config(
                bg=COLOR_CORRECT,
                fg="#000000"
            )

            self.score += 100

            self.lbl_score.config(
                text=f"SCORE: {self.score}"
            )

        # ======================================================================
        # ERRO
        # ======================================================================

        else:

            self.buttons[
                selected_idx
            ].config(
                bg=COLOR_INCORRECT,
                fg=COLOR_TEXT_MAIN
            )

            self.buttons[
                correct_idx
            ].config(
                bg=COLOR_CORRECT,
                fg="#000000"
            )

            self.lives -= 1

            self.lbl_firewall.config(
                text=(
                    f"🛡️ FIREWALL: "
                    f"{'█ ' * self.lives}"
                )
            )

            # ------------------------------------------------------------------
            # GAME OVER
            # ------------------------------------------------------------------

            if self.lives <= 0:

                self.root.after(
                    1000,
                    self.game_over
                )

                return

        # ----------------------------------------------------------------------
        # PRÓXIMA QUESTÃO
        # ----------------------------------------------------------------------

        self.current_q += 1

        self.root.after(
            1200,
            self.load_question
        )


    # ==========================================================================
    # GAME OVER
    # ==========================================================================

    def game_over(self):

        if self.finalizando:
            return

        self.finalizando = True

        messagebox.showerror(
            "Game Over ⚠️",

            "O firewall caiu e o sistema foi comprometido!\n\n"
            "Tente novamente.",

            parent=self.root
        )

        # ----------------------------------------------------------------------
        # NÃO DESTRUÍMOS A JANELA.
        #
        # O main.py é responsável pelo controle da aplicação.
        # ----------------------------------------------------------------------

        return


    # ==========================================================================
    # FINALIZAR FASE
    # ==========================================================================

    def finalizar_fase(self):

        if self.finalizando:
            return

        self.finalizando = True

        messagebox.showinfo(
            "FASE 5 CONCLUÍDA! 🏆",

            "Você protegeu a rede com sucesso!\n\n"

            "Você concluiu o treinamento de navegação segura, "
            "HTTPS, phishing, typosquatting e defesa contra "
            "links maliciosos.\n\n"

            f"Pontuação Final: {self.score}\n\n"

            "Preparando a próxima fase...",

            parent=self.root
        )

        # ----------------------------------------------------------------------
        # NÃO DESTRUÍMOS A JANELA.
        #
        # A próxima fase assume o controle.
        # ----------------------------------------------------------------------

        if self.proxima_fase:

            self.root.after(
                100,
                self.proxima_fase
            )


# ==============================================================================
# FUNÇÃO USADA PELO MAIN.PY
# ==============================================================================

def executar(
    root,
    proxima_fase=None
):

    return CyberQuizApp(
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