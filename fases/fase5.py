import os
import time
import string
import itertools
import hmac
import hashlib

<<<<<<< HEAD
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
# --- DADOS DO QUIZ INTEGRADOS (6 PERGUNTAS) ---
# ==============================================================================
=======
# Tenta importar o tkinter de forma segura. Se não tiver, o jogo avisa em vez de travar.
try:
    import tkinter as tk
    from tkinter import messagebox
    TKINTER_DISPONIVEL = True
except ImportError:
    TKINTER_DISPONIVEL = False

# ===================================================================== #
# CONFIGURAÇÕES DA INTERFACE GRÁFICA (SE DISPONÍVEL)                    #
# ===================================================================== #
COLOR_BG = "#0B132B"         
COLOR_CARD = "#1C2541"       
COLOR_BTN = "#00B4D8"        
COLOR_TEXT = "#FFFFFF"       
COLOR_HEALTH = "#06D6A0"     

>>>>>>> 619d68e0d4299beee6ca457452ce8d648260d936
QUESTIONS = [
    {
        "category": "🔒 SENHAS SEGURAS",
        "question": "Qual das alternativas abaixo representa uma senha forte?",
        "options": ["12345678", "admin2026", "K#9vP!x2$Lq", "senhasecreta"],
        "answer": 2
    },
    {
        "category": "✉️ PHISHING",
        "question": "Você recebe um e-mail urgente do seu banco pedindo para clicar num link. O que fazer?",
        "options": [
            "Clicar imediatamente",
            "Ignorar e verificar o remetente / canal oficial",
            "Encaminhar para todos os amigos",
            "Responder fornecendo sua senha"
        ],
        "answer": 1
    }
]

class CyberQuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("CyberShield: Ethical Hacker Quiz")
<<<<<<< HEAD
        self.root.geometry("680x600")
        self.root.resizable(False, False)

=======
        self.root.geometry("600x500")
        self.root.configure(bg=COLOR_BG)
>>>>>>> 619d68e0d4299beee6ca457452ce8d648260d936
        self.current_q = 0
        self.lives = 3
        self.score = 0
        self.setup_ui()
        self.load_question()

    def setup_ui(self):
<<<<<<< HEAD
        # --- CANVAS DE FUNDO (DEGRADÊ + DETALHES DE CIRCUITO) ---
        self.bg_canvas = tk.Canvas(self.root, width=680, height=600, highlightthickness=0)
        self.bg_canvas.pack(fill="both", expand=True)
        self.draw_cyber_background()

        # --- HEADER DE STATUS ---
        self.status_frame = tk.Frame(self.bg_canvas, bg=COLOR_BG_TOP)
        self.bg_canvas.create_window(340, 35, window=self.status_frame, width=640)
=======
        self.status_frame = tk.Frame(self.root, bg=COLOR_BG)
        self.status_frame.pack(fill="x", padx=20, pady=15)
>>>>>>> 619d68e0d4299beee6ca457452ce8d648260d936

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

<<<<<<< HEAD
        # --- CARD PRINCIPAL DE CONTEÚDO ---
        self.card_frame = tk.Frame(
            self.bg_canvas, 
            bg=COLOR_CARD_BG, 
            highlightbackground=COLOR_CARD_BORDER, 
            highlightthickness=2,
            bd=0
        )
        self.bg_canvas.create_window(340, 310, window=self.card_frame, width=640, height=470)
=======
        self.card_frame = tk.Frame(self.root, bg=COLOR_CARD, bd=2, relief="groove")
        self.card_frame.pack(fill="both", expand=True, padx=20, pady=10)
>>>>>>> 619d68e0d4299beee6ca457452ce8d648260d936

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
<<<<<<< HEAD
            font=("Segoe UI", 11), 
            fg=COLOR_TEXT_MAIN, 
            bg=COLOR_CARD_BG, 
            wraplength=580, 
=======
            font=("Helvetica", 13), 
            fg=COLOR_TEXT, 
            bg=COLOR_CARD, 
            wraplength=500, 
>>>>>>> 619d68e0d4299beee6ca457452ce8d648260d936
            justify="left"
        )
        self.lbl_question.pack(anchor="w", padx=20, pady=10)

