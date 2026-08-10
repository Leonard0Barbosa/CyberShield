import os
import time
import string
import itertools
import hmac
import hashlib

# ===================================================================== #
# FASE 2: SIMULAÇÃO INTERATIVA DE SEGURANÇA - SENHAS & PROTEÇÃO        #
# ===================================================================== #
print("=" * 60)
print("INICIANDO SIMULAÇÃO: EVOLUÇÃO DA SEGURANÇA DIGITAL")
print("=" * 60)

# ---------------------------------------------------------------------
# PASSO 1: O PERIGO DO TEXTO PURO E REUTILIZAÇÃO
# ---------------------------------------------------------------------
print("\n[PASSO 1] Testando vulnerabilidades de armazenamento e reuso.")
senha_usuario = input("Digite uma senha simples para salvar no arquivo (ex: 12345): ")

# Simulação: Escrever em senhas.txt
with open("senhas.txt", "w", encoding="utf-8") as f:
    f.write(senha_usuario)
print(f"[D] Arquivo 'senhas.txt' criado com a senha: '{senha_usuario}'")
input("\n[Pressione ENTER para simular a execução de um Malware local...]")

# Malware local atacando o arquivo
senha_roubada = ""
if os.path.exists("senhas.txt"):
    with open("senhas.txt", "r", encoding="utf-8") as f:
        senha_roubada = f.read().strip()
    print(f"[❌] MALWARE: Sucesso! Arquivo lido. Senha capturada: '{senha_roubada}'")
    os.remove("senhas.txt")

# Efeito dominó da reutilização
input("\n[Pressione ENTER para o Hacker usar essa senha em outros sites...]")
contas_alvo = ["E-mail Principal", "Internet Banking", "Rede Social"]
print("\n[B] Hacker inicia ataque de Credential Stuffing usando a senha roubada...")
for conta in contas_alvo:
    print(f"[*] Testando credenciais roubadas no sistema do: {conta}")
    print(f"[❌] INVASÃO BEM-SUCEDIDA! Acesso liberado ao {conta}.")
print("-" * 50)

# ---------------------------------------------------------------------
# PASSO 2: A FRAGILIDADE DAS SENHAS CURTAS
# ---------------------------------------------------------------------
print("\n[PASSO 2] Nova política: Mudar a senha para uma curta toda semana.")
senha_curta_da_semana = input("Digite uma senha curta de até 4 letras minúsculas (ex: gato): ").lower()

print(f"[A] Nova senha semanal definida: '{senha_curta_da_semana}'")
input("\n[Pressione ENTER para iniciar o ataque de Força Bruta automatizado...]")
print("[!] Quebrando senha por Força Bruta...")

caracteres = string.ascii_lowercase
inicio_forca_bruta = time.time()
tentativas = 0
senha_descoberta = None

# Loop que testa combinações geométricas até encontrar o alvo
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

# ---------------------------------------------------------------------
# PASSO 3: A SOLUÇÃO IDEAL - SENHA EXCLUSIVA + MFA
# ---------------------------------------------------------------------
print("\n[PASSO 3] Adotando a postura correta (Senha Forte Exclusiva + MFA)...")

SENHA_BANCO_REAL = "Super#Senha#Exclusiva#Longa#2026"
CHAVE_MFA_SECRETA = b"CHAVE_SECRETA_DO_CELULAR_DO_USUARIO_123"

def gerar_codigo_mfa_temporario():
    passo_tempo = int(time.time() // 30)
    mensagem = passo_tempo.to_bytes(8, byteorder='big')
    hash_hmac = hmac.new(CHAVE_MFA_SECRETA, msg=mensagem, digestmod=hashlib.sha256).digest()
    codigo_mfa = str(int.from_bytes(hash_hmac[-4:], byteorder='big') % 1000000).zfill(6)
    return codigo_mfa

print(f"[C] Usuário configurou a senha forte: '{SENHA_BANCO_REAL}'")
print("[MFA] Sistema gerou um token temporário no celular do usuário real.")

# O Hacker tenta invadir
print("\n[CENÁRIO] O hacker descobriu sua senha por Phishing, mas o banco tem MFA.")
codigo_real_do_celular = gerar_codigo_mfa_temporario()

# Agora o usuário finge ser o hacker tentando adivinhar
codigo_tentado_pelo_hacker = input("\n[VOCÊ É O HACKER] Tente adivinhar o Token de 6 dígitos do MFA: ")

print(f"\n[*] Código digitado pelo invasor: {codigo_tentado_pelo_hacker}")
print(f"[*] Código real gerado no app do usuário: {codigo_real_do_celular}")

if codigo_tentado_pelo_hacker == codigo_real_do_celular:
    print("[❌] Falha grave! O hacker acertou o token aleatório. Acesso concedido.")
else:
    print("[✅] DEFESA TOTAL: Token incorreto! Sistema BLOQUEOU a tentativa de login.")

print("\n" + "=" * 60)
print("FIM DA SIMULAÇÃO: O USO DE SENHA EXCLUSIVA + MFA DEFENDEU A CONTA.")
print("=" * 60)
