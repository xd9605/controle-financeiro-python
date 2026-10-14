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