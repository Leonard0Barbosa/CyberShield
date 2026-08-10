#Fase 5 — Redes de Computadores

'''Pergunta: Qual serviço é responsável por traduzir nomes de domínio (ex: site.com) para endereços IP?

A) DHCP ❌

Por que está errada: O DHCP distribui automaticamente endereços IP para os dispositivos da rede.

💡 Dica: DHCP = Distribuição de IPs na rede local.

B) Firewall ❌

Por que está errada: O firewall filtra e controla o tráfego de rede com base em regras de segurança.

💡 Dica: Firewall = Controle e bloqueio de acessos.

C) DNS ✅

Por que está correta: O DNS funciona como a "agenda telefônica" da internet, traduzindo URLs legíveis em endereços IP.

D) HTTP ❌

Por que está errada: O HTTP é o protocolo de transferência para carregar páginas web.

💡 Dica: HTTP = Transporte de páginas web.'''
import time

# Estrutura de dados contendo o simulado de Redes de Computadores
questoes = [
    {
        "topico": "Modelo OSI",
        "pergunta": "Qual é a principal função da Camada de Rede (Camada 3) no modelo OSI?",
        "opcoes": {
            "A": "Transmissão de bits brutos pelo meio físico.",
            "B": "Estabelecimento, manutenção e encerramento de sessões entre aplicações.",
            "C": "Determinação do melhor caminho e roteamento de pacotes.",
            "D": "Formatação, criptografia e compressão de dados."
        },
        "correta": "C",
        "explicações": {
            "A": "Incorreta. Esta é a função da Camada Física (Camada 1), e não da Camada de Rede.",
            "B": "Incorreta. Esta é a responsabilidade da Camada de Sessão (Camada 5).",
            "C": "Correta! A Camada de Rede é responsável pelo roteamento e por determinar o melhor caminho para os dados alcançarem o destino.",
            "D": "Incorreta. Estas são as funções principais da Camada de Apresentação (Camada 6)."
        },
        "dica": "Pense em como os dados encontram o caminho através da internet global, de um roteador para outro."
    },
    {
        "topico": "Endereçamento IP",
        "pergunta": "Quantos bits compõem um endereço IPv4 padrão?",
        "opcoes": {
            "A": "32 bits",
            "B": "64 bits",
            "C": "128 bits",
            "D": "256 bits"
        },
        "correta": "A",
        "explicações": {
            "A": "Correta! O endereço IPv4 é formado por 32 bits, geralmente divididos em 4 octetos de 8 bits cada.",
            "B": "Incorreta. Os endereços IPv4 não utilizam 64 bits. Esse tamanho é mais comum em outras tecnologias de rede.",
            "C": "Incorreta. Este é o tamanho de um endereço IPv6, que foi criado para substituir o IPv4.",
            "D": "Incorreta. Não existem endereços IP com tamanho de 256 bits no padrão atual da internet."
        },
        "dica": "Lembre-se de que o IPv4 é representado por 4 números decimais separados por pontos (ex: 192.168.1.1)."
    },
    {
        "topico": "Protocolos de Transporte",
        "pergunta": "Qual dos seguintes protocolos pertence à camada de Transporte, é orientado à conexão e garante a entrega dos dados?",
        "opcoes": {
            "A": "UDP",
            "B": "IP",
            "C": "TCP",
            "D": "ICMP"
        },
        "correta": "C",
        "explicações": {
            "A": "Incorreta. O UDP é muito rápido, mas não é orientado à conexão e não garante a entrega dos pacotes.",
            "B": "Incorreta. O protocolo IP pertence à Camada de Rede, não à Camada de Transporte.",
            "C": "Correta! O TCP (Transmission Control Protocol) garante que os dados sejam entregues de forma confiável e em ordem.",
            "D": "Incorreta. O ICMP é utilizado para diagnósticos e controle de erros, como no caso do comando 'ping'."
        },
        "dica": "Pense em um protocolo que verifica se todos os pacotes chegaram e, se algum foi perdido, solicita o reenvio."
    },
    {
        "topico": "Protocolos de Aplicação",
        "pergunta": "Qual é a principal diferença entre os protocolos HTTP e HTTPS?",
        "opcoes": {
            "A": "O HTTP é usado apenas para arquivos de áudio, enquanto o HTTPS é para imagens.",
            "B": "O HTTPS utiliza criptografia, tornando a transmissão de dados mais segura.",
            "C": "O HTTPS é uma versão desatualizada e mais lenta do protocolo HTTP.",
            "D": "O HTTP permite acesso a redes privadas, e o HTTPS é exclusivo para a internet pública."
        },
        "correta": "B",
        "explicações": {
            "A": "Incorreta. Ambos são usados para transferir dados de páginas web, independentemente do tipo de mídia.",
            "B": "Correta! O HTTPS adiciona uma camada de segurança (SSL/TLS) ao HTTP, criptografando os dados trocados.",
            "C": "Incorreta. Pelo contrário, o HTTPS é a versão moderna e padrão de segurança atual.",
            "D": "Incorreta. Ambos podem ser utilizados tanto em redes locais quanto na internet pública."
        },
        "dica": "O 'S' no final do nome da sigla frequentemente remete à palavra em inglês para 'Segurança' (Security)."
    },
    {
        "topico": "Segurança de Rede",
        "pergunta": "Qual é o principal objetivo de um Firewall em uma rede de computadores?",
        "opcoes": {
            "A": "Fornecer e gerenciar automaticamente os endereços IP dos dispositivos.",
            "B": "Filtrar e controlar o tráfego de rede com base em regras de segurança.",
            "C": "Traduzir nomes de sites (URLs) em endereços IP legíveis.",
            "D": "Ampliar o alcance do sinal de Wi-Fi em grandes empresas."
        },
        "correta": "B",
        "explicações": {
            "A": "Incorreta. Esta é a principal função do protocolo DHCP.",
            "B": "Correta! O Firewall atua como uma barreira que monitora e filtra o tráfego de entrada e saída.",
            "C": "Incorreta. A tradução de nomes de domínio para endereços IP é a função do serviço DNS.",
            "D": "Incorreta. Equipamentos como repetidores ou Access Points são usados para ampliar o sinal de Wi-Fi."
        },
        "dica": "Imagine um guarda de segurança na porta de um evento. Ele verifica as credenciais de quem entra e sai."
    }
]

