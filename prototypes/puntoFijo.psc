Algoritmo puntoFijo
	
	Definir fx, gx, derivadaDeGx Como Caracter
	Definir x0, xi, err, ea, gxi Como Real
	Definir acabar Como Logico
	Leer fx, x0, err
	acabar = Falso
	Mientras calcularDespejesParaGx() y no(acabar) Hacer
		gx = despejarGX()
		derivadaDeGx = derivarGX()
		xi = x0
		Mientras (reemplazarEnDerivadaDeGx(xi, derivadaDeGx) <= 1) y no(acabar) Hacer
			gxi = reemplazarEnGx(xi, gx)
			ea = (xi - gxi)*(100/xi)
			xi = gxi
			
			Si ea <= err Entonces
				Escribir "El valor aproximado del cero de la funci�n es " + ConvertirATexto(xi)
				acabar = Verdadero
			Fin Si
		Fin Mientras
	Fin Mientras
	
	
FinAlgoritmo

Funcion  gx <-  despejarGX
	// L�gica para despegar g(x)
	gx = "Despeje de g(x)"
FinFuncion

Funcion v <- calcularDespejesParaGx
	// L�gica para lograr obtener si hay m�s despejes para g(x) disponibles
	v  = Verdadero
FinFuncion

Funcion  dgx <-  derivarGX
	// L�gica para derivar g(x)
	dgx = "Derivdada de g(x)"
FinFuncion

Funcion  dgx <-  reemplazarEnDerivadaDeGx(x, gx)
	// L�gica para reemplazar x en la derivada de g(x) y obtener el valor absoluto
	dgx = 0.5
FinFuncion

Funcion  dgx <-  reemplazarEnGx(x, gx)
	// L�gica para reemplazar x en g(x)
	dgx = 0.5
FinFuncion

	