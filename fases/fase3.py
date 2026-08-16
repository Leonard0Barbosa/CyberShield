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
# QUESTÕES DA FASE 3
# ==============================================================================

QUESTIONS = [

    {
        "category": "🎣 FASE 3 — ENGENHARIA SOCIAL",

        "question": (
            "Você recebe um e-mail urgente pedindo login através de um link. "
            "O que deve fazer primeiro?"
        ),

        "options": [
            "Clicar rapidamente para evitar o bloqueio",
            "Responder pedindo a senha do remetente",
            "Verificar remetente, endereço e contexto da mensagem",
            "Encaminhar para todos os colegas"
        ],

        "answer": 2,

        "explanations": [
            (
                "❌ INCORRETO!\n\n"
                "O senso de urgência é um dos principais gatilhos psicológicos "
                "usados em ataques de phishing.\n\n"
                "💡 Dica: mensagens que exigem uma ação desesperada devem "
                "ser analisadas com cuidado."
            ),

            (
                "❌ INCORRETO!\n\n"
                "Responder à própria mensagem suspeita não confirma a identidade "
                "do remetente e pode aumentar o risco."
            ),

            (
                "✅ CORRETO!\n\n"
                "Antes de clicar, analise o endereço real do remetente, o domínio, "
                "o contexto da mensagem e o destino do link.\n\n"
                "💡 Regra de ouro: desconfie de mensagens inesperadas que "
                "pedem informações ou ações urgentes."
            ),

            (
                "❌ INCORRETO!\n\n"
                "Encaminhar uma mensagem suspeita pode espalhar o possível golpe "
                "para outras pessoas.\n\n"
                "💡 O correto é comunicar o incidente ao responsável pela "
                "segurança ou à equipe de TI."
            )
        ]
    },

    {
        "category": "🔎 FASE 3 — ANÁLISE DE LINKS",

        "question": (
            "Qual destes sinais pode indicar que um link recebido por e-mail "
            "é suspeito?"
        ),

        "options": [
            "O domínio corresponde exatamente ao site oficial",
            "O link possui um domínio estranho ou diferente do esperado",
            "A mensagem foi enviada por um contato conhecido",
            "O site utiliza HTTPS"
        ],

        "answer": 1,

        "explanations": [
            (
                "❌ INCORRETO!\n\n"
                "Um domínio legítimo e esperado é um sinal positivo, embora "
                "ainda seja importante analisar o contexto."
            ),

            (
                "✅ CORRETO!\n\n"
                "Domínios estranhos, alterações sutis no nome ou endereços "
                "diferentes do esperado podem indicar uma tentativa de phishing."
            ),

            (
                "❌ INCORRETO!\n\n"
                "Uma conta conhecida pode ter sido comprometida ou alguém pode "
                "estar se passando por essa pessoa."
            ),

            (
                "❌ INCORRETO!\n\n"
                "HTTPS protege a comunicação entre navegador e servidor, mas "
                "não significa automaticamente que o site seja legítimo."
            )
        ]
    },

    {
        "category": "🧠 FASE 3 — ENGENHARIA SOCIAL",

        "question": (
            "Um suposto funcionário de TI liga dizendo que precisa da sua senha "
            "para realizar uma manutenção urgente. Qual é a atitude mais segura?"
        ),

        "options": [
            "Informar a senha porque ele trabalha na empresa",
            "Enviar a senha somente por mensagem",
            "Recusar o compartilhamento e confirmar a solicitação por um canal oficial",
            "Fornecer apenas os primeiros caracteres da senha"
        ],

        "answer": 2,

        "explanations": [
            (
                "❌ INCORRETO!\n\n"
                "A identidade de alguém não deve ser considerada verdadeira "
                "apenas porque a pessoa afirma trabalhar na empresa."
            ),

            (
                "❌ INCORRETO!\n\n"
                "Enviar uma senha por mensagem continua sendo compartilhamento "
                "de uma credencial sensível."
            ),

            (
                "✅ CORRETO!\n\n"
                "Credenciais não devem ser compartilhadas. Uma solicitação "
                "suspeita deve ser confirmada por um canal oficial e independente."
            ),

            (
                "❌ INCORRETO!\n\n"
                "Mesmo parte de uma senha pode fornecer informações úteis "
                "para um atacante."
            )
        ]
    },

    {
        "category": "🚨 FASE 3 — INDÍCIOS DE PHISHING",

        "question": (
            "Qual combinação apresenta vários sinais típicos de uma tentativa "
            "de phishing?"
        ),

        "options": [
            "Mensagem inesperada + urgência + pedido de dados + link suspeito",
            "Mensagem esperada + domínio oficial + nenhuma solicitação",
            "Aviso interno confirmado pela equipe de TI",
            "Documento escolar enviado por um professor conhecido"
        ],

        "answer": 0,

        "explanations": [
            (
                "✅ CORRETO!\n\n"
                "A combinação de urgência, pedido de informações, mensagem "
                "inesperada e link suspeito é um forte sinal de phishing."
            ),

            (
                "❌ INCORRETO!\n\n"
                "Esses elementos, isoladamente, não caracterizam uma tentativa "
                "de phishing."
            ),

            (
                "❌ INCORRETO!\n\n"
                "Uma comunicação confirmada por um canal confiável apresenta "
                "um contexto diferente de uma mensagem suspeita."
            ),

            (
                "❌ INCORRETO!\n\n"
                "O fato de uma pessoa ser conhecida não é suficiente para "
                "determinar se uma mensagem é maliciosa, mas essa opção não "
                "apresenta os principais sinais descritos na questão."
            )
        ]
    }
]