<<<<<<< HEAD
        # --- CONTAINER DOS BOTÕES ---
        self.btn_frame = tk.Frame(self.card_frame, bg=COLOR_CARD_BG)
        self.btn_frame.pack(fill="both", expand=True, padx=20, pady=(5, 15))
=======
        self.btn_frame = tk.Frame(self.card_frame, bg=COLOR_CARD)
        self.btn_frame.pack(fill="x", padx=15, pady=15)
>>>>>>> 619d68e0d4299beee6ca457452ce8d648260d936

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
        
        # Gradiente suave
        for y in range(height):
            r = int(r1 + (r2 - r1) * (y / height))
            g = int(g1 + (g2 - g1) * (y / height))
            b = int(b1 + (b2 - b1) * (y / height))
            color = f"#{r:02x}{g:02x}{b:02x}"
            self.bg_canvas.create_line(0, y, width, y, fill=color)

        # Linhas de circuito cibernético
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
        if btn["state"] == "normal":
            btn.config(bg=COLOR_BTN_HOVER, fg=COLOR_TEXT_MAIN)

    def on_hover_leave(self, btn):
        if btn["state"] == "normal":
            btn.config(bg=COLOR_BTN_BG, fg=COLOR_TEXT_MUTED)

    def load_question(self):
        if self.current_q < len(QUESTIONS):
            q_data = QUESTIONS[self.current_q]
            self.lbl_category.config(text=q_data["category"])
            self.lbl_question.config(text=q_data["question"])
            for i, opt in enumerate(q_data["options"]):
<<<<<<< HEAD
                self.buttons[i].config(
                    text=f"[ {chr(65+i)} ]  {opt}",
                    bg=COLOR_BTN_BG,
                    fg=COLOR_TEXT_MUTED,
                    state="normal"
                )
=======
                self.buttons[i].config(text=f"[ {chr(65+i)} ]  {opt}")
>>>>>>> 619d68e0d4299beee6ca457452ce8d648260d936
        else:
            messagebox.showinfo("Vitória! 🏆", f"Você protegeu a rede com sucesso!\n\nPontuação Final: {self.score}")
            self.root.destroy()

    def check_answer(self, selected_idx):
        correct_idx = QUESTIONS[self.current_q]["answer"]
<<<<<<< HEAD
        
        for btn in self.buttons:
            btn.config(state="disabled")

        if selected_idx == correct_idx:
            self.score += 100
            self.lbl_score.config(text=f"SCORE: {self.score}")
            self.buttons[selected_idx].config(bg=COLOR_CORRECT, fg="#000000")
        else:
            self.lives -= 1
            self.lbl_firewall.config(text=f"🛡️ FIREWALL: {'█ ' * self.lives}")
            self.buttons[selected_idx].config(bg=COLOR_INCORRECT, fg=COLOR_TEXT_MAIN)
            self.buttons[correct_idx].config(bg=COLOR_CORRECT, fg="#000000")

=======
        if selected_idx == correct_idx:
            self.score += 100
            self.lbl_score.config(text=f"SCORE: {self.score}")
        else:
            self.lives -= 1
            self.lbl_firewall.config(text=f"🛡️ FIREWALL: {'█ ' * self.lives}")
>>>>>>> 619d68e0d4299beee6ca457452ce8d648260d936
            if self.lives == 0:
                messagebox.showerror("Game Over", "O sistema foi hackeado! Tente novamente.")
                self.root.destroy()
                return
        self.current_q += 1
<<<<<<< HEAD
        self.root.after(1200, self.load_question)

    def game_over(self):
        messagebox.showerror("Game Over ⚠️", "O firewall caiu e o sistema foi comprometido!\n\nTente novamente.")
        self.root.destroy()
=======
        self.load_question()

# ===================================================================== #
# SIMULAÇÕES VIA TERMINAL                                               #
# ===================================================================== #
def rodar_simulacao_terminal():
    print("\n" + "=" * 60)
    print("MODO SIMULAÇÃO TÉCNICA ATIVADO")
    print("=" * 60)
    
    print("\n[PASSO 1] Testando vulnerabilidades de armazenamento e reuso.")
    senha_usuario = input("Digite uma senha simples para salvar no arquivo (ex: 12345): ")
