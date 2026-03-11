nome = input("Digite o nome do estudante")

soma_notas = 0
quantidade_trimestres = 3
meta_aprovacao = 180

for i in range(1, quantidade_trimestres + 1):
    nota = float(input(f"Informe a nota do {i}º período:"))
    soma_notas += nota
    
print ("-" * 30)
print (f"Estudante: {nome}")
print(f"Pontuação Total: {soma_notas}")
 
if soma_notas >= meta_aprovacao:
  print ("Statu: Aprovado! Parabéns!")
else:
  pontos_faltantes = meta_aprovacao - soma_notas
  print ("Status: Reprovado!")
  print("Faltaram {pontos_faltantes} pontos para atingir o minímo de {meta_aprovação}.")