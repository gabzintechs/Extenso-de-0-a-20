#Crie um programa que tenha uma Tupla totalmente preenchida com uma contagem por extenso,
# de zero até vinte.
# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

c = 0
parar = 1

while c is not parar :
	
	inteiros = [ 'zero', "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez", "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete", "dezoito","dezenove", "vinte"]
	
	ler = int(input('''Digite um numero de 0 a 20.
você receberá o retorno por extenso	'''))

	
	if ler < 0 or ler > 20 :
		print('-' * 35)
		print('			ERRO !, tente numeros de 0 a 20')
		print('')
		print('Encerrando programa..')
		break
		
	print('-' * 36)
	
	print('O numero {}, por extenso, se escreve : '.format(ler),inteiros[ler])
	
	print('-' * 35)
	
	parar = str(input('Deseja parar ? pressione N : ')).upper()
	
	if parar == 'N' :
		print('Encerrando programa...')
		break
	
	
		
	

