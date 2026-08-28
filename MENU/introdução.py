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

Cibersegurança é a área responsável por proteger computadores, redes, sistemas, aplicações e dados contra ataques digitais, acessos não autorizados, alterações indevidas, interrupções e outros riscos.

A TRÍADE CIA

A Tríade CIA representa três princípios fundamentais da segurança da informação.

CONFIDENCIALIDADE

A confidencialidade garante que uma informação seja acessada somente por pessoas autorizadas. Uma senha, por exemplo, ajuda a impedir que outras pessoas entrem em uma conta. A criptografia também protege a confidencialidade ao transformar os dados em um formato que não pode ser facilmente compreendido sem a chave adequada.

Exemplo: o saldo de uma conta bancária deve ser acessível apenas ao cliente e às pessoas autorizadas pelo banco.

INTEGRIDADE

A integridade garante que os dados permaneçam corretos, completos e confiáveis. Uma informação não deve ser modificada, apagada ou corrompida sem autorização.

Funções de hash podem ser utilizadas para verificar se um arquivo foi alterado. O hash funciona como uma espécie de impressão digital dos dados. Se o conteúdo mudar, o resultado do hash também poderá mudar.

Exemplo: se uma transferência bancária for registrada como cinquenta reais, o sistema deve impedir que o valor seja alterado indevidamente para quinhentos reais.

DISPONIBILIDADE

A disponibilidade garante que sistemas, serviços e informações estejam acessíveis quando forem necessários.

Para aumentar a disponibilidade, organizações podem utilizar backups, servidores redundantes, fontes alternativas de energia, monitoramento e mecanismos de proteção contra ataques que tentam deixar serviços indisponíveis.

Exemplo: um sistema bancário precisa continuar funcionando quando um cliente precisa realizar uma operação.

AMEAÇAS DIGITAIS

Malware é o termo utilizado para programas maliciosos desenvolvidos para causar danos, obter acesso indevido, roubar informações ou realizar outras ações não autorizadas.

VÍRUS

Um vírus é um tipo de malware que pode se associar a arquivos ou programas e se espalhar quando esses arquivos são executados ou compartilhados.

WORMS

Worms são programas maliciosos capazes de se espalhar automaticamente por redes e sistemas vulneráveis, sem depender necessariamente da ação direta do usuário.

PHISHING

Phishing é uma técnica de engenharia social que utiliza mensagens falsas para tentar enganar a vítima. O atacante pode se passar por uma empresa, banco, serviço ou pessoa conhecida.

O objetivo pode ser induzir a vítima a fornecer informações, acessar uma página falsa ou realizar alguma ação insegura.

RANSOMWARE

Ransomware é um tipo de malware que pode impedir o acesso aos dados da vítima, geralmente por meio de criptografia. Os criminosos podem exigir um pagamento para tentar devolver o acesso.

Uma das principais formas de reduzir o impacto desse tipo de ameaça é manter backups seguros e atualizados.

ENGENHARIA SOCIAL

Engenharia social consiste em explorar comportamentos e fatores humanos para conseguir informações ou induzir alguém a realizar determinada ação.

Um criminoso pode, por exemplo, fingir ser um funcionário de suporte técnico e tentar convencer uma pessoa a revelar informações de acesso.

BARREIRAS DE DEFESA

A segurança normalmente utiliza várias camadas de proteção. Isso significa que uma única ferramenta não deve ser considerada suficiente para proteger todo o sistema.

FIREWALL

O firewall controla determinados tipos de tráfego de rede com base em regras. Ele pode ajudar a bloquear conexões que não deveriam ser permitidas e controlar a comunicação entre redes ou dispositivos.

ANTIVÍRUS

O antivírus procura identificar, bloquear ou remover determinados tipos de software malicioso.

EDR

EDR significa Endpoint Detection and Response. É uma tecnologia utilizada para monitorar dispositivos, identificar comportamentos suspeitos e auxiliar na resposta a incidentes.

AUTENTICAÇÃO DE DOIS FATORES

A autenticação de dois fatores adiciona uma segunda etapa de verificação ao processo de login.

Por exemplo, além da senha, o usuário pode precisar confirmar sua identidade utilizando um aplicativo autenticador, código temporário ou outro método de autenticação.

Isso dificulta o acesso indevido mesmo quando uma senha é comprometida.

O FATOR HUMANO

As pessoas fazem parte da segurança de qualquer organização. Um sistema pode possuir firewall, antivírus e outras ferramentas, mas uma ação insegura ainda pode criar riscos.

Por isso, treinamento e conscientização são importantes para ensinar usuários a reconhecer mensagens suspeitas, proteger suas credenciais, utilizar senhas adequadas e seguir procedimentos de segurança.

CAMADAS DE SEGURANÇA

Uma estratégia de segurança eficiente utiliza diferentes mecanismos de proteção ao mesmo tempo.

Senhas protegem contas.

MFA adiciona outra camada de autenticação.

Firewalls controlam tráfego.

Antivírus e EDR monitoram dispositivos.

Criptografia protege informações.

Backups ajudam na recuperação de dados.

Monitoramento e logs ajudam a identificar atividades suspeitas.

RESUMO

Cibersegurança busca proteger sistemas e informações contra ameaças digitais. A Tríade CIA estabelece três objetivos fundamentais: manter as informações confidenciais, preservar sua integridade e garantir sua disponibilidade. Para alcançar esses objetivos, são utilizadas diferentes camadas de proteção, como autenticação, criptografia, firewalls, antivírus, EDR, backups e conscientização dos usuários.

DICA DA FASE

Quando uma questão falar sobre um dado que foi alterado, pense em Integridade.
Se falar sobre quem pode ver ou acessar uma informação, pense em Confidencialidade.
Se o problema for um sistema indisponível ou fora do ar, pense em Disponibilidade.

"""
    },

    "FASE 2": {
        "titulo": "FASE 2 — REDES E COMUNICAÇÃO",
        "icone": "🌐",
        "texto": """
REDES DE COMPUTADORES

Uma rede de computadores é um conjunto de dispositivos conectados para permitir a comunicação e o compartilhamento de informações e recursos.

Esses dispositivos podem incluir computadores, celulares, servidores, impressoras, roteadores, switches e outros equipamentos.

As redes são fundamentais para a internet, empresas, escolas, bancos, sistemas industriais e praticamente qualquer ambiente que utilize computadores conectados.

COMO FUNCIONA UMA REDE

Quando um dispositivo precisa enviar uma informação para outro, os dados são divididos em pequenas unidades chamadas pacotes.

Esses pacotes são enviados pela rede seguindo determinadas regras e protocolos.

O dispositivo de destino recebe os pacotes e utiliza as informações necessárias para reconstruir os dados enviados.

Exemplo:

Quando você acessa um site, seu computador envia solicitações pela rede até o servidor que hospeda aquele site. O servidor responde e os dados retornam para o seu dispositivo.

ENDEREÇO IP

O endereço IP é utilizado para identificar logicamente um dispositivo dentro de uma rede.

Um endereço IPv4 possui quatro grupos de números separados por pontos.

Exemplo:

192.168.1.10

Existem também endereços IPv6, criados principalmente para oferecer uma quantidade muito maior de endereços disponíveis.

Exemplo:

2001:db8::1

O endereço IP é importante porque permite que os dispositivos saibam para onde determinados dados devem ser enviados.

IP PÚBLICO E IP PRIVADO

Um IP privado é utilizado dentro de uma rede local e normalmente não é diretamente acessível pela internet.

Exemplos de faixas privadas incluem:

192.168.0.0/16
172.16.0.0/12
10.0.0.0/8

Um IP público é utilizado para identificar uma rede ou dispositivo em comunicação com a internet.

Em uma rede doméstica, vários dispositivos podem utilizar endereços IP privados e compartilhar uma conexão utilizando um endereço IP público.

ENDEREÇO MAC

O endereço MAC é um identificador associado à interface de rede de um dispositivo.

Ele é utilizado principalmente na comunicação dentro da rede local.

Enquanto o IP está relacionado ao endereçamento lógico e ao encaminhamento de dados entre redes, o endereço MAC é utilizado na comunicação da camada de enlace da rede local.

DNS

DNS significa Domain Name System.

Sua função principal é permitir que nomes de domínio sejam associados aos respectivos endereços IP.

As pessoas preferem utilizar nomes fáceis de lembrar, como exemplo.com, em vez de memorizar endereços IP.

Quando um usuário acessa um domínio, o sistema pode consultar um servidor DNS para descobrir qual endereço IP está associado àquele nome.

DHCP

DHCP significa Dynamic Host Configuration Protocol.

Ele permite que dispositivos recebam automaticamente configurações de rede.

Entre essas configurações podem estar:

Endereço IP
Máscara de rede
Gateway
Servidor DNS

