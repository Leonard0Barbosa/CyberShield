import tkinter as tk
from tkinter import messagebox


# ============================================================
# CYBERSHIELD — FASE 10
# BOSS FINAL
# ============================================================

COLOR_BG = "#050509"
COLOR_BG_DARK = "#0A080C"

COLOR_CARD = "#130D12"
COLOR_CARD_BORDER = "#5C1625"

COLOR_RED = "#FF1744"
COLOR_RED_DARK = "#8B1028"
COLOR_RED_BRIGHT = "#FF003C"

COLOR_CYAN = "#00F0FF"
COLOR_GREEN = "#00E676"
COLOR_YELLOW = "#FFD600"

COLOR_TEXT = "#FFFFFF"
COLOR_MUTED = "#B8AEB2"

COLOR_BUTTON = "#24131A"
COLOR_BUTTON_HOVER = "#5E1628"


# ============================================================
# PERGUNTAS DO BOSS
# ============================================================

BOSS_BATTLE_DATA = [

    # --------------------------------------------------------
    # PERGUNTA 1
    # --------------------------------------------------------

    {
        "categoria": "🔐 INTEGRIDADE",

        "questao": (
            "Um administrador percebe que o hash SHA-256 de um "
            "arquivo crítico mudou após uma alteração que não foi "
            "registrada. O que essa evidência indica com maior "
            "precisão?"
        ),

        "opcoes": [
            "O arquivo ficou indisponível",
            "A confidencialidade foi necessariamente comprometida",
            "O conteúdo do arquivo foi alterado e precisa ser investigado",
            "O servidor obrigatoriamente foi desligado"
        ],

        "resposta_correta": 2,

        "dificuldade": 2,

        "explicacao": (
            "O hash funciona como uma impressão digital dos dados. "
            "Se o arquivo muda, seu hash normalmente também muda. "
            "Isso indica uma alteração, mas não permite concluir "
            "sozinho quem realizou a alteração ou qual foi a causa."
        )
    },


    # --------------------------------------------------------
    # PERGUNTA 2
    # --------------------------------------------------------

    {
        "categoria": "🔑 AUTENTICAÇÃO",

        "questao": (
            "Uma empresa descobriu que uma senha de funcionário "
            "apareceu em um vazamento. A conta utiliza uma senha "
            "exclusiva, mas ainda não possui MFA. Qual medida "
            "oferece uma camada adicional de proteção?"
        ),

        "opcoes": [
            "Usar a mesma senha em outros sistemas",
            "Ativar MFA e redefinir a credencial comprometida",
            "Colocar a senha em um arquivo de texto",
            "Diminuir o tamanho da senha"
        ],

        "resposta_correta": 1,

        "dificuldade": 2,

        "explicacao": (
            "Uma senha comprometida deve ser substituída. "
            "O MFA adiciona outro fator de autenticação, reduzindo "
            "o impacto caso a senha seja descoberta."
        )
    },


    # --------------------------------------------------------
    # PERGUNTA 3
    # --------------------------------------------------------

    {
        "categoria": "🎣 PHISHING",

        "questao": (
            "Um funcionário recebe um e-mail aparentemente enviado "
            "pelo setor financeiro. O texto exige uma ação urgente "
            "e contém um link para login. O domínio do link possui "
            "uma pequena alteração em relação ao domínio oficial. "
            "Qual é a melhor resposta?"
        ),

        "opcoes": [
            "Clicar rapidamente antes que a conta seja bloqueada",
            "Responder ao e-mail pedindo confirmação",
            "Verificar a mensagem por um canal oficial e não utilizar o link",
            "Encaminhar o e-mail para toda a empresa"
        ],

        "resposta_correta": 2,

        "dificuldade": 3,

        "explicacao": (
            "Domínios parecidos são frequentemente utilizados para "
            "enganar usuários. A urgência também é um sinal de alerta. "
            "A mensagem deve ser verificada por um canal confiável."
        )
    },


    # --------------------------------------------------------
    # PERGUNTA 4
    # --------------------------------------------------------

    {
        "categoria": "🌐 DNS / REDE",

        "questao": (
            "Durante uma investigação, um analista precisa descobrir "
            "qual endereço IP está associado ao domínio "
            "'empresa-exemplo.com'. Qual serviço é responsável "
            "normalmente por realizar essa resolução?"
        ),

        "opcoes": [
            "DHCP",
            "Firewall",
            "DNS",
            "MFA"
        ],

        "resposta_correta": 2,

        "dificuldade": 2,

        "explicacao": (
            "O DNS traduz nomes de domínio em endereços IP. "
            "O DHCP possui outra função: distribuir configurações "
            "de rede, como endereços IP."
        )
    },


    # --------------------------------------------------------
    # PERGUNTA 5
    # --------------------------------------------------------

    {
        "categoria": "🗄️ BANCO DE DADOS",

        "questao": (
            "Um usuário consegue fazer login normalmente, porém "
            "após a autenticação consegue acessar registros "
            "administrativos que não deveriam estar disponíveis "
            "para sua função. Qual controle provavelmente falhou?"
        ),

        "opcoes": [
            "Autenticação",
            "Autorização / controle de acesso",
            "DNS",
            "Disponibilidade"
        ],

        "resposta_correta": 1,

        "dificuldade": 3,

        "explicacao": (
            "A autenticação confirmou a identidade do usuário. "
            "O problema está no que ele pode fazer depois de "
            "autenticado, portanto envolve autorização e controle "
            "de acesso."
        )
    },


    # --------------------------------------------------------
    # PERGUNTA 6
    # --------------------------------------------------------

    {
        "categoria": "🛡️ DESENVOLVIMENTO SEGURO",

        "questao": (
            "Uma aplicação recebe dados diretamente de usuários e "
            "os utiliza em operações internas. Qual abordagem é "
            "mais adequada para reduzir riscos relacionados a "
            "entradas maliciosas?"
        ),

        "opcoes": [
            "Confiar nos dados porque o usuário está autenticado",
            "Aumentar a velocidade do servidor",
            "Validar, normalizar e tratar adequadamente as entradas",
            "Desativar o firewall"
        ],

        "resposta_correta": 2,

        "dificuldade": 3,

        "explicacao": (
            "Autenticação não torna automaticamente os dados "
            "confiáveis. As entradas devem ser validadas e tratadas "
            "de acordo com o contexto em que serão utilizadas."
        )
    },


    # --------------------------------------------------------
    # PERGUNTA 7
    # --------------------------------------------------------

    {
        "categoria": "🚨 SOC / INCIDENTE",

        "questao": (
            "O SOC detecta dezenas de falhas de login, seguidas "
            "por um login bem-sucedido de uma localização incomum "
            "e posteriormente um download elevado de arquivos. "
            "Qual conclusão é mais apropriada?"
        ),

        "opcoes": [
            "O computador está definitivamente infectado",
            "O usuário apenas esqueceu a senha",
            "Existe um comportamento suspeito que merece investigação",
            "O servidor necessariamente está desligado"
        ],

        "resposta_correta": 2,

        "dificuldade": 3,

        "explicacao": (
            "Os eventos formam um padrão suspeito, mas os registros "
            "não são suficientes para afirmar definitivamente que "
            "houve comprometimento. O correto é investigar e "
            "correlacionar os eventos."
        )
    },


    # --------------------------------------------------------
    # PERGUNTA 8
    # --------------------------------------------------------

    {
        "categoria": "🔏 CRIPTOGRAFIA",

        "questao": (
            "Uma equipe precisa verificar se um arquivo recebido "
            "foi alterado durante o processo de distribuição. "
            "Ela possui um hash conhecido do arquivo original. "
            "O que deve fazer?"
        ),

        "opcoes": [
            "Comparar o hash do arquivo recebido com o hash esperado",
            "Converter o arquivo para Base64",
            "Alterar o nome do arquivo",
            "Reiniciar o servidor"
        ],

        "resposta_correta": 0,

        "dificuldade": 3,

        "explicacao": (
            "Calculando o hash do arquivo recebido e comparando-o "
            "com o valor esperado, é possível detectar alterações "
            "no conteúdo."
        )
    },


    # --------------------------------------------------------
    # PERGUNTA 9
    # --------------------------------------------------------

    {
        "categoria": "✍️ ASSINATURA DIGITAL",

        "questao": (
            "Uma organização precisa verificar a autenticidade de "
            "uma mensagem e também detectar se ela foi modificada "
            "depois de assinada. Qual mecanismo é apropriado?"
        ),

        "opcoes": [
            "Compressão",
            "Base64",
            "Assinatura digital",
            "DHCP"
        ],

        "resposta_correta": 2,

        "dificuldade": 3,

        "explicacao": (
            "Uma assinatura digital permite verificar a autenticidade "
            "da origem e detectar alterações na mensagem."
        )
    },


    # --------------------------------------------------------
    # PERGUNTA 10 — MAIS DIFÍCIL
    # --------------------------------------------------------

    {
        "categoria": "☠️ INCIDENT RESPONSE",

        "questao": (
            "Durante um incidente, uma conta administrativa apresenta "
            "atividade suspeita. O atacante pode ainda estar conectado. "
            "Qual ação representa uma abordagem inicial mais adequada?"
        ),

        "opcoes": [
            "Apagar todos os computadores da empresa",
            "Publicar imediatamente todos os detalhes do incidente",
            "Conter o acesso comprometido, preservar evidências e iniciar a investigação",
            "Ignorar o comportamento até aparecer uma prova definitiva"
        ],

        "resposta_correta": 2,

        "dificuldade": 4,

        "explicacao": (
            "Em um incidente real, é importante conter o problema "
            "sem destruir evidências. A equipe deve proteger as "
            "contas afetadas, preservar informações relevantes e "
            "seguir o procedimento de resposta a incidentes."
        )
    },


    # --------------------------------------------------------
    # PERGUNTA 11 — BOSS FINAL
    # --------------------------------------------------------

    {
        "categoria": "👹 PROTOCOLO FINAL",

        "questao": (
            "O SOC correlaciona logs e encontra: múltiplas tentativas "
            "de autenticação, acesso administrativo fora do padrão, "
            "alterações em arquivos críticos e transferência de "
            "dados para um destino externo. Qual interpretação é "
            "mais tecnicamente responsável?"
        ),

        "opcoes": [
            "É apenas uma falha de senha sem relação entre os eventos",
            "É possível afirmar exatamente quem é o atacante sem investigação",
            "Existe um forte conjunto de indicadores de possível comprometimento que exige resposta imediata",
            "Os arquivos foram necessariamente apagados"
        ],

        "resposta_correta": 2,

        "dificuldade": 5,

        "explicacao": (
            "A combinação de eventos aumenta significativamente a "
            "suspeita de um incidente. Ainda assim, os logs não "
            "permitem concluir automaticamente a identidade do "
            "atacante. É necessário investigar, correlacionar "
            "evidências e executar o plano de resposta."
        )
    }
]


