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