Sem DHCP, muitas redes exigiriam que essas informações fossem configuradas manualmente em cada dispositivo.

ROTEADOR

O roteador é um equipamento responsável por encaminhar pacotes entre diferentes redes.

Em uma residência, por exemplo, o roteador pode conectar a rede local à internet.

Ele analisa informações presentes nos pacotes e utiliza sua tabela de roteamento para determinar por onde os dados devem seguir.

SWITCH

O switch conecta vários dispositivos dentro de uma rede local.

Ele pode receber dados de um dispositivo e encaminhá-los para o dispositivo correto dentro da rede.

É muito utilizado em empresas, laboratórios, escolas e outros ambientes que possuem vários equipamentos conectados.

MODEM

O modem é um equipamento utilizado para estabelecer a comunicação entre a rede do usuário e determinados tipos de infraestrutura fornecida pelo provedor de internet.

Em muitos ambientes domésticos, modem e roteador podem estar integrados no mesmo equipamento.

CLIENTE E SERVIDOR

Em uma arquitetura cliente-servidor, o cliente solicita algum serviço ou recurso e o servidor responde a essa solicitação.

Exemplo:

Quando você acessa um site, o navegador funciona como cliente e envia uma solicitação para o servidor que hospeda o site.

O servidor processa a solicitação e envia uma resposta.

PROTOCOLOS DE REDE

Protocolos são regras utilizadas para permitir que dispositivos diferentes consigam se comunicar.

Alguns protocolos importantes são:

TCP
UDP
IP
HTTP
HTTPS
DNS
DHCP
SSH

Cada protocolo possui funções específicas dentro da comunicação.

TCP

TCP significa Transmission Control Protocol.

Ele estabelece uma comunicação orientada à conexão e possui mecanismos para verificar a entrega dos dados.

É utilizado quando a confiabilidade da comunicação é importante.

UDP

UDP significa User Datagram Protocol.

Ele possui uma comunicação mais simples e não oferece os mesmos mecanismos de confiabilidade e controle de entrega do TCP.

Por isso, pode ser útil em situações nas quais velocidade e baixa latência são importantes.

PORTAS DE REDE

Portas ajudam a identificar serviços ou processos de comunicação em um dispositivo.

Uma mesma máquina pode executar vários serviços utilizando diferentes portas.

Alguns exemplos conhecidos:

HTTP utiliza tradicionalmente a porta 80.

HTTPS utiliza tradicionalmente a porta 443.

DNS utiliza tradicionalmente a porta 53.

SSH utiliza tradicionalmente a porta 22.

A existência de uma porta aberta não significa automaticamente que existe um ataque. Porém, serviços desnecessários ou mal configurados podem aumentar a superfície de ataque.

PACOTES DE DADOS

Os dados transmitidos por uma rede podem ser divididos em pacotes.

Cada pacote possui informações utilizadas para que a comunicação possa acontecer corretamente.

Essas informações podem incluir endereços de origem e destino e outros dados relacionados ao protocolo utilizado.

Os pacotes podem atravessar diferentes equipamentos até chegar ao destino.

LATÊNCIA

Latência representa o tempo necessário para que os dados percorram determinado caminho entre origem e destino.

Quanto maior a latência, maior pode ser o atraso percebido em uma comunicação.

Em jogos online, chamadas de vídeo e outras aplicações em tempo real, uma latência baixa geralmente é desejável.

LARGURA DE BANDA

Largura de banda representa a capacidade de transmissão de dados de uma conexão.

Uma conexão com maior largura de banda pode transportar uma quantidade maior de dados por unidade de tempo.

É importante não confundir largura de banda com latência.

Uma conexão pode possuir alta largura de banda e ainda apresentar latência elevada.

LAN E WAN

LAN significa Local Area Network.

É uma rede que cobre uma área relativamente pequena, como uma casa, escola ou empresa.

WAN significa Wide Area Network.

É utilizada para conectar redes que estão em áreas geográficas maiores.

A internet pode ser considerada um enorme conjunto de redes interconectadas.

INTERNET

A internet é uma rede mundial formada pela interconexão de diversas redes.

Ela permite que dispositivos e sistemas localizados em diferentes partes do mundo troquem informações utilizando protocolos padronizados.

SEGURANÇA DE REDES

As redes precisam ser protegidas contra acessos não autorizados, interceptação de informações, exploração de vulnerabilidades e outras ameaças.

Algumas medidas importantes incluem:

Utilizar firewalls.

Manter sistemas atualizados.

Utilizar criptografia.

Proteger redes Wi-Fi com configurações seguras.

Utilizar senhas fortes.

Desativar serviços desnecessários.

Monitorar atividades suspeitas.

Separar diferentes partes da rede quando necessário.

SEGMENTAÇÃO DE REDE

A segmentação divide uma rede em partes menores.

Isso pode ajudar a controlar o tráfego e limitar o impacto de determinados incidentes.

Por exemplo, uma empresa pode separar a rede dos funcionários da rede utilizada por visitantes.

Isso reduz a possibilidade de que um problema em uma parte da rede afete diretamente todas as outras.

REDE WI-FI

Wi-Fi permite que dispositivos se conectem a uma rede utilizando comunicação sem fio.

Uma rede Wi-Fi deve utilizar configurações de segurança adequadas e uma senha forte.

Também é importante manter o roteador atualizado e evitar configurações desnecessariamente expostas.

SUPERFÍCIE DE ATAQUE

A superfície de ataque representa os pontos que podem ser explorados para comprometer um sistema ou rede.

Serviços desnecessários, portas expostas, sistemas desatualizados e configurações inseguras podem aumentar essa superfície.

Reduzir serviços desnecessários e manter os sistemas atualizados são práticas importantes para diminuir riscos.

RESUMO

Redes de computadores permitem que dispositivos troquem informações e compartilhem recursos. Para que essa comunicação aconteça, são utilizados endereços, equipamentos e protocolos.

O IP identifica logicamente dispositivos e auxilia no encaminhamento dos dados.

O DNS relaciona nomes de domínio a endereços IP.

O DHCP fornece automaticamente configurações de rede.

O roteador encaminha dados entre redes.

O switch conecta dispositivos dentro de uma rede local.

TCP prioriza confiabilidade, enquanto UDP possui uma comunicação mais simples e pode ser utilizado quando baixa latência é importante.

HTTP e HTTPS são utilizados na comunicação web, sendo o HTTPS protegido por criptografia através do TLS.

A segurança de redes depende de várias medidas, como firewalls, criptografia, atualizações, senhas fortes, segmentação, monitoramento e configuração adequada dos dispositivos.

DICA DA FASE: 
    dica: Pense em quantas camadas de proteção existem. Uma senha sozinha depende de apenas um segredo.
    dica: Pense em uma ferramenta que permite usar senhas diferentes e difíceis sem precisar memorizar todas.
    dica: Pense no que acontece quando uma pessoa reutiliza a mesma senha em vários sites e um desses sites sofre um vazamento.
"""
    },

    "FASE 3": {
        "titulo": "FASE 3 — AMEAÇAS E ATAQUES",
        "icone": "⚠️",
        "texto": """
AMEAÇAS DIGITAIS

Ameaças digitais são riscos, ataques ou ações maliciosas que podem comprometer computadores, redes, sistemas, aplicações, contas e informações. Elas podem ter como objetivo roubar dados, obter acesso não autorizado, causar prejuízos, interromper serviços ou enganar usuários.

MALWARE

Malware é o termo utilizado para definir softwares maliciosos criados para realizar ações prejudiciais ou não autorizadas em um sistema. Existem diferentes tipos de malware, cada um com características e objetivos diferentes.

VÍRUS

Vírus é um malware que se associa a arquivos ou programas e pode se espalhar quando o arquivo infectado é executado ou compartilhado. Dependendo do caso, pode modificar, danificar ou apagar arquivos.

WORM

Worm é um malware capaz de se espalhar automaticamente por redes e dispositivos vulneráveis. Diferentemente de muitos vírus, ele não precisa necessariamente que o usuário execute um arquivo infectado para continuar sua propagação.

TROJAN

Trojan, ou Cavalo de Troia, é um programa malicioso que se apresenta como algo legítimo ou útil para enganar o usuário. Depois de executado, pode realizar ações não autorizadas no sistema.

RANSOMWARE

Ransomware é um malware que pode bloquear o acesso a arquivos ou sistemas, frequentemente utilizando criptografia para tornar os dados inacessíveis. Os criminosos podem exigir um pagamento para tentar devolver o acesso.

SPYWARE

Spyware é um software desenvolvido para monitorar atividades ou coletar informações sem o conhecimento adequado do usuário. Pode tentar obter dados como hábitos de navegação, informações pessoais ou credenciais.

KEYLOGGER

Keylogger é um tipo de ferramenta capaz de registrar teclas digitadas. Quando utilizado de forma maliciosa, pode ser empregado para tentar capturar informações digitadas pelo usuário, como credenciais.

