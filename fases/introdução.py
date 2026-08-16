import tkinter as tk


# ==============================================================================
# CYBERSHIELD — INTRODUÇÃO
# ACADEMIA DO HACKER ÉTICO
# ==============================================================================


# ==============================================================================
# CORES PRINCIPAIS
# ==============================================================================

BG_TOP = "#081A24"
BG_BOTTOM = "#06131B"

PANEL = "#0B2532"
PANEL_LIGHT = "#123847"

CYAN = "#00E5FF"
CYAN_DARK = "#008DA0"

GREEN = "#28C76F"
GREEN_DARK = "#16844A"

WHITE = "#FFFFFF"
TEXT = "#D8EDF2"
TEXT_DARK = "#8FB6C2"

YELLOW = "#FFD166"

GRID = "#0D2B38"
GRID_LIGHT = "#123A49"

RED = "#6B2020"
RED_HOVER = "#9B2E2E"


# ==============================================================================
# CORES DAS FASES
# ==============================================================================

CORES_FASES = {

    "FASE 1": {
        "normal": "#4FAF7A",
        "hover": "#65C98F"
    },

    "FASE 2": {
        "normal": "#4BAFAF",
        "hover": "#63CACA"
    },

    "FASE 3": {
        "normal": "#579AC7",
        "hover": "#70B2DE"
    },

    "FASE 4": {
        "normal": "#607FC4",
        "hover": "#7897DB"
    },

    "FASE 5": {
        "normal": "#756FC0",
        "hover": "#8B85D7"
    },

    "FASE 6": {
        "normal": "#8A69B5",
        "hover": "#A07CCB"
    },

    "FASE 7": {
        "normal": "#A46D9E",
        "hover": "#BB82B5"
    },

    "FASE 8": {
        "normal": "#B66F83",
        "hover": "#CC8498"
    },

    "FASE 9": {
        "normal": "#B96D65",
        "hover": "#D18178"
    },

    "FASE 10": {
        "normal": "#A94F55",
        "hover": "#C5666C"
    }
}


# ==============================================================================
# DICIONÁRIO
# ==============================================================================

