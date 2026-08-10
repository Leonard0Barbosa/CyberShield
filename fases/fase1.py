#Fase 1 — Fundamentos & Tríade CIA

def fase1(resposta,correta,info):
    
    while True:
        
        info = ['Dica: Falou em sistema fora do ar ou inacessível? Pense em Disponibilidade.' ,  'Dica: Se alguém apenas leu/viu dados sem permissão, pense em Confidencialidade.' , 'Por que está correta: A integridade garante que os dados permaneçam exatos, completos e sem alterações indevidas.'
        ,   ' Dica: Falou em confirmar quem é o usuário? Pense em Autenticação.'    ]

        resposta = str(input('pinto'))[0]

        if resposta in 'Aa' or resposta in '1':
            print(info[0])

        if resposta in 'Bb' or resposta in '2':
            print(info[1])  

        if resposta in 'Cc' or resposta in '3':
            print(info[2])   

        if resposta in 'Dd' or resposta in '4':
            print(info[3])
        if correta == resposta:
            print('Parabéns! Você acertou a questão!')
            break


correta = 'C'
pergunta = str(input('Um arquivo importante foi alterado sem autorização. Qual princípio da segurança foi afetado?\n\nA) Disponibilidade\nB) Confidencialidade\nC) Integridade\nD) Autenticação\n\nDigite a letra correspondente à sua resposta: '))
print(fase1(pergunta, correta))


'''Pergunta: Um arquivo importante foi alterado sem autorização. Qual princípio da segurança foi afetado?

A) Disponibilidade ❌

Por que está errada: A disponibilidade garante que dados e sistemas estejam acessíveis quando necessários. O arquivo continuou acessível, porém modificado.

💡 Dica: Falou em sistema fora do ar ou inacessível? Pense em Disponibilidade.

B) Confidencialidade ❌

Por que está errada: A confidencialidade protege as informações contra acesso não autorizado (vazamento). O foco da questão foi a alteração do conteúdo.

💡 Dica: Se alguém apenas leu/viu dados sem permissão, pense em Confidencialidade.

C) 2Integridade ✅

Por que está correta: A integridade garante que os dados permaneçam exatos, completos e sem alterações indevidas.

D) Autenticação ❌

Por que está errada: A autenticação verifica a identidade de quem acessa, mas não garante que o arquivo permaneça inalterado.

💡 Dica: Falou em confirmar quem é o usuário? Pense em Autenticação.'''