def executar_quiz():
    pontuacao = 0
    total_questoes = len(questoes)
    
    print("=" * 60)
    print("      SIMULADO INTERATIVO: FASE 5 — REDES DE COMPUTADORES      ")
    print("=" * 60)
    print("Digite a letra correspondente à opção (A, B, C ou D).")
    print("Digite 'DICA' se precisar de uma ajuda extra.\n")
    time.sleep(1)

    for i, q in enumerate(questoes, 1):
        print(f"\nQuestão {i}/{total_questoes} [Tópico: {q['topico']}]")
        print(f"-> {q['pergunta']}\n")
        
        for letra, texto in q['opcoes'].items():
            print(f"  {letra}) {texto}")
        print()

        encontrou_resposta = False
        usou_dica = False
        
        while not encontrou_resposta:
            resposta = input("Sua resposta: ").strip().upper()
            
            if resposta == "DICA":
                if not usou_dica:
                    print(f"💡 Dica: {q['dica']}\n")
                    usou_dica = True
                else:
                    print("Você já visualizou a dica para esta questão!\n")
                continue
                
            if resposta in ["A", "B", "C", "D"]:
                encontrou_resposta = True
                print("\n" + "-" * 40)
                
                # Exibe o feedback visual baseado no gabarito
                if resposta == q['correta']:
                    print(f"Opção {resposta} ✅")
                    print(f"Por que está correta: {q['explicações'][resposta]}")
                    pontuacao += 1
                else:
                    print(f"Opção {resposta} ❌ (Incorreta)")
                    print(f"Por que está errada: {q['explicações'][resposta]}")
                    print(f"\nA resposta correta era a alternativa {q['correta']}:")
                    print(f"-> {q['explicações'][q['correta']]}")
                
                print("-" * 40)
                time.sleep(1.5)
            else:
                print("Entrada inválida! Digite A, B, C, D ou DICA.")

    # Resultado Final
    print("\n" + "=" * 60)
    print("                      FIM DO SIMULADO                      ")
    print("=" * 60)
    porcentagem = (pontuacao / total_questoes) * 100
    print(f"Você acertou {pontuacao} de {total_questoes} questões ({porcentagem:.1f}%).")
    
    if porcentagem == 100:
        print("Excelente! Você dominou os conceitos de Redes da Fase 5! 🚀")
    elif porcentagem >= 70:
        print("Muito bom! Ótimo conhecimento técnico demonstrado. 👍")
    else:
        print("Vale a pena revisar os tópicos errados para fixar bem a matéria! 📚")
    print("=" * 60)

if __name__ == "__main__":
    executar_quiz()