BOTNET

Botnet é uma rede de dispositivos que foram comprometidos por malware e podem ser controlados remotamente por um atacante. Essas máquinas podem ser utilizadas para realizar diversas atividades maliciosas.

PHISHING

Phishing é uma técnica de engenharia social utilizada para enganar pessoas por meio de mensagens, sites ou comunicações falsas. O criminoso pode se passar por uma empresa, banco, serviço ou pessoa conhecida para induzir a vítima a fornecer informações ou realizar alguma ação.

SPEAR PHISHING

Spear phishing é uma forma mais direcionada de phishing. Em vez de enviar uma mensagem genérica para muitas pessoas, o atacante personaliza a tentativa para atingir uma pessoa ou organização específica.

ENGENHARIA SOCIAL

Engenharia social explora o comportamento humano para conseguir informações ou induzir alguém a realizar determinada ação. O atacante pode utilizar confiança, urgência, medo ou autoridade como elementos de manipulação.

FORÇA BRUTA

Um ataque de força bruta consiste em testar diversas possibilidades para tentar descobrir uma credencial, chave ou senha. Senhas longas e únicas, além de mecanismos como MFA e limitação de tentativas, ajudam a reduzir esse risco.

CREDENTIAL STUFFING

Credential stuffing ocorre quando credenciais obtidas em um vazamento são testadas automaticamente em outros serviços. Esse ataque funciona principalmente quando uma pessoa reutiliza a mesma senha em diferentes plataformas.

DDoS

Um ataque DDoS tenta deixar um serviço indisponível enviando uma quantidade muito grande de requisições ou tráfego para ele. O objetivo é sobrecarregar os recursos do serviço, dificultando ou impedindo o acesso de usuários legítimos.

MAN IN THE MIDDLE

Man-in-the-Middle, ou MITM, ocorre quando um atacante consegue se posicionar entre duas partes que estão se comunicando e tenta interceptar ou manipular essa comunicação. Protocolos seguros e criptografia ajudam a reduzir esse risco.

ROGUE ACCESS POINT

Um Rogue Access Point é um ponto de acesso de rede não autorizado. Ele pode ser utilizado para tentar enganar usuários e fazê-los conectar seus dispositivos a uma rede controlada por terceiros.

VULNERABILIDADE

Vulnerabilidade é uma fraqueza existente em um sistema, aplicação, dispositivo, configuração ou processo que pode ser explorada para causar algum impacto.

EXPLOIT

Exploit é uma técnica, código ou mecanismo utilizado para explorar uma vulnerabilidade existente em um sistema ou aplicação.

ZERO DAY

Uma vulnerabilidade zero-day é uma falha que ainda não possui uma correção disponível ou que é desconhecida pelo responsável pelo sistema. Por isso, pode representar um risco elevado até que uma solução seja desenvolvida e aplicada.

AMEAÇAS INTERNAS

Nem toda ameaça vem de fora da organização. Uma ameaça interna pode ocorrer quando alguém que possui acesso legítimo utiliza esse acesso de maneira inadequada, intencionalmente ou por acidente.

VAZAMENTO DE DADOS

Um vazamento de dados acontece quando informações são expostas, acessadas ou obtidas por pessoas que não deveriam ter acesso a elas. Os dados envolvidos podem incluir informações pessoais, credenciais ou informações corporativas.

COMO SE PROTEGER

A proteção contra ameaças digitais utiliza várias camadas de segurança. Manter sistemas atualizados reduz vulnerabilidades conhecidas. Senhas fortes e únicas dificultam ataques contra contas. MFA adiciona uma camada extra de autenticação. Antivírus e EDR ajudam a identificar comportamentos maliciosos. Firewalls controlam determinados tipos de comunicação. Backups seguros ajudam na recuperação após incidentes. Treinamento e conscientização ajudam usuários a reconhecer phishing e outras técnicas de engenharia social.

PRINCÍPIO DA DEFESA EM PROFUNDIDADE

Defesa em profundidade significa utilizar várias camadas de segurança ao mesmo tempo. Se uma proteção falhar, outras ainda podem impedir ou limitar o impacto do ataque.

RESUMO

Ameaças digitais podem explorar sistemas, redes, aplicações ou pessoas para obter acesso indevido, roubar informações, causar danos ou interromper serviços. Entre as principais ameaças estão vírus, worms, trojans, ransomware, spyware, phishing, engenharia social, força bruta, credential stuffing, DDoS, MITM e exploração de vulnerabilidades. A proteção depende de várias camadas, como atualizações, autenticação, criptografia, firewalls, antivírus, EDR, backups, monitoramento e conscientização dos usuários.

DICA DA FASE:
    dica: Mensagens que tentam provocar uma reação rápida merecem atenção redobrada.
    dica: Observe atentamente o endereço para identificar se ele corresponde ao serviço que deveria representar.
    dica: Pense no que pode acontecer se uma informação usada para acessar uma conta cair nas mãos erradas.
    dica: Analise a mensagem como um todo e procure elementos que, juntos, possam indicar uma tentativa de enganar o usuário.
"""
    },

    "FASE 4": {
        "titulo": "FASE 4 — AUTENTICAÇÃO E SENHAS",
        "icone": "🔑",
        "texto": """
 AUTENTICAÇÃO

1. O que é autenticação

Autenticação é o processo de verificar se uma pessoa, dispositivo ou sistema realmente é quem afirma ser.

Em termos simples, a autenticação responde à pergunta: “Quem é você?”

Exemplo: ao entrar em uma conta, você informa seu usuário e sua senha. O sistema verifica essas informações antes de permitir o acesso.

2. Identificação e autenticação

Identificação é quando o usuário informa quem afirma ser.

Autenticação é quando o sistema verifica se essa informação é verdadeira.

Exemplo:

Identificação: “Meu usuário é Leonardo.”

Autenticação: “Digite sua senha para confirmar sua identidade.”

O processo geralmente segue a ordem: identificação, autenticação e, depois, autorização.

3. Autenticação e autorização

Autenticação verifica quem você é.

Autorização determina o que você pode acessar ou fazer.

Exemplo:

Você entra em uma plataforma usando sua senha. Isso é autenticação. Depois, o sistema permite que você veja apenas os arquivos aos quais possui acesso. Isso é autorização.

4. Fatores de autenticação

Os fatores de autenticação representam diferentes formas de comprovar uma identidade.

O primeiro fator é algo que você sabe, como uma senha, PIN ou código.

O segundo fator é algo que você possui, como um celular, token, cartão ou chave de segurança.

O terceiro fator é algo que você é, como impressão digital, reconhecimento facial ou íris.

Também podem ser considerados fatores relacionados ao comportamento, dispositivo, localização ou contexto do acesso.

5. Senhas

As senhas são uma das formas mais utilizadas de autenticação.

Uma senha segura deve ser difícil de adivinhar e não deve ser reutilizada em vários serviços.

Senhas como “123456”, “senha123” ou informações pessoais são facilmente previsíveis.

O ideal é utilizar senhas longas e únicas para cada serviço.

6. Reutilização de senhas

Utilizar a mesma senha em vários serviços aumenta o risco de comprometimento de contas.

Exemplo:

Se uma senha utilizada em um site for exposta em um vazamento, um atacante pode tentar utilizar essa mesma combinação de usuário e senha em outros sites.

Esse tipo de ataque é chamado de credential stuffing.

7. Autenticação multifator

A autenticação multifator, conhecida como MFA, utiliza dois ou mais fatores diferentes para confirmar a identidade do usuário.

Exemplo:

Senha mais código de um aplicativo autenticador.

Nesse caso, mesmo que alguém descubra a senha, ainda precisará do segundo fator para conseguir acesso.

8. Autenticação de dois fatores

A autenticação de dois fatores, conhecida como 2FA, é um tipo de MFA que utiliza exatamente dois fatores.

Um exemplo é utilizar uma senha e depois confirmar o acesso através de um aplicativo autenticador.

MFA é um conceito mais amplo, enquanto 2FA especifica o uso de dois fatores.

9. Códigos temporários

Alguns sistemas utilizam códigos que mudam periodicamente para confirmar uma autenticação.

Um exemplo são os códigos TOTP, normalmente encontrados em aplicativos autenticadores.

Esses códigos possuem tempo limitado e devem ser tratados como informações confidenciais.

10. Biometria

A autenticação biométrica utiliza características físicas ou comportamentais para ajudar a confirmar a identidade de uma pessoa.

Exemplos incluem impressão digital, reconhecimento facial, íris e reconhecimento de voz.

A biometria é prática, mas exige proteção adequada porque características biométricas não podem ser simplesmente substituídas como uma senha.

11. Passkeys

Passkeys são uma alternativa moderna às senhas tradicionais.

