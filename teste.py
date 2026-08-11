import os
import time
import string
import itertools
import hmac
import hashlib
import tkinter as tk
from tkinter import messagebox

# ===================================================================== #
# CONFIGURAÇÕES DA INTERFACE GRÁFICA (TEMA HACKER ÉTICO)               #
# ===================================================================== #
COLOR_BG = "#0B132B"         
COLOR_CARD = "#1C2541"       
COLOR_BTN = "#00B4D8"        
COLOR_TEXT = "#FFFFFF"       
COLOR_HEALTH = "#06D6A0"     

# --- NOVAS PERGUNTAS ATUALIZADAS DO QUIZ ---
QUESTIONS = [
    {
        "category": "🔑 AUTENTICAÇÃO (MFA)",
        "question": "Como funciona o método TOTP usado na autenticação multifator (MFA)?",
        "options": [
            "Envia um SMS padrão para o chip do celular",
            "Gera códigos temporários baseados em chaves secretas e no horário atual",
            "Valida apenas as perguntas de segurança do cadastro",
            "Usa uma lista fixa de senhas guardada no computador"
        ],
        "answer": 1
    },
    {
        "category": "🧠 ENGENHARIA SOCIAL",
        "question": "O que caracteriza um ataque de 'Spear Phishing'?",
        "options": [
            "Um ataque em massa enviado aleatoriamente para milhares de pessoas",
            "O roubo físico de roteadores dentro de uma empresa",
            "E-mails altamente personalizados direcionados a alvos específicos",
            "Bloqueio de arquivos do sistema exigindo resgate em criptomoedas"
        ],
        "answer": 2
    },
    {
        "category": "🦠 MALWARE",
        "question": "Qual tipo de malware criptografa os arquivos da vítima e exige pagamento?",
        "options": [
            "Spyware",
            "Ransomware",
            "Rootkit",
            "Trojan-Banker"
        ],
        "answer": 1
    },
    {
        "category": "⚙️ MANUTENÇÃO",
        "question": "Por que atualizações de segurança do sistema operacional devem ser instaladas logo?",
        "options": [
            "Apenas para mudar a parte visual e os ícones das janelas",
            "Para corrigir vulnerabilidades já conhecidas que hackers exploram",
            "Para apagar arquivos antigos e liberar espaço em disco",
            "Para desativar firewalls e antivírus antigos por completo"
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
# FASE 1: SIMULAÇÃO INTERATIVA DE SEGURANÇA (NO TERMINAL)              #
# ===================================================================== #
def rodar_simulacao_terminal():
    print("=" * 60)
    print("INICIANDO SIMULAÇÃO: EVOLUÇÃO DA SEGURANÇA DIGITAL")
    print("=" * 60)

    # PASSO 1: O PERIGO DO TEXTO PURO E REUTILIZAÇÃO
    print("\n[PASSO 1] Testando vulnerabilidades de armazenamento e reuso.")
    senha_usuario = input("Digite uma senha simples para salvar no arquivo (ex: 12345): ")

    with open("senhas.txt", "w", encoding="utf-8") as f:
        f.write(senha_usuario)
    print(f"[D] Arquivo 'senhas.txt' criado com a senha: '{senha_usuario}'")
    input("\n[Pressione ENTER para simular a execução de um Malware local...]")

    senha_roubada = ""
    if os.path.exists("senhas.txt"):
        with open("senhas.txt", "r", encoding="utf-8") as f:
            senha_roubada = f.read().strip()
        print(f"[❌] MALWARE: Sucesso! Arquivo lido. Senha capturada: '{senha_roubada}'")
        os.remove("senhas.txt")

    input("\n[Pressione ENTER para o Hacker usar essa senha em outros sites...]")
    contas_alvo = ["E-mail Principal", "Internet Banking", "Rede Social"]
    print("\n[B] Hacker inicia ataque de Credential Stuffing usando a senha roubada...")
    for conta in contas_alvo:
        print(f"[*] Testando credenciais roubadas no sistema do: {conta}")
        print(f"[❌] INVASÃO BEM-SUCEDIDA! Acesso liberado ao {conta}.")
    print("-" * 50)

    # PASSO 2: A FRAGILIDADE DAS SENHAS CURTAS
    print("\n[PASSO 2] Nova política: Mudar a senha para uma curta toda semana.")
    senha_curta_da_semana = input("Digite uma senha curta de até 4 letras minúsculas (ex: gato): ").lower()

    print(f"[A] Nova senha semanal definida: '{senha_curta_da_semana}'")
    input("\n[Pressione ENTER para iniciar o ataque de Força Bruta automatizado...]")
    print("[!] Quebrando senha por Força Bruta...")

    caracteres = string.ascii_lowercase
    inicio_forca_bruta = time.time()
    tentativas = 0
    senha_descoberta = None

    for comprimento in range(1, len(senha_curta_da_semana) + 1):
        for combinacao in itertools.product(caracteres, repeat=comprimento):
            tentativas += 1
            palpite = "".join(combinacao)
            if palpite == senha_curta_da_semana:
                senha_descoberta = palpite
                break
        if senha_descoberta:
            break

    tempo_gasto = time.time() - inicio_forca_bruta
    print(f"[❌] SENHA QUEBRADA: '{senha_descoberta}'")
    print(f"[*] Total de combinações testadas: {tentativas}")
    print(f"[*] Tempo necessário: {tempo_gasto:.4f} segundos")
    print("-" * 50)

    # PASSO 3: A SOLUÇÃO IDEAL - SENHA EXCLUSIVA + MFA
    print("\n[PASSO 3] Adotando a postura correta (Senha Forte Exclusiva + MFA)...")

    SENHA_BANCO_REAL = "Super#Senha#Exclusiva#Longa#2026"
    CHAVE_MFA_SECRETA = b"CHAVE_SECRETA_DO_CELULAR_DO_USUARIO_123"

    passo_tempo = int(time.time() // 30)
    mensagem = passo_tempo.to_bytes(8, byteorder='big')
    hash_hmac = hmac.new(CHAVE_MFA_SECRETA, msg=mensagem, digestmod=hashlib.sha256).digest()
    codigo_real_do_celular = str(int.from_bytes(hash_hmac[-4:], byteorder='big') % 1000000).zfill(6)

    print(f"[C] Usuário configurou a senha forte: '{SENHA_BANCO_REAL}'")
    print("[MFA] Sistema gerou um token temporário no celular do usuário real.")
    print("\n[CENÁRIO] O hacker descobriu sua senha por Phishing, mas o banco tem MFA.")
    
    codigo_tentado_pelo_hacker = input("\n[VOCÊ É O HACKER] Tente adivinhar o Token de 6 dígitos do MFA: ")

    print(f"\n[*] Código digitado pelo invasor: {codigo_tentado_pelo_hacker}")
    print(f"[*] Código real gerado no app do usuário: {codigo_real_do_celular}")

    if codigo_tentado_pelo_hacker == codigo_real_do_celular:
        print("[❌] Falha grave! O hacker acertou o token aleatório. Acesso concedido.")
    else:
        print("[✅] DEFESA TOTAL: Token incorreto! Sistema BLOQUEOU a tentativa de login.")

    print("\n" + "=" * 60)
