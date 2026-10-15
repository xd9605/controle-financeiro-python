print("===== CONTROLE FINANCEIRO =====")

nome = input("digite seu nome: ")

receitas_texto = input("quanto dinheiro entrou? R$ ").replace(",", ".")
receitas = float(receitas_texto)


despesas_texto = input("quanto dinheiro saiu? R$ ").replace(",", ".")
despesas = float(despesas_texto)


saldo = receitas - despesas 


print("\n===== RESUMO FINANCEIRO =====")
print(f"Usuário: {nome}")
print(f"Receitas: R$ {receitas:.2f}")
print(f"despesas: R$ {despesas:.2f}")
print(f"saldo: R$ {saldo:.2f}")

meta = 1000

if receitas > 0:
    percentual_despesas =(despesas / receitas) * 100


    print(f"porcentagem da receita gasta: {percentual_despesas:.1f}%")


    if percentual_despesas <= 50:
        print("Você gastou ate metade da usa receita.")


    elif percentual_despesas <= 80:
        print("Atenção: você utilizou boa parte da sua receita.")


    else:
        print("Alerta: você utilizou mais de 80% da sua receita.")


else:
    print("Não foi possivel clacular: receita igual a zero.")


if saldo >= meta:
    print("Parabens! voce atingiu a sua meta financeira.")


elif saldo > 0:
    print("você ficou no positivo, mas nao atingiu a meta.")


elif saldo == 0:
    print("voçe terminou o mês sem sobrar dinheiro.")


else:
    print("Atençao! Suas despesas superaram suas receitas.")