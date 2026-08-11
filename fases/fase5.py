import os
import time
import string
import itertools
import hmac
import hashlib

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
        self.root.geometry("600x500")
        self.root.configure(bg=COLOR_BG)
        self.current_q = 0
        self.lives = 3
        self.score = 0
        self.setup_ui()
        self.load_question()

    def setup_ui(self):
        self.status_frame = tk.Frame(self.root, bg=COLOR_BG)
        self.status_frame.pack(fill="x", padx=20, pady=15)

        self.lbl_firewall = tk.Label(
            self.status_frame, 
            text=f"🛡️ FIREWALL: {'█ ' * self.lives}", 
            font=("Consolas", 14, "bold"), 
            fg=COLOR_HEALTH, 
            bg=COLOR_BG
        )
        self.lbl_firewall.pack(side="left")

        self.lbl_score = tk.Label(
            self.status_frame, 
            text=f"SCORE: {self.score}", 
            font=("Consolas", 14, "bold"), 
            fg=COLOR_TEXT, 
            bg=COLOR_BG
        )
        self.lbl_score.pack(side="right")

        self.card_frame = tk.Frame(self.root, bg=COLOR_CARD, bd=2, relief="groove")
        self.card_frame.pack(fill="both", expand=True, padx=20, pady=10)

        self.lbl_category = tk.Label(
            self.card_frame, 
            text="", 
            font=("Helvetica", 11, "bold"), 
            fg=COLOR_BTN, 
            bg=COLOR_CARD
        )
        self.lbl_category.pack(anchor="w", padx=15, pady=(15, 5))

        self.lbl_question = tk.Label(
            self.card_frame, 
            text="", 
            font=("Helvetica", 13), 
            fg=COLOR_TEXT, 
            bg=COLOR_CARD, 
            wraplength=500, 
            justify="left"
        )
        self.lbl_question.pack(anchor="w", padx=15, pady=10)

        self.btn_frame = tk.Frame(self.card_frame, bg=COLOR_CARD)
        self.btn_frame.pack(fill="x", padx=15, pady=15)

        self.buttons = []
        for i in range(4):
            btn = tk.Button(
                self.btn_frame, 
                text="", 
                font=("Helvetica", 11), 
                bg=COLOR_BTN, 
                fg="#000000", 
                activebackground="#48CAE4",
                relief="flat",
                cursor="hand2",
                command=lambda idx=i: self.check_answer(idx)
            )
            btn.pack(fill="x", pady=5)
            self.buttons.append(btn)

    def load_question(self):
        if self.current_q < len(QUESTIONS):
            q_data = QUESTIONS[self.current_q]
            self.lbl_category.config(text=q_data["category"])
            self.lbl_question.config(text=q_data["question"])
            for i, opt in enumerate(q_data["options"]):
                self.buttons[i].config(text=f"[ {chr(65+i)} ]  {opt}")
        else:
            messagebox.showinfo("Vitória!", f"Você protegeu o sistema!\nPontuação final: {self.score}")
            self.root.destroy()

    def check_answer(self, selected_idx):
        correct_idx = QUESTIONS[self.current_q]["answer"]
        if selected_idx == correct_idx:
            self.score += 100
            self.lbl_score.config(text=f"SCORE: {self.score}")
        else:
            self.lives -= 1
            self.lbl_firewall.config(text=f"🛡️ FIREWALL: {'█ ' * self.lives}")
            if self.lives == 0:
                messagebox.showerror("Game Over", "O sistema foi hackeado! Tente novamente.")
                self.root.destroy()
                return
        self.current_q += 1
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
