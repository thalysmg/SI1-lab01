def maximo(array):
	maximo = array[0]
	for i in array:
		if i > maximo:
			maximo = i
	return maximo

def minimo(array):
	minimo = array[0]
	for i in array:
		if i < minimo:
			minimo = i
	return minimo	

