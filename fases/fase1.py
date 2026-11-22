import tkinter as tk
from tkinter import messagebox

import pygame
import os
import glob


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
# QUESTÕES DA FASE 1
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
                "❌ INCORRETO!\n\n"
                "A disponibilidade garante que o sistema esteja acessível. "
                "O arquivo continuou lá, porém alterado.\n\n"
                "💡 Dica: Falou em sistema fora do ar? "
                "Pense em Disponibilidade."
            ),

            (
                "❌ INCORRETO!\n\n"
                "A confidencialidade protege contra acesso não autorizado "
                "(vazamento). O foco aqui foi a alteração.\n\n"
                "💡 Dica: Apenas leu dados sem permissão? "
                "Pense em Confidencialidade."
            ),

            (
                "✅ CORRETO!\n\n"
                "A integridade garante que os dados permaneçam exatos, "
                "completos e sem alterações indevidas."
            ),

            (
                "❌ INCORRETO!\n\n"
                "A autenticação verifica a identidade de quem acessa, "
                "mas não o conteúdo do arquivo.\n\n"
                "💡 Dica: Confirmar quem é o usuário? "
                "Pense em Autenticação."
            )
        ]
    }
]


# ==============================================================================
# APLICAÇÃO DA FASE 1
# ==============================================================================