Elas utilizam criptografia para permitir que um dispositivo prove que possui a credencial correta sem depender do envio de uma senha tradicional.

A autenticação pode ser confirmada usando impressão digital, reconhecimento facial ou o método de desbloqueio do dispositivo.

As passkeys também podem oferecer maior resistência contra ataques de phishing.

12. Chaves de segurança

Chaves de segurança são dispositivos físicos utilizados para confirmar uma autenticação.

Elas podem utilizar padrões como FIDO2 e WebAuthn.

Exemplo:

O usuário informa seu nome de usuário, conecta ou aproxima sua chave de segurança e confirma a autenticação.

13. Sessões de login

Depois que o usuário é autenticado, o sistema precisa manter o acesso durante sua utilização.

Para isso, pode ser criada uma sessão de login.

Exemplo:

O usuário entra em uma plataforma, é autenticado e continua navegando pelas páginas sem precisar digitar a senha novamente a cada página.

Essa sessão também precisa ser protegida contra ataques.

14. Logout

Logout é o processo de encerrar uma sessão de acesso.

É especialmente importante utilizar logout em computadores compartilhados ou públicos.

Exemplo:

Depois de utilizar uma conta em um computador da escola, o usuário encerra a sessão para impedir que outra pessoa continue utilizando sua conta.

15. Limitação de tentativas

Sistemas podem limitar a quantidade ou frequência de tentativas de autenticação.

Essa proteção ajuda a impedir ataques automatizados que tentam descobrir senhas.

Uma técnica utilizada para isso é o rate limiting, que limita a quantidade de tentativas realizadas em determinado período.

16. Brute Force

Brute force é um ataque que tenta descobrir uma senha testando diversas combinações.

Quanto mais previsível for uma senha, maior pode ser o risco de ela ser descoberta por tentativas automatizadas.

Senhas fortes, MFA e limitação de tentativas ajudam a reduzir esse risco.

17. Password Spraying

Password spraying ocorre quando uma mesma senha comum é testada contra várias contas.

Em vez de tentar muitas senhas em uma única conta, o atacante tenta uma senha em várias contas diferentes.

Esse método procura evitar determinados mecanismos de bloqueio.

18. Armazenamento de senhas

Sistemas seguros não devem armazenar senhas diretamente em texto puro.

Em vez disso, devem utilizar métodos específicos para armazenamento seguro de credenciais, como Argon2, bcrypt, scrypt ou PBKDF2.

Dessa forma, mesmo que o banco de dados seja comprometido, as senhas não ficam armazenadas diretamente.

19. Hash e criptografia

Hash e criptografia são conceitos diferentes.

Hash transforma uma informação em um valor derivado que não deve ser tratado como algo simplesmente reversível.

Criptografia transforma dados utilizando uma chave e pode permitir que eles sejam recuperados posteriormente através do processo adequado de descriptografia.

Para armazenamento de senhas, são utilizados métodos de derivação e hash apropriados, não criptografia reversível comum.

20. Salt

Salt é um valor adicional utilizado durante o processo de armazenamento seguro de uma senha.

Ele ajuda a impedir que senhas iguais produzam necessariamente o mesmo resultado armazenado e dificulta determinados ataques baseados em valores pré-computados.

21. Phishing e autenticação

Ataques de phishing podem tentar roubar senhas, códigos de autenticação ou informações relacionadas às sessões.

Por isso, o usuário deve verificar o endereço do site, o domínio e o contexto da solicitação antes de fornecer credenciais.

Métodos como passkeys podem oferecer maior resistência contra determinados ataques de phishing.

22. Autenticação adaptativa

Sistemas mais avançados podem analisar o contexto de uma tentativa de login.

Exemplo:

Um usuário normalmente acessa uma conta pelo mesmo dispositivo. De repente, ocorre uma tentativa de acesso em um dispositivo desconhecido e em um horário incomum.

O sistema pode solicitar uma verificação adicional antes de permitir o acesso.

23. Single Sign-On

Single Sign-On, conhecido como SSO, permite que o usuário faça uma autenticação e depois utilize diferentes serviços relacionados sem precisar realizar um novo login em cada serviço.

Exemplo:

Uma conta institucional pode permitir acesso ao e-mail, armazenamento de arquivos e outros sistemas da mesma organização.

24. OAuth 2.0

OAuth 2.0 é utilizado principalmente para delegar autorização entre aplicações.

Ele permite que uma aplicação obtenha acesso limitado a determinados recursos sem precisar receber diretamente a senha do usuário.

É importante não confundir OAuth com autenticação. Para identidade e autenticação sobre OAuth, existe o OpenID Connect.

25. OpenID Connect

OpenID Connect, conhecido como OIDC, é uma camada de identidade construída sobre OAuth 2.0.

Ele permite que uma aplicação obtenha informações sobre a identidade de um usuário que foi autenticado por um provedor de identidade.

26. Autenticação de dispositivos

A autenticação não é utilizada apenas para pessoas.

Computadores, celulares, servidores e outros dispositivos também podem utilizar credenciais para provar sua identidade.

Exemplo:

Um servidor pode precisar apresentar uma credencial válida antes de conseguir se comunicar com outro sistema.

27. Principais ataques relacionados à autenticação

Brute Force consiste em testar várias combinações para tentar descobrir uma credencial.

Credential Stuffing utiliza credenciais obtidas de vazamentos anteriores para tentar acessar outros serviços.

Password Spraying testa uma senha comum contra várias contas.

Phishing tenta enganar o usuário para obter informações de autenticação.

Session Hijacking busca assumir uma sessão de usuário já autenticada.

MFA Fatigue tenta convencer ou pressionar o usuário a aprovar solicitações de autenticação inesperadas.

28. Boas práticas

Utilizar senhas fortes e diferentes para cada serviço.

Ativar MFA sempre que estiver disponível.

Não compartilhar senhas ou códigos de autenticação.

Verificar o endereço dos sites antes de inserir credenciais.

Evitar realizar login através de links suspeitos.

Manter sistemas e dispositivos atualizados.

Utilizar métodos modernos de autenticação quando disponíveis.

Encerrar sessões em computadores compartilhados.

29. Conceito principal

Autenticação é o processo de verificar quem você é.

Autorização é o processo de determinar o que você pode acessar ou fazer.

Uma boa segurança de autenticação combina credenciais fortes, múltiplos fatores, proteção das sessões e mecanismos capazes de identificar tentativas suspeitas.

DICA DA FASE:
    Dica: Dica: Observe atentamente o endereço completo do site. Pequenas alterações no domínio podem indicar uma tentativa de imitação.
    Dica: HTTPS protege a comunicação entre o navegador e o servidor, mas não significa que o site seja necessariamente confiável.
    Dica: Antes de clicar, observe o endereço real mostrado pelo link e procure diferenças no domínio em relação ao serviço oficial.
    Dica: Quando um link esconde seu endereço verdadeiro, fica mais difícil verificar para onde ele realmente vai antes de clicar.
"""
    },

    "FASE 5": {
        "titulo": "FASE 5 — CONTROLE DE ACESSO",
        "icone": "🚪",
        "texto": """
1. O que é controle de acesso?

Controle de acesso é o conjunto de regras e mecanismos utilizados para determinar quem pode acessar determinado recurso e quais ações essa pessoa pode realizar.

Em termos simples, o controle de acesso responde a duas perguntas:

Quem pode acessar?

O que essa pessoa pode fazer?

Exemplo:

João pode visualizar suas notas, mas não pode alterar as notas de outros alunos.

2. Autenticação e autorização

Controle de acesso está diretamente relacionado à autenticação e à autorização.

Autenticação verifica quem é o usuário.

Autorização determina quais recursos e ações esse usuário pode utilizar.

Exemplo:

João entra em uma conta utilizando sua senha.

Isso é autenticação.

Depois, o sistema verifica se João possui permissão para acessar determinada área.

Isso é autorização.

3. Identificação

Identificação é quando o usuário informa ao sistema quem afirma ser.

Exemplo:

Usuário: joao123

Nesse momento, o sistema conhece a identidade informada, mas ainda precisa verificar se ela realmente pertence ao usuário.

4. Autorização

Autorização acontece depois da autenticação.

O sistema verifica quais permissões estão associadas ao usuário.

Exemplo:

Um funcionário pode acessar documentos da empresa, mas somente um administrador pode excluí-los.

5. Permissões

Permissões determinam quais ações um usuário pode realizar sobre determinado recurso.

Algumas permissões comuns são:

Ler

Criar

Editar

Excluir

Executar

Compartilhar

Exemplo:

João pode visualizar um arquivo, mas não possui permissão para modificá-lo.

6. Recursos

Um recurso é qualquer elemento que precisa ser protegido contra acessos ou alterações não autorizadas.

Exemplos:

Arquivos

Pastas

Bancos de dados

Sistemas

Aplicações

Contas

Servidores