# ==============================================================================
# APLICAÇÃO DA FASE 3
# ==============================================================================

class CyberQuizApp:

    def __init__(self, root, proxima_fase=None):

        self.root = root
        self.proxima_fase = proxima_fase

        # ----------------------------------------------------------------------
        # CONFIGURAÇÃO DA JANELA
        # ----------------------------------------------------------------------

        self.root.title(
            "CyberShield: Fase 3 — Phishing"
        )

        self.root.geometry(
            "660x560"
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
            padx=max(20, int(card_width * 0.03))
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
            330,
            35,
            window=self.status_frame,
            width=620
        )

        # ----------------------------------------------------------------------
        # NOME DA FASE
        # ----------------------------------------------------------------------

        self.lbl_phase = tk.Label(
            self.status_frame,
            text="🎣 FASE 3 — PHISHING",
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
            330,
            290,
            window=self.card_frame,
            width=620,
            height=430
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
            wraplength=570,
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
                660
            )

        if height is None:
            height = max(
                self.root.winfo_height(),
                560
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
        # GARANTE QUE O FUNDO FIQUE ATRÁS DOS ELEMENTOS
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

        self.lbl_progress.config(
            text=(
                f"QUESTÃO "
                f"{self.current_q + 1}/"
                f"{len(QUESTIONS)}"
            )
        )

        self.lbl_category.config(
            text=q_data["category"]
        )

        self.lbl_question.config(
            text=q_data["question"]
        )

        # ----------------------------------------------------------------------
        # CARREGA ALTERNATIVAS
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

        # ----------------------------------------------------------------------
        # DESABILITA OS BOTÕES
        # ----------------------------------------------------------------------

        for btn in self.buttons:

            btn.config(
                state="disabled"
            )

        q_data = QUESTIONS[
            self.current_q
        ]

        correct_idx = q_data[
            "answer"
        ]

        explanation = q_data[
            "explanations"
        ][selected_idx]

        selected_btn = self.buttons[
            selected_idx
        ]

        # ======================================================================
        # ACERTO
        # ======================================================================

        if selected_idx == correct_idx:

            selected_btn.config(
                bg=COLOR_CORRECT,
                fg="#000000"
            )

            self.root.update()

            self.score += 100

            self.lbl_score.config(
                text=f"SCORE: {self.score}"
            )

            messagebox.showinfo(
                "Resposta Correta! ✅",
                explanation,
                parent=self.root
            )

        # ======================================================================
        # ERRO
        # ======================================================================

        else:

            selected_btn.config(
                bg=COLOR_INCORRECT,
                fg="#FFFFFF"
            )

            self.buttons[
                correct_idx
            ].config(
                bg=COLOR_CORRECT,
                fg="#000000"
            )

            self.root.update()

            self.lives -= 1

            self.lbl_firewall.config(
                text=(
                    f"🛡️ FIREWALL: "
                    f"{'█ ' * self.lives}"
                )
            )

            messagebox.showwarning(
                "Resposta Incorreta! ❌",
                explanation,
                parent=self.root
            )

            # ------------------------------------------------------------------
            # GAME OVER
            # ------------------------------------------------------------------

            if self.lives <= 0:

                messagebox.showerror(
                    "Game Over",
                    "O firewall caiu!\n\n"
                    "Você não conseguiu identificar "
                    "as ameaças.",
                    parent=self.root
                )

                for btn in self.buttons:

                    btn.config(
                        state="disabled"
                    )

                return

        # ----------------------------------------------------------------------
        # PRÓXIMA QUESTÃO
        # ----------------------------------------------------------------------

        self.current_q += 1

        self.load_question()


    # ==========================================================================
    # FINALIZAR FASE
    # ==========================================================================

    def finalizar_fase(self):

        if self.finalizando:
            return

        self.finalizando = True

        messagebox.showinfo(
            "FASE 3 CONCLUÍDA! 🏆",

            "Excelente trabalho!\n\n"
            "Você concluiu o treinamento de "
            "identificação de phishing e "
            "engenharia social.\n\n"
            f"Pontuação da Fase 3: {self.score}\n\n"
            "Preparando a próxima fase...",

            parent=self.root
        )

        # ----------------------------------------------------------------------
        # NÃO DESTRUÍMOS A JANELA.
        #
        # O main.py é responsável pela troca da fase.
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

