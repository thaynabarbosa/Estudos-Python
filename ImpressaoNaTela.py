print("Meu texto em uma linha")
print()
print("Meu texto em duas linhas\n uma em cima da outra!")
print("\tMeu texto com tabulação no começo")
print("Meu texto com tabulação no \tfim!")
num = 7
print("Meu texto e meu numero inteiro com valor", num)
num2 = 20.57
print("Meu texto e o float",num2,"no meio")
num3 = 10.4/3.4
print("Meu float cheio de casas decimasi: ", num3)
print("Meu float com uma casa decimal: %.1f" % num3)
print("Meu float com duas casas decimais: %.2f" % num3)
print("Meu float com três casas decimais: %.3f" % num3)
print("Meu float com quatro casas decimais: %.4f" % num3,"e posso colocar mais texto =)")
print("E posso imprimir %.3f" % num3, "e %.2f" % num2, "e quantos eu quiser!")
num3 = float("%.2f"% num3)
print("Novo num3 = ", num3)
print("Você vê o espaço antes e depois da impressão do valor",num3,"?")
textoNum = str(num)
print("Usando impressão de"+textoNum+"sem espaço!")