DICIONARIO = {

    "FASE 1": {
        "titulo": "FASE 1 — FUNDAMENTOS DA CIBERSEGURANÇA",
        "icone": "🛡️",
        "texto": """
CIBERSEGURANÇA

Cibersegurança é o conjunto de práticas utilizadas
para proteger computadores, redes, sistemas e dados
contra acessos indevidos, ataques e outros riscos.

Os três princípios fundamentais da segurança da informação
são conhecidos como Tríade CIA:

• CONFIDENCIALIDADE
Somente pessoas autorizadas devem acessar determinadas
informações.

• INTEGRIDADE
Os dados devem permanecer corretos e não serem alterados
sem autorização.

• DISPONIBILIDADE
Sistemas e informações devem estar disponíveis quando
necessários.

Exemplo:

Uma conta bancária precisa manter os dados protegidos,
impedir alterações indevidas e continuar disponível
para o usuário.

CONCEITO IMPORTANTE:

Segurança não depende de uma única ferramenta.
Ela utiliza várias camadas de proteção.
"""
    },

    "FASE 2": {
        "titulo": "FASE 2 — REDES E COMUNICAÇÃO",
        "icone": "🌐",
        "texto": """
REDES DE COMPUTADORES

Uma rede permite que dispositivos troquem informações.

Alguns conceitos importantes:

• IP
Identifica um dispositivo dentro de uma rede.

• DNS
Converte nomes de domínio, como exemplo.com,
em endereços IP.

• DHCP
Pode fornecer automaticamente configurações de rede,
como endereço IP.

• ROTEADOR
Encaminha dados entre diferentes redes.

• FIREWALL
Controla determinados tipos de tráfego de rede
de acordo com regras configuradas.

POR QUE REDES SÃO IMPORTANTES?

Grande parte dos ataques ocorre através de sistemas
conectados. Por isso, compreender como uma rede funciona
é fundamental para entender como protegê-la.
"""
    },

    "FASE 3": {
        "titulo": "FASE 3 — AMEAÇAS E ATAQUES",
        "icone": "⚠️",
        "texto": """
AMEAÇAS DIGITAIS

Existem diversos tipos de ameaças no ambiente digital.

MALWARE
Software criado para realizar ações prejudiciais
ou indesejadas.

PHISHING
Tentativa de enganar uma pessoa para obter informações
ou fazê-la realizar uma ação insegura.

RANSOMWARE
Tipo de malware que pode bloquear o acesso aos dados
e exigir alguma forma de pagamento.

ENGENHARIA SOCIAL
Utilização de manipulação psicológica para induzir
uma pessoa a revelar informações ou realizar ações.

BOA PRÁTICA:

Antes de clicar em um link ou abrir um arquivo,
verifique sua origem e desconfie de mensagens inesperadas.
"""
    },

    "FASE 4": {
        "titulo": "FASE 4 — AUTENTICAÇÃO E SENHAS",
        "icone": "🔑",
        "texto": """
AUTENTICAÇÃO

Autenticação é o processo utilizado para verificar
a identidade de uma pessoa ou sistema.

SENHAS

Uma senha segura deve ser difícil de adivinhar
e não deve ser reutilizada em vários serviços.

MFA — AUTENTICAÇÃO MULTIFATOR

MFA adiciona outras formas de confirmação além da senha.

Exemplos:

• Senha
• Código temporário
• Aplicativo autenticador
• Chave de segurança

PRINCÍPIO:

Mesmo que uma senha seja descoberta, um segundo fator
pode impedir que a conta seja acessada.

NUNCA compartilhe suas credenciais com outras pessoas.
"""
    },

    "FASE 5": {
        "titulo": "FASE 5 — CONTROLE DE ACESSO",
        "icone": "🚪",
        "texto": """
CONTROLE DE ACESSO

Nem todo usuário deve possuir acesso a todos os recursos.

PRINCÍPIO DO MENOR PRIVILÉGIO

Cada usuário deve possuir somente as permissões
necessárias para realizar suas tarefas.

Exemplo:

Um funcionário responsável por relatórios pode precisar
ler determinados arquivos, mas não necessariamente
possuir permissão para modificar configurações críticas
do servidor.

CONTROLE DE ACESSO PODE ENVOLVER:

• Usuários
• Grupos
• Funções
• Permissões
• Recursos

Quanto menor o acesso desnecessário,
menor pode ser o impacto de uma conta comprometida.
"""
    },

    "FASE 6": {
        "titulo": "FASE 6 — CRIPTOGRAFIA",
        "icone": "🔐",
        "texto": """
CRIPTOGRAFIA

Criptografia utiliza técnicas matemáticas para proteger
informações.

HASH

Uma função hash transforma dados em um resumo de tamanho
fixo.

Ela pode ser utilizada para verificar integridade.

Exemplo:

SHA-256 gera um resumo hexadecimal de 256 bits.

CRIPTOGRAFIA SIMÉTRICA

Utiliza uma chave para cifrar e decifrar informações.

CRIPTOGRAFIA ASSIMÉTRICA

Utiliza um par de chaves:

• Chave pública
• Chave privada

ASSINATURA DIGITAL

Pode ser utilizada para verificar a autenticidade
e a integridade de uma mensagem.

CONCEITO:

Se o conteúdo de uma mensagem assinada for alterado,
a verificação da assinatura poderá detectar a alteração.
"""
    },

    "FASE 7": {
        "titulo": "FASE 7 — BANCO DE DADOS E ACESSO",
        "icone": "🗄️",
        "texto": """
BANCO DE DADOS E SEGURANÇA

Aplicações frequentemente armazenam informações
em bancos de dados.

Um dos riscos conhecidos é a SQL Injection.

SQL INJECTION

Pode ocorrer quando uma aplicação utiliza entradas
fornecidas pelo usuário de maneira insegura
na construção de consultas SQL.

COMO REDUZIR O RISCO?

Uma prática importante é utilizar consultas
parametrizadas / Prepared Statements.

Além disso, aplicações devem validar entradas,
utilizar permissões adequadas e seguir princípios
de desenvolvimento seguro.

ABAC

Attribute-Based Access Control utiliza atributos
para tomar decisões de autorização.

Exemplos de atributos:

• Cargo
• Horário
• Local
• Recurso solicitado

SEGURANÇA DE BANCO DE DADOS ENVOLVE:

Proteção dos dados, controle de acesso,
validação das entradas e monitoramento.
"""
    },

    "FASE 8": {
        "titulo": "FASE 8 — DESENVOLVIMENTO SEGURO",
        "icone": "🛠️",
        "texto": """
DESENVOLVIMENTO SEGURO

Um sistema seguro deve ser pensado como seguro
desde sua criação.

VALIDAÇÃO DE ENTRADAS

Dados enviados pelos usuários não devem ser
considerados automaticamente confiáveis.

A aplicação deve verificar se os dados possuem
o formato e os valores esperados.

EXEMPLO:

Se um campo espera uma idade, o sistema pode verificar
se o valor realmente corresponde a um número válido.

OUTRAS BOAS PRÁTICAS:

• Validar entradas
• Utilizar consultas parametrizadas
• Controlar permissões
• Proteger informações sensíveis
• Manter dependências atualizadas
• Registrar eventos importantes
• Testar o sistema

SEGURANÇA NÃO DEVE SER ADICIONADA
SOMENTE NO FINAL DO PROJETO.
"""
    },

    "FASE 9": {
        "titulo": "FASE 9 — RESPOSTA A INCIDENTES",
        "icone": "🚨",
        "texto": """
RESPOSTA A INCIDENTES

Um incidente de segurança precisa ser tratado
de maneira organizada.

ETAPAS IMPORTANTES:

1. IDENTIFICAÇÃO
Descobrir que existe uma atividade suspeita.

2. ANÁLISE
Investigar o que aconteceu e qual pode ser o impacto.

3. CONTENÇÃO
Reduzir a propagação ou impacto do incidente.

4. ERRADICAÇÃO
Remover a causa ou ameaça identificada.

5. RECUPERAÇÃO
Restaurar os serviços de maneira segura.

6. APRENDIZADO
Analisar o incidente para melhorar a segurança futura.

EXEMPLO:

Se uma máquina corporativa apresentar sinais de infecção,
pode ser necessário isolá-la da rede e iniciar uma análise.

IMPORTANTE:

Não se deve simplesmente apagar evidências
sem antes compreender o incidente.
"""
    },

    "FASE 10": {
        "titulo": "FASE 10 — BOSS FINAL",
        "icone": "☠️",
        "texto": """
BOSS FINAL — OPERAÇÃO CYBERSHIELD

Nesta etapa, você deverá utilizar os conhecimentos
adquiridos durante toda a Academia.

O desafio pode envolver:

• Contas comprometidas
• Phishing
• Malware
• Ransomware
• SQL Injection
• Firewall
• MFA
• Logs
• Controle de acesso
• Desenvolvimento seguro
• Resposta a incidentes

A ideia não é simplesmente decorar respostas.

Um profissional de segurança precisa analisar
uma situação, identificar riscos e escolher
uma ação adequada.

MISSÃO:

PROTEGER O CYBERSHIELD.

Use tudo o que aprendeu nas fases anteriores
para enfrentar a ameaça final.
"""
    }
}