Informações pessoais

7. Usuários e grupos

Os sistemas podem controlar o acesso individualmente ou através de grupos.

Exemplo:

Grupo Alunos

Pode visualizar materiais.

Grupo Professores

Pode visualizar e adicionar materiais.

Grupo Administradores

Pode gerenciar usuários e configurações.

O uso de grupos facilita a administração de muitos usuários.

8. Controle de acesso baseado em funções

RBAC significa Role-Based Access Control.

Nesse modelo, as permissões são associadas a funções ou cargos.

Exemplo:

Administrador

Pode criar, editar e excluir usuários.

Professor

Pode criar e editar conteúdos.

Aluno

Pode visualizar conteúdos.

O usuário recebe uma função e essa função determina suas permissões.

9. Controle de acesso baseado em atributos

ABAC significa Attribute-Based Access Control.

Nesse modelo, o acesso pode depender de diferentes atributos.

Exemplos:

Cargo

Horário

Localização

Dispositivo

Tipo de recurso

Nível de segurança

Exemplo:

Um funcionário pode acessar determinado sistema somente durante o horário de trabalho e utilizando um dispositivo autorizado.

10. RBAC e ABAC

RBAC utiliza principalmente funções e cargos.

ABAC utiliza atributos e condições.

Exemplo de RBAC:

Professor pode acessar o sistema.

Exemplo de ABAC:

Professor pode acessar o sistema somente durante o horário permitido e utilizando um dispositivo autorizado.

11. Princípio do menor privilégio

O princípio do menor privilégio determina que cada usuário deve receber somente as permissões necessárias para realizar suas atividades.

Exemplo:

Um funcionário responsável por consultar relatórios não precisa ter permissão para excluir o banco de dados.

Isso reduz os possíveis danos caso a conta seja comprometida.

12. Negação por padrão

A negação por padrão significa bloquear o acesso inicialmente e permitir somente aquilo que foi autorizado.

Exemplo:

Se João não possui permissão para acessar uma determinada pasta, o sistema deve bloquear o acesso.

Esse conceito também é conhecido como Deny by Default.

13. Controle de acesso discricionário

DAC significa Discretionary Access Control.

Nesse modelo, o proprietário de um recurso pode determinar quem terá acesso a ele.

Exemplo:

João cria uma pasta e decide quais usuários poderão visualizar ou modificar os arquivos.

14. Controle de acesso obrigatório

MAC significa Mandatory Access Control.

Nesse modelo, as regras de acesso são determinadas por políticas centralizadas do sistema.

O usuário não pode simplesmente alterar essas regras por conta própria.

Esse modelo é utilizado principalmente em ambientes que exigem controles de segurança mais rígidos.

15. Controle de acesso baseado em regras

Nesse modelo, o sistema utiliza regras específicas para decidir se uma ação será permitida.

Exemplo:

Permitir acesso somente entre 08:00 e 18:00.

Outro exemplo:

Bloquear conexões provenientes de determinadas redes.

16. Controle de acesso físico

O controle de acesso também existe no mundo físico.

Exemplos:

Cartões de acesso

Biometria

Crachás

Fechaduras eletrônicas

Portões controlados

Exemplo:

Somente funcionários autorizados podem entrar em uma sala onde ficam servidores.

17. Controle de acesso lógico

O controle de acesso lógico protege sistemas, aplicações e informações digitais.

Exemplos:

Senhas

MFA

Permissões de arquivos

Contas de usuário

Tokens

Políticas de acesso

18. Listas de controle de acesso

ACL significa Access Control List.

Uma ACL contém regras que determinam quais usuários ou grupos podem realizar determinadas ações sobre um recurso.

Exemplo:

Arquivo: relatorio.pdf

João: leitura

Professor: leitura e edição

Administrador: leitura, edição e exclusão

19. Controle de acesso em arquivos

Sistemas operacionais permitem definir permissões para arquivos e diretórios.

Exemplo:

Um arquivo pode permitir que João leia seu conteúdo, enquanto outro usuário pode ter permissão para editar ou excluir o arquivo.

Isso ajuda a impedir alterações não autorizadas.

20. Controle de acesso em bancos de dados

Bancos de dados também utilizam permissões para proteger informações.

Um usuário pode receber permissão para consultar dados, mas não para alterá-los ou excluí-los.

Exemplo:

Usuário comum:

Pode consultar dados.

Administrador:

Pode consultar, modificar e administrar estruturas do banco.

21. Controle de acesso em aplicações

Aplicações precisam verificar as permissões do usuário antes de executar determinadas ações.

Exemplo:

João tenta acessar uma área administrativa.

O sistema verifica se ele possui a permissão necessária.

Caso contrário, o acesso deve ser negado.

22. Escalonamento de privilégios

Escalonamento de privilégios ocorre quando alguém consegue obter permissões maiores do que deveria.

Existem dois tipos principais.

Escalonamento vertical:

Um usuário comum consegue obter privilégios de administrador.

Escalonamento horizontal:

Um usuário consegue acessar recursos pertencentes a outro usuário com privilégios semelhantes.

23. Falha de controle de acesso

Uma falha de controle de acesso acontece quando o sistema permite que alguém realize uma ação que não deveria ser permitida.

Exemplo:

João tenta acessar informações pertencentes a outra conta.

Se o servidor não verificar corretamente a autorização, informações privadas podem ser expostas.

24. IDOR

IDOR significa Insecure Direct Object Reference.

É uma vulnerabilidade relacionada ao acesso indevido a objetos ou recursos através de identificadores.

Exemplo conceitual:

Um sistema utiliza:

/perfil/100

para acessar um perfil.

Se João alterar o identificador para:

/perfil/101

e conseguir visualizar informações que não deveria acessar, pode existir uma falha de controle de acesso.

25. Separação de funções

A separação de funções evita que uma única pessoa tenha controle excessivo sobre processos importantes.

Exemplo:

Uma pessoa solicita uma alteração financeira e outra precisa aprová-la.

Isso reduz riscos de erros e abusos.

26. Princípio Zero Trust

Zero Trust significa não confiar automaticamente em um usuário ou dispositivo apenas porque ele está dentro de uma rede considerada confiável.

O acesso deve ser verificado de acordo com as políticas de segurança.

O conceito pode ser resumido como:

"Nunca confie automaticamente. Sempre verifique."

27. Controle de sessões

Depois que um usuário é autenticado, o sistema precisa proteger sua sessão.

É importante controlar:

Tempo de sessão

Logout

Tokens

Cookies

Expiração

Reautenticação

Uma sessão mal protegida pode permitir que outra pessoa utilize o acesso de um usuário.

28. Auditoria e registros

Sistemas seguros registram eventos relacionados ao acesso.

Exemplos:

Login

Logout

Tentativas de acesso

Alteração de permissões

Acesso a informações sensíveis

Esses registros ajudam a identificar comportamentos suspeitos e investigar incidentes.

29. Revisão de permissões

As permissões devem ser revisadas regularmente.

Quando um funcionário muda de função, suas permissões antigas podem não ser mais necessárias.

Quando alguém deixa uma organização, seus acessos devem ser removidos.

Isso reduz a quantidade de contas e permissões desnecessárias.

30. Boas práticas

Utilizar o princípio do menor privilégio.

Negar acesso por padrão.

Utilizar autenticação forte.

Separar funções importantes.

Revisar permissões regularmente.

Remover acessos desnecessários.

Proteger sessões.

Registrar eventos importantes.

Verificar autorização no servidor.

Não confiar apenas nas informações fornecidas pelo usuário.

31. Exemplo completo

Imagine um sistema escolar.

João faz login utilizando sua senha.

O sistema realiza a autenticação.

Depois, verifica suas permissões.

Como aluno, João pode visualizar suas próprias notas.

Ele não possui permissão para alterar notas.

Um professor possui permissões diferentes.

Um administrador possui permissões ainda maiores.

Nesse exemplo:

Login representa a autenticação.

Permissões representam a autorização.

Notas são um recurso protegido.

Aluno, professor e administrador são funções.

As regras que determinam o que cada usuário pode fazer representam o controle de acesso.

32. Conceito principal

Controle de acesso é responsável por garantir que cada usuário tenha acesso somente aos recursos e ações para os quais possui autorização.

Autenticação responde:

"Quem é você?"

Autorização responde:

"O que você pode fazer?"

Controle de acesso aplica essas regras para proteger sistemas, informações e recursos.

DICA DA FASE:
    Dica: Observe cuidadosamente o endereço do site. Pequenas alterações em nomes conhecidos podem ser um sinal de fraude.
    Dica: HTTPS protege a comunicação entre você e o servidor, mas isso não significa automaticamente que o site seja confiável.
    Dica: Analise o endereço do link. Sites falsos podem utilizar domínios parecidos com os verdadeiros para enganar o usuário.
    Dica: Antes de clicar, pense se é possível descobrir para onde o link realmente levará.
    Dica: Alguns ataques utilizam caracteres visualmente semelhantes aos de outros alfabetos para fazer um endereço parecer legítimo.
    Dica: Não confie apenas na aparência da página. Verifique cuidadosamente o domínio antes de informar qualquer credencial.