class CyberQuizApp:

    def __init__(self, root, proxima_fase=None):

        self.root = root
        self.proxima_fase = proxima_fase

        self.root.title(
            "CyberShield: Fase 1"
        )

        # ----------------------------------------------------------------------
        # TAMANHO INICIAL
        # ----------------------------------------------------------------------

        self.root.geometry(
            "1000x700"
        )

        self.root.minsize(
            800,
            600
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
        # VARIÁVEIS DO JOGO
        # ----------------------------------------------------------------------

        self.current_q = 0
        self.lives = 3
        self.score = 0

        self.finalizando = False

        # ----------------------------------------------------------------------
        # INTERFACE
        # ----------------------------------------------------------------------

        self.setup_ui()

        self.load_question()

        # ----------------------------------------------------------------------
        # MÚSICA
        # ----------------------------------------------------------------------

        self.iniciar_musica()


    # ==========================================================================
    # MÚSICA
    # ==========================================================================

    def iniciar_musica(self):

        try:

            # Inicializa o mixer do pygame
            pygame.mixer.init()

            # ------------------------------------------------------------------
            # LOCALIZA A PASTA ASSETS
            #
            # Estrutura esperada:
            #
            # projeto/
            # ├── main.py
            # ├── fases/
            # │   └── fase1.py
            # └── assets/
            #     └── musica.mp3
            # ------------------------------------------------------------------

            pasta_assets = os.path.abspath(
                os.path.join(
                    os.path.dirname(__file__),
                    "..",
                    "assets"
                )
            )

            # Procura arquivos MP3 dentro da pasta assets
            arquivos_mp3 = glob.glob(
                os.path.join(
                    pasta_assets,
                    "*.mp3"
                )
            )

            # ------------------------------------------------------------------
            # SE NÃO ENCONTRAR A MÚSICA
            # ------------------------------------------------------------------

            if not arquivos_mp3:

                print(
                    "⚠️ Nenhum arquivo .mp3 encontrado em:"
                )

                print(
                    pasta_assets
                )

                return

            # ------------------------------------------------------------------
            # PEGA O PRIMEIRO MP3 ENCONTRADO
            # ------------------------------------------------------------------

            caminho_musica = arquivos_mp3[0]

            print(
                "🎵 Música encontrada:"
            )

            print(
                caminho_musica
            )

            # ------------------------------------------------------------------
            # CARREGA A MÚSICA
            # ------------------------------------------------------------------

            pygame.mixer.music.load(
                caminho_musica
            )

            # ------------------------------------------------------------------
            # TOCA EM LOOP INFINITO
            # ------------------------------------------------------------------

            pygame.mixer.music.play(
                loops=-1
            )

            print(
                "🎵 Música iniciada em loop!"
            )

        except Exception as erro:

            print(
                "⚠️ Erro ao iniciar a música:"
            )

            print(
                erro
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

        self.root.after(
            50,
            self.update_interface
        )

        return "break"


    # --------------------------------------------------------------------------

    def exit_fullscreen(self, event=None):

        if self.fullscreen:

            self.fullscreen = False

            self.root.attributes(
                "-fullscreen",
                False
            )

            self.root.after(
                50,
                self.update_interface
            )

        return "break"


    # ==========================================================================
    # INTERFACE
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
        # DESENHO DO FUNDO
        # ----------------------------------------------------------------------

        self.bg_canvas.bind(
            "<Configure>",
            self.on_resize
        )

        # ----------------------------------------------------------------------
        # HEADER
        # ----------------------------------------------------------------------

        self.status_frame = tk.Frame(
            self.bg_canvas,
            bg=COLOR_BG_TOP
        )

        self.status_window = self.bg_canvas.create_window(
            0,
            0,
            window=self.status_frame,
            anchor="nw"
        )

        # ----------------------------------------------------------------------
        # FASE
        # ----------------------------------------------------------------------

        self.lbl_phase = tk.Label(
            self.status_frame,
            text="🛡️ FASE 1 — FUNDAMENTOS",
            font=("Consolas", 12, "bold"),
            fg=COLOR_HEALTH,
            bg=COLOR_BG_TOP
        )

        self.lbl_phase.pack(
            side="left"
        )

        # ----------------------------------------------------------------------
        # FIREWALL
        # ----------------------------------------------------------------------

        self.lbl_firewall = tk.Label(
            self.status_frame,
            text=f"🛡️ FIREWALL: {'█ ' * self.lives}",
            font=("Consolas", 13, "bold"),
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
            font=("Consolas", 13, "bold"),
            fg=COLOR_CYAN_GLOW,
            bg=COLOR_BG_TOP
        )

        self.lbl_score.pack(
            side="right",
            padx=20
        )

        # ----------------------------------------------------------------------
        # BOTÃO TELA CHEIA
        # ----------------------------------------------------------------------

        self.btn_fullscreen = tk.Button(
            self.bg_canvas,
            text="⛶  TELA CHEIA (F11)",
            font=("Consolas", 9, "bold"),
            fg=COLOR_TEXT_MAIN,
            bg=COLOR_BTN_BG,
            activeforeground=COLOR_TEXT_MAIN,
            activebackground=COLOR_BTN_HOVER,
            relief="flat",
            cursor="hand2",
            padx=15,
            pady=6,
            command=self.toggle_fullscreen
        )

        self.fullscreen_window = self.bg_canvas.create_window(
            0,
            0,
            window=self.btn_fullscreen,
            anchor="ne"
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
            0,
            0,
            window=self.card_frame,
            anchor="center"
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
            padx=25,
            pady=(15, 0)
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
            padx=25,
            pady=(5, 8)
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
            wraplength=850,
            justify="left"
        )

        self.lbl_question.pack(
            anchor="w",
            padx=25,
            pady=12
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
            padx=25,
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
                command=lambda idx=i:
                self.check_answer(idx)
            )

            btn.pack(
                fill="x",
                pady=6,
                ipady=7
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

        # ----------------------------------------------------------------------
        # ATUALIZA TAMANHO
        # ----------------------------------------------------------------------

        self.root.after(
            100,
            self.update_interface
        )


    # ==========================================================================
    # REDIMENSIONAMENTO
    # ==========================================================================

    def on_resize(self, event=None):

        self.update_interface()


    # --------------------------------------------------------------------------

    def update_interface(self):

        width = self.root.winfo_width()
        height = self.root.winfo_height()

        if width < 100:
            return

        if height < 100:
            return

        # ----------------------------------------------------------------------
        # REDESENHA FUNDO
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
            width - 60
        )

        self.bg_canvas.coords(
            self.status_window,
            30,
            30
        )

        self.bg_canvas.itemconfig(
            self.status_window,
            width=header_width
        )

        # ----------------------------------------------------------------------
        # BOTÃO FULLSCREEN
        # ----------------------------------------------------------------------

        self.bg_canvas.coords(
            self.fullscreen_window,
            width - 25,
            25
        )

        # ----------------------------------------------------------------------
        # TAMANHO DO CARD
        # ----------------------------------------------------------------------

        card_width = min(
            900,
            max(
                650,
                width - 100
            )
        )

        card_height = min(
            570,
            max(
                430,
                height - 180
            )
        )

        # ----------------------------------------------------------------------
        # POSIÇÃO DO CARD
        # ----------------------------------------------------------------------

        card_x = width / 2
        card_y = height / 2 + 25

        self.bg_canvas.coords(
            self.card_window,
            card_x,
            card_y
        )

        self.bg_canvas.itemconfig(
            self.card_window,
            width=card_width,
            height=card_height
        )

        # ----------------------------------------------------------------------
        # AJUSTA TEXTO
        # ----------------------------------------------------------------------

        question_wrap = max(
            500,
            card_width - 80
        )

        self.lbl_question.config(
            wraplength=question_wrap
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


    # --------------------------------------------------------------------------

    def on_hover_leave(self, btn):

        if btn["state"] == "normal":

            btn.config(
                bg=COLOR_BTN_BG,
                fg=COLOR_TEXT_MUTED
            )


    # ==========================================================================
    # FUNDO
    # ==========================================================================

    def draw_cyber_background(
        self,
        width=None,
        height=None
    ):

        if width is None:

            width = self.root.winfo_width()

        if height is None:

            height = self.root.winfo_height()

        if width < 10:

            return

        if height < 10:

            return

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
        # DEGRADÊ
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

        # Circuito superior

        x1 = int(
            width * 0.04
        )

        x2 = int(
            width * 0.25
        )

        x3 = int(
            width * 0.35
        )

        x4 = int(
            width * 0.70
        )

        self.bg_canvas.create_line(
            x1,
            25,
            x2,
            25,
            x3,
            50,
            x4,
            50,
            fill=line_color,
            width=2,
            tags="background"
        )

        self.bg_canvas.create_oval(
            x2 - 3,
            22,
            x2 + 3,
            28,
            fill=glow_dot,
            outline="",
            tags="background"
        )

        self.bg_canvas.create_oval(
            x4 - 3,
            47,
            x4 + 3,
            53,
            fill=glow_dot,
            outline="",
            tags="background"
        )

        # ----------------------------------------------------------------------
        # CIRCUITO INFERIOR
        # ----------------------------------------------------------------------

        y_bottom = height - 35

        self.bg_canvas.create_line(
            int(width * 0.05),
            y_bottom,
            int(width * 0.25),
            y_bottom,
            int(width * 0.32),
            y_bottom - 20,
            int(width * 0.78),
            y_bottom - 20,
            int(width * 0.90),
            y_bottom + 5,
            fill=line_color,
            width=2,
            tags="background"
        )

        self.bg_canvas.create_oval(
            int(width * 0.32) - 3,
            y_bottom - 23,
            int(width * 0.32) + 3,
            y_bottom - 17,
            fill=glow_dot,
            outline="",
            tags="background"
        )

        self.bg_canvas.create_oval(
            int(width * 0.78) - 3,
            y_bottom - 23,
            int(width * 0.78) + 3,
            y_bottom - 17,
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
        # DESABILITA BOTÕES
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
                f"Parabéns! Você acertou!\n\n"
                f"{explanation}",
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
                    "Você perdeu todas as vidas "
                    "e não pode avançar.",
                    parent=self.root
                )

                # ----------------------------------------------------------------
                # A janela continua pertencendo ao main.
                #
                # Não destruímos a root.
                # ----------------------------------------------------------------

                self.root.after(
                    100,
                    self.resetar_fase
                )

                return

        # ----------------------------------------------------------------------
        # PRÓXIMA QUESTÃO
        # ----------------------------------------------------------------------

        self.current_q += 1

        self.load_question()


    # ==========================================================================
    # RESETAR FASE
    # ==========================================================================

    def resetar_fase(self):

        self.current_q = 0
        self.lives = 3
        self.score = 0
        self.finalizando = False

        self.lbl_firewall.config(
            text=f"🛡️ FIREWALL: {'█ ' * self.lives}"
        )

        self.lbl_score.config(
            text=f"SCORE: {self.score}"
        )

        self.load_question()


    # ==========================================================================
    # FINALIZAR FASE
    # ==========================================================================

    def finalizar_fase(self):

        if self.finalizando:

            return

        self.finalizando = True

        messagebox.showinfo(
            "FASE 1 CONCLUÍDA! 🏆",

            "Excelente trabalho!\n\n"
            "Você concluiu os fundamentos de segurança "
            "da informação.\n\n"
            f"Pontuação da Fase 1: {self.score}\n\n"
            "Preparando a próxima fase...",

            parent=self.root
        )

        # ----------------------------------------------------------------------
        # CHAMA A PRÓXIMA FASE
        # ----------------------------------------------------------------------

        if self.proxima_fase:

            self.root.after(
                100,
                self.proxima_fase
            )

        else:

            messagebox.showinfo(
                "Fim",
                "A Fase 1 foi concluída!",
                parent=self.root
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