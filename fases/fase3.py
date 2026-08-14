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

        self.root.title("CyberShield: Fase 3 — Phishing")
        self.root.geometry("660x560")
        self.root.resizable(False, False)

        self.current_q = 0
        self.lives = 3
        self.score = 0

        self.finalizando = False

        self.setup_ui()
        self.load_question()

    # ==========================================================================
    # INTERFACE
    # ==========================================================================

    def setup_ui(self):

        self.bg_canvas = tk.Canvas(
            self.root,
            width=660,
            height=560,
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
            330,
            35,
            window=self.status_frame,
            width=620
        )

        self.lbl_phase = tk.Label(
            self.status_frame,
            text="🎣 FASE 3 — PHISHING",
            font=("Consolas", 12, "bold"),
            fg=COLOR_HEALTH,
            bg=COLOR_BG_TOP
        )

        self.lbl_phase.pack(side="left")

        self.lbl_firewall = tk.Label(
            self.status_frame,
            text=f"🛡️ FIREWALL: {'█ ' * self.lives}",
            font=("Consolas", 12, "bold"),
            fg=COLOR_HEALTH,
            bg=COLOR_BG_TOP
        )

        self.lbl_firewall.pack(side="right")

        self.lbl_score = tk.Label(
            self.status_frame,
            text=f"SCORE: {self.score}",
            font=("Consolas", 12, "bold"),
            fg=COLOR_CYAN_GLOW,
            bg=COLOR_BG_TOP
        )

        self.lbl_score.pack(side="right", padx=20)

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

        self.bg_canvas.create_window(
            330,
            290,
            window=self.card_frame,
            width=620,
            height=430
        )

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
        # BOTÕES
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
                command=lambda idx=i: self.check_answer(idx)
            )

            btn.pack(
                fill="x",
                pady=5,
                ipady=4
            )

            btn.bind(
                "<Enter>",
                lambda e, b=btn: self.on_hover_enter(b)
            )

            btn.bind(
                "<Leave>",
                lambda e, b=btn: self.on_hover_leave(b)
            )

            self.buttons.append(btn)

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
    # FUNDO
    # ==========================================================================

    def draw_cyber_background(self):

        width = 660
        height = 560

        r1, g1, b1 = self.hex_to_rgb(COLOR_BG_TOP)
        r2, g2, b2 = self.hex_to_rgb(COLOR_BG_BOTTOM)

        # ----------------------------------------------------------------------
        # DEGRADÊ
        # ----------------------------------------------------------------------

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

        # ----------------------------------------------------------------------
        # CIRCUITOS
        # ----------------------------------------------------------------------

        line_color = "#0B3254"
        glow_dot = COLOR_CYAN_GLOW

        self.bg_canvas.create_line(
            30,
            25,
            180,
            25,
            230,
            50,
            430,
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
            427,
            47,
            433,
            53,
            fill=glow_dot,
            outline=""
        )

        self.bg_canvas.create_line(
            50,
            530,
            200,
            530,
            250,
            510,
            500,
            510,
            550,
            535,
            fill=line_color,
            width=1.5
        )

        self.bg_canvas.create_oval(
            247,
            507,
            253,
            513,
            fill=glow_dot,
            outline=""
        )

        self.bg_canvas.create_oval(
            497,
            507,
            503,
            513,
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
    # CARREGAR QUESTÃO
    # ==========================================================================

    def load_question(self):

        if self.current_q >= len(QUESTIONS):

            self.finalizar_fase()
            return

        q_data = QUESTIONS[self.current_q]

        self.lbl_progress.config(
            text=f"QUESTÃO {self.current_q + 1}/{len(QUESTIONS)}"
        )

        self.lbl_category.config(
            text=q_data["category"]
        )

        self.lbl_question.config(
            text=q_data["question"]
        )

        for i, option in enumerate(q_data["options"]):

            self.buttons[i].config(
                text=f"[ {chr(65 + i)} ]   {option}",
                bg=COLOR_BTN_BG,
                fg=COLOR_TEXT_MUTED,
                state="normal"
            )

    # ==========================================================================
    # VERIFICAR RESPOSTA
    # ==========================================================================

    def check_answer(self, selected_idx):

        if self.finalizando:
            return

        for btn in self.buttons:
            btn.config(state="disabled")

        q_data = QUESTIONS[self.current_q]

        correct_idx = q_data["answer"]

        explanation = q_data["explanations"][selected_idx]

        selected_btn = self.buttons[selected_idx]

        # ----------------------------------------------------------------------
        # ACERTO
        # ----------------------------------------------------------------------

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

        # ----------------------------------------------------------------------
        # ERRO
        # ----------------------------------------------------------------------

        else:

            selected_btn.config(
                bg=COLOR_INCORRECT,
                fg="#FFFFFF"
            )

            self.buttons[correct_idx].config(
                bg=COLOR_CORRECT,
                fg="#000000"
            )

            self.root.update()

            self.lives -= 1

            self.lbl_firewall.config(
                text=f"🛡️ FIREWALL: {'█ ' * self.lives}"
            )

            messagebox.showwarning(
                "Resposta Incorreta! ❌",
                explanation,
                parent=self.root
            )

            if self.lives <= 0:

                messagebox.showerror(
                    "Game Over",
                    "O firewall caiu!\n\n"
                    "Você não conseguiu identificar as ameaças.",
                    parent=self.root
                )

                # NÃO chama destroy aqui.
                # O mainloop continua funcionando.
                self.root.quit()

                return

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
            "Você concluiu o treinamento de identificação de phishing "
            "e engenharia social.\n\n"
            f"Pontuação da Fase 3: {self.score}\n\n"
            "Preparando a próxima fase...",
            parent=self.root
        )

        # IMPORTANTE:
        # A Fase 3 não destrói a janela.
        # O main.py será responsável pela troca.

        if self.proxima_fase:
            self.root.after(
                100, 
                self.proxima_fase
                )


# ==============================================================================
# FUNÇÃO COMPATÍVEL COM O MAIN.PY
# ==============================================================================

def executar(root, proxima_fase=None):

    return CyberQuizApp(
        root,
        proxima_fase
    )