"""
    },

    "FASE 6": {
        "titulo": "FASE 6 — CRIPTOGRAFIA",
        "icone": "🔐",
        "texto": """
CRIPTOGRAFIA

1. O que é criptografia

Criptografia é a técnica utilizada para proteger informações transformando dados legíveis em uma forma que não pode ser facilmente compreendida por pessoas não autorizadas.

Em termos simples:

Texto original → criptografia → texto protegido

Para recuperar a informação:

Texto protegido → descriptografia → texto original

Exemplo:

João envia uma mensagem para Maria.

Sem criptografia, alguém que consiga interceptar a comunicação pode conseguir ler a mensagem.

Com criptografia, a mensagem é transformada em dados protegidos e somente quem possui os meios necessários consegue recuperar o conteúdo.

2. Para que serve a criptografia

A criptografia é utilizada principalmente para proteger informações contra acesso não autorizado.

Ela pode ajudar a garantir:

Confidencialidade

Integridade

Autenticidade

Não repúdio

Esses objetivos fazem parte dos principais conceitos de segurança da informação.

3. Confidencialidade

Confidencialidade significa impedir que pessoas não autorizadas tenham acesso às informações.

Exemplo:

João envia uma mensagem criptografada para Maria.

Mesmo que alguém consiga interceptar os dados, não deverá conseguir compreender o conteúdo sem a chave apropriada.

4. Integridade

Integridade significa garantir que uma informação não tenha sido alterada de maneira indevida.

Exemplo:

Um arquivo é enviado pela internet.

O sistema pode utilizar mecanismos criptográficos para verificar se o arquivo recebido continua exatamente igual ao original.

5. Autenticidade

Autenticidade permite verificar se uma mensagem, arquivo ou comunicação realmente veio de quem afirma ter enviado.

Exemplo:

Um sistema recebe uma mensagem assinada digitalmente.

A assinatura pode ajudar a verificar a identidade do remetente e se o conteúdo foi alterado.

6. Não repúdio

Não repúdio é a capacidade de fornecer evidências de que determinada ação ou mensagem foi realizada por uma determinada entidade.

As assinaturas digitais podem contribuir para esse objetivo.

7. Texto claro

Texto claro é a informação original antes da criptografia.

Também pode ser chamado de plaintext.

Exemplo:

"Olá Maria"

Esse é o conteúdo legível antes de ser protegido.

8. Texto cifrado

Texto cifrado é o resultado obtido depois que uma informação passa por um processo de criptografia.

Também é chamado de ciphertext.

O objetivo é fazer com que o conteúdo não seja compreensível sem o procedimento adequado de descriptografia.

9. Chave criptográfica

A chave é uma informação utilizada por um algoritmo criptográfico para realizar operações de criptografia ou descriptografia.

De forma simplificada:

Mensagem + chave + algoritmo → informação protegida

A segurança de um sistema moderno não deve depender de esconder o algoritmo, mas principalmente de proteger corretamente as chaves.

10. Algoritmo criptográfico

Um algoritmo criptográfico é um conjunto de operações matemáticas utilizadas para proteger ou verificar informações.

Exemplos conhecidos:

AES

RSA

ECC

SHA-256

Cada um possui finalidades diferentes.

11. Criptografia simétrica

Na criptografia simétrica, a mesma chave secreta é utilizada para criptografar e descriptografar os dados.

Exemplo:

João e Maria possuem a mesma chave secreta.

João criptografa a mensagem usando a chave.

Maria utiliza a chave para descriptografá-la.

A principal vantagem é a eficiência.

A principal dificuldade é compartilhar a chave de maneira segura.

12. AES

AES significa Advanced Encryption Standard.

É um algoritmo de criptografia simétrica amplamente utilizado para proteger dados.

Pode ser utilizado em:

Arquivos

Sistemas

Aplicações

Comunicações

Armazenamento de dados

13. Criptografia assimétrica

Na criptografia assimétrica são utilizadas duas chaves relacionadas matematicamente:

Chave pública

Chave privada

A chave pública pode ser compartilhada.

A chave privada deve ser protegida.

14. Chave pública

A chave pública pode ser disponibilizada para outras pessoas ou sistemas.

Ela pode ser utilizada em determinados processos para criptografia ou verificação de assinaturas digitais.

15. Chave privada

A chave privada deve permanecer protegida.

Ela é utilizada em operações que exigem segredo, como descriptografia em determinados sistemas e criação de assinaturas digitais.

Se uma chave privada for comprometida, a segurança do sistema pode ser afetada.

16. RSA

RSA é um algoritmo de criptografia assimétrica.

Ele utiliza conceitos matemáticos relacionados à dificuldade de fatorar números grandes.

Pode ser utilizado em:

Criptografia

Assinaturas digitais

Troca ou proteção de chaves

17. ECC

ECC significa Elliptic Curve Cryptography.

É uma família de técnicas criptográficas baseada em curvas elípticas.

Uma vantagem importante é conseguir níveis elevados de segurança utilizando chaves menores em comparação com alguns sistemas tradicionais.

18. Criptografia híbrida

Sistemas modernos frequentemente combinam criptografia simétrica e assimétrica.

A criptografia assimétrica pode ajudar no estabelecimento ou proteção de uma chave.

Depois, a criptografia simétrica pode ser utilizada para proteger grandes quantidades de dados de maneira eficiente.

19. Hash

Hash é uma função que transforma uma entrada de tamanho variável em uma saída de tamanho determinado.

Exemplo:

Informação → função hash → valor de hash

Um hash é diferente de uma criptografia comum porque não foi projetado para permitir a recuperação do conteúdo original.

20. SHA-256

SHA-256 é uma função hash da família SHA-2.

Ela produz um valor de 256 bits.

É utilizada em diversas aplicações de segurança, como verificação de integridade e outros mecanismos criptográficos.

21. Hash não é criptografia

Essa diferença é muito importante.

Criptografia:

Possui processos destinados a permitir a recuperação do conteúdo original mediante a chave ou mecanismo apropriado.

Hash:

É utilizado principalmente para gerar uma representação de tamanho fixo da informação.

Por isso:

Criptografia ≠ Hash

22. Senhas e hash

Sistemas não devem armazenar senhas simplesmente como texto puro.

Em sistemas seguros, as senhas são normalmente armazenadas utilizando funções específicas de derivação de chave para senhas, juntamente com salt.

Exemplos:

Argon2

bcrypt

scrypt

PBKDF2

23. Salt

Salt é um valor aleatório utilizado junto com uma senha durante o processo de derivação.

Ele ajuda a impedir que senhas iguais produzam exatamente o mesmo resultado armazenado e dificulta determinados ataques baseados em tabelas pré-computadas.

24. Criptografia de ponta a ponta

A criptografia de ponta a ponta, conhecida como E2EE, protege a comunicação de forma que apenas os participantes autorizados possam acessar o conteúdo.

O objetivo é impedir que intermediários tenham acesso ao conteúdo em texto claro.

25. HTTPS

HTTPS utiliza TLS para proteger a comunicação entre navegador e servidor.

Ele ajuda a fornecer:

Confidencialidade

Integridade

Autenticação do servidor

Importante:

HTTPS não significa que o site seja automaticamente confiável.

Um site malicioso também pode utilizar HTTPS.

26. TLS

TLS significa Transport Layer Security.

É um protocolo utilizado para proteger comunicações através de redes.

Ele é utilizado em diversas situações, incluindo conexões HTTPS.

27. Certificados digitais

Certificados digitais ajudam a associar uma identidade a uma chave pública.

Em HTTPS, certificados são utilizados para ajudar o navegador a verificar a identidade do servidor.

Autoridades certificadoras, conhecidas como CAs, participam desse sistema de confiança.

28. Assinatura digital

Assinatura digital é um mecanismo criptográfico utilizado para verificar a autenticidade e a integridade de uma informação.

De forma simplificada:

Mensagem → assinatura digital

O destinatário pode verificar a assinatura utilizando a chave pública correspondente.

29. Criptografia em arquivos

A criptografia pode proteger arquivos armazenados em computadores e servidores.

Exemplo:

Um arquivo contendo informações importantes é criptografado.

Mesmo que alguém consiga copiar o arquivo, o conteúdo permanece protegido sem a chave necessária.

30. Criptografia de disco

A criptografia de disco protege os dados armazenados em um dispositivo.

Exemplo:

Um notebook é perdido.

Se o armazenamento estiver corretamente criptografado, torna-se muito mais difícil para uma pessoa não autorizada acessar os dados diretamente.

