import tkinter as tk
from tkinter import messagebox

# Se a fase 2 estiver em outro arquivo .py no mesmo diretório:
# import fase2


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


# ==============================================================================
# --- DADOS DO QUIZ ---
# ==============================================================================

QUESTIONS = [
    {
        "category": "🛡️ PRINCÍPIOS DE SEGURANÇA",
        "question": (
            "Um arquivo importante foi alterado sem autorização. "
            "Qual princípio da segurança foi afetado?"
        ),
        "options": [
            "Disponibilidade",
            "Confidencialidade",
            "Integridade",
            "Autenticação"
        ],
        "answer": 2,
        "explanations": [
            (
                "A disponibilidade garante que o sistema esteja acessível. "
                "O arquivo continuou lá, porém alterado.\n\n"
                "💡 Dica: Falou em sistema fora do ar? Pense em Disponibilidade."
            ),
            (
                "A confidencialidade protege contra acesso não autorizado "
                "(vazamento). O foco aqui foi a alteração.\n\n"
                "💡 Dica: Apenas leu dados sem permissão? Pense em Confidencialidade."
            ),
            (
                "A integridade garante que os dados permaneçam exatos, "
                "completos e sem alterações indevidas."
            ),
            (
                "A autenticação verifica a identidade de quem acessa, "
                "mas não o conteúdo do arquivo.\n\n"
                "💡 Dica: Confirmar quem é o usuário? Pense em Autenticação."
            )
        ]
    }
]


# ==============================================================================
# --- APLICAÇÃO DA FASE 1 ---
# ==============================================================================

class CyberQuizApp:

    def __init__(self, root, proxima_fase=None):
        self.root = root
        self.proxima_fase = proxima_fase

        self.root.title("CyberShield: Ethical Hacker Quiz")
        self.root.geometry("660x560")
        self.root.resizable(False, False)

        self.current_q = 0
        self.lives = 3
        self.score = 0
        self.disabled_options = set()

        self.setup_ui()
        self.load_question()

    # ==========================================================================
    # --- INTERFACE ---
    # ==========================================================================

    def setup_ui(self):
        # Canvas de fundo
        self.bg_canvas = tk.Canvas(
            self.root,
            width=660,
            height=560,
            highlightthickness=0
        )
        self.bg_canvas.pack(fill="both", expand=True)
        self.draw_cyber_background()

        # Header / Barra de status
        self.status_frame = tk.Frame(self.bg_canvas, bg=COLOR_BG_TOP)
        self.bg_canvas.create_window(330, 35, window=self.status_frame, width=620)

        self.lbl_firewall = tk.Label(
            self.status_frame,
            text=f"🛡️ FIREWALL: {'█ ' * self.lives}",
            font=("Consolas", 13, "bold"),
            fg=COLOR_HEALTH,
            bg=COLOR_BG_TOP
        )
        self.lbl_firewall.pack(side="left")

        self.lbl_score = tk.Label(
            self.status_frame,
            text=f"SCORE: {self.score}",
            font=("Consolas", 13, "bold"),
            fg=COLOR_CYAN_GLOW,
            bg=COLOR_BG_TOP
        )
        self.lbl_score.pack(side="right")

        # Card Principal
        self.card_frame = tk.Frame(
            self.bg_canvas,
            bg=COLOR_CARD_BG,
            highlightbackground=COLOR_CARD_BORDER,
            highlightthickness=2,
            bd=0
        )
        self.bg_canvas.create_window(330, 290, window=self.card_frame, width=620, height=430)

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
            font=("Segoe UI", 12),
            fg=COLOR_TEXT_MAIN,
            bg=COLOR_CARD_BG,
            wraplength=570,
            justify="left"
        )
        self.lbl_question.pack(anchor="w", padx=20, pady=10)

        # Botões
        self.btn_frame = tk.Frame(self.card_frame, bg=COLOR_CARD_BG)
        self.btn_frame.pack(fill="both", expand=True, padx=20, pady=10)

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
            btn.pack(fill="x", pady=6, ipady=4)

            btn.bind("<Enter>", lambda e, b=btn: self.on_hover_enter(b))
            btn.bind("<Leave>", lambda e, b=btn: self.on_hover_leave(b))

            self.buttons.append(btn)

    # ==========================================================================
    # --- HOVER DOS BOTÕES ---
    # ==========================================================================

    def on_hover_enter(self, btn):
        if str(btn["state"]) == "normal":
            btn.config(bg=COLOR_BTN_HOVER, fg=COLOR_TEXT_MAIN)

    def on_hover_leave(self, btn):
        if str(btn["state"]) == "normal":
            btn.config(bg=COLOR_BTN_BG, fg=COLOR_TEXT_MUTED)

    # ==========================================================================
    # --- FUNDO ---
    # ==========================================================================

    def draw_cyber_background(self):
        width, height = 660, 560
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

        self.bg_canvas.create_line(30, 25, 180, 25, 230, 50, 430, 50, fill=line_color, width=1.5)
        self.bg_canvas.create_oval(177, 22, 183, 28, fill=glow_dot, outline="")
        self.bg_canvas.create_oval(427, 47, 433, 53, fill=glow_dot, outline="")

        self.bg_canvas.create_line(50, 530, 200, 530, 250, 510, 500, 510, 550, 535, fill=line_color, width=1.5)
        self.bg_canvas.create_oval(247, 507, 253, 513, fill=glow_dot, outline="")
        self.bg_canvas.create_oval(497, 507, 503, 513, fill=glow_dot, outline="")

    @staticmethod
    def hex_to_rgb(hex_str):
        hex_str = hex_str.lstrip("#")
        return tuple(int(hex_str[i:i + 2], 16) for i in (0, 2, 4))

    # ==========================================================================
    # --- CARREGAR PERGUNTA ---
    # ==========================================================================

    def load_question(self):
        if self.current_q < len(QUESTIONS):
            q_data = QUESTIONS[self.current_q]
            self.lbl_category.config(text=q_data["category"])
            self.lbl_question.config(text=q_data["question"])

            for i, opt in enumerate(q_data["options"]):
                if i not in self.disabled_options:
                    self.buttons[i].config(
                        text=f"[ {chr(65 + i)} ]   {opt}",
                        bg=COLOR_BTN_BG,
                        fg=COLOR_TEXT_MUTED,
                        state="normal",
                        cursor="hand2"
                    )
        else:
            messagebox.showinfo(
                "Fase 1 concluída! 🏆",
                f"Você protegeu o sistema!\n\nPontuação final: {self.score}"
            )
            if self.proxima_fase:
                self.proxima_fase()

    # ==========================================================================
    # --- VERIFICAR RESPOSTA ---
    # ==========================================================================

    def check_answer(self, selected_idx):
        q_data = QUESTIONS[self.current_q]
        correct_idx = q_data["answer"]
        explanation = q_data["explanations"][selected_idx]
        selected_btn = self.buttons[selected_idx]

        # ----------------------------------------------------------------------
        # RESPOSTA CORRETA
        # ----------------------------------------------------------------------
        if selected_idx == correct_idx:
            for btn in self.buttons:
                btn.config(state="disabled", cursor="arrow")

            selected_btn.config(
                bg=COLOR_CORRECT,
                fg="#000000",
                disabledforeground="#000000"
            )
            self.root.update()

            self.score += 100
            self.lbl_score.config(text=f"SCORE: {self.score}")

            messagebox.showinfo(
                "Resposta Correta! ✅",
                f"Parabéns! Você acertou!\n\n{explanation}"
            )

            self.current_q += 1
            self.disabled_options.clear()
            self.load_question()

        # ----------------------------------------------------------------------
        # RESPOSTA INCORRETA
        # ----------------------------------------------------------------------
        else:
            self.lives -= 1
            self.disabled_options.add(selected_idx)

            selected_btn.config(
                bg=COLOR_INCORRECT,
                fg="#FFFFFF",
                disabledforeground="#FFFFFF",
                state="disabled",
                cursor="arrow"
            )

            self.lbl_firewall.config(text=f"🛡️ FIREWALL: {'█ ' * self.lives}")
            self.root.update()

            messagebox.showwarning("Resposta Incorreta! ❌", explanation)

            # Game Over
            if self.lives == 0:
                messagebox.showerror(
                    "Game Over",
                    "O firewall caiu! O sistema foi hackeado.\n\nA Fase 1 será reiniciada."
                )
                self.current_q = 0
                self.lives = 3
                self.score = 0
                self.disabled_options.clear()

                self.lbl_firewall.config(text=f"🛡️ FIREWALL: {'█ ' * self.lives}")
                self.lbl_score.config(text=f"SCORE: {self.score}")
                self.load_question()


# ==============================================================================
# --- FUNÇÕES DE TRANSIÇÃO E EXECUÇÃO ---
# ==============================================================================

def executar(root, proxima_fase=None):
    return CyberQuizApp(root, proxima_fase)


def iniciar_fase_3():
    print("Fase 3 iniciada!")


def iniciar_fase_2():
    root = tk.Tk()
    # Exemplo caso o módulo fase2 esteja importado:
    # fase2.executar(root, iniciar_fase_3)
    root.mainloop()


if __name__ == "__main__":
    root = tk.Tk()
    app = CyberQuizApp(root)
    root.mainloop()
    import time
import string
import random
import itertools
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
# --- DADOS DAS PERGUNTAS DA FASE 2 ---
# ==============================================================================

QUIZ_QUESTIONS = [
    {
        "category": "🟢 FASE 2 (NÍVEL 1) — MÚLTIPLOS FATORES (MFA)",

        "question": (
            "Qual das opções abaixo oferece a melhor redução de risco "
            "no acesso a uma conta?"
        ),

        "options": [
            "A) Trocar a senha toda semana por uma frase curta",
            "B) Usar a mesma senha forte em todos os serviços bancários",
            "C) Usar uma senha forte e exclusiva combinada com MFA "
            "(Autenticação de Múltiplos Fatores)",
            "D) Salvar a senha no bloco de notas do computador"
        ],

        "answer": 2,

        "explanations": [
            "❌ INCORRETO: Senhas curtas continuam vulneráveis a "
            "força bruta, independente da frequência de troca.",

            "❌ INCORRETO: Reutilizar a mesma senha em múltiplos serviços "
            "cria o risco de vazamento em cascata.",

            "✅ CORRETO! A combinação de uma senha exclusiva com MFA "
            "cria duas camadas independentes de proteção.",

            "❌ INCORRETO: Arquivos de texto sem criptografia podem "
            "ser facilmente capturados por malwares locais."
        ]
    },

    {
        "category": "🟢 FASE 2 (NÍVEL 2) — GERENCIADORES DE SENHAS",

        "question": (
            "Qual é a principal vantagem de utilizar um Gerenciador "
            "de Senhas homologado?"
        ),

        "options": [
            "A) Permite memorizar dezenas de senhas complexas sem anotações",

            "B) Gera e armazena senhas longas, aleatórias e únicas "
            "para cada serviço sob um cofre criptografado",

            "C) Elimina a necessidade de usar senhas ou códigos de verificação",

            "D) Impede que computadores contraiam vírus ao navegar na internet"
        ],

        "answer": 1,

        "explanations": [
            "❌ INCORRETO: Você não precisa memorizá-las; "
            "o cofre faz isso por você.",

            "✅ CORRETO! O gerenciador elimina o reuso de senhas "
            "e armazena tudo sob uma única senha-mestre forte.",

            "❌ INCORRETO: A senha-mestre e o MFA ainda são essenciais "
            "para proteger o cofre.",

            "❌ INCORRETO: O gerenciador protege credenciais, "
            "não a execução de arquivos maliciosos no sistema."
        ]
    },

    {
        "category": "🟢 FASE 2 (NÍVEL 3) — CREDENTIAL STUFFING",

        "question": "O que é um ataque de 'Credential Stuffing'?",

        "options": [
            "A) Tentativa de adivinhar o PIN de 4 dígitos "
            "do celular por força bruta",

            "B) Automatização que testa pares de login/senha vazados "
            "de um site em vários outros serviços",

            "C) Criptografia maliciosa dos arquivos do computador "
            "para exigir resgate",

            "D) Redirecionamento da navegação para um roteador wi-fi falso"
        ],

        "answer": 1,

        "explanations": [
            "❌ INCORRETO: Esse é um ataque direto de PIN "
            "ou força bruta simples.",

            "✅ CORRETO! Atacantes usam vazamentos antigos para "
            "invadir contas de pessoas que reutilizam a mesma senha.",

            "❌ INCORRETO: Isso descreve a atuação de um Ransomware.",

            "❌ INCORRETO: Trata-se de um ataque Man-in-the-Middle "
            "ou Rogue AP."
        ]
    }
]