# ==============================================================================
# CLASSE PRINCIPAL
# ==============================================================================

class Introducao:

    def __init__(self, root, proxima_fase):

        # ----------------------------------------------------------------------
        # RECEBE A MESMA JANELA DO MAIN
        # ----------------------------------------------------------------------

        self.root = root
        self.proxima_fase = proxima_fase

        self.fullscreen = False
        self.dicionario_aberto = False

        self.root.title(
            "CyberShield — Introdução"
        )

        self.root.geometry(
            "1000x700"
        )

        self.root.minsize(
            800,
            600
        )

        self.root.configure(
            bg=BG_TOP
        )

        # ----------------------------------------------------------------------
        # ATALHOS
        # ----------------------------------------------------------------------

        self.root.bind(
            "<F11>",
            self.toggle_fullscreen
        )

        self.root.bind(
            "<Escape>",
            self.exit_fullscreen
        )

        # ----------------------------------------------------------------------
        # SCROLL GLOBAL
        # ----------------------------------------------------------------------

        self.root.bind_all(
            "<MouseWheel>",
            self.controlar_scroll,
            add="+"
        )

        self.criar_interface()


    # ==========================================================================
    # TELA CHEIA
    # ==========================================================================

    def toggle_fullscreen(self, event=None):

        self.fullscreen = not self.fullscreen

        self.root.attributes(
            "-fullscreen",
            self.fullscreen
        )


    def exit_fullscreen(self, event=None):

        if self.fullscreen:

            self.fullscreen = False

            self.root.attributes(
                "-fullscreen",
                False
            )


    # ==========================================================================
    # INTERFACE
    # ==========================================================================

    def criar_interface(self):

        self.canvas = tk.Canvas(
            self.root,
            bg=BG_TOP,
            highlightthickness=0
        )

        self.canvas.pack(
            fill="both",
            expand=True
        )

        self.scrollbar = tk.Scrollbar(
            self.root,
            orient="vertical",
            command=self.canvas.yview
        )

        self.scrollbar.pack(
            side="right",
            fill="y"
        )

        self.canvas.configure(
            yscrollcommand=self.scrollbar.set
        )

        self.mundo = tk.Frame(
            self.canvas,
            bg=BG_TOP
        )

        self.canvas_window = self.canvas.create_window(
            0,
            0,
            window=self.mundo,
            anchor="nw"
        )

        self.mundo.bind(
            "<Configure>",
            self.atualizar_scroll
        )

        self.canvas.bind(
            "<Configure>",
            self.ajustar_largura
        )

        self.criar_cenario()

        self.criar_conteudo()


    # ==========================================================================
    # CONTROLE DO SCROLL
    # ==========================================================================

    def controlar_scroll(self, event):

        if self.dicionario_aberto:

            if hasattr(self, "dict_canvas"):

                self.dict_canvas.yview_scroll(
                    int(-1 * (event.delta / 120)),
                    "units"
                )

            return

        if hasattr(self, "canvas"):

            self.canvas.yview_scroll(
                int(-1 * (event.delta / 120)),
                "units"
            )


    def atualizar_scroll(self, event=None):

        self.canvas.configure(
            scrollregion=self.canvas.bbox("all")
        )


    def ajustar_largura(self, event):

        self.canvas.itemconfig(
            self.canvas_window,
            width=event.width
        )


    # ==========================================================================
    # CENÁRIO MINIMALISTA CYBERSECURITY
    # ==========================================================================

    def criar_cenario(self):

        self.cenario = tk.Canvas(
            self.mundo,
            height=330,
            bg=BG_TOP,
            highlightthickness=0
        )

        self.cenario.pack(
            fill="x"
        )

        self.cenario.bind(
            "<Configure>",
            self.desenhar_cenario
        )


    def desenhar_cenario(self, event=None):

        canvas = self.cenario

        width = canvas.winfo_width()

        if width < 10:
            return

        canvas.delete("all")

        height = 330

        # ----------------------------------------------------------------------
        # FUNDO
        # ----------------------------------------------------------------------

        canvas.create_rectangle(
            0,
            0,
            width,
            height,
            fill=BG_TOP,
            outline=""
        )

        # ----------------------------------------------------------------------
        # GRID
        # ----------------------------------------------------------------------

        espacamento = 35

        for x in range(0, width, espacamento):

            canvas.create_line(
                x,
                0,
                x,
                height,
                fill=GRID,
                width=1
            )

        for y in range(0, height, espacamento):

            canvas.create_line(
                0,
                y,
                width,
                y,
                fill=GRID,
                width=1
            )

        # ----------------------------------------------------------------------
        # CIRCUITOS
        # ----------------------------------------------------------------------

        linhas = [
            (80, 55, 220, 55, 220, 95),
            (width - 80, 70, width - 220, 70, width - 220, 115),
            (100, 235, 260, 235, 260, 200),
            (width - 100, 220, width - 270, 220, width - 270, 180),
        ]

        for pontos in linhas:

            canvas.create_line(
                *pontos,
                fill=CYAN_DARK,
                width=2
            )

        # ----------------------------------------------------------------------
        # NÓS
        # ----------------------------------------------------------------------

        pontos = [
            (80, 55),
            (220, 95),
            (width - 80, 70),
            (width - 220, 115),
            (100, 235),
            (260, 200),
            (width - 100, 220),
            (width - 270, 180),
        ]

        for x, y in pontos:

            canvas.create_oval(
                x - 4,
                y - 4,
                x + 4,
                y + 4,
                fill=CYAN,
                outline=""
            )

        # ----------------------------------------------------------------------
        # ESCUDO CENTRAL
        # ----------------------------------------------------------------------

        centro_x = width // 2
        centro_y = 150

        canvas.create_polygon(
            centro_x,
            centro_y - 92,
            centro_x + 70,
            centro_y - 62,
            centro_x + 60,
            centro_y + 35,
            centro_x,
            centro_y + 85,
            centro_x - 60,
            centro_y + 35,
            centro_x - 70,
            centro_y - 62,
            fill=PANEL_LIGHT,
            outline=CYAN_DARK,
            width=2
        )

        canvas.create_polygon(
            centro_x,
            centro_y - 70,
            centro_x + 52,
            centro_y - 48,
            centro_x + 44,
            centro_y + 28,
            centro_x,
            centro_y + 63,
            centro_x - 44,
            centro_y + 28,
            centro_x - 52,
            centro_y - 48,
            fill=PANEL,
            outline=CYAN,
            width=2
        )

        # ----------------------------------------------------------------------
        # CADEADO
        # ----------------------------------------------------------------------

        canvas.create_arc(
            centro_x - 20,
            centro_y - 30,
            centro_x + 20,
            centro_y + 18,
            start=0,
            extent=180,
            style="arc",
            outline=CYAN,
            width=5
        )

        canvas.create_rectangle(
            centro_x - 23,
            centro_y - 5,
            centro_x + 23,
            centro_y + 30,
            fill=CYAN_DARK,
            outline=CYAN,
            width=2
        )

        canvas.create_oval(
            centro_x - 4,
            centro_y + 5,
            centro_x + 4,
            centro_y + 13,
            fill=WHITE,
            outline=""
        )

        canvas.create_line(
            centro_x,
            centro_y + 12,
            centro_x,
            centro_y + 20,
            fill=WHITE,
            width=2
        )

        # ----------------------------------------------------------------------
        # TÍTULO
        # ----------------------------------------------------------------------

        canvas.create_text(
            centro_x,
            285,
            text="CYBERSHIELD",
            font=("Consolas", 27, "bold"),
            fill=WHITE
        )

        canvas.create_text(
            centro_x,
            310,
            text="ACADEMIA DO HACKER ÉTICO",
            font=("Consolas", 10, "bold"),
            fill=TEXT_DARK
        )


    # ==========================================================================
    # CONTEÚDO
    # ==========================================================================

    def criar_conteudo(self):

        titulo_frame = tk.Frame(
            self.mundo,
            bg=BG_TOP
        )

        titulo_frame.pack(
            fill="x",
            pady=(20, 5)
        )

        tk.Label(
            titulo_frame,
            text="AMBIENTE DE TREINAMENTO",
            font=("Consolas", 18, "bold"),
            fg=CYAN,
            bg=BG_TOP
        ).pack()

        tk.Label(
            titulo_frame,
            text="Aprenda os fundamentos necessários para proteger sistemas digitais.",
            font=("Segoe UI", 10),
            fg=TEXT,
            bg=BG_TOP
        ).pack(
            pady=8
        )

        # ----------------------------------------------------------------------
        # BOTÃO INICIAR
        # ----------------------------------------------------------------------

        self.btn_iniciar = tk.Button(
            titulo_frame,
            text="▶  INICIAR ACADEMIA — FASE 1",
            font=("Consolas", 12, "bold"),
            fg=WHITE,
            bg=GREEN_DARK,
            activeforeground=WHITE,
            activebackground=GREEN,
            relief="flat",
            cursor="hand2",
            padx=30,
            pady=12,
            command=self.iniciar_fase_1
        )

        self.btn_iniciar.pack(
            pady=(10, 5)
        )

        # ----------------------------------------------------------------------
        # TELA CHEIA
        # ----------------------------------------------------------------------

        tk.Button(
            titulo_frame,
            text="⛶  TELA CHEIA (F11)",
            font=("Consolas", 9, "bold"),
            fg=WHITE,
            bg=PANEL,
            activeforeground=WHITE,
            activebackground=PANEL_LIGHT,
            relief="flat",
            cursor="hand2",
            padx=20,
            pady=7,
            command=self.toggle_fullscreen
        ).pack(
            pady=5
        )

        # ----------------------------------------------------------------------
        # MAPA
        # ----------------------------------------------------------------------

        self.criar_mapa_fases()


    # ==========================================================================
    # MAPA DAS FASES
    # ==========================================================================

    def criar_mapa_fases(self):

        tk.Label(
            self.mundo,
            text="▣  MAPA DO CONHECIMENTO",
            font=("Consolas", 18, "bold"),
            fg=CYAN,
            bg=BG_TOP
        ).pack(
            pady=(35, 5)
        )

        tk.Label(
            self.mundo,
            text="Selecione uma fase para consultar o Dicionário CyberShield.",
            font=("Segoe UI", 10),
            fg=TEXT_DARK,
            bg=BG_TOP
        ).pack(
            pady=(0, 20)
        )

        self.mapa_frame = tk.Frame(
            self.mundo,
            bg=BG_TOP
        )

        self.mapa_frame.pack(
            fill="x",
            padx=35,
            pady=10
        )

        fases = list(DICIONARIO.keys())

        for i, fase in enumerate(fases):

            linha = i // 2
            coluna = i % 2

            self.criar_botao_fase(
                fase,
                linha,
                coluna
            )

        # ----------------------------------------------------------------------
        # FINAL
        # ----------------------------------------------------------------------

        tk.Label(
            self.mundo,
            text="────────────────────────────────────────",
            font=("Consolas", 10),
            fg=CYAN_DARK,
            bg=BG_TOP
        ).pack(
            pady=(35, 10)
        )

        tk.Label(
            self.mundo,
            text="🛡  CONHECIMENTO É A PRIMEIRA LINHA DE DEFESA.",
            font=("Consolas", 11, "bold"),
            fg=TEXT,
            bg=BG_TOP
        ).pack(
            pady=(0, 40)
        )


    # ==========================================================================
    # BOTÃO DE FASE
    # ==========================================================================

    def criar_botao_fase(
        self,
        fase,
        linha,
        coluna
    ):

        dados = DICIONARIO[fase]
        cores = CORES_FASES[fase]

        frame = tk.Frame(
            self.mapa_frame,
            bg=BG_TOP
        )

        frame.grid(
            row=linha,
            column=coluna,
            padx=12,
            pady=12,
            sticky="nsew"
        )

        self.mapa_frame.grid_columnconfigure(
            coluna,
            weight=1
        )

        botao = tk.Button(
            frame,
            text=(
                f"{dados['icone']}  {fase}\n"
                f"{dados['titulo'].split('—', 1)[-1].strip()}"
            ),
            font=("Consolas", 10, "bold"),
            fg=WHITE,
            bg=cores["normal"],
            activeforeground=WHITE,
            activebackground=cores["hover"],
            relief="flat",
            cursor="hand2",
            wraplength=360,
            justify="center",
            padx=15,
            pady=13,
            command=lambda f=fase: self.abrir_dicionario(f)
        )

        botao.pack(
            fill="both",
            expand=True
        )

        botao.bind(
            "<Enter>",
            lambda event, b=botao, c=cores:
            self.hover_entrar(
                b,
                c["hover"]
            )
        )

        botao.bind(
            "<Leave>",
            lambda event, b=botao, c=cores:
            self.hover_sair(
                b,
                c["normal"]
            )
        )


    # ==========================================================================
    # HOVER
    # ==========================================================================

    def hover_entrar(self, botao, cor):

        botao.config(
            bg=cor
        )


    def hover_sair(self, botao, cor):

        botao.config(
            bg=cor
        )


    # ==========================================================================
    # ABRIR DICIONÁRIO
    # ==========================================================================

    def abrir_dicionario(self, fase):

        if self.dicionario_aberto:
            return

        self.dicionario_aberto = True

        dados = DICIONARIO[fase]

        self.overlay = tk.Frame(
            self.root,
            bg="#061E29"
        )

        self.overlay.place(
            relx=0,
            rely=0,
            relwidth=1,
            relheight=1
        )

        # ----------------------------------------------------------------------
        # CABEÇALHO
        # ----------------------------------------------------------------------

        header = tk.Frame(
            self.overlay,
            bg=PANEL,
            height=70
        )

        header.pack(
            fill="x"
        )

        tk.Label(
            header,
            text=f"{dados['icone']}  {dados['titulo']}",
            font=("Consolas", 14, "bold"),
            fg=CYAN,
            bg=PANEL
        ).pack(
            side="left",
            padx=25,
            pady=20
        )

        tk.Button(
            header,
            text="✕ FECHAR",
            font=("Consolas", 9, "bold"),
            fg=WHITE,
            bg=RED,
            activeforeground=WHITE,
            activebackground=RED_HOVER,
            relief="flat",
            cursor="hand2",
            padx=15,
            pady=7,
            command=self.fechar_dicionario
        ).pack(
            side="right",
            padx=20
        )

        # ----------------------------------------------------------------------
        # ÁREA DO DICIONÁRIO
        # ----------------------------------------------------------------------

        area = tk.Frame(
            self.overlay,
            bg="#061E29"
        )

        area.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=20
        )

        self.dict_canvas = tk.Canvas(
            area,
            bg="#061E29",
            highlightthickness=0
        )

        self.dict_scroll = tk.Scrollbar(
            area,
            orient="vertical",
            command=self.dict_canvas.yview
        )

        self.dict_canvas.pack(
            side="left",
            fill="both",
            expand=True
        )

        self.dict_scroll.pack(
            side="right",
            fill="y"
        )

        self.dict_canvas.configure(
            yscrollcommand=self.dict_scroll.set
        )

        conteudo = tk.Frame(
            self.dict_canvas,
            bg="#061E29"
        )

        self.dict_window = self.dict_canvas.create_window(
            0,
            0,
            window=conteudo,
            anchor="nw"
        )

        conteudo.bind(
            "<Configure>",
            lambda event:
            self.dict_canvas.configure(
                scrollregion=self.dict_canvas.bbox("all")
            )
        )

        self.dict_canvas.bind(
            "<Configure>",
            lambda event:
            self.dict_canvas.itemconfig(
                self.dict_window,
                width=event.width
            )
        )

        # ----------------------------------------------------------------------
        # TEXTO
        # ----------------------------------------------------------------------

        texto = dados["texto"].strip()

        tk.Label(
            conteudo,
            text=texto,
            font=("Segoe UI", 11),
            fg=WHITE,
            bg="#061E29",
            wraplength=850,
            justify="left",
            anchor="nw"
        ).pack(
            fill="x",
            padx=30,
            pady=30
        )

        # ----------------------------------------------------------------------
        # DICA
        # ----------------------------------------------------------------------

        dica = tk.Frame(
            conteudo,
            bg=PANEL
        )

        dica.pack(
            fill="x",
            padx=30,
            pady=(0, 30)
        )

        tk.Label(
            dica,
            text="💡 CONCEITO-CHAVE",
            font=("Consolas", 10, "bold"),
            fg=YELLOW,
            bg=PANEL
        ).pack(
            anchor="w",
            padx=20,
            pady=(15, 5)
        )

        tk.Label(
            dica,
            text=(
                "Não tente apenas decorar os termos. "
                "Durante as fases, você deverá reconhecer "
                "quando e por que cada conceito é utilizado."
            ),
            font=("Segoe UI", 10),
            fg=WHITE,
            bg=PANEL,
            wraplength=800,
            justify="left"
        ).pack(
            anchor="w",
            padx=20,
            pady=(0, 15)
        )

        self.dict_canvas.focus_set()


    # ==========================================================================
    # FECHAR DICIONÁRIO
    # ==========================================================================

    def fechar_dicionario(self):

        if not self.dicionario_aberto:
            return

        self.dicionario_aberto = False

        if hasattr(self, "overlay"):

            self.overlay.destroy()

        self.canvas.focus_set()


    # ==========================================================================
    # INICIAR FASE 1
    # ==========================================================================

    def iniciar_fase_1(self):

        # ----------------------------------------------------------------------
        # Fecha o dicionário caso esteja aberto.
        # ----------------------------------------------------------------------

        if self.dicionario_aberto:

            self.fechar_dicionario()

        # ----------------------------------------------------------------------
        # Evita múltiplos cliques.
        # ----------------------------------------------------------------------

        if hasattr(self, "btn_iniciar"):

            self.btn_iniciar.config(
                state="disabled"
            )

        # ----------------------------------------------------------------------
        # IMPORTANTE:
        #
        # A INTRODUÇÃO NÃO CRIA tk.Tk()
        # A INTRODUÇÃO NÃO USA root.destroy()
        #
        # Ela apenas informa ao MAIN que terminou.
        #
        # O MAIN será responsável por:
        #
        # 1. Limpar a introdução.
        # 2. Iniciar a Fase 1.
        #
        # ----------------------------------------------------------------------

        self.proxima_fase()


# ==============================================================================
# FUNÇÃO USADA PELO MAIN
# ==============================================================================

def executar(root, proxima_fase):

    """
    Função chamada pelo main.py.

    Recebe:

        root
            Janela principal criada pelo main.

        proxima_fase
            Função que será chamada quando a introdução terminar.

    A introdução utiliza a mesma janela do jogo.
    """

    Introducao(
        root,
        proxima_fase
    )


# ==============================================================================
# EXECUÇÃO INDIVIDUAL
#
# Serve somente para testar a introdução separadamente.
# Não é utilizado pelo main.py.
# ==============================================================================

if __name__ == "__main__":

    root = tk.Tk()

    def teste():

        print(
            "Introdução concluída!"
        )

    executar(
        root,
        teste
    )

    root.mainloop() 