31. Criptografia em bancos de dados

Bancos de dados podem utilizar criptografia para proteger informações sensíveis.

Exemplos:

Dados pessoais

Informações financeiras

Documentos

Informações de clientes

32. Criptografia em redes Wi-Fi

Redes Wi-Fi modernas utilizam mecanismos de segurança criptográfica para proteger a comunicação entre dispositivos e o ponto de acesso.

Exemplos de padrões:

WPA2

WPA3

WEP é considerado antigo e inseguro.

33. Criptografia em dispositivos móveis

Celulares podem utilizar criptografia para proteger dados armazenados no dispositivo.

Isso ajuda a proteger informações caso o aparelho seja perdido ou roubado.

34. Criptografia em armazenamento

A criptografia pode proteger dados armazenados em:

HDs

SSDs

Pendrives

Cartões de memória

Servidores

Celulares

Computadores

35. Criptografia em comunicação

A criptografia pode proteger informações durante a transmissão.

Exemplos:

HTTPS

VPNs

Mensagens protegidas por E2EE

Conexões seguras entre sistemas

36. Criptoanálise

Criptoanálise é o estudo de métodos utilizados para analisar ou tentar quebrar sistemas criptográficos.

O objetivo pode ser descobrir informações sem possuir a chave legítima.

37. Ataque de força bruta

Um ataque de força bruta tenta testar muitas possibilidades até encontrar uma combinação válida.

Exemplo conceitual:

Um atacante tenta várias senhas até encontrar a correta.

Senhas maiores e mais imprevisíveis aumentam significativamente o número de possibilidades.

38. Ataque de dicionário

Um ataque de dicionário utiliza listas de palavras e combinações comuns para tentar descobrir senhas.

Por isso, senhas baseadas em palavras muito comuns podem ser mais vulneráveis.

39. Man-in-the-Middle

Man-in-the-Middle, ou MITM, ocorre quando um atacante consegue se posicionar entre duas partes que estão se comunicando.

Protocolos seguros e autenticação adequada ajudam a reduzir esse risco.

40. Gestão de chaves

Não basta utilizar criptografia.

É necessário proteger corretamente as chaves.

Uma organização precisa considerar:

Armazenamento

Rotação

Controle de acesso

Backup

Revogação

Distribuição

41. Chave comprometida

Se uma chave secreta for roubada ou exposta, informações protegidas por ela podem ficar vulneráveis.

Por isso, chaves devem receber proteção adequada.

42. Criptografia forte

Uma criptografia forte utiliza algoritmos e configurações considerados seguros contra os ataques conhecidos dentro do modelo de ameaça considerado.

Não significa que seja absolutamente impossível quebrá-la.

Segurança depende também de:

Tamanho das chaves

Implementação

Gerenciamento das chaves

Configuração

Proteção dos dispositivos

43. Criptografia fraca

Criptografia fraca utiliza algoritmos antigos, configurações inadequadas ou chaves insuficientes.

Exemplo:

WEP em redes Wi-Fi modernas é considerado inseguro.

44. Criptografia não substitui outras medidas de segurança

Criptografia é apenas uma parte da segurança.

Um sistema também precisa utilizar:

Autenticação

Controle de acesso

Atualizações

Backups

Monitoramento

Antivírus e outras proteções apropriadas

Boas práticas de programação

45. Exemplo completo

Imagine que João envie uma mensagem para Maria utilizando um sistema seguro.

A mensagem original é o texto claro.

O sistema utiliza mecanismos criptográficos para proteger a comunicação.

Os dados são transmitidos de forma protegida.

Maria recebe os dados e o sistema utiliza os mecanismos apropriados para recuperar e verificar a mensagem.

Nesse exemplo:

Mensagem original = texto claro

Mensagem protegida = texto cifrado

Chave = informação utilizada pelo mecanismo criptográfico

Algoritmo = método matemático utilizado

TLS = proteção da comunicação

Assinatura digital = verificação de autenticidade e integridade

46. Criptografia simétrica x assimétrica

Simétrica:

Utiliza uma chave secreta compartilhada.

É geralmente mais rápida.

É muito utilizada para proteger grandes volumes de dados.

Assimétrica:

Utiliza chave pública e chave privada.

É geralmente mais pesada computacionalmente.

É muito utilizada em autenticação, assinaturas digitais e estabelecimento de chaves.

47. Criptografia x codificação

Criptografia não deve ser confundida com codificação.

Codificação transforma dados para um formato específico, geralmente para compatibilidade ou transmissão.

Exemplo:

Base64.

Base64 não é criptografia porque não foi projetado para esconder informações.

48. Criptografia x esteganografia

Criptografia transforma ou protege o conteúdo.

Esteganografia procura esconder a existência da mensagem dentro de outro meio.

Exemplo:

Uma mensagem pode ser escondida dentro de uma imagem.

49. Principais conceitos para memorizar

Criptografia = proteção de informações.

Chave = informação usada pelo algoritmo criptográfico.

Texto claro = informação original.

Texto cifrado = informação protegida.

Simétrica = uma chave secreta.

Assimétrica = chave pública + chave privada.

Hash = representação de tamanho fixo, não destinada à reversão.

Salt = valor adicional usado no processamento de senhas.

HTTPS = HTTP protegido por TLS.

TLS = protocolo de segurança para comunicação.

Certificado digital = associa identidade a uma chave pública.

Assinatura digital = ajuda a verificar autenticidade e integridade.

AES = criptografia simétrica.

RSA = criptografia assimétrica.

ECC = criptografia baseada em curvas elípticas.

SHA-256 = função hash.

E2EE = criptografia de ponta a ponta.

DICA DA FASE:
    Dica: Pense em uma impressão digital dos dados. Qualquer alteração no conteúdo pode gerar um resultado completamente diferente.
    Dica: Está relacionada à identidade de quem enviou a mensagem e à confirmação de que o conteúdo não foi alterado.
    Dica: Lembre-se de que existem duas chaves diferentes e que uma delas pode ser compartilhada publicamente.
    Dica: Acontece quando conteúdos diferentes acabam produzindo exatamente o mesmo resultado criptográfico.
    Dica: Hash está ligado à integridade, criptografia à proteção dos dados e assinatura digital à autenticidade e integridade.
"""
    },

    "FASE 7": {
        "titulo": "FASE 7 — BANCO DE DADOS E ACESSO",
        "icone": "🗄️",
        "texto": """
BANCO DE DADOS E SEGURANÇA

Banco de dados é um sistema utilizado para armazenar organizar consultar e gerenciar informações de forma estruturada

A segurança de banco de dados tem como objetivo proteger as informações contra acesso não autorizado alteração indevida perda vazamento e destruição

Autenticação é o processo responsável por verificar a identidade de uma pessoa ou sistema que tenta acessar o banco de dados

Autorização determina quais ações cada usuário pode realizar depois que sua identidade foi confirmada

Controle de acesso limita o acesso aos dados de acordo com as permissões de cada usuário

Princípio do menor privilégio significa fornecer somente as permissões necessárias para cada usuário realizar sua função

Criptografia protege informações transformando os dados em uma forma que não pode ser compreendida facilmente por pessoas não autorizadas

Backup consiste em manter cópias dos dados para possibilitar a recuperação das informações após falhas ataques ou exclusões acidentais

Auditoria registra atividades realizadas no banco de dados permitindo identificar acessos alterações e comportamentos suspeitos

SQL Injection é uma vulnerabilidade que ocorre quando informações fornecidas pelo usuário são inseridas de maneira insegura em comandos SQL

Um ataque de SQL Injection pode permitir que um invasor manipule consultas e obtenha acesso indevido a informações

Prepared Statements são utilizados para separar os dados fornecidos pelo usuário dos comandos SQL ajudando a prevenir SQL Injection

A validação de entrada verifica se os dados fornecidos pelo usuário estão dentro das regras esperadas

Senhas de usuários não devem ser armazenadas diretamente no banco de dados

Senhas devem ser protegidas utilizando funções de hash apropriadas e mecanismos de segurança adequados

A confidencialidade garante que somente pessoas autorizadas possam acessar determinadas informações

A integridade garante que os dados não sejam alterados de maneira indevida

A disponibilidade garante que as informações estejam acessíveis quando forem necessárias

Confidencialidade integridade e disponibilidade formam a Tríade CIA da Segurança da Informação

ABAC é um modelo de controle de acesso baseado em atributos

ABAC pode considerar atributos como usuário cargo horário localização dispositivo e recurso solicitado

Uma política de segurança pode permitir ou negar determinado acesso dependendo dos atributos apresentados

Atualizar o SGBD e seus componentes é importante para corrigir vulnerabilidades conhecidas

Monitoramento ajuda a identificar comportamentos anormais tentativas de acesso indevido e possíveis ataques

