
# ==========================================
# PROJETO: CONTROLE FINANCEIRO
# ==========================================

print("===== CONTROLE FINANCEIRO =====")


# 1. ENTRADA DE DADOS

nome = input("Digite seu nome: ")

receitas_texto = input("Quanto dinheiro entrou? R$ ").replace(",", ".")
receitas = float(receitas_texto)

despesas_texto = input("Quanto dinheiro saiu? R$ ").replace(",", ".")
despesas = float(despesas_texto)


# 2. CÁLCULOS INICIAIS

saldo = receitas - despesas
meta = 1000


# 3. RESUMO FINANCEIRO

print("\n===== RESUMO FINANCEIRO =====")
print(f"Usuário: {nome}")
print(f"Receitas: R$ {receitas:.2f}")
print(f"Despesas: R$ {despesas:.2f}")
print(f"Saldo: R$ {saldo:.2f}")


# 4. ANÁLISE DO PERCENTUAL DE DESPESAS

print("\n===== ANÁLISE DE DESPESAS =====")

if receitas > 0:
    percentual_despesas = (despesas / receitas) * 100

    print(f"Porcentagem da receita gasta: "f"{percentual_despesas:.1f}%")
    

    if percentual_despesas <= 50:
        print("Você gastou até metade da sua receita.")

    elif percentual_despesas <= 80:
        print("Atenção: você utilizou boa parte da sua receita.")

    else:
        print("Alerta: você utilizou mais de 80% da sua receita.")

else:
    print("Não foi possível calcular os percentuais: receita igual a zero.")


# 5. ANÁLISE DA ECONOMIA

print("\n===== ANÁLISE DA ECONOMIA =====")

if receitas > 0 and saldo > 0:
    percentual_economia = (saldo / receitas) * 100

    print(f"Porcentagem economizada: {percentual_economia:.1f}%")

elif receitas > 0 and saldo <= 0:
    print("Você não conseguiu economizar dinheiro neste mês.")


# 6. VERIFICAÇÃO DA META FINANCEIRA

print("\n===== META FINANCEIRA =====")

if saldo >= meta:
    print("Parabéns! Você atingiu sua meta financeira.")

elif saldo > 0:
    print("Você ficou no positivo, mas não atingiu a meta.")

elif saldo == 0:
    print("Você terminou o mês sem sobrar dinheiro.")

else:
    print("Atenção! Suas despesas superaram suas receitas.")
