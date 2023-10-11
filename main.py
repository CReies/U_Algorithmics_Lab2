import os
from Classes.Queue import Queue
from Classes.Stack import Stack

queues : list[Queue] = []
stacks : list[Stack] = []

def printSeparator():
	print('\n====================\n')

def clearScreen():
	for i in range(os.get_terminal_size().lines):
		print('\n')

def pressEnter():
	input('Presione enter para continuar...')

def invalidOption():
	print('Opción inválida')
	pressEnter()
	clearScreen()

while True:
	clearScreen()
	print('Bienvenido al programa de pilas y colas')

	printSeparator()

	print('Seleccione el tipo de estructura que desea utilizar')
	structure = input('1. Pila\n2. Cola\n3. Salir\n')
	validStructures = ['1', '2', '3']

	if structure not in validStructures:
		invalidOption()
		continue

	if structure == '3':
		break

	printSeparator()

	if structure == '1': 
		structure = 'Pila'
		print('Pilas:\n')
		for i in range (len(stacks)):
			print(f'{i+1}. {stacks[i].getData()}')

	elif structure == '2': 
		structure = 'Cola'
		print('Colas:\n')
		for i in range (len(queues)):
			print(f'{i+1}. {queues[i].getData()}')

	printSeparator()

	selectedStructure = input(f'Seleccione la {structure} que desea utilizar o ingrese 0 para crear una nueva: ')
	
	if structure == 'Pila' and int(selectedStructure) > len(stacks) or structure == 'Cola' and int(selectedStructure) > len(queues):
		invalidOption()
		continue

	if selectedStructure == '0':
		if structure == 'Pila':
			stacks.append(Stack())
			selectedStructure = len(stacks)
		elif structure == 'Cola':
			queues.append(Queue())
			selectedStructure = len(queues)
	
	if structure == 'Pila':
		selectedStructure = stacks[int(selectedStructure)-1]
	elif structure == 'Cola':
		selectedStructure = queues[int(selectedStructure)-1]

	printSeparator()

	print('Seleccione la operación que desea realizar')
	operation = input('1. Agregar\n2. Eliminar\n3. Modificar\n4. Está vacia\n5. Salir\n')

	validOperations = ['1', '2', '3', '4', '5']

	if operation not in validOperations:
		invalidOption()
		continue

	if operation == '5':
		break

	printSeparator()

	if operation == '1':
		value = input('Ingrese el valor que desea agregar: ')
		if isinstance(selectedStructure, Stack):
			selectedStructure.stack(value)
		elif isinstance(selectedStructure, Queue):
			selectedStructure.queue(value)

	elif operation == '2':
		value = input('Ingrese la cantidad de elementos que desea eliminar: ')
		if isinstance(selectedStructure, Stack):
			selectedStructure.unstack(value)
		elif isinstance(selectedStructure, Queue):
			selectedStructure.dequeue(value)

	elif operation == '3':
		value = input('Ingrese el valor con el que desea modificar: ')
		selectedStructure.modify(value)
		selectedStructure.print()

	elif operation == '4':
		print(f'La {structure} está vacía') if selectedStructure.is_empty() else print(f'La {structure} no está vacía')
	