Uma boa segurança de banco de dados combina autenticação autorização controle de acesso criptografia backups auditoria validação de entradas atualizações e monitoramento

O objetivo final é garantir que os dados permaneçam protegidos corretos disponíveis e acessíveis somente para pessoas autorizadas

DICA DA FASE:
    Dica: Nunca coloque dados do usuário diretamente nos comandos SQL. Use consultas parametrizadas para evitar SQL Injection.
    Dica: Senhas nunca devem ser armazenadas em texto puro. Utilize hashing seguro com Salt para proteger as credenciais.
    Dica: O ABAC utiliza atributos do usuário, recurso e contexto para decidir se um acesso deve ser permitido.
    Dica: Conceda ao usuário do banco apenas as permissões necessárias para realizar sua função. Esse é o Princípio do Menor Privilégio.
"""
    },

    "FASE 8": {
        "titulo": "FASE 8 — DESENVOLVIMENTO SEGURO",
        "icone": "🛠️",
        "texto": """
DESENVOLVIMENTO SEGURO

Desenvolvimento seguro é a prática de criar sistemas aplicações e softwares considerando a segurança desde o início do projeto até sua manutenção

Validação de entrada consiste em verificar os dados recebidos pelo sistema antes de utilizá los evitando entradas inesperadas ou maliciosas

Autenticação é o processo de verificar a identidade de um usuário enquanto autorização determina quais recursos esse usuário pode acessar

Senhas devem ser armazenadas utilizando funções de hash específicas para senhas como Argon2 ou bcrypt e nunca em texto puro

SQL Injection ocorre quando entradas controladas pelo usuário conseguem alterar comandos SQL e pode ser evitado principalmente com consultas parametrizadas

Cross Site Scripting ocorre quando conteúdo malicioso é inserido em páginas web e executado no navegador de outros usuários

Controle de acesso garante que cada usuário consiga acessar somente os recursos permitidos de acordo com suas funções e atributos

Princípio do menor privilégio determina que usuários aplicações e serviços devem possuir somente as permissões necessárias para executar suas funções

Segredos como senhas chaves de API e tokens não devem ser armazenados diretamente no código fonte

Criptografia protege informações contra acesso não autorizado e deve ser utilizada principalmente para dados sensíveis

HTTPS protege a comunicação entre cliente e servidor utilizando criptografia durante a transmissão dos dados

Dependências e bibliotecas devem ser mantidas atualizadas porque versões antigas podem possuir vulnerabilidades conhecidas

Tratamento seguro de erros evita revelar informações internas como estrutura do sistema banco de dados caminhos de arquivos ou credenciais

Logs de segurança permitem registrar eventos importantes e ajudam na identificação investigação e resposta a incidentes

Testes de segurança procuram vulnerabilidades antes da aplicação chegar ao usuário e podem incluir testes automatizados análise de código e testes de penetração

Desenvolvimento seguro deve fazer parte de todo o ciclo de vida do software incluindo planejamento desenvolvimento testes implantação monitoramento e manutenção

DICA DA FASE:
    Dica: Verifique cuidadosamente os dados recebidos pela aplicação antes de permitir que sejam processados.
    Dica: Pense no que pode acontecer quando uma entrada contém elementos que não deveriam ser interpretados pela aplicação.
    Dica: Observe como o navegador pode interpretar informações fornecidas por usuários quando elas são exibidas em uma página.
    Dica: Considere que um sistema seguro não depende de apenas uma barreira de proteção.
    Dica: Pense em quando a segurança deve começar a ser considerada durante o desenvolvimento de um sistema.    
"""
    },

    "FASE 9": {
        "titulo": "FASE 9 — RESPOSTA A INCIDENTES",
        "icone": "🚨",
        "texto": """
RESPOSTA A INCIDENTES

1. O que é um incidente de segurança?

Um incidente de segurança é um evento que pode comprometer a confidencialidade, integridade ou disponibilidade de sistemas, redes ou informações.

Exemplos:

* Vazamento de dados
* Conta comprometida
* Infecção por malware
* Acesso não autorizado
* Phishing bem-sucedido
* Indisponibilidade de um serviço
* Alteração indevida de informações

2. Objetivo da resposta a incidentes

A resposta a incidentes busca identificar, conter, investigar, corrigir e recuperar um ambiente afetado, reduzindo os danos e evitando que o problema aconteça novamente.

3. Ciclo de resposta a incidentes

Preparação
Definição de equipes, responsabilidades, ferramentas, procedimentos e formas de comunicação antes que um incidente aconteça.

Identificação e detecção
Percepção de atividades anormais e confirmação de que realmente existe um incidente.

Análise
Investigação para descobrir o que aconteceu, quais sistemas foram afetados e qual pode ser a causa.

Contenção
Medidas para limitar a propagação e o impacto do incidente.

Erradicação
Remoção da causa ou dos elementos responsáveis pelo incidente.

Recuperação
Restauração dos sistemas afetados e retorno seguro às operações normais.

Lições aprendidas
Análise do incidente para identificar falhas e melhorar os controles de segurança.

4. Detecção de incidentes

A detecção pode utilizar:

* Logs
* Sistemas de monitoramento
* Alertas de segurança
* Sistemas de detecção de intrusão
* Antivírus e EDR
* Relatórios de usuários
* Análise de comportamento

5. Classificação do incidente

Os incidentes podem ser classificados considerando:

* Tipo de ameaça
* Sistemas afetados
* Quantidade de dados envolvidos
* Impacto
* Urgência
* Gravidade

6. Evidências digitais

Durante uma investigação, informações importantes podem incluir:

* Logs de sistemas
* Registros de autenticação
* Eventos de rede
* Arquivos relacionados ao incidente
* Registros de acesso
* Alertas de ferramentas de segurança

As evidências devem ser preservadas adequadamente para evitar alterações ou perda de informações.

7. Comunicação

A resposta a incidentes também envolve comunicação entre as pessoas responsáveis.

Podem participar:

* Equipe de segurança
* Desenvolvedores
* Administradores de sistemas
* Gestão
* Jurídico
* Responsáveis pela proteção de dados
* Comunicação
* Órgãos externos, quando necessário

8. Contenção

A contenção procura impedir que o incidente continue causando danos.

Pode envolver:

* Isolamento de sistemas afetados
* Bloqueio de contas comprometidas
* Restrição de acessos
* Separação de dispositivos afetados
* Aplicação temporária de controles de segurança

9. Erradicação

Depois da contenção, é necessário eliminar a causa do incidente.

Pode envolver:

* Remoção de componentes maliciosos
* Correção de vulnerabilidades
* Atualização de sistemas
* Alteração de credenciais comprometidas
* Correção de configurações inseguras

10. Recuperação

A recuperação consiste em retornar os serviços à operação normal de maneira controlada.

É necessário verificar:

* Se o problema foi eliminado
* Se os sistemas estão funcionando corretamente
* Se os controles de segurança estão ativos
* Se não existem sinais de comprometimento persistente

11. Pós-incidente

Depois da resolução, a organização deve documentar:

* O que aconteceu
* Quando aconteceu
* Como foi detectado
* Sistemas afetados
* Impactos
* Ações realizadas
* Causa provável
* Melhorias necessárias

12. Plano de Resposta a Incidentes

Um plano define previamente quem faz o quê, quando e como durante um incidente.

Normalmente contém:

* Responsabilidades
* Contatos
* Procedimentos
* Critérios de classificação
* Fluxos de comunicação
* Processos de contenção e recuperação
* Formas de documentação

13. Conceitos importantes

IOC — Indicator of Compromise
É uma evidência que pode indicar que um sistema foi comprometido.

TTPs — Tactics, Techniques and Procedures
Representam as táticas, técnicas e procedimentos utilizados por agentes de ameaça.

MTTD — Mean Time to Detect
Tempo médio necessário para detectar um incidente.

MTTR — Mean Time to Respond/Recover
Tempo médio necessário para responder ou recuperar-se de um incidente, dependendo da definição utilizada.

Playbook
Procedimento previamente definido para lidar com determinado tipo de incidente.

Forense digital
Processo de coleta e análise de evidências digitais para compreender um incidente.

14. Exemplo de um incidente

Uma organização percebe vários acessos suspeitos a uma conta.

1. Detecção: o sistema identifica atividades anormais.
2. Identificação: a equipe confirma o incidente.
3. Análise: investiga os registros e determina o alcance.
4. Contenção: limita o acesso da conta comprometida.
5. Erradicação: corrige a causa e elimina o acesso indevido.
6. Recuperação: restaura as operações normais.
7. Lições aprendidas: analisa o incidente e melhora os controles.

Em resumo, resposta a incidentes é o processo organizado de preparar, detectar, analisar, conter, erradicar, recuperar e aprender com incidentes de segurança.

DICA DA FASE:
    Dica: Observe os eventos em conjunto e procure comportamentos fora do padrão.
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