>>>>>>> 619d68e0d4299beee6ca457452ce8d648260d936

    with open("senhas.txt", "w", encoding="utf-8") as f:
        f.write(senha_usuario)
    print(f"[D] Arquivo 'senhas.txt' criado.")
    input("[Aperte ENTER para o Malware agir...]")

    if os.path.exists("senhas.txt"):
        with open("senhas.txt", "r", encoding="utf-8") as f:
            senha_roubada = f.read().strip()
        print(f"[❌] MALWARE: Senha capturada do arquivo: '{senha_roubada}'")
        os.remove("senhas.txt")

    input("\n[Aperte ENTER para testar Credential Stuffing...]")
    contas_alvo = ["E-mail Principal", "Internet Banking", "Rede Social"]
    for conta in contas_alvo:
        print(f"[❌] INVASÃO BEM-SUCEDIDA no site: {conta}")
    print("-" * 50)

    print("\n[PASSO 2] Quebra de senha curta.")
    senha_curta = input("Digite uma senha curta de até 4 letras (ex: gato): ").lower()
    print("[!] Quebrando por Força Bruta automatizada...")
    
    caracteres = string.ascii_lowercase
    inicio = time.time()
    tentativas = 0
    descoberta = None

    for comp in range(1, len(senha_curta) + 1):
        for comb in itertools.product(caracteres, repeat=comp):
            tentativas += 1
            if "".join(comb) == senha_curta:
                descoberta = "".join(comb)
                break
        if descoberta: break

    print(f"[❌] SENHA QUEBRADA: '{descoberta}' em {time.time() - inicio:.4f} segundos ({tentativas} testes).")
    print("-" * 50)

    print("\n[PASSO 3] Teste de MFA (Token Celular).")
    print("Gerando token dinâmico de 30 segundos baseado em tempo...")
    
    passo_tempo = int(time.time() // 30)
    msg = passo_tempo.to_bytes(8, byteorder='big')
    hash_hmac = hmac.new(b"CHAVE_123", msg=msg, digestmod=hashlib.sha256).digest()
    codigo_real = str(int.from_bytes(hash_hmac[-4:], byteorder='big') % 1000000).zfill(6)

    chute = input("Tente adivinhar o token de 6 dígitos agora: ")
    print(f"[*] Seu palpite: {chute} | Token Real do Sistema: {codigo_real}")
    
    if chute == codigo_real:
        print("[❌] Inacreditável! Você burlou o token.")
    else:
        print("[✅] DEFESA TOTAL: Token incorreto. O sistema barrou o acesso do hacker.")
    
    input("\n[Simulação concluída. Aperte ENTER para voltar ao menu]")

# ===================================================================== #
# MENU PRINCIPAL DE EXECUÇÃO                                            #
# ===================================================================== #
if __name__ == "__main__":
<<<<<<< HEAD
    root = tk.Tk()
    
    # Centralização da janela na tela
    window_width = 680
    window_height = 600
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    position_right = int(screen_width/2 - window_width/2)
    position_top = int(screen_height/2 - window_height/2)
    root.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")
    
    app = CyberQuizApp(root)
    root.mainloop()
=======
    while True:
        print("\n" + "=" * 50)
        print("         PAINEL DE SEGURANÇA DIGITAL            ")
        print("=" * 50)
        print("1. Rodar Simulação de Ataques (Via Terminal)")
        print("2. Abrir o Jogo CyberShield Quiz (Interface Gráfica)")
        print("3. Sair")
        print("=" * 50)
        
        opcao = input("Escolha uma opção (1, 2 ou 3): ").strip()
        
        if opcao == "1":
            rodar_simulacao_terminal()
        elif opcao == "2":
            if not TKINTER_DISPONIVEL:
                print("\n[⚠️ ERRO] A interface gráfica (Tkinter) não está instalada no seu Python.")
                print("Se você usa Linux Ubuntu/Debian, instale rodando: sudo apt-get install python3-tk")
                input("\nPressione ENTER para voltar.")
            else:
                print("\nAbrindo janela do Quiz na tela...")
                root = tk.Tk()
                app = CyberQuizApp(root)
                root.mainloop()
        elif opcao == "3":
            print("\nEncerrando simulador.")
            break
        else:
            print("\nOpção inválida! Escolha 1, 2 ou 3.")
>>>>>>> 619d68e0d4299beee6ca457452ce8d648260d936
