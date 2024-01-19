print("Opções: [A]dicionar afazer na lista, [V]isualizar lista ou [S]air do programa")

def mostrar_lista(lista):
	# se a lista estiver vazia, não loope, saia da função
	if len(lista) == 0:
		print("A lista está vazia no momento")
		return 0

	for i in range(len(lista)):
		print("* " +lista[i])

def main():
	lista = []

	while(True):
		user_input = str(input(">> "))

		if user_input == 'V':
			mostrar_lista(lista)
			
		if user_input == 'A':
			afazer = str(input("Digite a tarefas do dia aqui: "))

			print("Afazer adicionado!")

			lista.append(afazer)

		if user_input == 'S':
			break

main()