# ==============================================================================
# --- APLICAÇÃO DA FASE 2 ---
# ==============================================================================

class Phase2App:

    def __init__(self, root, proxima_fase=None):

        self.root = root
        self.proxima_fase = proxima_fase

        self.root.title(
            "CyberShield: Fase 2 — Gestão e Proteção de Senhas"
        )

        self.root.geometry("700x640")
        self.root.resizable(False, False)

        self.current_q = 0

        self.generated_mfa_token = ""
        self.mfa_time_left = 30
        self.mfa_timer_job = None

        self.setup_ui()
        self.load_step_brute_force()


    # ==========================================================================
    # --- INTERFACE PRINCIPAL ---
    # ==========================================================================

    def setup_ui(self):

        self.bg_canvas = tk.Canvas(
            self.root,
            width=700,
            height=640,
            highlightthickness=0
        )

        self.bg_canvas.pack(fill="both", expand=True)

        self.draw_cyber_background()

        # HEADER

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
            text="🔑 FASE 2: GESTÃO & PROTEÇÃO DE SENHAS",
            font=("Consolas", 11, "bold"),
            fg=COLOR_HEALTH,
            bg=COLOR_BG_TOP
        )

        self.lbl_header.pack(side="left")

        self.lbl_mode = tk.Label(
            self.status_frame,
            text="ETAPA 1/4",
            font=("Consolas", 11, "bold"),
            fg=COLOR_CYAN_GLOW,
            bg=COLOR_BG_TOP
        )

        self.lbl_mode.pack(side="right")

        # CARD

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
    # --- FUNDO ---
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
            30, 25,
            180, 25,
            230, 50,
            480, 50,
            fill=line_color,
            width=1.5
        )

        self.bg_canvas.create_oval(
            177, 22,
            183, 28,
            fill=glow_dot,
            outline=""
        )

        self.bg_canvas.create_oval(
            477, 47,
            483, 53,
            fill=glow_dot,
            outline=""
        )

        self.bg_canvas.create_line(
            50, 610,
            200, 610,
            250, 590,
            550, 590,
            fill=line_color,
            width=1.5
        )

        self.bg_canvas.create_oval(
            247, 587,
            253, 593,
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
    # --- FUNÇÕES AUXILIARES ---
    # ==========================================================================

    def clear_card(self):

        if self.mfa_timer_job:

            try:
                self.root.after_cancel(self.mfa_timer_job)
            except tk.TclError:
                pass

            self.mfa_timer_job = None

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
    # --- ETAPA 1: FORÇA BRUTA ---
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
            wraplength=600,
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

        self.entry_pass.insert(0, "gato")

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

        self.btn_next1.config(state="disabled")


    def run_brute_force(self):

        senha = self.entry_pass.get().strip().lower()

        if (
            not senha
            or len(senha) > 4
            or not senha.isalpha()
        ):
            messagebox.showwarning(
                "Aviso",
                "Informe uma palavra contendo de 1 a 4 letras minúsculas."
            )
            return

        caracteres = string.ascii_lowercase

        inicio = time.time()
        tentativas = 0
        descoberta = None

        for comp in range(1, len(senha) + 1):

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
            "[!] Iniciando simulação de força bruta...\n"
            f"[❌] SENHA ENCONTRADA: '{descoberta}'\n"
            f"[*] Total de combinações testadas: {tentativas:,}\n"
            f"[*] Tempo total de processamento: {tempo_gasto:.4f} segundos\n\n"
            "⚠️ CONCLUSÃO TÉCNICA: Senhas curtas e previsíveis "
            "possuem baixa resistência contra tentativas automatizadas."
        )

        self.txt_console.config(state="normal")

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
    # --- ETAPA 2: SENHA FORTE ---
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
            wraplength=600,
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
            text=f"{'✅' if has_len else '❌'} Pelo menos 8 caracteres",
            fg=COLOR_CORRECT if has_len else COLOR_INCORRECT
        )

        self.lbl_req_upper.config(
            text=f"{'✅' if has_upper else '❌'} Pelo menos 1 letra maiúscula (A-Z)",
            fg=COLOR_CORRECT if has_upper else COLOR_INCORRECT
        )

        self.lbl_req_lower.config(
            text=f"{'✅' if has_lower else '❌'} Pelo menos 1 letra minúscula (a-z)",
            fg=COLOR_CORRECT if has_lower else COLOR_INCORRECT
        )

        self.lbl_req_digit.config(
            text=f"{'✅' if has_digit else '❌'} Pelo menos 1 número (0-9)",
            fg=COLOR_CORRECT if has_digit else COLOR_INCORRECT
        )

        self.lbl_req_symbol.config(
            text=f"{'✅' if has_symbol else '❌'} Pelo menos 1 símbolo (!@#$%^&*)",
            fg=COLOR_CORRECT if has_symbol else COLOR_INCORRECT
        )

        score = sum([
            has_len,
            has_upper,
            has_lower,
            has_digit,
            has_symbol
        ])

        self.canvas_strength.delete("all")

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
            self.btn_next2.config(state="normal")
        else:
            self.btn_next2.config(state="disabled")


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

        random.shuffle(password)

        res = "".join(password)

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
    # --- ETAPA 3: MFA ---
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
                "credenciais e solicite o token:"
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

        # TOKEN

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
        ).pack(side="left")

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


    def request_mfa_token(self):

        if self.mfa_timer_job:

            try:
                self.root.after_cancel(
                    self.mfa_timer_job
                )
            except tk.TclError:
                pass

        self.generated_mfa_token = str(
            random.randint(100000, 999999)
        )

        self.mfa_time_left = 30

        self.update_mfa_timer()


    def update_mfa_timer(self):

        if self.mfa_time_left > 0:

            self.lbl_mfa_display.config(
                text=(
                    f"📲 TOKEN MFA: {self.generated_mfa_token} "
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

            self.mfa_timer_job = None

            self.lbl_mfa_display.config(
                text="📲 TOKEN EXPIRADO! Solicite um novo código.",
                fg=COLOR_INCORRECT
            )


    def verify_full_login(self):

        u = self.entry_login_user.get().strip()
        p = self.entry_login_pass.get().strip()
        tok = self.entry_token_user.get().strip()

        if not u or not p:

            messagebox.showwarning(
                "Erro de Validação",
                "Preencha o usuário e a senha!"
            )

            return

        if not self.generated_mfa_token:

            messagebox.showerror(
                "Acesso Negado",
                "Solicite um Token MFA válido antes de tentar o acesso."
            )

            return

        if tok == self.generated_mfa_token:

            messagebox.showinfo(
                "Autenticação Concluída! 🔐",
                "Login bem-sucedido!\n\n"
                "A combinação da senha exclusiva com a "
                "validação em dois fatores (MFA) impediu "
                "o acesso não autorizado."
            )

            self.load_quiz_mode()

        else:

            messagebox.showerror(
                "Falha no Login ❌",
                "Código MFA incorreto ou expirado! "
                "Verifique e tente novamente."
            )


    # ==========================================================================
    # --- ETAPA 4: QUIZ ---
    # ==========================================================================

    def load_quiz_mode(self):

        self.clear_card()

        self.lbl_mode.config(
            text=(
                f"ETAPA 4/4 — QUIZ "
                f"({self.current_q + 1}/{len(QUIZ_QUESTIONS)})"
            )
        )

        q_data = QUIZ_QUESTIONS[self.current_q]

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

            btn.pack(
                fill="x",
                padx=20,
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

            self.quiz_buttons.append(btn)


    def check_quiz_answer(self, selected_idx):

        for btn in self.quiz_buttons:
            btn.config(state="disabled")

        q_data = QUIZ_QUESTIONS[self.current_q]

        correct_idx = q_data["answer"]

        selected_btn = self.quiz_buttons[selected_idx]

        if selected_idx == correct_idx:

            selected_btn.config(
                bg=COLOR_CORRECT,
                fg="#000000"
            )

            self.root.update()

            messagebox.showinfo(
                "Resposta Correta! 🎯",
                q_data["explanations"][selected_idx]
            )

            self.current_q += 1

            if self.current_q < len(QUIZ_QUESTIONS):
                self.load_quiz_mode()
            else:
                self.advance_to_next_phase()

        else:

            selected_btn.config(
                bg=COLOR_INCORRECT,
                fg="#FFFFFF"
            )

            correct_btn = self.quiz_buttons[correct_idx]
            correct_btn.config(
                bg=COLOR_CORRECT,
                fg="#000000"
            )

            self.root.update()

            messagebox.showerror(
                "Resposta Incorreta ❌",
                q_data["explanations"][selected_idx]
            )

            self.current_q += 1

            if self.current_q < len(QUIZ_QUESTIONS):
                self.load_quiz_mode()
            else:
                self.advance_to_next_phase()


    def advance_to_next_phase(self):

        messagebox.showinfo(
            "Fase 2 Concluída! 🏆",
            "Parabéns! Você concluiu todos os treinamentos "
            "e perguntas da Fase 2."
        )

        if callable(self.proxima_fase):
            self.proxima_fase()
        else:
            self.root.destroy()


# ==============================================================================
# --- EXECUÇÃO PRINCIPAL ---
# ==============================================================================

if __name__ == "__main__":
    root = tk.Tk()
    app = Phase2App(root)
    root.mainloop()
    import tkinter as tk
from tkinter import messagebox

# ==============================================================================
# CORES
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

# ==============================================================================
# PERGUNTAS DA FASE 3
# ==============================================================================

QUESTIONS = [
    {
        "category": "🎣 FASE 3 — ENGENHARIA SOCIAL (PHISHING)",

        "question": (
            "Você recebe um e-mail urgente pedindo login através "
            "de um link. O que deve fazer primeiro?"
        ),

        "options": [
            "Clicar rapidamente para evitar o bloqueio",
            "Responder pedindo a senha do remetente",
            "Verificar remetente, endereço e contexto da mensagem",
            "Encaminhar para todos os colegas"
        ],

        "answer": 2,

        "explanations": [
            "O senso de urgência é um dos principais gatilhos "
            "psicológicos usados em ataques de phishing.\n\n"
            "💡 Dica: Desconfie de mensagens que exigem ação imediata.",

            "Não valida a identidade do remetente e pode expor "
            "você ainda mais ao atacante.\n\n"
            "💡 Dica: Nunca forneça senhas ou informações pessoais.",

            "Exato! Analisar o endereço real de envio, os links "
            "e a coerência do texto ajuda a evitar golpes.",

            "Pode espalhar um possível link malicioso para outras "
            "pessoas.\n\n"
            "💡 Dica: Notifique a equipe de segurança/TI."
        ]
    }
]


# ==============================================================================
# APLICAÇÃO
# ==============================================================================

class CyberQuizApp:

    def __init__(self, root, proxima_fase=None):

        self.root = root
        self.proxima_fase = proxima_fase

        self.root.title(
            "CyberShield: Fase 3 — Engenharia Social"
        )

        self.root.geometry("660x560")
        self.root.resizable(False, False)

        self.current_q = 0
        self.lives = 3
        self.score = 0
        self.buttons = []

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

        # HEADER

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

        self.lbl_firewall = tk.Label(
            self.status_frame,
            text=f"🛡️ FIREWALL: {'█ ' * self.lives}",
            font=("Consolas", 13, "bold"),
            fg=COLOR_HEALTH,
            bg=COLOR_BG_TOP
        )

        self.lbl_firewall.pack(
            side="left"
        )

        self.lbl_score = tk.Label(
            self.status_frame,
            text=f"SCORE: {self.score}",
            font=("Consolas", 13, "bold"),
            fg=COLOR_CYAN_GLOW,
            bg=COLOR_BG_TOP
        )

        self.lbl_score.pack(
            side="right"
        )

        # CARD

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

        for y in range(height):

            r = int(r1 + (r2 - r1) * (y / height))
            g = int(g1 + (g2 - g1) * (y / height))
            b = int(b1 + (b2 - b1) * (y / height))

            color = f"#{r:02x}{g:02x}{b:02x}"

            self.bg_canvas.create_line(
                0, y, width, y,
                fill=color
            )

        line_color = "#0B3254"
        glow_dot = COLOR_CYAN_GLOW

        # Circuito superior
        self.bg_canvas.create_line(
            30, 25, 180, 25, 230, 50, 430, 50,
            fill=line_color, width=1.5
        )
        self.bg_canvas.create_oval(
            177, 22, 183, 28, fill=glow_dot, outline=""
        )
        self.bg_canvas.create_oval(
            427, 47, 433, 53, fill=glow_dot, outline=""
        )

        # Circuito inferior
        self.bg_canvas.create_line(
            50, 530, 200, 530, 250, 510, 500, 510, 550, 535,
            fill=line_color, width=1.5
        )
        self.bg_canvas.create_oval(
            247, 507, 253, 513, fill=glow_dot, outline=""
        )
        self.bg_canvas.create_oval(
            497, 507, 503, 513, fill=glow_dot, outline=""
        )

    # ==========================================================================
    # CONVERSÃO DE COR
    # ==========================================================================

    @staticmethod
    def hex_to_rgb(hex_str):

        hex_str = hex_str.lstrip("#")

        return tuple(
            int(hex_str[i:i + 2], 16)
            for i in (0, 2, 4)
        )

    # ==========================================================================
    # CARREGAR PERGUNTA
    # ==========================================================================

    def load_question(self):

        if self.current_q < len(QUESTIONS):

            q_data = QUESTIONS[self.current_q]

            self.lbl_category.config(text=q_data["category"])
            self.lbl_question.config(text=q_data["question"])

            # Limpa botões antigos caso existam
            for btn in self.buttons:
                btn.destroy()
            self.buttons.clear()

            # Cria botões dinamicamente conforme a quantidade de opções
            for i, opt in enumerate(q_data["options"]):

                btn = tk.Button(
                    self.btn_frame,
                    text=f"[ {chr(65 + i)} ]   {opt}",
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
                    pady=6,
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

        else:
            self.finish_phase()

    # ==========================================================================
    # VERIFICAR RESPOSTA
    # ==========================================================================

    def check_answer(self, selected_idx):

        for btn in self.buttons:
            btn.config(state="disabled")

        q_data = QUESTIONS[self.current_q]
        correct_idx = q_data["answer"]
        explanation = q_data["explanations"][selected_idx]
        selected_btn = self.buttons[selected_idx]

        if selected_idx == correct_idx:

            selected_btn.config(
                bg=COLOR_CORRECT,
                fg="#000000"
            )

            self.root.update()

            self.score += 100
            self.lbl_score.config(text=f"SCORE: {self.score}")

            messagebox.showinfo(
                "Resposta Correta! ✅",
                f"Parabéns! Você acertou!\n\n{explanation}"
            )

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
                explanation
            )

            if self.lives <= 0:

                messagebox.showerror(
                    "Game Over",
                    "O firewall caiu!\n\n"
                    "O sistema foi comprometido. "
                    "Tente novamente."
                )

                self.root.destroy()
                return

        self.current_q += 1
        self.load_question()

    # ==========================================================================
    # FINAL DA FASE
    # ==========================================================================

    def finish_phase(self):

        messagebox.showinfo(
            "Fase 3 Concluída! 🏆",
            "Parabéns!\n\n"
            "Você concluiu o treinamento de "
            "Engenharia Social e Phishing.\n\n"
            f"Pontuação da Fase 3: {self.score}"
        )

        if callable(self.proxima_fase):
            self.proxima_fase()
        else:
            self.root.destroy()


# ==============================================================================
# FUNÇÃO PARA O MAIN.PY
# ==============================================================================

def executar(root, proxima_fase=None):
    app = CyberQuizApp(root, proxima_fase)
    return app


# ==============================================================================
# EXECUÇÃO DIRETA PARA TESTE
# ==============================================================================

if __name__ == "__main__":
    root = tk.Tk()
    app = executar(root)
    root.mainloop()
    import tkinter as tk
from tkinter import messagebox
import re

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
# --- BANCO DE PERGUNTAS DA FASE 4 (INTERNET, LINKS E PHISHING) ---
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


class Phase4App:
    def __init__(self, root):
        self.root = root
        self.root.title("CyberShield: Fase 4 — Internet, Links & Phishing")
        self.root.geometry("700x640")
        self.root.resizable(False, False)

        self.current_q = 0

        # Atributos do Simulador de Phishing (Etapa 2)
        self.phish_sender_var = None
        self.phish_link_var = None
        self.phish_urgency_var = None
        self.phish_attachment_var = None

        self.setup_ui()
        self.load_step_url_lab()

    def setup_ui(self):
        # --- CANVAS DE FUNDO ---
        self.bg_canvas = tk.Canvas(self.root, width=700, height=640, highlightthickness=0)
        self.bg_canvas.pack(fill="both", expand=True)
        self.draw_cyber_background()

        # --- HEADER DE STATUS ---
        self.status_frame = tk.Frame(self.bg_canvas, bg=COLOR_BG_TOP)
        self.bg_canvas.create_window(350, 35, window=self.status_frame, width=660)

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

        # --- CARD PRINCIPAL ---
        self.card_frame = tk.Frame(
            self.bg_canvas, 
            bg=COLOR_CARD_BG, 
            highlightbackground=COLOR_CARD_BORDER, 
            highlightthickness=2,
            bd=0
        )
        self.bg_canvas.create_window(350, 330, window=self.card_frame, width=660, height=520)

    def draw_cyber_background(self):
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

    @staticmethod
    def hex_to_rgb(hex_str):
        hex_str = hex_str.lstrip('#')
        return tuple(int(hex_str[i:i+2], 16) for i in (0, 2, 4))

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

    def on_hover_enter(self, btn):
        if btn["state"] == "normal":
            btn.config(bg=COLOR_BTN_HOVER, fg=COLOR_TEXT_MAIN)

    def on_hover_leave(self, btn):
        if btn["state"] == "normal":
            btn.config(bg=COLOR_BTN_BG, fg=COLOR_TEXT_MUTED)

    # ==========================================================================
    # --- ETAPA 1: LABORATÓRIO DE INSPEÇÃO DE URLS E DOMÍNIOS ---
    # ==========================================================================
    def load_step_url_lab(self):
        self.clear_card()
        self.lbl_mode.config(text="ETAPA 1/3 — INSPEÇÃO DE URLS E DOMÍNIOS")

        lbl_title = tk.Label(
            self.card_frame, 
            text="🔍 LABORATÓRIO DE ANÁLISE DE URLS & TYPOSQUATTING", 
            font=("Segoe UI", 10, "bold"), 
            fg=COLOR_CYAN_GLOW, 
            bg=COLOR_CARD_BG
        )
        lbl_title.pack(anchor="w", padx=20, pady=(12, 4))

        lbl_desc = tk.Label(
            self.card_frame, 
            text="Insira uma URL para analisar a estrutura do domínio. Teste com os exemplos fornecidos para identificar truques de camuflagem de atacantes:", 
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

        tk.Label(frame_input, text="URL para Análise:", font=("Segoe UI", 9, "bold"), fg=COLOR_TEXT_MUTED, bg=COLOR_CARD_BG).pack(anchor="w")

        self.entry_url_input = tk.Entry(
            frame_input, 
            font=("Segoe UI", 10), 
            bg=COLOR_BG_TOP, 
            fg=COLOR_TEXT_MAIN, 
            insertbackground=COLOR_TEXT_MAIN,
            bd=1,
            relief="solid"
        )
        self.entry_url_input.insert(0, "https://www.banc0-seguro-login.com/atualizacao")
        self.entry_url_input.pack(fill="x", pady=2)
        self.entry_url_input.bind("<KeyRelease>", self.update_live_url_analysis)

        # Botões Rápidos de Payloads de Teste
        frame_payloads = tk.Frame(frame_input, bg=COLOR_CARD_BG)
        frame_payloads.pack(fill="x", pady=2)

        btn_p1 = tk.Button(
            frame_payloads, text="⚡ Teste 1: Typosquatting", font=("Segoe UI", 8, "bold"),
            bg="#1B3B6F", fg=COLOR_CYAN_GLOW, activebackground=COLOR_BTN_HOVER, activeforeground=COLOR_TEXT_MAIN,
            relief="flat", cursor="hand2", command=lambda: self.set_url_payload("https://www.banc0-seguro-login.com/atualizacao")
        )
        btn_p1.pack(side="left", padx=(0, 5))

        btn_p2 = tk.Button(
            frame_payloads, text="⚡ Teste 2: Subdomínio Falso", font=("Segoe UI", 8, "bold"),
            bg="#1B3B6F", fg=COLOR_CYAN_GLOW, activebackground=COLOR_BTN_HOVER, activeforeground=COLOR_TEXT_MAIN,
            relief="flat", cursor="hand2", command=lambda: self.set_url_payload("https://www.meubanco.com.br.login-atendimento.net/auth")
        )
        btn_p2.pack(side="left", padx=5)

        btn_p3 = tk.Button(
            frame_payloads, text="⚡ Teste 3: URL Oficial", font=("Segoe UI", 8, "bold"),
            bg="#1B3B6F", fg=COLOR_CYAN_GLOW, activebackground=COLOR_BTN_HOVER, activeforeground=COLOR_TEXT_MAIN,
            relief="flat", cursor="hand2", command=lambda: self.set_url_payload("https://www.meubanco.com.br/login")
        )
        btn_p3.pack(side="left", padx=5)

        # Painel de Resultados de Inspeção
        tk.Label(self.card_frame, text="Decomposição da URL:", font=("Segoe UI", 9, "bold"), fg=COLOR_TEXT_MUTED, bg=COLOR_CARD_BG).pack(anchor="w", padx=20, pady=(4, 1))

        self.lbl_url_protocol = tk.Label(self.card_frame, text="", font=("Consolas", 8, "bold"), fg=COLOR_HEALTH, bg=COLOR_BG_TOP, bd=1, relief="solid", anchor="w", padx=10)
        self.lbl_url_protocol.pack(fill="x", padx=20, pady=2)

        self.lbl_url_domain = tk.Label(self.card_frame, text="", font=("Consolas", 8, "bold"), fg=COLOR_WARNING, bg=COLOR_BG_TOP, bd=1, relief="solid", anchor="w", padx=10)
        self.lbl_url_domain.pack(fill="x", padx=20, pady=2)

        self.lbl_url_status = tk.Label(self.card_frame, text="", font=("Segoe UI", 9, "bold"), bg=COLOR_CARD_BG, wraplength=600, justify="left")
        self.lbl_url_status.pack(anchor="w", padx=20, pady=6)

        self.update_live_url_analysis()

        btn_next1 = self.create_custom_button(self.card_frame, "Avançar para o Analisador de E-mail Phishing ➔", self.load_step_phishing_lab)
        btn_next1.pack(fill="x", padx=20, pady=(6, 12))

    def set_url_payload(self, url):
        self.entry_url_input.delete(0, tk.END)
        self.entry_url_input.insert(0, url)
        self.update_live_url_analysis()

    def update_live_url_analysis(self, event=None):
        url = self.entry_url_input.get().strip()

        # Extração simples de Protocolo e Domínio
        protocol_match = re.match(r'^(https?://)', url, re.IGNORECASE)
        protocol = protocol_match.group(1) if protocol_match else "HTTP (Não Seguro / Ausente)"
        
        clean_url = re.sub(r'^(https?://)', '', url, flags=re.IGNORECASE)
        domain_part = clean_url.split('/')[0] if '/' in clean_url else clean_url

        self.lbl_url_protocol.config(text=f"PROTOCOLO: {protocol}")
        self.lbl_url_domain.config(text=f"DOMÍNIO PRINCIPAL RECONHECIDO: {domain_part}")

        alerts = []
        if "0" in domain_part or "1" in domain_part:
            alerts.append("⚠️ Leet Speak / Substituição de letras por números detectada (ex: '0' no lugar de 'o').")
        if domain_part.count(".") > 2:
            alerts.append("⚠️ Múltiplos subdomínios encadeados. O domínio real é a última parte antes do TLD (.net, .com).")
        if "-" in domain_part:
            alerts.append("⚠️ Uso de hífen em nomes de marcas (técnica comum em Typosquatting).")
        if not url.startswith("https://"):
            alerts.append("❌ Conexão não criptografada (Sem HTTPS).")

        if alerts:
            self.lbl_url_status.config(
                text="AMEAÇA DETECTADA:\n" + "\n".join(alerts),
                fg=COLOR_INCORRECT
            )
        else:
            self.lbl_url_status.config(
                text="✅ ESTRUTURA NORMAL: O domínio aparenta seguir padrões legítimos de formatação.",
                fg=COLOR_HEALTH
            )

    # ==========================================================================
    # --- ETAPA 2: SIMULADOR DE ANÁLISE DE PHISHING (AVALIADOR DE E-MAIL) ---
    # ==========================================================================
    def load_step_phishing_lab(self):
        self.clear_card()
        self.lbl_mode.config(text="ETAPA 2/3 — ANALISADOR DE PHISHING")

        lbl_title = tk.Label(
            self.card_frame, 
            text="🛡️ MINIGAME: MOTOR DE DETECÇÃO DE PHISHING EM E-MAILS", 
            font=("Segoe UI", 10, "bold"), 
            fg=COLOR_CYAN_GLOW, 
            bg=COLOR_CARD_BG
        )
        lbl_title.pack(anchor="w", padx=20, pady=(10, 2))

        lbl_desc = tk.Label(
            self.card_frame, 
            text="Ajuste os parâmetros da mensagem recebida para simular a análise de um filtro Anti-Phishing de e-mail:", 
            font=("Segoe UI", 9), 
            fg=COLOR_TEXT_MAIN, 
            bg=COLOR_CARD_BG, 
            wraplength=610, 
            justify="left"
        )
        lbl_desc.pack(anchor="w", padx=20, pady=2)

        # Grid de Atributos do E-mail
        grid_frame = tk.Frame(self.card_frame, bg=COLOR_CARD_BG)
        grid_frame.pack(fill="x", padx=20, pady=6)

        # Atributo 1: Remetente
        tk.Label(grid_frame, text="Remetente:", font=("Segoe UI", 9, "bold"), fg=COLOR_TEXT_MUTED, bg=COLOR_CARD_BG).grid(row=0, column=0, sticky="w", pady=3)
        self.phish_sender_var = tk.StringVar(value="suporte@seguranca-banco.com")
        opt_sender = tk.OptionMenu(grid_frame, self.phish_sender_var, "suporte@seguranca-banco.com", "contato@bancooficial.com.br")
        opt_sender.config(bg=COLOR_BTN_BG, fg=COLOR_TEXT_MAIN, activebackground=COLOR_BTN_HOVER, activeforeground=COLOR_TEXT_MAIN, highlightthickness=0, width=28)
        opt_sender.grid(row=0, column=1, sticky="w", padx=10, pady=3)

        # Atributo 2: Urgência do Texto
        tk.Label(grid_frame, text="Tom da Mensagem:", font=("Segoe UI", 9, "bold"), fg=COLOR_TEXT_MUTED, bg=COLOR_CARD_BG).grid(row=1, column=0, sticky="w", pady=3)
        self.phish_urgency_var = tk.StringVar(value="Urgente: Conta Bloqueada em 2h!")
        opt_urgency = tk.OptionMenu(grid_frame, self.phish_urgency_var, "Urgente: Conta Bloqueada em 2h!", "Informativo: Seu Extrato Mensal")
        opt_urgency.config(bg=COLOR_BTN_BG, fg=COLOR_TEXT_MAIN, activebackground=COLOR_BTN_HOVER, activeforeground=COLOR_TEXT_MAIN, highlightthickness=0, width=28)
        opt_urgency.grid(row=1, column=1, sticky="w", padx=10, pady=3)

        # Atributo 3: Destino do Link
        tk.Label(grid_frame, text="Link de Destino:", font=("Segoe UI", 9, "bold"), fg=COLOR_TEXT_MUTED, bg=COLOR_CARD_BG).grid(row=2, column=0, sticky="w", pady=3)
        self.phish_link_var = tk.StringVar(value="http://bit.ly/recuperar-senha")
        opt_link = tk.OptionMenu(grid_frame, self.phish_link_var, "http://bit.ly/recuperar-senha", "https://bancooficial.com.br/extrato")
        opt_link.config(bg=COLOR_BTN_BG, fg=COLOR_TEXT_MAIN, activebackground=COLOR_BTN_HOVER, activeforeground=COLOR_TEXT_MAIN, highlightthickness=0, width=28)
        opt_link.grid(row=2, column=1, sticky="w", padx=10, pady=3)

        # Atributo 4: Anexo
        tk.Label(grid_frame, text="Arquivo Anexo:", font=("Segoe UI", 9, "bold"), fg=COLOR_TEXT_MUTED, bg=COLOR_CARD_BG).grid(row=3, column=0, sticky="w", pady=3)
        self.phish_attachment_var = tk.StringVar(value="Comprovante.pdf.exe")
        opt_attach = tk.OptionMenu(grid_frame, self.phish_attachment_var, "Comprovante.pdf.exe", "Sem Anexo / Nenhum")
        opt_attach.config(bg=COLOR_BTN_BG, fg=COLOR_TEXT_MAIN, activebackground=COLOR_BTN_HOVER, activeforeground=COLOR_TEXT_MAIN, highlightthickness=0, width=28)
        opt_attach.grid(row=3, column=1, sticky="w", padx=10, pady=3)

        btn_eval = self.create_custom_button(self.card_frame, "⚙️ Executar Varredura Anti-Phishing", self.evaluate_phishing)
        btn_eval.pack(fill="x", padx=20, pady=6)

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
        self.lbl_phish_result.pack(fill="x", padx=20, pady=4)

        self.btn_next2 = self.create_custom_button(self.card_frame, "Ir para o Quiz Conceitual Expandido ➔", self.load_quiz_mode)
        self.btn_next2.pack(fill="x", padx=20, pady=(8, 12))

    def evaluate_phishing(self):
        sender = self.phish_sender_var.get()
        urgency = self.phish_urgency_var.get()
        link = self.phish_link_var.get()
        attach = self.phish_attachment_var.get()

        flags = []
        if "seguranca-banco.com" in sender:
            flags.append("❌ Domínio do remetente não oficial.")
        if "Urgente" in urgency:
            flags.append("❌ Gatilho alarmista de urgência/falso senso de pânico.")
        if "bit.ly" in link or "http://" in link:
            flags.append("❌ Uso de link encurtado/não seguro (HTTP).")
        if ".exe" in attach:
            flags.append("❌ Anexo com extensão executável dupla perigosa (.pdf.exe).")

        if not flags:
            messagebox.showinfo(
                "E-MAIL LEGÍTIMO VERIFICADO! 🟢",
                "Nenhum indicador de comprometimento (IoC) foi encontrado.\n\n- Remetente Oficial\n- Comunicação Normal\n- Link Seguro com HTTPS\n- Sem Anexos Suspeitos"
            )
            self.lbl_phish_result.config(text="✅ DECISÃO: E-MAIL SEGURO / CAIXA DE ENTRADA", fg=COLOR_HEALTH)
        else:
            reason_str = "\n".join(flags)
            messagebox.showerror(
                "PHISHING DETECTADO! 🚨",
                f"O motor de segurança identificou os seguintes alertas de ameaça:\n\n{reason_str}"
            )
            self.lbl_phish_result.config(text=f"❌ DECISÃO: AMEAÇA BLOQUEADA ({len(flags)} ALERTAS)", fg=COLOR_INCORRECT)

    # ==========================================================================
    # --- ETAPA 3: QUIZ EDUCATIVO EXPANDIDO ---
    # ==========================================================================
    def load_quiz_mode(self):
        self.clear_card()
        self.lbl_mode.config(text=f"ETAPA 3/3 — QUIZ ({self.current_q + 1}/{len(QUIZ_FASE_4)})")

        q_data = QUIZ_FASE_4[self.current_q]

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
            btn = self.create_custom_button(
                self.card_frame, 
                text=opt, 
                command=lambda idx=i: self.check_quiz_answer(idx)
            )
            btn.config(anchor="w", justify="left", padx=15, pady=8)
            btn.pack(fill="x", padx=20, pady=4)
            self.quiz_buttons.append(btn)

    def check_quiz_answer(self, selected_idx):
        q_data = QUIZ_FASE_4[self.current_q]
        correct_idx = q_data["answer"]

        # Desativa os botões para evitar duplo clique
        for btn in self.quiz_buttons:
            btn.config(state="disabled")

        if selected_idx == correct_idx:
            self.quiz_buttons[selected_idx].config(bg=COLOR_CORRECT, fg="#000000")
            messagebox.showinfo(
                "RESPOSTA CORRETA! 🎯", 
                f"{q_data['explanations'][selected_idx]}\n\n{q_data['tip']}"
            )
        else:
            self.quiz_buttons[selected_idx].config(bg=COLOR_INCORRECT, fg="#FFFFFF")
            self.quiz_buttons[correct_idx].config(bg=COLOR_CORRECT, fg="#000000")
            messagebox.showerror(
                "RESPOSTA INCORRETA! ❌", 
                f"{q_data['explanations'][selected_idx]}\n\n{q_data['tip']}"
            )

        self.current_q += 1

        if self.current_q < len(QUIZ_FASE_4):
            self.root.after(800, self.load_quiz_mode)
        else:
            self.root.after(800, self.finish_phase)

    def finish_phase(self):
        self.clear_card()
        self.lbl_mode.config(text="FASE CONCLUÍDA")

        lbl_end = tk.Label(
            self.card_frame, 
            text="🚀 FASE 4 CONCLUÍDA COM SUCESSO!", 
            font=("Segoe UI", 12, "bold"), 
            fg=COLOR_HEALTH, 
            bg=COLOR_CARD_BG
        )
        lbl_end.pack(pady=(40, 10))

        lbl_sub = tk.Label(
            self.card_frame, 
            text="Você dominou a inspeção de URLs, identificou ataques de Typosquatting/Phishing e compreendeu o funcionamento real do protocolo HTTPS.\n\nSistema protegido contra links maliciosos!", 
            font=("Segoe UI", 10), 
            fg=COLOR_TEXT_MAIN, 
            bg=COLOR_CARD_BG, 
            wraplength=550, 
            justify="center"
        )
        lbl_sub.pack(pady=10)

        btn_close = self.create_custom_button(self.card_frame, "Encerrar Módulo", self.root.destroy)
        btn_close.pack(pady=30)

if __name__ == "__main__":
    root = tk.Tk()
    app = Phase4App(root)
    root.mainloop()

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
    import hashlib
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
COLOR_HEALTH = "#00F5D4"       # Verde/Ciano Neon
COLOR_CORRECT = "#00E676"      # Verde vibrante para acerto
COLOR_INCORRECT = "#FF3366"    # Vermelho/Rosa Neon para erro
COLOR_WARNING = "#FFD166"      # Amarelo/Laranja para alertas

# ==============================================================================
# --- BANCO DE PERGUNTAS DA FASE 6 ---
# ==============================================================================
QUIZ_FASE_6 = [
    {
        "category": "🔐 INTEGRIDADE DE DADOS",
        "question": "Qual técnica gera um resumo criptográfico de tamanho fixo para verificar a integridade de um arquivo?",
        "options": [
            "A) DNS",
            "B) Hash",
            "C) DHCP",
            "D) MFA"
        ],
        "answer": 1,
        "explanations": [
            "❌ INCORRETO: DNS é o protocolo que traduz nomes de domínio em endereços IP.",
            "✅ CORRETO! O Hash é uma função unidirecional. Se o arquivo mudar apenas 1 bit, o Hash resultante muda completamente (Efeito Avalanche).",
            "❌ INCORRETO: DHCP atribui endereços IP dinamicamente para dispositivos da rede.",
            "❌ INCORRETO: MFA (Autenticação de Múltiplos Fatores) é usado para proteger o acesso a contas."
        ],
        "tip": "💡 Dica: Para checar se um arquivo baixado da internet foi alterado ou corrompido, compare o seu código Hash!"
    },
    {
        "category": "🔏 AUTENTICIDADE E NÃO-REPÚDIO",
        "question": "O que garante tanto a AUTENTICIDADE do remetente quanto a INTEGRIDADE da mensagem?",
        "options": [
            "A) Compressão de dados (.zip)",
            "B) Codificação Base64",
            "C) Assinatura Digital",
            "D) Configuração DHCP"
        ],
        "answer": 2,
        "explanations": [
            "❌ INCORRETO: A compressão apenas reduz o tamanho de arquivos.",
            "❌ INCORRETO: Base64 apenas converte dados binários em texto; não oferece segurança nem sigilo.",
            "✅ CORRETO! A Assinatura Digital utiliza criptografia assimétrica vinculando a identidade do autor ao conteúdo, garantindo o não-repúdio.",
            "❌ INCORRETO: DHCP é um serviço de atribuição de IP de rede."
        ],
        "tip": "💡 Dica: Assinatura Digital = Identidade do Autor + Validação contra alterações de conteúdo!"
    },
    {
        "category": "🔑 CRIPTOGRAFIA SIMÉTRICA VS ASSIMÉTRICA",
        "question": "Na Criptografia Assimétrica, qual chave é utilizada para CRIPTOGRAFAR um dado enviado com segurança para um destinatário específico?",
        "options": [
            "A) A Chave Privada do remetente",
            "B) A Chave Pública do destinatário",
            "C) A Chave Privada do destinatário",
            "D) A mesma Chave Única compartilhada via pendrive"
        ],
        "answer": 1,
        "explanations": [
            "❌ INCORRETO: A chave privada do remetente é usada para assinar digitalmente, não para encriptar arquivos confidenciais.",
            "✅ CORRETO! Qualquer pessoa pode usar a Chave Pública do destinatário para cifrar a mensagem, mas SOMENTE a Chave Privada do destinatário consegue decifrá-la.",
            "❌ INCORRETO: A chave privada do destinatário é secreta e nunca deve ser compartilhada.",
            "❌ INCORRETO: Usar uma única chave compartilhada descreve a Criptografia Simétrica."
        ],
        "tip": "💡 Dica: Criptografia Assimétrica: Chave Pública cifra, Chave Privada decifra!"
    },
    {
        "category": "⚠️ VULNERABILIDADES CRIPTOGRÁFICAS",
        "question": "O que ocorre durante um fenômeno conhecido como 'Colisão de Hash' (Hash Collision)?",
        "options": [
            "A) O algoritmo de Hash trava ao processar um arquivo muito grande",
            "B) Dois arquivos com conteúdos completamente diferentes geram exatamente o mesmo Hash",
            "C) A chave privada é exposta publicamente durante a transmissão",
            "D) O Hash do arquivo muda sozinho após o reinício do sistema"
        ],
        "answer": 1,
        "explanations": [
            "❌ INCORRETO: As funções de hash tratam arquivos de qualquer tamanho sem travar.",
            "✅ CORRETO! Uma colisão ocorre quando dois dados distintos resultam no mesmo Hash. É por isso que algoritmos antigos como MD5 e SHA-1 foram descontinuados.",
            "❌ INCORRETO: Colisões afetam algoritmos de hash, não a exposição de chaves privadas.",
            "❌ INCORRETO: O hash de um arquivo estático é determinístico e nunca muda espontaneamente."
        ],
        "tip": "💡 Dica: Algoritmos modernos como SHA-256 e SHA-3 são projetados para evitar colisões!"
    }
]

class Phase6App:
    def __init__(self, root):
        self.root = root
        self.root.title("CyberShield: Fase 6 — Integridade, Hash & Criptografia")
        self.root.geometry("700x640")
        self.root.resizable(False, False)

        self.current_q = 0
        self.simulated_message = "Transferir R$ 10.000,00 para Conta A"
        self.simulated_signature = ""

        self.setup_ui()
        self.load_step_hash_lab()

    def setup_ui(self):
        # --- CANVAS DE FUNDO ---
        self.bg_canvas = tk.Canvas(self.root, width=700, height=640, highlightthickness=0)
        self.bg_canvas.pack(fill="both", expand=True)
        self.draw_cyber_background()

        # --- HEADER DE STATUS ---
        self.status_frame = tk.Frame(self.bg_canvas, bg=COLOR_BG_TOP)
        self.bg_canvas.create_window(350, 35, window=self.status_frame, width=660)

        self.lbl_header = tk.Label(
            self.status_frame, 
            text="🛡️ FASE 6: INTEGRIDADE & CRIPTOGRAFIA", 
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
        self.card_frame = tk.Frame(
            self.bg_canvas, 
            bg=COLOR_CARD_BG, 
            highlightbackground=COLOR_CARD_BORDER, 
            highlightthickness=2,
            bd=0
        )
        self.bg_canvas.create_window(350, 330, window=self.card_frame, width=660, height=520)

    def draw_cyber_background(self):
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

    @staticmethod
    def hex_to_rgb(hex_str):
        hex_str = hex_str.lstrip('#')
        return tuple(int(hex_str[i:i+2], 16) for i in (0, 2, 4))

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

    def on_hover_enter(self, btn):
        if str(btn["state"]) == "normal":
            btn.config(bg=COLOR_BTN_HOVER, fg=COLOR_TEXT_MAIN)

    def on_hover_leave(self, btn):
        if str(btn["state"]) == "normal":
            btn.config(bg=COLOR_BTN_BG, fg=COLOR_TEXT_MUTED)

    # ==========================================================================
    # --- ETAPA 1: LABORATÓRIO DE HASHING & EFEITO AVALANCHE ---
    # ==========================================================================
    def load_step_hash_lab(self):
        self.clear_card()
        self.lbl_mode.config(text="ETAPA 1/3 — GERADOR DE HASH")

        lbl_title = tk.Label(
            self.card_frame, 
            text="⚡ LABORATÓRIO DE HASHING (SHA-256 EM TEMPO REAL)", 
            font=("Segoe UI", 10, "bold"), 
            fg=COLOR_CYAN_GLOW, 
            bg=COLOR_CARD_BG
        )
        lbl_title.pack(anchor="w", padx=20, pady=(15, 5))

        lbl_desc = tk.Label(
            self.card_frame, 
            text="Digite qualquer texto na caixa abaixo. Mude apenas 1 letra ou ponto para observar o 'Efeito Avalanche': o resumo de tamanho fixo muda 100%!", 
            font=("Segoe UI", 9), 
            fg=COLOR_TEXT_MAIN, 
            bg=COLOR_CARD_BG, 
            wraplength=600, 
            justify="left"
        )
        lbl_desc.pack(anchor="w", padx=20, pady=5)

        self.entry_hash_input = tk.Entry(
            self.card_frame, 
            font=("Segoe UI", 10), 
            bg=COLOR_BG_TOP, 
            fg=COLOR_TEXT_MAIN, 
            insertbackground=COLOR_TEXT_MAIN,
            bd=1,
            relief="solid"
        )
        self.entry_hash_input.insert(0, "Relatorio_Financeiro_2026.pdf")
        self.entry_hash_input.pack(fill="x", padx=20, pady=5)
        self.entry_hash_input.bind("<KeyRelease>", self.update_live_hash)

        tk.Label(self.card_frame, text="Resumo Criptográfico SHA-256 (64 caracteres hex):", font=("Segoe UI", 9, "bold"), fg=COLOR_TEXT_MUTED, bg=COLOR_CARD_BG).pack(anchor="w", padx=20, pady=(10, 2))

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
        self.lbl_hash_output.pack(fill="x", padx=20, pady=5)

        self.lbl_hash_info = tk.Label(
            self.card_frame, 
            text="💡 Teste: Adicione um ponto no final do texto acima e compare o resultado Hash obtido!", 
            font=("Segoe UI", 9, "italic"), 
            fg=COLOR_WARNING, 
            bg=COLOR_CARD_BG
        )
        self.lbl_hash_info.pack(anchor="w", padx=20, pady=10)

        self.update_live_hash()

        btn_next1 = self.create_custom_button(self.card_frame, "Avançar para Simulador de Assinatura Digital ➔", self.load_step_signature_lab)
        btn_next1.pack(fill="x", padx=20, pady=(10, 15))

    def update_live_hash(self, event=None):
        text = self.entry_hash_input.get()
        hash_result = hashlib.sha256(text.encode('utf-8')).hexdigest()
        self.lbl_hash_output.config(text=hash_result)

    # ==========================================================================
    # --- ETAPA 2: SIMULADOR DE ASSINATURA DIGITAL & TAMPERING ---
    # ==========================================================================
    def load_step_signature_lab(self):
        self.clear_card()
        self.lbl_mode.config(text="ETAPA 2/3 — ASSINATURA DIGITAL")

        lbl_title = tk.Label(
            self.card_frame, 
            text="🔏 MINIGAME: AUDITORIA E VERIFICAÇÃO DE ADULTERAÇÃO", 
            font=("Segoe UI", 10, "bold"), 
            fg=COLOR_CYAN_GLOW, 
            bg=COLOR_CARD_BG
        )
        lbl_title.pack(anchor="w", padx=20, pady=(15, 5))

        lbl_desc = tk.Label(
            self.card_frame, 
            text="A Assinatura Digital une o Hash da mensagem encriptado com a Chave Privada do remetente. Experimente alterar a ordem de pagamento e tente validar:", 
            font=("Segoe UI", 9), 
            fg=COLOR_TEXT_MAIN, 
            bg=COLOR_CARD_BG, 
            wraplength=600, 
            justify="left"
        )
        lbl_desc.pack(anchor="w", padx=20, pady=5)

        tk.Label(self.card_frame, text="Conteúdo do Documento / Ordem Bancária:", font=("Segoe UI", 9, "bold"), fg=COLOR_TEXT_MUTED, bg=COLOR_CARD_BG).pack(anchor="w", padx=20, pady=(5, 2))

        self.entry_doc_content = tk.Entry(
            self.card_frame, 
            font=("Segoe UI", 10), 
            bg=COLOR_BG_TOP, 
            fg=COLOR_TEXT_MAIN, 
            insertbackground=COLOR_TEXT_MAIN, 
            bd=1, 
            relief="solid"
        )
        self.entry_doc_content.insert(0, self.simulated_message)
        self.entry_doc_content.pack(fill="x", padx=20, pady=2)

        btn_sign = self.create_custom_button(self.card_frame, "✍️ Assinar Documento com Chave Privada", self.generate_digital_signature)
        btn_sign.pack(fill="x", padx=20, pady=6)

        self.lbl_sig_status = tk.Label(
            self.card_frame, 
            text="Status: Documento NÃO Assinado", 
            font=("Consolas", 9, "bold"), 
            fg=COLOR_WARNING, 
            bg=COLOR_BG_TOP, 
            bd=1, 
            relief="solid", 
            pady=6
        )
        self.lbl_sig_status.pack(fill="x", padx=20, pady=4)

        btn_verify = self.create_custom_button(self.card_frame, "🔍 Auditar Assinatura com Chave Pública", self.verify_digital_signature)
        btn_verify.pack(fill="x", padx=20, pady=6)

        self.btn_next2 = self.create_custom_button(self.card_frame, "Ir para o Quiz Conceitual Expandido ➔", self.load_quiz_mode)
        self.btn_next2.pack(fill="x", padx=20, pady=(10, 15))
        self.btn_next2.config(state="disabled")

    def generate_digital_signature(self):
        text = self.entry_doc_content.get().strip()
        if not text:
            messagebox.showwarning("Aviso", "O documento não pode estar vazio!")
            return

        self.simulated_message = text
        raw_hash = hashlib.sha256(text.encode('utf-8')).hexdigest()
        self.simulated_signature = f"SIG_PRIVKEY_RSA2048[{raw_hash[:16]}]"

        self.lbl_sig_status.config(
            text=f"✅ ASSINADO DIGITALMENTE!\nHash: {raw_hash[:24]}...\nAssinatura: {self.simulated_signature}",
            fg=COLOR_HEALTH
        )

    def verify_digital_signature(self):
        if not self.simulated_signature:
            messagebox.showerror("Erro de Auditoria", "Assine o documento primeiro para gerar o registro de validação!")
            return

        current_text = self.entry_doc_content.get().strip()
        current_hash = hashlib.sha256(current_text.encode('utf-8')).hexdigest()
        expected_hash = hashlib.sha256(self.simulated_message.encode('utf-8')).hexdigest()

        if current_hash == expected_hash:
            messagebox.showinfo(
                "INTEGRIDADE E AUTENTICIDADE CONFIRMADAS! 🎯", 
                "1. INTEGRIDADE: NENHUM bit do texto foi alterado.\n"
                "2. AUTENTICIDADE: A assinatura corresponde exatamente à Chave Pública do autor.\n\n"
                "Status: VÁLIDO (Garantia de Não-Repúdio)."
            )
            self.btn_next2.config(state="normal")
        else:
            messagebox.showerror(
                "ALERTA DE SEGURANÇA: DOCUMENTO ADULTERADO! ❌", 
                "Falha na Verificação!\n\n"
                "O Hash do conteúdo atual difere do Hash vinculado à Assinatura Digital.\n"
                "Alguém modificou a mensagem durante a transmissão!"
            )

    # ==========================================================================
    # --- ETAPA 3: QUIZ EDUCATIVO EXPANDIDO ---
    # ==========================================================================
    def load_quiz_mode(self):
        self.clear_card()
        self.lbl_mode.config(text=f"ETAPA 3/3 — QUIZ ({self.current_q + 1}/{len(QUIZ_FASE_6)})")

        q_data = QUIZ_FASE_6[self.current_q]

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
            font=("Segoe UI", 11), 
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

        q_data = QUIZ_FASE_6[self.current_q]
        correct_idx = q_data["answer"]
        selected_btn = self.quiz_buttons[selected_idx]

        if selected_idx == correct_idx:
            selected_btn.config(bg=COLOR_CORRECT, fg="#000000")
            self.root.update_idletasks()
            
            messagebox.showinfo(
                "Resposta Correta! 🎯", 
                f"{q_data['explanations'][selected_idx]}\n\n{q_data['tip']}"
            )
            
            self.current_q += 1
            if self.current_q < len(QUIZ_FASE_6):
                self.load_quiz_mode()
            else:
                messagebox.showinfo(
                    "Fase 6 Concluída com Excelência! 🏆", 
                    "Parabéns! Você dominou os conceitos essenciais de Hashing, Integridade, Criptografia Assimétrica e Assinatura Digital!"
                )
                self.root.destroy()
        else:
            selected_btn.config(bg=COLOR_INCORRECT, fg="#FFFFFF")
            self.quiz_buttons[correct_idx].config(bg=COLOR_CORRECT, fg="#000000")
            self.root.update_idletasks()
            
            messagebox.showerror(
                "Resposta Incorreta! ⚠️", 
                f"{q_data['explanations'][selected_idx]}\n\n{q_data['tip']}"
            )
            # Recarrega a pergunta após dar ok no messagebox
            self.load_quiz_mode()

if __name__ == "__main__":
    root = tk.Tk()
    
    # Centralização da janela
    window_width = 700
    window_height = 640
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    position_right = int(screen_width/2 - window_width/2)
    position_top = int(screen_height/2 - window_height/2)
    root.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")

    import tkinter as tk
from tkinter import messagebox

if __name__ == "__main__":
    root = tk.Tk()
    app = Phase6App(root)
    root.mainloop()

# ==============================================================================
# CYBERSHIELD — FASE 8: DESENVOLVIMENTO SEGURO
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


# ==============================================================================
# PERGUNTA E EXPLICAÇÕES
# ==============================================================================

QUESTION = {
    "category": "🛠️ FASE 8 — DESENVOLVIMENTO SEGURO",
    "question": (
        "Durante o desenvolvimento de um sistema, "
        "foi identificada uma falha relacionada aos dados "
        "enviados pelos usuários.\n\n"
        "Qual medida é mais adequada para reduzir esse risco?"
    ),
    "options": [
        "Aumentar a velocidade do servidor",
        "Desativar o firewall",
        "Validar e tratar adequadamente as entradas",
        "Armazenar todos os dados em texto puro"
    ],
    "answer": 2
}

EXPLANATIONS = {
    0: (
        "❌ Aumentar a velocidade do servidor\n\n"
        "Desempenho não corrige falhas de validação. "
        "Um servidor mais rápido continuará vulnerável "
        "se aceitar entradas maliciosas."
    ),
    1: (
        "❌ Desativar o firewall\n\n"
        "Desativar o firewall reduziria ainda mais a segurança "
        "e não corrige o problema relacionado à validação."
    ),
    2: (
        "✅ Validar e tratar adequadamente as entradas\n\n"
        "A validação e o tratamento adequado das entradas "
        "ajudam a impedir que dados maliciosos sejam aceitos "
        "pelo sistema."
    ),
    3: (
        "❌ Armazenar todos os dados em texto puro\n\n"
        "Isso aumenta o risco de exposição e vazamento "
        "de informações."
    )
}


# ==============================================================================
# CLASSE DA FASE 8
# ==============================================================================

class Fase8:

    def __init__(self, root, proxima_fase=None):
        self.root = root
        self.proxima_fase = proxima_fase

        self.lives = 3
        self.score = 0
        self.disabled_buttons = set()  # Armazena os índices já errados

        self.clear_screen()

        # Configuração da janela
        self.root.title("CyberShield — Fase 8")
        self.root.geometry("660x560")
        self.root.resizable(False, False)

        self.setup_ui()
        self.load_question()

    def clear_screen(self):
        """ Limpa widgets antigos do root antes de iniciar a fase. """
        for widget in self.root.winfo_children():
            widget.destroy()

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
        self.bg_canvas.pack(fill="both", expand=True)

        self.draw_cyber_background()

        # Barra Superior
        self.status_frame = tk.Frame(self.bg_canvas, bg=COLOR_BG_TOP)
        self.bg_canvas.create_window(330, 35, window=self.status_frame, width=620)

        # Status Firewall
        self.lbl_firewall = tk.Label(
            self.status_frame,
            text=f"🛡️ FIREWALL: {'█ ' * self.lives}",
            font=("Consolas", 13, "bold"),
            fg=COLOR_HEALTH,
            bg=COLOR_BG_TOP
        )
        self.lbl_firewall.pack(side="left")

        # Score
        self.lbl_score = tk.Label(
            self.status_frame,
            text=f"SCORE: {self.score}",
            font=("Consolas", 13, "bold"),
            fg=COLOR_CYAN_GLOW,
            bg=COLOR_BG_TOP
        )
        self.lbl_score.pack(side="right")

        # Card Principal
        self.card_frame = tk.Frame(
            self.bg_canvas,
            bg=COLOR_CARD_BG,
            highlightbackground=COLOR_CARD_BORDER,
            highlightthickness=2,
            bd=0
        )
        self.bg_canvas.create_window(330, 290, window=self.card_frame, width=620, height=430)

        # Categoria
        self.lbl_category = tk.Label(
            self.card_frame,
            text="",
            font=("Segoe UI", 10, "bold"),
            fg=COLOR_CYAN_GLOW,
            bg=COLOR_CARD_BG
        )
        self.lbl_category.pack(anchor="w", padx=20, pady=(15, 5))

        # Pergunta
        self.lbl_question = tk.Label(
            self.card_frame,
            text="",
            font=("Segoe UI", 12),
            fg=COLOR_TEXT_MAIN,
            bg=COLOR_CARD_BG,
            wraplength=570,
            justify="left"
        )
        self.lbl_question.pack(anchor="w", padx=20, pady=10)

        # Botões
        self.btn_frame = tk.Frame(self.card_frame, bg=COLOR_CARD_BG)
        self.btn_frame.pack(fill="both", expand=True, padx=20, pady=10)

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
            btn.pack(fill="x", pady=6, ipady=4)

            btn.bind("<Enter>", lambda event, b=btn: self.on_hover_enter(b))
            btn.bind("<Leave>", lambda event, b=btn: self.on_hover_leave(b))

            self.buttons.append(btn)

    # ==========================================================================
    # HOVER
    # ==========================================================================

    def on_hover_enter(self, btn):
        if str(btn["state"]) == "normal":
            btn.config(bg=COLOR_BTN_HOVER, fg=COLOR_TEXT_MAIN)

    def on_hover_leave(self, btn):
        if str(btn["state"]) == "normal":
            btn.config(bg=COLOR_BTN_BG, fg=COLOR_TEXT_MUTED)

    # ==========================================================================
    # FUNDO CYBER
    # ==========================================================================

    def draw_cyber_background(self):
        width, height = 660, 560
        r1, g1, b1 = self.hex_to_rgb(COLOR_BG_TOP)
        r2, g2, b2 = self.hex_to_rgb(COLOR_BG_BOTTOM)

        for y in range(height):
            r = int(r1 + (r2 - r1) * (y / height))
            g = int(g1 + (g2 - g1) * (y / height))
            b = int(b1 + (b2 - b1) * (y / height))
            color = f"#{r:02x}{g:02x}{b:02x}"
            self.bg_canvas.create_line(0, y, width, y, fill=color)

        line_color = "#0B3254"

        # Circuito Superior
        self.bg_canvas.create_line(30, 25, 180, 25, 230, 50, 430, 50, fill=line_color, width=1.5)
        self.bg_canvas.create_oval(177, 22, 183, 28, fill=COLOR_CYAN_GLOW, outline="")
        self.bg_canvas.create_oval(427, 47, 433, 53, fill=COLOR_CYAN_GLOW, outline="")

        # Circuito Inferior
        self.bg_canvas.create_line(50, 530, 200, 530, 250, 510, 500, 510, 550, 535, fill=line_color, width=1.5)
        self.bg_canvas.create_oval(247, 507, 253, 513, fill=COLOR_CYAN_GLOW, outline="")
        self.bg_canvas.create_oval(497, 507, 503, 513, fill=COLOR_CYAN_GLOW, outline="")

    @staticmethod
    def hex_to_rgb(hex_str):
        hex_str = hex_str.lstrip("#")
        return tuple(int(hex_str[i:i + 2], 16) for i in (0, 2, 4))

    # ==========================================================================
    # CARREGAR PERGUNTA
    # ==========================================================================

    def load_question(self):
        self.lbl_category.config(text=QUESTION["category"])
        self.lbl_question.config(text=QUESTION["question"])

        for i, option in enumerate(QUESTION["options"]):
            self.buttons[i].config(
                text=f"[ {chr(65 + i)} ]   {option}",
                bg=COLOR_BTN_BG,
                fg=COLOR_TEXT_MUTED,
                state="normal",
                cursor="hand2"
            )

    # ==========================================================================
    # VERIFICAR RESPOSTA
    # ==========================================================================

    def check_answer(self, selected_idx):
        correct_idx = QUESTION["answer"]
        selected_btn = self.buttons[selected_idx]

        # ----------------------------------------------------------------------
        # RESPOSTA CORRETA
        # ----------------------------------------------------------------------
        if selected_idx == correct_idx:
            for btn in self.buttons:
                btn.config(state="disabled", cursor="arrow")

            selected_btn.config(bg=COLOR_CORRECT, fg="#000000")
            self.root.update()

            self.score += 100
            self.lbl_score.config(text=f"SCORE: {self.score}")

            messagebox.showinfo(
                "Resposta Correta! 🎯",
                EXPLANATIONS[selected_idx] + "\n\n+100 PTS"
            )

            if self.proxima_fase is not None:
                self.proxima_fase()
            else:
                messagebox.showinfo(
                    "Fase 8 concluída!",
                    "🛡️ Desenvolvimento seguro concluído!\n\nVocê protegeu o sistema."
                )
                self.root.destroy()
            return

        # ----------------------------------------------------------------------
        # RESPOSTA INCORRETA
        # ----------------------------------------------------------------------
        self.lives -= 1
        self.disabled_buttons.add(selected_idx)

        # Atualiza o botão errado mantendo-o vermelho e desativado
        selected_btn.config(
            bg=COLOR_INCORRECT,
            fg="#FFFFFF",
            state="disabled",
            cursor="arrow"
        )
        
        self.lbl_firewall.config(text=f"🛡️ FIREWALL: {'█ ' * self.lives}")
        self.root.update()

        messagebox.showerror(
            "Resposta Incorreta! ⚠️",
            EXPLANATIONS[selected_idx]
        )

        # ----------------------------------------------------------------------
        # GAME OVER
        # ----------------------------------------------------------------------
        if self.lives <= 0:
            # Revela qual era a resposta correta em verde antes de fechar
            self.buttons[correct_idx].config(bg=COLOR_CORRECT, fg="#000000")
            for btn in self.buttons:
                btn.config(state="disabled", cursor="arrow")
            self.root.update()

            messagebox.showerror(
                "GAME OVER",
                "🚨 O firewall caiu!\n\nO sistema foi comprometido.\n\nTente novamente."
            )
            self.root.destroy()


# ==============================================================================
# FUNÇÃO USADA PELO MAIN
# ==============================================================================

def executar(root, proxima_fase):
    Fase8(root, proxima_fase)


if __name__ == "__main__":
    root = tk.Tk()
    app = Fase8(root)
    root.mainloop()
    import tkinter as tk
from tkinter import messagebox


# ==============================================================================
# --- CYBERSHIELD: FASE 9 — SOC ---
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

# CORES DA TELA BOSS
COLOR_BOSS_BG = "#050000"
COLOR_BOSS_RED = "#FF1744"
COLOR_BOSS_RED_DARK = "#8B0000"
COLOR_BOSS_TEXT = "#FFFFFF"
COLOR_BOSS_MUTED = "#FF8A9B"


QUESTIONS = [
    {
        "category": "🔴 FASE 9 — SOC",
        "question": (
            "Um analista do SOC identificou os seguintes eventos nos logs:\n\n"
            "• 08:41 — 5 falhas de login consecutivas\n"
            "• 08:45 — login realizado com sucesso\n"
            "• 08:47 — acesso originado de uma localização incomum\n"
            "• 08:49 — download de vários arquivos\n\n"
            "Qual é a conclusão mais adequada neste momento?"
        ),
        "options": [
            "O computador está definitivamente infectado",
            "O servidor está necessariamente desligado",
            "Existe um comportamento suspeito que merece investigação",
            "O usuário esqueceu a senha"
        ],
        "answer": 2,
        "explanations": [
            (
                "❌ RESPOSTA INCORRETA\n\n"
                "Não existem evidências suficientes para afirmar que o computador "
                "está definitivamente infectado.\n\n"
                "Os eventos indicam uma possível atividade suspeita, mas ainda "
                "é necessária uma investigação para determinar o que realmente aconteceu."
            ),
            (
                "❌ RESPOSTA INCORRETA\n\n"
                "Os registros mostram atividade no ambiente, incluindo um login "
                "bem-sucedido, acesso de localização incomum e download de arquivos.\n\n"
                "Portanto, não existe base suficiente para afirmar que o servidor "
                "está necessariamente desligado."
            ),
            (
                "✅ RESPOSTA CORRETA\n\n"
                "As falhas de login, o acesso de uma localização incomum e o "
                "download de arquivos formam um conjunto de indicadores que "
                "merece investigação pelo SOC.\n\n"
                "A conclusão adequada é identificar o comportamento como "
                "suspeito sem afirmar prematuramente que ocorreu uma invasão ou uma infecção."
            ),
            (
                "❌ RESPOSTA INCORRETA\n\n"
                "As falhas de login podem realmente acontecer porque um usuário "
                "esqueceu a senha.\n\n"
                "Porém, essa explicação é insuficiente para explicar os eventos "
                "seguintes, como o acesso de uma localização incomum e o "
                "download de vários arquivos."
            )
        ],
        "tip": (
            "💡 DICA SOC\n\n"
            "Em segurança, investigue os indícios antes de tirar conclusões "
            "definitivas.\n\n"
            "Observe o conjunto de eventos e procure comportamentos anormais "
            "antes de determinar a causa."
        )
    }
]


class CyberQuizApp:

    def __init__(self, root):
        self.root = root
        self.root.title("CyberShield: Ethical Hacker Quiz")
        self.root.geometry("660x560")
        self.root.resizable(False, False)

        self.current_q = 0
        self.lives = 3
        self.score = 0
        self.anim_job = None  # CORREÇÃO: Guarda a referência da animação para cancelamento seguro

        self.setup_ui()
        self.load_question()

    def setup_ui(self):
        self.bg_canvas = tk.Canvas(
            self.root, width=660, height=560, highlightthickness=0
        )
        self.bg_canvas.pack(fill="both", expand=True)

        self.draw_cyber_background()

        # Status Bar
        self.status_frame = tk.Frame(self.bg_canvas, bg=COLOR_BG_TOP)
        self.bg_canvas.create_window(330, 35, window=self.status_frame, width=620)

        self.lbl_firewall = tk.Label(
            self.status_frame,
            text=f"🛡️ FIREWALL: {'█ ' * self.lives}",
            font=("Consolas", 13, "bold"),
            fg=COLOR_HEALTH,
            bg=COLOR_BG_TOP
        )
        self.lbl_firewall.pack(side="left")

        self.lbl_score = tk.Label(
            self.status_frame,
            text=f"SCORE: {self.score}",
            font=("Consolas", 13, "bold"),
            fg=COLOR_CYAN_GLOW,
            bg=COLOR_BG_TOP
        )
        self.lbl_score.pack(side="right")

        # Card Principal
        self.card_frame = tk.Frame(
            self.bg_canvas,
            bg=COLOR_CARD_BG,
            highlightbackground=COLOR_CARD_BORDER,
            highlightthickness=2,
            bd=0
        )
        self.bg_canvas.create_window(330, 290, window=self.card_frame, width=620, height=430)

        self.lbl_category = tk.Label(
            self.card_frame, text="", font=("Segoe UI", 10, "bold"),
            fg=COLOR_CYAN_GLOW, bg=COLOR_CARD_BG
        )
        self.lbl_category.pack(anchor="w", padx=20, pady=(15, 5))

        self.lbl_question = tk.Label(
            self.card_frame, text="", font=("Segoe UI", 10, "bold"),
            fg=COLOR_TEXT_MAIN, bg=COLOR_CARD_BG, wraplength=570, justify="left"
        )
        self.lbl_question.pack(anchor="w", padx=20, pady=10)

        self.btn_frame = tk.Frame(self.card_frame, bg=COLOR_CARD_BG)
        self.btn_frame.pack(fill="both", expand=True, padx=20, pady=10)

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
            btn.pack(fill="x", pady=5, ipady=3)
            btn.bind("<Enter>", lambda e, b=btn: self.on_hover_enter(b))
            btn.bind("<Leave>", lambda e, b=btn: self.on_hover_leave(b))
            self.buttons.append(btn)

    def on_hover_enter(self, btn):
        if btn["state"] == "normal":
            btn.config(bg=COLOR_BTN_HOVER, fg=COLOR_TEXT_MAIN)

    def on_hover_leave(self, btn):
        if btn["state"] == "normal":
            btn.config(bg=COLOR_BTN_BG, fg=COLOR_TEXT_MUTED)

    def draw_cyber_background(self):
        width, height = 660, 560
        r1, g1, b1 = self.hex_to_rgb(COLOR_BG_TOP)
        r2, g2, b2 = self.hex_to_rgb(COLOR_BG_BOTTOM)

        for y in range(height):
            r = int(r1 + (r2 - r1) * (y / height))
            g = int(g1 + (g2 - g1) * (y / height))
            b = int(b1 + (b2 - b1) * (y / height))
            self.bg_canvas.create_line(0, y, width, y, fill=f"#{r:02x}{g:02x}{b:02x}")

        line_color = "#0B3254"
        glow_dot = COLOR_CYAN_GLOW

        self.bg_canvas.create_line(30, 25, 180, 25, 230, 50, 430, 50, fill=line_color, width=1.5)
        self.bg_canvas.create_oval(177, 22, 183, 28, fill=glow_dot, outline="")
        self.bg_canvas.create_oval(427, 47, 433, 53, fill=glow_dot, outline="")

        self.bg_canvas.create_line(50, 530, 200, 530, 250, 510, 500, 510, 550, 535, fill=line_color, width=1.5)
        self.bg_canvas.create_oval(247, 507, 253, 513, fill=glow_dot, outline="")
        self.bg_canvas.create_oval(497, 507, 503, 513, fill=glow_dot, outline="")

    @staticmethod
    def hex_to_rgb(hex_str):
        hex_str = hex_str.lstrip("#")
        return tuple(int(hex_str[i:i + 2], 16) for i in (0, 2, 4))

    def load_question(self):
        if self.current_q < len(QUESTIONS):
            q_data = QUESTIONS[self.current_q]
            self.lbl_category.config(text=q_data["category"])
            self.lbl_question.config(text=q_data["question"])

            # CORREÇÃO: Gerencia dinamicamente a quantidade de opções
            num_options = len(q_data["options"])
            for i in range(4):
                if i < num_options:
                    self.buttons[i].config(
                        text=f"[ {chr(65 + i)} ]   {q_data['options'][i]}",
                        bg=COLOR_BTN_BG,
                        fg=COLOR_TEXT_MUTED,
                        state="normal"
                    )
                    self.buttons[i].pack(fill="x", pady=5, ipady=3)
                else:
                    self.buttons[i].pack_forget()
        else:
            self.show_boss_transition()

    def check_answer(self, selected_idx):
        for btn in self.buttons:
            btn.config(state="disabled")

        q_data = QUESTIONS[self.current_q]
        correct_idx = q_data["answer"]
        selected_btn = self.buttons[selected_idx]

        if selected_idx == correct_idx:
            selected_btn.config(bg=COLOR_CORRECT, fg="#000000")
            self.score += 100
            self.lbl_score.config(text=f"SCORE: {self.score}")
            
            # CORREÇÃO: Força renderização do botão verde antes do alert
            self.root.update_idletasks()

            messagebox.showinfo(
                "Resposta Correta! 🎯",
                f"{q_data['explanations'][selected_idx]}\n\n{q_data['tip']}\n\n🏆 +100 PONTOS"
            )
        else:
            selected_btn.config(bg=COLOR_INCORRECT, fg="#FFFFFF")
            self.lives -= 1
            self.lbl_firewall.config(text=f"🛡️ FIREWALL: {'█ ' * self.lives}")

            # CORREÇÃO: Força renderização do botão vermelho antes do alert
            self.root.update_idletasks()

            messagebox.showerror(
                "Resposta Incorreta! ⚠️",
                f"{q_data['explanations'][selected_idx]}\n\n{q_data['tip']}"
            )

            if self.lives == 0:
                messagebox.showerror(
                    "GAME OVER 💀",
                    "O firewall caiu!\n\nVocê não conseguiu identificar corretamente o comportamento suspeito."
                )
                self.root.destroy()
                return

        self.current_q += 1
        self.load_question()

    def show_boss_transition(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        self.boss_canvas = tk.Canvas(
            self.root, width=660, height=560, bg=COLOR_BOSS_BG, highlightthickness=0
        )
        self.boss_canvas.pack(fill="both", expand=True)

        for y in range(560):
            intensity = int(5 + 25 * (y / 560))
            self.boss_canvas.create_line(0, y, 660, y, fill=f"#{intensity:02x}0000")

        for y in range(80, 520, 45):
            self.boss_canvas.create_line(0, y, 660, y, fill="#240006", width=1)

        self.boss_title = self.boss_canvas.create_text(
            330, 60, text="⚠  ALERTA CRÍTICO  ⚠", font=("Consolas", 25, "bold"), fill=COLOR_BOSS_RED
        )

        self.boss_canvas.create_text(
            330, 105, text="SECURITY BREACH DETECTED", font=("Consolas", 16, "bold"), fill=COLOR_BOSS_TEXT
        )

        self.boss_canvas.create_line(70, 130, 590, 130, fill=COLOR_BOSS_RED_DARK, width=2)

        self.boss_canvas.create_text(
            330, 170, text="NÍVEL DE AMEAÇA", font=("Consolas", 12, "bold"), fill=COLOR_BOSS_MUTED
        )

        self.boss_canvas.create_text(
            330, 205, text="EXTREMO", font=("Consolas", 27, "bold"), fill=COLOR_BOSS_RED
        )

        self.boss_canvas.create_rectangle(80, 235, 580, 255, outline=COLOR_BOSS_RED_DARK, width=2)
        self.boss_canvas.create_rectangle(84, 239, 576, 251, fill=COLOR_BOSS_RED, outline="")

        self.boss_canvas.create_text(
            330, 290,
            text="🔴 SISTEMA: SOB AMEAÇA\n🔴 FIREWALL: SOB PRESSÃO\n🔴 INCIDENTE: NÃO CONTIDO",
            font=("Consolas", 12, "bold"), fill=COLOR_BOSS_MUTED, justify="center"
        )

        self.boss_canvas.create_text(
            330, 375,
            text="VOCÊ CHEGOU AO PONTO CRÍTICO.\n\nA próxima operação será diferente.\nCada decisão poderá determinar o destino\nde todo o sistema.",
            font=("Segoe UI", 11, "bold"), fill=COLOR_BOSS_TEXT, justify="center"
        )

        self.boss_canvas.create_text(
            330, 455, text="⚠  FASE 10 — BOSS INCOMING  ⚠", font=("Consolas", 18, "bold"), fill=COLOR_BOSS_RED
        )

        self.boss_canvas.create_text(
            330, 485, text=f"SCORE ATUAL: {self.score}", font=("Consolas", 11, "bold"), fill=COLOR_BOSS_MUTED
        )

        self.boss_button = tk.Button(
            self.root,
            text="⚠  ENTRAR NO BOSS  ⚠",
            font=("Consolas", 12, "bold"),
            bg=COLOR_BOSS_RED_DARK,
            fg=COLOR_BOSS_TEXT,
            activebackground=COLOR_BOSS_RED,
            activeforeground="#FFFFFF",
            relief="flat",
            cursor="hand2",
            bd=2,
            highlightbackground=COLOR_BOSS_RED,
            command=self.enter_boss
        )
        self.boss_button.place(x=220, y=510, width=220, height=38)

        self.boss_flash_state = False
        self.animate_boss_alert()

    def animate_boss_alert(self):
        # CORREÇÃO: Garante que o loop pare se a janela não existir
        if not self.root.winfo_exists():
            return

        new_color = "#660010" if self.boss_flash_state else COLOR_BOSS_RED
        self.boss_canvas.itemconfig(self.boss_title, fill=new_color)
        self.boss_flash_state = not self.boss_flash_state

        # Salva o job do temporizador
        self.anim_job = self.root.after(500, self.animate_boss_alert)

    def enter_boss(self):
        # CORREÇÃO: Cancela o temporizador antes de fechar a janela
        if self.anim_job:
            self.root.after_cancel(self.anim_job)

        messagebox.showwarning(
            "🔴 FASE 10 — BOSS",
            "CONEXÃO ESTABELECIDA.\n\nO próximo desafio será iniciado.\n\nPrepare-se para tomar decisões críticas."
        )
        self.root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = CyberQuizApp(root)
    root.mainloop()
    import tkinter as tk
from tkinter import messagebox

# --- CONFIGURAÇÕES DE DESIGN ---
COLOR_BG_TOP = "#030D22"
COLOR_CARD_BG = "#0D1F38"
COLOR_HEALTH_PLAYER = "#00F5D4"     # Ciano Neon
COLOR_HEALTH_BOSS = "#FF3366"       # Rosa Neon
COLOR_TEXT = "#FFFFFF"

# --- BANCO DE DADOS DA FASE 10 ---
BOSS_BATTLE_DATA = [
    {
        "questao": "Acesso suspeito detectado na conta Admin. Ação imediata?", 
        "opcoes": ["A) Ignorar", "B) Publicar na rede", "C) Bloquear credenciais", "D) Apagar tudo"], 
        "resposta_correta": 2, 
        "dificuldade": 1 
    },
    {
        "questao": "Servidor sofrendo injeção SQL. O que priorizar?", 
        "opcoes": ["A) Reiniciar servidor", "B) Isolar o servidor da rede", "C) Mudar o plano de fundo", "D) Ignorar logs"], 
        "resposta_correta": 1, 
        "dificuldade": 2 
    },
    {
        "questao": "Ameaça Zero-Day ativa! Qual o protocolo de contenção?", 
        "opcoes": ["A) Ficar parado", "B) Criar regras de WAF/Firewall", "C) Formatar toda a rede", "D) Falar com RH"], 
        "resposta_correta": 1, 
        "dificuldade": 3 
    }
]

class BossFightApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🛡️ BOSS FIGHT — FASE 10")
        self.root.geometry("700x500")
        self.root.configure(bg=COLOR_BG_TOP)
        
        self.vida_jogador = 100
        self.vida_boss = 100
        self.indice_questao = 0
        
        self.setup_header()
        self.setup_card()
        self.atualizar_barras()

    def setup_header(self):
        self.header = tk.Frame(self.root, bg=COLOR_BG_TOP, height=100)
        self.header.pack(fill="x", pady=10)
        
        self.canvas_status = tk.Canvas(self.header, bg=COLOR_BG_TOP, height=80, highlightthickness=0)
        self.canvas_status.pack(fill="x", padx=20)
        
        # --- PLAYER ---
        self.canvas_status.create_text(120, 15, text="PLAYER", fill=COLOR_HEALTH_PLAYER, font=("Consolas", 10, "bold"), anchor="w")
        self.barra_jogador = self.canvas_status.create_rectangle(120, 35, 320, 55, fill="#0F3356", outline="")
        self.fill_jogador = self.canvas_status.create_rectangle(120, 35, 320, 55, fill=COLOR_HEALTH_PLAYER, outline="")
        
        # --- BOSS ---
        self.canvas_status.create_text(580, 15, text="BOSS", fill=COLOR_HEALTH_BOSS, font=("Consolas", 10, "bold"), anchor="e")
        self.barra_boss = self.canvas_status.create_rectangle(380, 35, 580, 55, fill="#0F3356", outline="")
        self.fill_boss = self.canvas_status.create_rectangle(380, 35, 580, 55, fill=COLOR_HEALTH_BOSS, outline="")

    def setup_card(self):
        self.card = tk.Frame(self.root, bg=COLOR_CARD_BG, highlightbackground="#144574", highlightthickness=2)
        self.card.pack(pady=20, padx=50, fill="both", expand=True)
        
        self.lbl_questao = tk.Label(self.card, text="", font=("Segoe UI", 12), fg=COLOR_TEXT, bg=COLOR_CARD_BG, wraplength=500)
        self.lbl_questao.pack(pady=40)
        
        self.frame_botoes = tk.Frame(self.card, bg=COLOR_CARD_BG)
        self.frame_botoes.pack()
        self.carregar_questao()

    def carregar_questao(self):
        dados = BOSS_BATTLE_DATA[self.indice_questao]
        self.lbl_questao.config(text=f"NÍVEL {dados['dificuldade']}: {dados['questao']}")
        for w in self.frame_botoes.winfo_children(): w.destroy()
        
        for i, opt in enumerate(dados["opcoes"]):
            tk.Button(self.frame_botoes, text=opt, width=40, bg="#1B3B6F", fg="white", 
                      command=lambda idx=i: self.processar_turno(idx)).pack(pady=5)

    def processar_turno(self, indice_escolhido):
        dados = BOSS_BATTLE_DATA[self.indice_questao]
        
        if indice_escolhido == dados["resposta_correta"]:
            self.vida_boss -= 34
            messagebox.showinfo("DANO CRÍTICO!", "✅ Ação de defesa bem-sucedida!")
        else:
            dano = dados["dificuldade"] * 25
            self.vida_jogador -= dano
            
            if dados["dificuldade"] == 3:
                self.vida_jogador = 0
                messagebox.showerror("FALHA CRÍTICA!", "💀 Você ignorou uma vulnerabilidade de Zero-Day. A rede caiu!")
            else:
                messagebox.showwarning("DANO SOFRIDO!", f"❌ Incorreto! O sistema sofreu {dano} de dano.")
        
        self.atualizar_barras()
        self.verificar_fim_de_jogo()

    def atualizar_barras(self):
        self.vida_jogador = max(0, self.vida_jogador)
        self.vida_boss = max(0, self.vida_boss)
        
        p_largura = self.vida_jogador * 2
        b_largura = self.vida_boss * 2
        
        self.canvas_status.coords(self.fill_jogador, 120, 35, 120 + p_largura, 55)
        self.canvas_status.coords(self.fill_boss, 580 - b_largura, 35, 580, 55)

    def verificar_fim_de_jogo(self):
        if self.vida_jogador <= 0:
            messagebox.showerror("GAME OVER", "💀 A segurança falhou. O sistema foi comprometido!")
            self.root.destroy()
        elif self.vida_boss <= 0:
            messagebox.showinfo("VITÓRIA", "🏆 O Boss foi contido! Você salvou a empresa.")
            self.root.destroy()
        else:
            self.indice_questao += 1
            if self.indice_questao < len(BOSS_BATTLE_DATA):
                self.carregar_questao()

if __name__ == "__main__":
    root = tk.Tk()
    app = BossFightApp(root)
    root.mainloop()