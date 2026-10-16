
# ==========================================
# PROJETO: CONTROLE FINANCEIRO
# Descrição: cálculo e análise financeira
# ==========================================

import math


# 1. INÍCIO DO PROGRAMA

print("===== CONTROLE FINANCEIRO =====")


# 2. ENTRADA DO NOME DO USUÁRIO

nome = input("Digite seu nome: ").strip()

while not nome:
    print("O nome não pode ficar vazio.")
    nome = input("Digite seu nome: ").strip()


# 3. ENTRADA E VALIDAÇÃO DAS RECEITAS

while True:
    try:
        receitas_texto = input(
            "Quanto dinheiro entrou? R$ "
        ).strip().replace(",", ".")

        receitas = float(receitas_texto)

        # Verifica se o número é válido e finito
        if not math.isfinite(receitas):
            print("Digite um valor numérico válido.")
            continue

        # Impede receitas negativas
        if receitas < 0:
            print("A receita não pode ser negativa.")
            continue

        # Encerra a repetição quando o valor é válido
        break

    except ValueError:
        print(
            "Entrada inválida! Digite um número, "
            "por exemplo: 3000,50."
        )


# 4. ENTRADA E VALIDAÇÃO DAS DESPESAS

while True:
    try:
        despesas_texto = input(
            "Quanto dinheiro saiu? R$ "
        ).strip().replace(",", ".")

        despesas = float(despesas_texto)

        # Verifica se o número é válido e finito
        if not math.isfinite(despesas):
            print("Digite um valor numérico válido.")
            continue

        # Impede despesas negativas
        if despesas < 0:
            print("A despesa não pode ser negativa.")
            continue

        # Encerra a repetição quando o valor é válido
        break

    except ValueError:
        print(
            "Entrada inválida! Digite um número, "
            "por exemplo: 1200,25."
        )


# 5. CÁLCULOS INICIAIS

saldo = receitas - despesas
meta = 1000


# 6. RESUMO FINANCEIRO

print("\n===== RESUMO FINANCEIRO =====")
print(f"Usuário: {nome}")
print(f"Receitas: R$ {receitas:.2f}")
print(f"Despesas: R$ {despesas:.2f}")
print(f"Saldo: R$ {saldo:.2f}")


# 7. ANÁLISE DO PERCENTUAL DE DESPESAS

print("\n===== ANÁLISE DE DESPESAS =====")

if receitas > 0:
    percentual_despesas = (despesas / receitas) * 100

    print(
        f"Porcentagem da receita gasta: "
        f"{percentual_despesas:.1f}%"
    )

    if percentual_despesas <= 50:
        print("Você gastou até metade da sua receita.")

    elif percentual_despesas <= 80:
        print(
            "Atenção: você utilizou boa parte "
            "da sua receita."
        )

    else:
        print(
            "Alerta: você utilizou mais de 80% "
            "da sua receita."
        )

else:
    print(
        "Não é possível calcular o percentual: "
        "receita igual a zero."
    )


# 8. ANÁLISE DA ECONOMIA

print("\n===== ANÁLISE DA ECONOMIA =====")

if receitas > 0 and saldo > 0:
    percentual_economia = (saldo / receitas) * 100

    print(
        f"Porcentagem economizada: "
        f"{percentual_economia:.1f}%"
    )

elif receitas > 0 and saldo <= 0:
    print(
        "Você não conseguiu economizar dinheiro "
        "neste mês."
    )

else:
    print(
        "Não é possível analisar a economia "
        "com receita igual a zero."
    )


# 9. VERIFICAÇÃO DA META FINANCEIRA

print("\n===== META FINANCEIRA =====")

if saldo >= meta:
    print(
        "Parabéns! Você atingiu sua meta financeira."
    )

elif saldo > 0:
    print(
        "Você ficou no positivo, mas não "
        "atingiu a meta."
    )

elif saldo == 0:
    print(
        "Você terminou o mês sem sobrar dinheiro."
    )

else:
    print(
        "Atenção! Suas despesas superaram "
        "suas receitas."
    )


# 10. ENCERRAMENTO DO PROGRAMA

print("\n===== FIM DO RELATÓRIO =====")
print(f"Obrigado por utilizar o programa, {nome}!")