# ============================================================
# APLICAÇÃO
# ============================================================

class BossFightApp:

    def __init__(self, root):

        self.root = root

        self.root.title("☠ CYBERSHIELD — BOSS FINAL")

        self.root.geometry("760x650")

        self.root.resizable(False, False)

        self.root.configure(bg=COLOR_BG)

        self.vida_jogador = 100

        self.vida_boss = 100

        self.indice_questao = 0

        self.pontos = 0

        self.respondendo = False

        self.mostrar_introducao()


    # ========================================================
    # INTRODUÇÃO
    # ========================================================

    def mostrar_introducao(self):

        self.limpar_janela()

        frame = tk.Frame(
            self.root,
            bg=COLOR_BG
        )

        frame.pack(
            fill="both",
            expand=True
        )

        tk.Label(
            frame,
            text="⚠️ ALERTA CRÍTICO ⚠️",
            font=("Consolas", 28, "bold"),
            fg=COLOR_RED_BRIGHT,
            bg=COLOR_BG
        ).pack(pady=(70, 20))

        tk.Label(
            frame,
            text="PROTOCOLO DE EMERGÊNCIA ATIVADO",
            font=("Consolas", 15, "bold"),
            fg=COLOR_RED,
            bg=COLOR_BG
        ).pack(pady=10)

        tk.Label(
            frame,
            text=(
                "\nVocê chegou ao núcleo do sistema.\n\n"
                "O invasor ultrapassou várias camadas de defesa.\n"
                "Agora não existem mais fases intermediárias.\n\n"
                "Cada decisão errada causará danos ao sistema.\n"
                "As próximas perguntas exigirão conhecimento real\n"
                "de segurança da informação.\n\n"
                "O protocolo final está aguardando uma decisão."
            ),
            font=("Segoe UI", 12),
            fg=COLOR_TEXT,
            bg=COLOR_BG,
            justify="center"
        ).pack(pady=20)

        tk.Label(
            frame,
            text="☠️  O BOSS ESTÁ AGUARDANDO.  ☠️",
            font=("Consolas", 16, "bold"),
            fg=COLOR_RED_BRIGHT,
            bg=COLOR_BG
        ).pack(pady=25)

        # Importante:
        # Não usamos messagebox aqui.
        # Assim o botão OK não interfere na criação da fase.

        tk.Button(
            frame,
            text="⚔️ ENTRAR NO NÚCLEO",
            font=("Consolas", 13, "bold"),
            bg=COLOR_RED_DARK,
            fg="white",
            activebackground=COLOR_RED_BRIGHT,
            activeforeground="white",
            relief="flat",
            cursor="hand2",
            padx=30,
            pady=12,
            command=self.iniciar_batalha
        ).pack(pady=20)


    # ========================================================
    # INICIAR BATALHA
    # ========================================================

    def iniciar_batalha(self):

        self.limpar_janela()

        self.criar_interface()

        self.carregar_questao()


    # ========================================================
    # LIMPAR JANELA
    # ========================================================

    def limpar_janela(self):

        for widget in self.root.winfo_children():

            widget.destroy()


    # ========================================================
    # INTERFACE
    # ========================================================

    def criar_interface(self):

        # ----------------------------------------------------
        # TÍTULO
        # ----------------------------------------------------

        tk.Label(
            self.root,
            text="☠ CYBERSHIELD — BOSS FINAL ☠",
            font=("Consolas", 21, "bold"),
            fg=COLOR_RED_BRIGHT,
            bg=COLOR_BG
        ).pack(pady=(15, 5))

        tk.Label(
            self.root,
            text="PROTOCOLO DE CONTENÇÃO // AMEAÇA CRÍTICA",
            font=("Consolas", 9, "bold"),
            fg=COLOR_MUTED,
            bg=COLOR_BG
        ).pack(pady=(0, 15))


        # ----------------------------------------------------
        # STATUS
        # ----------------------------------------------------

        self.status = tk.Frame(
            self.root,
            bg=COLOR_BG
        )

        self.status.pack(
            fill="x",
            padx=40
        )


        # ----------------------------------------------------
        # PLAYER
        # ----------------------------------------------------

        tk.Label(
            self.status,
            text="🛡️ OPERADOR",
            font=("Consolas", 11, "bold"),
            fg=COLOR_CYAN,
            bg=COLOR_BG
        ).grid(
            row=0,
            column=0,
            sticky="w"
        )


        self.lbl_vida_player = tk.Label(
            self.status,
            text="100 / 100",
            font=("Consolas", 10, "bold"),
            fg=COLOR_GREEN,
            bg=COLOR_BG
        )

        self.lbl_vida_player.grid(
            row=1,
            column=0,
            sticky="w"
        )


        self.canvas_player = tk.Canvas(
            self.status,
            width=300,
            height=22,
            bg="#251018",
            highlightthickness=1,
            highlightbackground=COLOR_RED_DARK
        )

        self.canvas_player.grid(
            row=2,
            column=0,
            padx=(0, 20),
            pady=5
        )


        self.fill_player = self.canvas_player.create_rectangle(
            0,
            0,
            300,
            22,
            fill=COLOR_GREEN,
            outline=""
        )


        # ----------------------------------------------------
        # BOSS
        # ----------------------------------------------------

        tk.Label(
            self.status,
            text="👹 BOSS — AMEAÇA",
            font=("Consolas", 11, "bold"),
            fg=COLOR_RED_BRIGHT,
            bg=COLOR_BG
        ).grid(
            row=0,
            column=1,
            sticky="e"
        )


        self.lbl_vida_boss = tk.Label(
            self.status,
            text="100 / 100",
            font=("Consolas", 10, "bold"),
            fg=COLOR_RED_BRIGHT,
            bg=COLOR_BG
        )

        self.lbl_vida_boss.grid(
            row=1,
            column=1,
            sticky="e"
        )


        self.canvas_boss = tk.Canvas(
            self.status,
            width=300,
            height=22,
            bg="#251018",
            highlightthickness=1,
            highlightbackground=COLOR_RED_DARK
        )

        self.canvas_boss.grid(
            row=2,
            column=1,
            pady=5
        )


        self.fill_boss = self.canvas_boss.create_rectangle(
            0,
            0,
            300,
            22,
            fill=COLOR_RED_BRIGHT,
            outline=""
        )


        # ----------------------------------------------------
        # SCORE
        # ----------------------------------------------------

        self.lbl_score = tk.Label(
            self.root,
            text="SCORE: 0",
            font=("Consolas", 11, "bold"),
            fg=COLOR_YELLOW,
            bg=COLOR_BG
        )

        self.lbl_score.pack(
            pady=8
        )


        # ----------------------------------------------------
        # CARD
        # ----------------------------------------------------

        self.card = tk.Frame(
            self.root,
            bg=COLOR_CARD,
            highlightbackground=COLOR_CARD_BORDER,
            highlightthickness=2
        )

        self.card.pack(
            fill="both",
            expand=True,
            padx=35,
            pady=10
        )


        self.lbl_categoria = tk.Label(
            self.card,
            text="",
            font=("Consolas", 10, "bold"),
            fg=COLOR_RED_BRIGHT,
            bg=COLOR_CARD
        )

        self.lbl_categoria.pack(
            pady=(18, 8)
        )


        self.lbl_numero = tk.Label(
            self.card,
            text="",
            font=("Consolas", 9),
            fg=COLOR_MUTED,
            bg=COLOR_CARD
        )

        self.lbl_numero.pack()


        self.lbl_questao = tk.Label(
            self.card,
            text="",
            font=("Segoe UI", 13, "bold"),
            fg=COLOR_TEXT,
            bg=COLOR_CARD,
            wraplength=630,
            justify="center"
        )

        self.lbl_questao.pack(
            pady=18,
            padx=30
        )


        self.frame_botoes = tk.Frame(
            self.card,
            bg=COLOR_CARD
        )

        self.frame_botoes.pack(
            fill="x",
            padx=35,
            pady=5
        )


        self.lbl_dificuldade = tk.Label(
            self.card,
            text="",
            font=("Consolas", 9, "bold"),
            fg=COLOR_RED,
            bg=COLOR_CARD
        )

        self.lbl_dificuldade.pack(
            pady=10
        )


    # ========================================================
    # CARREGAR QUESTÃO
    # ========================================================

    def carregar_questao(self):

        if self.indice_questao >= len(BOSS_BATTLE_DATA):

            self.vitoria()

            return


        dados = BOSS_BATTLE_DATA[
            self.indice_questao
        ]


        self.respondendo = False


        self.lbl_categoria.config(
            text=dados["categoria"]
        )


        self.lbl_numero.config(
            text=(
                f"QUESTÃO "
                f"{self.indice_questao + 1}"
                f"/"
                f"{len(BOSS_BATTLE_DATA)}"
            )
        )


        self.lbl_questao.config(
            text=dados["questao"]
        )


        dificuldade = dados["dificuldade"]

        estrelas = "★" * dificuldade

        self.lbl_dificuldade.config(
            text=f"DIFICULDADE: {estrelas}"
        )


        # Remove botões antigos

        for widget in self.frame_botoes.winfo_children():

            widget.destroy()


        # Cria alternativas

        for i, opcao in enumerate(
            dados["opcoes"]
        ):

            botao = tk.Button(
                self.frame_botoes,
                text=opcao,
                font=("Segoe UI", 10, "bold"),
                bg=COLOR_BUTTON,
                fg=COLOR_TEXT,
                activebackground=COLOR_BUTTON_HOVER,
                activeforeground=COLOR_TEXT,
                relief="flat",
                cursor="hand2",
                anchor="w",
                padx=15,
                pady=8,
                command=lambda idx=i:
                self.processar_resposta(idx)
            )

            botao.pack(
                fill="x",
                pady=4
            )


    # ========================================================
    # PROCESSAR RESPOSTA
    # ========================================================

    def processar_resposta(
        self,
        indice_escolhido
    ):

        if self.respondendo:

            return


        self.respondendo = True


        dados = BOSS_BATTLE_DATA[
            self.indice_questao
        ]


        correta = (
            indice_escolhido
            ==
            dados["resposta_correta"]
        )


        # ====================================================
        # ACERTO
        # ====================================================

        if correta:

            dano = 12 + (
                dados["dificuldade"] * 5
            )

            self.vida_boss -= dano

            self.pontos += (
                dados["dificuldade"] * 100
            )


            self.atualizar_barras()


            messagebox.showinfo(
                "⚔️ ATAQUE BEM-SUCEDIDO",
                (
                    f"✅ Resposta correta!\n\n"
                    f"O Boss sofreu {dano} de dano.\n\n"
                    f"+{dados['dificuldade'] * 100} pontos\n\n"
                    f"{dados['explicacao']}"
                )
            )


        # ====================================================
        # ERRO
        # ====================================================

        else:

            dano = 8 + (
                dados["dificuldade"] * 8
            )

            self.vida_jogador -= dano


            self.atualizar_barras()


            messagebox.showerror(
                "☠️ DEFESA ROMPIDA",
                (
                    "❌ Resposta incorreta!\n\n"
                    f"O sistema sofreu {dano} de dano.\n\n"
                    f"{dados['explicacao']}"
                )
            )


        # ====================================================
        # VERIFICAR RESULTADO
        # ====================================================

        if self.vida_boss <= 0:

            self.vitoria()

            return


        if self.vida_jogador <= 0:

            self.game_over()

            return


        # Próxima questão

        self.indice_questao += 1


        if self.indice_questao >= len(
            BOSS_BATTLE_DATA
        ):

            # Caso o Boss ainda esteja vivo,
            # ele recebe uma recuperação pequena
            # e a batalha continua em modo difícil.

            self.indice_questao = 0

            self.vida_boss = min(
                100,
                self.vida_boss + 15
            )


            messagebox.showwarning(
                "⚠️ O BOSS RESISTIU",
                (
                    "O Boss ainda está de pé.\n\n"
                    "Ele recuperou parte da defesa.\n\n"
                    "As perguntas serão reiniciadas.\n"
                    "Agora você precisa finalizar o combate."
                )
            )


        self.carregar_questao()


    # ========================================================
    # ATUALIZAR BARRAS
    # ========================================================

    def atualizar_barras(self):

        self.vida_jogador = max(
            0,
            self.vida_jogador
        )

        self.vida_boss = max(
            0,
            self.vida_boss
        )


        largura_player = (
            self.vida_jogador * 3
        )

        largura_boss = (
            self.vida_boss * 3
        )


        self.canvas_player.coords(
            self.fill_player,
            0,
            0,
            largura_player,
            22
        )


        self.canvas_boss.coords(
            self.fill_boss,
            0,
            0,
            largura_boss,
            22
        )


        self.lbl_vida_player.config(
            text=f"{self.vida_jogador} / 100"
        )


        self.lbl_vida_boss.config(
            text=f"{self.vida_boss} / 100"
        )


        self.lbl_score.config(
            text=f"SCORE: {self.pontos}"
        )


    # ========================================================
    # GAME OVER
    # ========================================================

    def game_over(self):

        self.limpar_janela()


        frame = tk.Frame(
            self.root,
            bg=COLOR_BG
        )

        frame.pack(
            fill="both",
            expand=True
        )


        tk.Label(
            frame,
            text="☠️",
            font=("Segoe UI", 60),
            fg=COLOR_RED_BRIGHT,
            bg=COLOR_BG
        ).pack(
            pady=(60, 10)
        )


        tk.Label(
            frame,
            text="GAME OVER",
            font=("Consolas", 38, "bold"),
            fg=COLOR_RED_BRIGHT,
            bg=COLOR_BG
        ).pack()


        tk.Label(
            frame,
            text="O SISTEMA FOI COMPROMETIDO",
            font=("Consolas", 14, "bold"),
            fg=COLOR_RED,
            bg=COLOR_BG
        ).pack(
            pady=15
        )


        tk.Label(
            frame,
            text=(
                "O operador não conseguiu conter a ameaça.\n\n"
                "O protocolo de segurança falhou."
            ),
            font=("Segoe UI", 12),
            fg=COLOR_TEXT,
            bg=COLOR_BG,
            justify="center"
        ).pack(
            pady=15
        )


        tk.Label(
            frame,
            text=f"SCORE FINAL: {self.pontos}",
            font=("Consolas", 13, "bold"),
            fg=COLOR_YELLOW,
            bg=COLOR_BG
        ).pack(
            pady=15
        )


        tk.Button(
            frame,
            text="SAIR",
            font=("Consolas", 12, "bold"),
            bg=COLOR_RED_DARK,
            fg="white",
            relief="flat",
            padx=40,
            pady=10,
            command=self.root.destroy
        ).pack(
            pady=20
        )


    # ========================================================
    # VITÓRIA
    # ========================================================

    def vitoria(self):

        self.limpar_janela()


        frame = tk.Frame(
            self.root,
            bg=COLOR_BG
        )

        frame.pack(
            fill="both",
            expand=True
        )


        # ----------------------------------------------------
        # EFEITO DE VITÓRIA
        # ----------------------------------------------------

        tk.Label(
            frame,
            text="🏆",
            font=("Segoe UI", 70),
            fg=COLOR_YELLOW,
            bg=COLOR_BG
        ).pack(
            pady=(45, 5)
        )


        tk.Label(
            frame,
            text="PARABÉNS!",
            font=("Consolas", 40, "bold"),
            fg=COLOR_GREEN,
            bg=COLOR_BG
        ).pack()


        tk.Label(
            frame,
            text="VOCÊ DERROTOU O BOSS",
            font=("Consolas", 18, "bold"),
            fg=COLOR_CYAN,
            bg=COLOR_BG
        ).pack(
            pady=12
        )


        tk.Label(
            frame,
            text=(
                "A ameaça foi contida.\n\n"
                "Você conseguiu atravessar todas as camadas "
                "de defesa e proteger o sistema.\n\n"
                "O protocolo CyberShield foi concluído."
            ),
            font=("Segoe UI", 13),
            fg=COLOR_TEXT,
            bg=COLOR_BG,
            justify="center"
        ).pack(
            pady=15
        )


        # ----------------------------------------------------
        # RESULTADO
        # ----------------------------------------------------

        resultado = tk.Frame(
            frame,
            bg=COLOR_CARD
        )

        resultado.pack(
            padx=80,
            pady=15,
            fill="x"
        )


        tk.Label(
            resultado,
            text="☑ AMEAÇA CONTIDA",
            font=("Consolas", 12, "bold"),
            fg=COLOR_GREEN,
            bg=COLOR_CARD
        ).pack(
            pady=(15, 5)
        )


        tk.Label(
            resultado,
            text="☑ SISTEMA PROTEGIDO",
            font=("Consolas", 12, "bold"),
            fg=COLOR_GREEN,
            bg=COLOR_CARD
        ).pack(
            pady=5
        )


        tk.Label(
            resultado,
            text="☑ BOSS DERROTADO",
            font=("Consolas", 12, "bold"),
            fg=COLOR_GREEN,
            bg=COLOR_CARD
        ).pack(
            pady=5
        )


        tk.Label(
            resultado,
            text=f"SCORE FINAL: {self.pontos}",
            font=("Consolas", 14, "bold"),
            fg=COLOR_YELLOW,
            bg=COLOR_CARD
        ).pack(
            pady=(10, 15)
        )


        tk.Button(
            frame,
            text="🏆 FINALIZAR JOGO",
            font=("Consolas", 13, "bold"),
            bg=COLOR_RED_DARK,
            fg="white",
            activebackground=COLOR_RED_BRIGHT,
            activeforeground="white",
            relief="flat",
            cursor="hand2",
            padx=35,
            pady=12,
            command=self.root.destroy
        ).pack(
            pady=15
        )


# ============================================================
# EXECUÇÃO
# ============================================================

if __name__ == "__main__":

    root = tk.Tk()

    app = BossFightApp(root)

    root.mainloop()
