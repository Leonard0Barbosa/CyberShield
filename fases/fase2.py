import time
import string
import itertools
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

# ==============================================================================
# --- DADOS DA FASE 2: SENHAS ---
# ==============================================================================
QUIZ_FASE_2 = {
    "category": "🟢 FASE 2 — SEGURANÇA DE SENHAS",
    "question": "Qual medida reduz melhor o risco de comprometimento de uma conta?",
    "options": [
        "A) Trocar a senha toda semana por uma curta",
        "B) Usar a mesma senha em vários serviços",
        "C) Usar senha exclusiva e MFA",
        "D) Escrever a senha em um arquivo chamado 'senhas.txt'"
    ],
    "answer": 2,  # Índice C
    "explanations": {
        0: "❌ INCORRETO: Senhas curtas são facilmente quebradas por força bruta, mesmo trocadas semanalmente.",
        1: "❌ INCORRETO: Reutilizar senhas gera o efeito dominó; se um serviço vazar, todos caem.",
        2: "✅ CORRETO! Uma senha exclusiva impede o efeito dominó e o MFA adiciona uma camada dupla de proteção.",
        3: "❌ INCORRETO: Arquivos em texto puro podem ser lidos por qualquer malware ou pessoa com acesso local."
    },
    "tip": "💡 Dica Educativa: Priorize senhas longas/exclusivas e ative Autenticação de Múltiplos Fatores (MFA) sempre que disponível!"
}

class Phase2App:
    def __init__(self, root):
        self.root = root
        self.root.title("CyberShield: Fase 2 — Gestão e Proteção de Senhas")
        self.root.geometry("680x600")
        self.root.resizable(False, False)

        self.setup_ui()
        self.load_sim_mode()

    def setup_ui(self):
        # --- CANVAS DE FUNDO ---
        self.bg_canvas = tk.Canvas(self.root, width=680, height=600, highlightthickness=0)
        self.bg_canvas.pack(fill="both", expand=True)
        self.draw_cyber_background()

        # --- HEADER DE STATUS ---
        self.status_frame = tk.Frame(self.bg_canvas, bg=COLOR_BG_TOP)
        self.bg_canvas.create_window(340, 35, window=self.status_frame, width=640)

        self.lbl_header = tk.Label(
            self.status_frame, 
            text="🔑 FASE 2: PROTEÇÃO DE SENHAS", 
            font=("Consolas", 12, "bold"), 
            fg=COLOR_HEALTH, 
            bg=COLOR_BG_TOP
        )
        self.lbl_header.pack(side="left")

        self.lbl_mode = tk.Label(
            self.status_frame, 
            text="MODO: SIMULAÇÃO", 
            font=("Consolas", 12, "bold"), 
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
        self.bg_canvas.create_window(340, 310, window=self.card_frame, width=640, height=470)

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
    # --- MÓDULO 1: SIMULAÇÃO PRÁTICA DE FORÇA BRUTA ---
    # ==========================================================================
    def load_sim_mode(self):
        self.clear_card()
        self.lbl_mode.config(text="ETAPA 1: LABORATÓRIO")

        lbl_title = tk.Label(
            self.card_frame, 
            text="⚡ TESTADOR DE VULNERABILIDADE (FORÇA BRUTA)", 
            font=("Segoe UI", 10, "bold"), 
            fg=COLOR_CYAN_GLOW, 
            bg=COLOR_CARD_BG
        )
        lbl_title.pack(anchor="w", padx=20, pady=(15, 5))

        lbl_desc = tk.Label(
            self.card_frame, 
            text="Digite uma senha curta de até 4 letras (ex: 'gato' ou 'code') para testar a velocidade do ataque de força bruta em tempo real:", 
            font=("Segoe UI", 9), 
            fg=COLOR_TEXT_MAIN, 
            bg=COLOR_CARD_BG, 
            wraplength=580, 
            justify="left"
        )
        lbl_desc.pack(anchor="w", padx=20, pady=5)

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
        self.entry_pass.pack(fill="x", padx=20, pady=5)

        btn_run = self.create_custom_button(self.card_frame, "▶️ Iniciar Ataque de Força Bruta", self.run_brute_force)
        btn_run.pack(fill="x", padx=20, pady=8)

        self.txt_console = tk.Text(
            self.card_frame, 
            height=8, 
            font=("Consolas", 9), 
            bg=COLOR_BG_TOP, 
            fg=COLOR_TEXT_MUTED, 
            bd=1, 
            relief="solid",
            state="disabled"
        )
        self.txt_console.pack(fill="both", expand=True, padx=20, pady=5)

        self.btn_next = self.create_custom_button(self.card_frame, "Ir para o Desafio Teórico ➔", self.load_quiz_mode)
        self.btn_next.pack(fill="x", padx=20, pady=(5, 15))
        self.btn_next.config(state="disabled")

    def run_brute_force(self):
        senha = self.entry_pass.get().strip().lower()
        if not senha or len(senha) > 4 or not senha.isalpha():
            messagebox.showwarning("Aviso", "Digite apenas uma palavra de até 4 letras minúsculas!")
            return

        caracteres = string.ascii_lowercase
        inicio = time.time()
        tentativas = 0
        descoberta = None

        for comp in range(1, len(senha) + 1):
            for comb in itertools.product(caracteres, repeat=comp):
                tentativas += 1
                palpite = "".join(comb)
                if palpite == senha:
                    descoberta = palpite
                    break
            if descoberta:
                break

        tempo_gasto = time.time() - inicio

        log = f"[!] Iniciando algoritmo de Força Bruta...\n"
        log += f"[❌] SENHA COMPROMETIDA: '{descoberta}'\n"
        log += f"[*] Combinações testadas: {tentativas:,}\n"
        log += f"[*] Tempo decorrido: {tempo_gasto:.4f} segundos\n\n"
        log += "⚠️ CONCLUSÃO: Senhas curtas oferecem resistência nula a sistemas automatizados!"

        self.txt_console.config(state="normal")
        self.txt_console.delete("1.0", tk.END)
        self.txt_console.insert(tk.END, log)
        self.txt_console.config(state="disabled")

        self.btn_next.config(state="normal")

    # ==========================================================================
    # --- MÓDULO 2: QUIZ EDUCATIVO CONCEITUAL ---
    # ==========================================================================
    def load_quiz_mode(self):
        self.clear_card()
        self.lbl_mode.config(text="ETAPA 2: DESAFIO")

        lbl_cat = tk.Label(
            self.card_frame, 
            text=QUIZ_FASE_2["category"], 
            font=("Segoe UI", 10, "bold"), 
            fg=COLOR_CYAN_GLOW, 
            bg=COLOR_CARD_BG
        )
        lbl_cat.pack(anchor="w", padx=20, pady=(15, 5))

        lbl_q = tk.Label(
            self.card_frame, 
            text=QUIZ_FASE_2["question"], 
            font=("Segoe UI", 11), 
            fg=COLOR_TEXT_MAIN, 
            bg=COLOR_CARD_BG, 
            wraplength=580, 
            justify="left"
        )
        lbl_q.pack(anchor="w", padx=20, pady=10)

        self.quiz_buttons = []
        for i, opt in enumerate(QUIZ_FASE_2["options"]):
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

        correct_idx = QUIZ_FASE_2["answer"]
        selected_btn = self.quiz_buttons[selected_idx]

        if selected_idx == correct_idx:
            selected_btn.config(bg=COLOR_CORRECT, fg="#000000")
            self.root.update()
            
            messagebox.showinfo(
                "Resposta Correta! 🎯", 
                f"{QUIZ_FASE_2['explanations'][selected_idx]}\n\n{QUIZ_FASE_2['tip']}"
            )
            messagebox.showinfo("Fase 2 Concluída!", "Parabéns! Você dominou os conceitos essenciais de segurança de senhas.")
            self.root.destroy()
        else:
            selected_btn.config(bg=COLOR_INCORRECT, fg="#FFFFFF")
            self.quiz_buttons[correct_idx].config(bg=COLOR_CORRECT, fg="#000000")
            self.root.update()
            
            messagebox.showerror(
                "Resposta Incorreta! ⚠️", 
                f"{QUIZ_FASE_2['explanations'][selected_idx]}\n\n{QUIZ_FASE_2['tip']}"
            )
            self.load_quiz_mode()  # Reinicia o quiz para nova tentativa

if __name__ == "__main__":
    root = tk.Tk()
    app = Phase2App(root)
    root.mainloop()